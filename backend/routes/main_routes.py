from flask import Blueprint, jsonify, render_template_string
from services.data_service import DataService
import time

main_bp = Blueprint('main', __name__)
data_service = DataService()

@main_bp.route("/")
def home():
    ts = int(time.time())
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Douban Movies</title>
        <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
        <div class="container">
            <h1>🎬 Douban Top 100 Movies</h1>
            <div class="controls">
                <a href="/api/movies" class="btn">View JSON Data</a>
            </div>
            <div class="plot">
                <h2>1. Average Rating by Genre</h2>
                <img src="/plots/avg_rating_by_genre.png?v={ts}" alt="Avg Rating">
            </div>
            <div class="plot">
                <h2>2. Number of Movies per Genre</h2>
                <img src="/plots/movie_count_by_genre.png?v={ts}" alt="Movie Count">
            </div>
            <div class="plot">
                <h2>3. Rating Distribution</h2>
                <img src="/plots/rating_distribution_by_genre.png?v={ts}" alt="Distribution">
            </div>
            <div class="plot">
                <h2>4. Genre × Region Heatmap</h2>
                <img src="/plots/heatmap_avg_rating.png?v={ts}" alt="Heatmap">
            </div>
        </div>
        <script src="/static/js/app.js"></script>
    </body>
    </html>
    """)

@main_bp.route("/api/movies")
def api_movies():
    return jsonify(data_service.get_all_movies())