🎬 OTT Movie Scout: Finding Our Next Big Hit
The Goal
Deciding which movie to add to a streaming platform is a multi-million dollar gamble. Usually, people just look at how popular a movie is. But I wanted to be smarter. I built an automated system that finds movies that are popular AND profitable.

I used a special 80/20 Rule to rank them:

80% Audience Buzz: (Do people love it?)

20% ROI: (Was it a good deal for the money?)

📊 The Final Result
This is the "brain" of the project. The podium automatically updates to show the top 3 movies we should buy right now based on our 80/20 math.

Caption: The dynamic podium showing our #1 acquisition target based on the latest data.

🛠️ How It Works (The Tech Stack)
I used three tools to make this happen without having to do manual work every day:

Python: My "Data Collector." It uses the TMDB API to grab the latest movie stats.

Power Automate Desktop: My "Manager." It handles the automation loop—running the script and refreshing the data.

Power BI: My "Presenter." It turns messy numbers into the interactive dashboard you see above.

🔄 The Automation Flow
I didn't want to run code manually every time. I set up a Power Automate flow so that everything happens with one click.

Caption: My automation flow that runs the Python script and refreshes Power BI.

What happens in this flow:

It opens a Command Prompt window so you can watch the Python script work in real-time.

It waits for the script to finish downloading the data.

It automatically refreshes the Power BI dashboard so the charts update instantly.

🔍 Strategic Analysis
I also created a Strategic Acquisition Map (a scatter chart). This helps us see which movies are "low risk" and which ones are "superstars."

Caption: Our Strategic Map. Movies in the top-right corner are our best buys.

⚙️ Requirements to Run
If you want to run this project on your machine, you will need:

Python installed.

A TMDB API Key (to get the movie data).

🌍 A VPN (Mandatory): The TMDB API requires a VPN to connect properly in certain regions. Make sure your VPN is ON before running the script.

Power BI Desktop to open the report.

📂 Project Structure
/Data: Stores the movie spreadsheets.

/Scripts: Contains the Python extraction code.

/Report: Contains the Power BI .pbix file.

/Assets: Stores the screenshots used in this README.
