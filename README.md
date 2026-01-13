# 🎬 OTT Movie Scout — Finding the Next Big Streaming Hit

## TL;DR
An **automated movie acquisition intelligence system** that:
- Pulls real-time movie data from the TMDB API
- Scores movies using an **80/20 model (Audience Buzz vs ROI Efficiency)**
- Automatically refreshes a **Power BI dashboard** using Power Automate
- Highlights the **Top 3 acquisition-ready movies** at any given time

---

## 🎯 Project Goal
Deciding which movie to add to a streaming platform is a **multi-million dollar gamble**.  
Most acquisition decisions rely heavily on raw popularity, which can lead to expensive mistakes.

This project introduces a **data-driven acquisition strategy** that balances:
- **Market demand** — what audiences are actively engaging with
- **Financial efficiency** — return on investment and cost discipline

The result is a **repeatable, automated system** for identifying high-value movie acquisitions.

---

## 🧠 Selection Logic (80 / 20 Model)
Each movie is scored using a weighted formula:

### 🔹 80% — Audience Buzz
- Popularity
- Viewer engagement
- Market visibility

### 🔹 20% — ROI Efficiency
- Budget vs revenue performance
- Financial downside protection

This approach prioritizes movies that are **both popular and financially sensible**, rather than chasing hype alone.

---

## 🏆 Final Output — Top 3 Movie Podium
The dashboard dynamically ranks movies and displays the **Top 3 acquisition candidates** based on the 80/20 scoring logic.

- 🥇 **Winner**
- 🥈 **Runner-up**
- 🥉 **Second Runner-up**

📸 *Podium visualization powered by real-time TMDB data.*

![Top 3 Movies Podium](assets/top_movies_podium.png)

---

## 📊 Strategic Acquisition Map
A scatter plot is used to visualize each movie’s **strategic position** in the market.

### Quadrant Interpretation
- **Top-Right (Gold Mine):** High demand + High profitability  
- **Top-Left (The Risk):** Popular but expensive acquisitions  
- **Bottom-Right:** Financially efficient niche titles  
- **Bottom-Left:** Low-impact candidates  

📸 *Visualizing profitability vs popularity to minimize acquisition risk.*

![Strategic Acquisition Map](assets/strategic_map.png)

---

## 🔄 Automated Workflow (Power Automate Desktop)
The entire pipeline is automated to keep insights **fresh and decision-ready**.

### Workflow Overview
1. Run Python script to fetch and process TMDB data
2. Update the master CSV dataset
3. Open the Power BI dashboard
4. Automatically trigger a dashboard refresh

This removes manual intervention and ensures the dashboard always reflects the **latest market conditions**.

---

## 🛠️ Tech Stack & Tools

### Programming & Data
- **Python 3.10+**
- `pandas` — data cleaning and transformation
- `requests` — TMDB API integration
- `python-dotenv` — secure API key management
- `pathlib`, `os` — cross-platform path handling
- `datetime`, `time` — date filtering and rate-limit handling

### Visualization & Automation
- **Power BI Desktop** — interactive analytics dashboard
- **Power Automate Desktop** — automated data refresh pipeline

---

## 📂 Project Structure
.
├── src/ # Python data extraction and processing
├── data/ # Generated CSV outputs (ignored in git)
├── powerbi/ # Power BI dashboard (.pbix)
├── assets/ # Screenshots and visuals
├── .env.template # Environment variable template
├── requirements.txt
└── README.md

---

## 🚀 How to Run the Project

### 1️⃣ Prerequisites
- Python **3.10+**
- Power BI Desktop
- TMDB API Key

#### 🌍 VPN Note
TMDB API access can be **region-restricted or unstable** in some locations.  
Using a VPN ensures consistent connectivity during data extraction.

---

### 2️⃣ Setup
Install dependencies:
```bash
pip install -r requirements.txt

Create a .env file using .env.template:
TMDB_API_KEY=your_api_key_here

3️⃣ Run the Pipeline

python src/tmdb_extractor.py

Processed data is saved to /data
Open the Power BI file from /powerbi
Refresh once (or allow Power Automate to handle refresh automatically)

🔮 Future Enhancements

Genre-based weighting (e.g., action vs drama ROI profiles)
Historical trend analysis over longer time windows
Cloud-based scheduling and deployment
Predictive acquisition scoring using ML models

📌 Key Takeaway

This project demonstrates how data engineering, automation, and business logic can be combined to support high-stakes strategic decisions in the streaming industry.

---

### ✅ Final verdict
- Portfolio-ready  
- Recruiter-friendly  
- Clear business value  
- Strong automation story  

If you want next, I can:
- Help you **write a LinkedIn post** for this project  
- Prepare a **2-minute interview explanation**
- Suggest **job titles** this project best aligns with  

Just say the word.
