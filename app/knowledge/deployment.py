def get_rules():
    return [
        # Deployment questions
        (r'(?i)deploy|deployment|host|server|production', [
            "For deployment, consider: 1) Your infrastructure needs 2) Scaling requirements 3) Maintenance strategy",
            "Common deployment options: cloud services (AWS), containers (Docker), or traditional servers"
        ]),
        
        # Cloud deployment
        (r'(?i)cloud|aws|azure|gcp|google cloud', [
            "Cloud deployment offers scalability but requires understanding of IAM, networking, and cost management.",
            "For cloud deployment, start with a simple architecture and expand as needed. AWS Elastic Beanstalk is beginner-friendly."
        ]),
        
        # Containerization
        (r'(?i)docker|container|kubernetes|k8s', [
            "Docker simplifies deployment by packaging apps and dependencies. Start with a Dockerfile for your project.",
            "For containers: 1) Create Dockerfile 2) Build image 3) Run container 4) Consider orchestration for multiple services"
        ]),
        
        # Specific platforms
        (r'(?i)vercel|netlify|heroku', [
            "Vercel/Netlify are great for frontend apps with automatic CI/CD. Heroku works well for simple backend services.",
            "These platforms offer free tiers for small projects but have limitations on scaling and customization."
        ])
    ]