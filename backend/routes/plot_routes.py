from flask import Blueprint, send_file
from services.data_service import DataService
from services.plot_service import PlotService

plot_bp = Blueprint('plots', __name__)
data_service = DataService()
plot_service = PlotService()

@plot_bp.route("/avg_rating_by_genre.png")
def avg_rating_by_genre():
    df = data_service.get_genres_data()
    df_ex = data_service.prepare_genre_data(df)
    avg = df_ex.groupby('genres_en')['rating'].mean().sort_values(ascending=False)
    buf = plot_service.create_bar_chart(
        avg, 'Average Rating by Genre', 
        'Average Rating', 'steelblue'
    )
    return send_file(buf, mimetype='image/png')

@plot_bp.route("/movie_count_by_genre.png")
def movie_count_by_genre():
    df = data_service.get_genres_data()
    df_ex = data_service.prepare_genre_data(df)
    counts = df_ex['genres_en'].value_counts()
    buf = plot_service.create_bar_chart(
        counts, 'Number of Movies by Genre',
        'Number of Movies', 'coral'
    )
    return send_file(buf, mimetype='image/png')

@plot_bp.route("/rating_distribution_by_genre.png")
def rating_distribution():
    df = data_service.get_genres_data()
    df_ex = data_service.prepare_genre_data(df)
    buf = plot_service.create_boxplot(df_ex)
    return send_file(buf, mimetype='image/png')

@plot_bp.route("/heatmap_avg_rating.png")
def heatmap():
    df = data_service.get_full_data()
    df_ex = data_service.prepare_genre_data(df, include_region=True)
    buf = plot_service.create_heatmap(df_ex)
    return send_file(buf, mimetype='image/png')