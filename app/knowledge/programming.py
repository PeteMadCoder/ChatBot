def get_rules():
    return [
        # Python questions
        (r'(?i)python|flask|django', [
            "Python is excellent for backend development. Flask is lightweight for small projects, Django for larger ones.",
            "For Python projects: use virtual environments, follow PEP8, and structure code with clear modules."
        ]),
        
        # JavaScript questions
        (r'(?i)javascript|react|vue|angular', [
            "JavaScript frameworks: React (flexible), Vue (approachable), Angular (comprehensive). Choose based on project needs.",
            "Modern JS tip: Use ES6+ features like async/await, modules, and destructuring for cleaner code."
        ]),
        
        # Debugging
        (r'(?i)debug|bug|error|issue', [
            "Debugging strategy: 1) Reproduce consistently 2) Isolate the problem 3) Fix incrementally 4) Verify",
            "Use print statements strategically or browser dev tools. Rubber duck debugging often reveals solutions!"
        ]),
        
        # Best practices
        (r'(?i)best practice|good practice|should i', [
            "General best practices: write modular code, document as you go, test early, and version control everything.",
            "Focus on: readable code, small commits, and automated testing where possible."
        ])
    ]