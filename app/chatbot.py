import re
import os
import importlib
import pkgutil

class SimpleChatbot:
    """Fred - A pure rule-based chatbot with no extra logic"""
    
    def __init__(self):
        self.rules = []
        self.rule_counters = {}  # Tracks which response to use next for each rule
        self.load_knowledge_modules()
    
    def load_knowledge_modules(self):
        """Load all knowledge modules from /knowledge directory"""
        knowledge_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'knowledge')
        
        # Clear existing rules
        self.rules = []
        
        # Load all knowledge modules
        for _, module_name, _ in pkgutil.iter_modules([knowledge_path]):
            try:
                module = importlib.import_module(f'app.knowledge.{module_name}')
                if hasattr(module, 'get_rules'):
                    rules = module.get_rules()
                    self.rules.extend(rules)
                    print(f"✅ Fred loaded: {module_name} ({len(rules)} rules)")
            except Exception as e:
                print(f"⚠️ Fred couldn't load {module_name}: {str(e)}")
        
        # Ensure we have a fallback rule
        if not any(r[0] == r'.+' for r in self.rules):
            self.rules.append((r'.+', [
                "I don't understand! Could you rephrase?",
                "You're breaking my circuits. Ask somehting I know."
            ]))

    def respond(self, user_input):
        """Fred's pure rule-matching response system"""
        # Try each rule in order
        for pattern, responses in self.rules:
            if re.search(pattern, user_input):
                # Rotate through responses for this rule
                idx = self.rule_counters.get(pattern, 0) % len(responses)
                self.rule_counters[pattern] = idx + 1
                
                # Handle both strings and lambdas
                response = responses[idx]
                return response() if callable(response) else response
        
        # Fallback (should never happen due to .+ rule)
        return "I'm crashing out."