📊 YouTube Trending Analysis

📌 Project Overview
This project focuses on analyzing YouTube trending videos to understand the factors that influence a video’s popularity. Using Apache Spark (PySpark), the project examines relationships between key engagement metrics such as views, likes, comments, and video categories.
The analysis helps identify trending content types and provides insights useful for content creators, marketers, and researchers.

🎯 Objectives
Understand the structure of the YouTube trending dataset
Clean and preprocess missing or inconsistent data
Analyze correlations between views, likes, and comments
Identify the top 10 trending video categories
Visualize trends using bar charts for easy interpretation

🗂 Dataset Description
Each row in the dataset represents a trending YouTube video with the following attributes:
Column Name	Description
video_id	Unique ID of the video
title	Video title
channel_title	Channel name
category	Video category
views	Total views
likes	Total likes
comments	Total comments
publish_time	Video publish date
trending_date	Date when video trended

🛠 Technologies Used
Apache Spark (PySpark)
Python
Matplotlib
Pandas
CSV Dataset

⚙️ Project Workflow
Initialize Spark session
Load the cleaned YouTube trending dataset
Handle missing values
Perform correlation analysis
Identify top 10 trending categories by average views
Visualize results using bar charts

📈 Key Results
Strong positive correlation between views and likes
Comments show a positive but weaker correlation with views
Gaming is the most trending category by average views
Comedy, Travel, and Music also perform strongly
Education and Sports have lower views but niche engagement

📊 Visualizations
Bar chart showing Top 10 Trending Categories by Average Views
Dashboard displaying views, likes, comments, and category distribution

🧠 Conclusion
Videos with higher views tend to receive more likes
Gaming and Comedy dominate YouTube trending content
Niche categories like Education and Health have focused audiences
Insights can guide creators to optimize content strategies

🔮 Future Enhancements
Include additional features like video duration and tags
Apply machine learning models to predict trending videos
Perform time-series analysis for trend evolution
