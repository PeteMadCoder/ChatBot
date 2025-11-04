from flask import Flask
import os

def create_app():
    """Create and configure the Flask application"""
    # Create app with proper static folder path
    app = Flask(__name__)
    
    # Register routes AFTER app creation
    from . import routes
    routes.init_app(app)
    
    return app