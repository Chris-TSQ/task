from flask import Flask
from flask_cors import CORS
from config import Config
from routes.main_routes import main_bp
from routes.plot_routes import plot_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    
    app.register_blueprint(main_bp)
    app.register_blueprint(plot_bp, url_prefix='/plots')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)