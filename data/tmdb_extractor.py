import os
import requests
import pandas as pd
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
from pathlib import Path

# Folder where this script lives → repo/src
SCRIPT_DIR = Path(__file__).resolve().parent

# Repo root folder
PROJECT_ROOT = SCRIPT_DIR.parent

# Load environment variables from repo root
load_dotenv(PROJECT_ROOT / ".env")

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3/"

# Output folder: repo/data
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = DATA_DIR / "final_movie_analysis_data.csv"
# Time window parameters
DATE_END_BUFFER = 10 
DATE_START_WINDOW = 60 

def get_movie_details(tmdb_id):
    """
    Fetches detailed financial and structural data for a single movie ID.
    """
    url = f"{TMDB_BASE_URL}movie/{tmdb_id}?api_key={TMDB_API_KEY}&language=en-US"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Image Logic
        poster_path = data.get('poster_path', '')
        IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"
        full_poster_url = f"{IMAGE_BASE_URL}{poster_path}" if poster_path else ""

        details = {
            'tmdb_id': tmdb_id,
            'budget': data.get('budget', 0),
            'revenue': data.get('revenue', 0),
            'runtime': data.get('runtime', 0),
            'genres': ', '.join([g['name'] for g in data.get('genres', [])]),
            'Poster_URL': full_poster_url,
            'production_companies': ', '.join([c['name'] for c in data.get('production_companies', [])]),
            'status': data.get('status', 'Unknown')
        }
        return details

    except requests.exceptions.RequestException as e:
        print(f"Error fetching details for ID {tmdb_id}: {e}")
        return None

def apply_data_quality_filters(df):
    """Filters the DataFrame to remove records with missing or zero critical metrics."""
    initial_count = len(df)

    # Condition 1 & 2: Financials must be greater than zero
    filter_financials = (df['budget'] > 0) & (df['revenue'] > 0)

    # Condition 3 & 4: Audience metrics must be valid (greater than zero)
    filter_audience = (df['Vote_Average'] > 0) & (df['Popularity'] > 0)

    # Condition 5: Release Date must not be null/blank
    filter_date = df['Release_Date'].notna()

    # Combine all conditions
    cleaned_df = df[filter_financials & filter_audience & filter_date].copy()

    dropped_count = initial_count - len(cleaned_df)
    print(f"\n--- Data Quality Check ---")
    print(f"Initial movie count: {initial_count}")
    print(f"Movies dropped due to zero/blank financials or ratings: {dropped_count}")
    print(f"Final clean movie count: {len(cleaned_df)}")

    return cleaned_df

def fetch_and_enrich_recent_movies():
    """
    Main function to execute Discovery, Enrichment, and Historical Merging.
    """
    if not TMDB_API_KEY:
        print("ERROR: TMDB_API_KEY not found in .env file.")
        return

    # 1. SETUP: Calculate date range
    date_60_days_ago = (datetime.now() - timedelta(days=DATE_START_WINDOW)).strftime('%Y-%m-%d')
    date_10_days_ago = (datetime.now() - timedelta(days=DATE_END_BUFFER)).strftime('%Y-%m-%d')

    print(f"1. Discovering movies released between {date_60_days_ago} and {date_10_days_ago}...")

    # 2. DISCOVER: Get Top 20 results by revenue
    discover_params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
        'sort_by': 'revenue.desc',
        'primary_release_date.gte': date_60_days_ago,
        'primary_release_date.lte': date_10_days_ago,
        'page': 1 
    }

    try:
        response = requests.get(f"{TMDB_BASE_URL}discover/movie", params=discover_params)
        response.raise_for_status()
        discover_data = response.json()

        initial_movies = []
        for movie in discover_data.get('results', []):
            initial_movies.append({
                'tmdb_id': movie.get('id'),
                'Title': movie.get('title'),
                'Release_Date': movie.get('release_date'),
                'Vote_Average': movie.get('vote_average'),
                'Popularity': movie.get('popularity')
            })

        df_initial = pd.DataFrame(initial_movies)
    except Exception as e:
        print(f"Error in Discover API call: {e}")
        return

    # 3. ENRICHMENT LOOP
    detailed_data = []
    print("2. Starting detailed enrichment loop...")

    for index, row in df_initial.iterrows():
        details = get_movie_details(row['tmdb_id'])
        if details:
            detailed_data.append(details)
        time.sleep(0.3) 

    # 4. MERGE & CLEAN NEW DATA (LOCAL TO THIS RUN)
    df_details = pd.DataFrame(detailed_data)
    final_df = pd.merge(df_initial, df_details, on='tmdb_id', how='left')
    final_df['Release_Date'] = pd.to_datetime(final_df['Release_Date'], errors='coerce')
    
    # Apply your original filters
    new_cleaned_df = apply_data_quality_filters(final_df)

    # 5. HISTORICAL MERGING LOGIC
    # Checks for the master database file
    if OUTPUT_FILE.exists():
        print(f"\nMerging with existing data in {OUTPUT_FILE}...")
        df_old = pd.read_csv(OUTPUT_FILE)
        df_old['Release_Date'] = pd.to_datetime(df_old['Release_Date'], errors='coerce')
        
        # Combine old data with new findings
        combined_df = pd.concat([df_old, new_cleaned_df], ignore_index=True)
        
        # Keep 'last' version to ensure stats like revenue update over time
        final_to_save = combined_df.drop_duplicates(subset=['tmdb_id'], keep='last')
    else:
        print(f"\nNo existing file found. Creating {OUTPUT_FILE}...")
        final_to_save = new_cleaned_df

    # 6. FINAL SAVE TO THE MASTER DATABASE
    final_to_save.to_csv(OUTPUT_FILE, index=False)
    print(f"\n --- SUCCESS ---")
    print(f"Total unique movies in master database: {len(final_to_save)}")
    
    return final_to_save

if __name__ == "__main__":
    fetch_and_enrich_recent_movies()