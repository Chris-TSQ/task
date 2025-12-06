/**
 * Configuration settings
 */

const CONFIG = {
    // API base URL
    // API_BASE_URL: 'http://localhost:5000',
    // ✅ ADDED:
    API_BASE_URL: window.location.hostname === 'localhost' 
        ? 'http://localhost:5000' 
        : 'https://douban-movies-api.onrender.com'
        
    // Plot filename mappings
    PLOT_MAPPINGS: {
        'avg-rating': 'avg_rating_by_genre',
        'movie-count': 'movie_count_by_genre',
        'rating-dist': 'rating_distribution_by_genre',
        'heatmap': 'heatmap_avg_rating'
    },
    
    // Auto-refresh interval (milliseconds)
    AUTO_REFRESH_INTERVAL: 300000, // 5 minutes
    
    // Request timeout (milliseconds)
    REQUEST_TIMEOUT: 10000
};