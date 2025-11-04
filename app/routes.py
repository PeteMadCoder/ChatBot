from flask import request, jsonify, send_from_directory
from .chatbot import SimpleChatbot
import os

def init_app(app):
    """Initialize routes for the application"""
    # Create chatbot instance
    chatbot = SimpleChatbot()
    
    # Set static folder path
    app.static_folder = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
        'static'
    )
    
    @app.route('/')
    def index():
        return send_from_directory(app.static_folder, 'index.html')
    
    @app.route('/<path:path>')
    def static_proxy(path):
        return send_from_directory(app.static_folder, path)
    
    @app.route('/chat', methods=['POST'])
    def chat():
        try:
            data = request.get_json()
            if not data or 'message' not in data:
                return jsonify({'error': 'No message provided'}), 400
                
            user_message = data['message']
            app.logger.info(f"User: {user_message}")
            
            # Get response from our rule-based system
            response = chatbot.respond(user_message)
            app.logger.info(f"Bot: {response}")
            
            return jsonify({'reply': response})
            
        except Exception as e:
            app.logger.error(f"Error: {str(e)}", exc_info=True)
            return jsonify({'reply': 'I encountered an error processing your message'}), 500

    @app.route('/reset', methods=['POST'])
    def reset():
        """Reset conversation state"""
        response = chatbot.reset()
        return jsonify({'reply': response})