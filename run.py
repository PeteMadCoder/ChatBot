from app import create_app
import os

if __name__ == '__main__':
    app = create_app()

    print("Access Fred in this website: http://localhost:5000/index.html")
    
    # Print ALL registered routes for debugging
    print("\n=== REGISTERED ROUTES ===")
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods - set(['HEAD', 'OPTIONS']))
        print(f"{rule.endpoint:15} {methods:15} {rule}")
    print("=========================\n")
    
    # Get port from environment or default to 5000
    port = int(os.getenv('PORT', 5000))
    
    print(f"🚀 Starting chatbot server on port {port}...")
    print("💡 Visit http://localhost:5000 in your browser")
    print("🔄 Press CTRL+C to stop the server\n")
    
    app.run(host='0.0.0.0', port=port, debug=False)