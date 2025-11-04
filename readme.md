# Fred - The cool Chatbot

![Fred Chatbot](/fred.png)

Fred is a **100% self-contained rule-based chatbot** designed specifically to be expanded. 

## Features

- **Pure rule-based system** - No AI models or external dependencies
- **Instant responses** - No waiting for model inference
- **Easy to customize** - Add new knowledge in minutes
- **100% offline** - Works without internet connection
- **Lightweight** - Minimal resource usage (under 50MB RAM)
- **Multilingual** - Currently optimized for English (easily expandable)
- **Fred's personality** - Friendly, helpful assistant with consistent voice

## Project Structure

``` bash
ChatBot/
├── app/
│   ├── __init__.py        # Flask application factory
│   ├── routes.py          # API endpoints and route definitions
│   ├── chatbot.py         # Fred's core logic and rule engine
│   └── knowledge/         # Fred's knowledge base (expandable)
│       ├── __init__.py
│       ├── general.py     # General conversation rules
|       └── other_rules.py # Rules of the model
├── static/
│   └── index.html         # Chat interface
├── venv/                  # Python virtual environment (not committed)
├── run.py                 # Application entry point
├── requirements.txt       # Python dependencies
└── README.md              # You're reading this!
```

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- Git (optional)

### 2. Installation

```bash
# Clone the repository (if using Git), or just download zip and extract

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. File Contents

**requirements.txt**:
```
flask
python-dotenv
```

## Running Fred

```bash
# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Start Fred
python run.py               # Depending on system, it may be python3 run.py
```

Visit `http://localhost:5000` in your browser to interact with Fred.

## Testing Fred

You can test Fred directly via curl:

```bash
# Test greeting
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"message": "Hello"}'
```


## Expanding Fred's Knowledge

Fred's knowledge is stored in the `app/knowledge/` directory. Adding new knowledge is simple:

### 1. Create a New Knowledge Module

```bash
touch app/knowledge/my_new_topic.py
```

### 2. Add Rules to the Module

```python
def get_rules():
    return [
        # Pattern 1
        (r'(?i)(keyword1|keyword2)', [
            "First response when pattern matches",
            "Second response (shown next time same pattern matches)"
        ]),
        
        # Pattern 2
        (r'(?i)(another|pattern)', [
            "Response for this pattern"
        ])
    ]
```

### 3. Restart Fred

Fred will automatically load your new knowledge module on restart.

### Example: Adding API Documentation Knowledge

Create `app/knowledge/api_docs.py`:

```python
def get_rules():
    return [
        (r'(?i)(api|endpoint|request)', [
            "Our API uses RESTful principles with JSON responses.",
            "All endpoints require authentication via Bearer token."
        ]),
        
        (r'(?i)(rate limit|throttle)', [
            "API rate limit is 100 requests/minute per user.",
            "Exceeding limits returns 429 status code with retry-after header."
        ])
    ]
```

## Customizing Fred's Personality

Fred's personality comes from his responses. To customize:

1. **Edit existing knowledge modules** in `app/knowledge/`
2. **Add Fred's signature phrases** to responses:
   ```python
   [
       "Fred here! Our API uses RESTful principles with JSON responses.",
       "Fred's tip: All endpoints require authentication via Bearer token."
   ]
   ```
3. **Add fallback responses** in `app/knowledge/general.py`

## Configuration

Fred has minimal configuration needs:

- **Port**: Set via environment variable `PORT` (default: 5000)
  ```bash
  export PORT=8080
  python run.py
  ```

## Troubleshooting

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| Routes not found (404) | Verify your directory structure matches the documentation |
| Knowledge modules not loading | Check console for "✅ Fred loaded: [module]" messages |
| Responses not matching | Use `curl` tests to verify rule matching |
| Greetings not working | Ensure regex patterns use `(?i)` for case-insensitivity |
| Time displays incorrectly | Verify datetime is imported in knowledge modules |

### Debugging Fred

Add this to `run.py` before `app.run()`:

```python
@app.route('/debug-rules', methods=['GET'])
def debug_rules():
    """Show all loaded rules for debugging"""
    rules_list = []
    for pattern, responses in chatbot.rules:
        rules_list.append({
            "pattern": pattern,
            "response_count": len(responses),
            "sample_response": responses[0] if responses else ""
        })
    return jsonify(rules_list)
```

Visit `http://localhost:5000/debug-rules` to see all loaded rules.


## Contact

For support or questions, please open an issue in this repository.