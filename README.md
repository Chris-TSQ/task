Douban Top 100 Movies Analytics

A full-stack data analytics web application that visualizes insights from the Douban Top 100 Movies dataset. This project combines Python (Flask) for data processing and visualization with a Node.js (Express) API and a lightweight frontend.

📌 Features
📊 Dynamic data visualizations:
Average rating by genre
Movie count by genre
Rating distribution
Genre × Region heatmap
🌐 RESTful API:
Fetch all movies
Filter by genre
Get aggregate statistics
🔄 Auto-refreshing plots
🌍 Chinese → English translation for genres & regions
🗄️ Supports both MySQL (Flask service) and PostgreSQL (Node API)
🏗️ Architecture Overview
Frontend (Vanilla JS)
        ↓
Node.js API (Express + PostgreSQL)
        ↓
Flask Service (Python + MySQL + Pandas)
        ↓
Database
📂 Project Structure
.
├── backend-flask/
│   ├── models/
│   │   └── database.py
│   ├── services/
│   │   ├── data_service.py
│   │   └── plot_service.py
│   ├── utils/
│   │   └── translators.py
│   ├── routes/
│   │   ├── main_routes.py
│   │   └── plot_routes.py
│   └── config.py
│
├── backend-node/
│   └── server.js
│
├── frontend/
│   ├── js/
│   │   ├── app.js
│   │   ├── api.js
│   │   └── config.js
│   ├── css/
│   └── index.html
│
└── README.md
⚙️ Tech Stack
Backend (Python - Flask)
Flask
Pandas
MySQL (mysql-connector-python)
Data visualization (Matplotlib/Seaborn assumed)
Backend (Node.js)
Express.js
PostgreSQL (pg)
CORS
Frontend
Vanilla JavaScript
HTML/CSS
🗄️ Database Schema
MySQL (Flask Service)

Table: douban_top100_movies

Column	Type
id	INT
title	TEXT
url	TEXT
genres	TEXT
region	TEXT
rating	FLOAT
PostgreSQL (Node API)

Table: douban_movies_top

Column	Type
title	TEXT
genre	TEXT
rating	FLOAT
🔧 Setup & Installation
1. Clone the Repository
git clone https://github.com/your-username/douban-movies.git
cd douban-movies
2. Environment Variables

Create a .env file:

DB_HOST=your_host
DB_PORT=3306
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=your_database
3. Install Dependencies
Python Backend
pip install -r requirements.txt
Node Backend
cd backend-node
npm install
4. Run the Services
Start Flask Server
flask run
Start Node API
node server.js
5. Open Frontend

Open index.html or deploy via GitHub Pages.

📡 API Endpoints
Health Check
GET /api/health
Get Statistics
GET /api/stats
Get All Movies
GET /api/movies
Get Movies by Genre
GET /api/movies/genre/:genre
📊 Visualization Endpoints (Flask)
/plots/avg_rating_by_genre.png
/plots/movie_count_by_genre.png
/plots/rating_distribution_by_genre.png
/plots/heatmap_avg_rating.png
🌍 Translation Layer

The project includes a built-in translator that:

Converts Chinese genres → English
Converts Chinese regions → English
Removes remaining Chinese characters


🔁 Frontend Behavior
Fetches stats from Node API
Dynamically loads plot images from Flask
Auto-refreshes visualizations every 5 minutes
Manual refresh button available
🚀 Deployment
Frontend: GitHub Pages
Node API: Render / Railway
Flask API: Render / Docker

🔮 Future Improvements
Add authentication
Add caching layer (Redis)
Replace static plots with interactive charts (e.g., Chart.js / D3.js)
Unify backend into a single service
Add search & filtering UI

📜 License

MIT License
