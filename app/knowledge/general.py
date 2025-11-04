from datetime import datetime

def get_rules():
    return [
        # FIXED GREETINGS PATTERN - THIS IS THE KEY CHANGE
        (r'(?i)(hello|hi|hey|greetings)', [  # Notice the parentheses!
            "Hello! How can I help you with your project today?",
            "Hi there! What development challenge can I help you with?"
        ]),
        
        # Help requests
        (r'(?i)(help|support|assist)', [
            "I can help with project setup, deployment, and programming concepts. What do you need?",
            "Ask me about: project structure, deployment options, or specific technologies."
        ]),
        
        # Time questions
        (r'(?i)(time|date|now)', [
            f"The current time is {datetime.now().strftime('%I:%M %p')}.",
            f"Today is {datetime.now().strftime('%A, %B %d')}."
        ]),
        
        # Reset command
        (r'(?i)(reset|start over|new conversation)', [
            "Resetting our conversation. How can I assist you with your project?",
            "Starting fresh! What would you like to discuss about your development project?"
        ])
    ]