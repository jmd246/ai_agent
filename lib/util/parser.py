import argparse
class Parser:
    def __init__(self, data):
        self.data = data
    def setup_argparse(self):
        self.parser = argparse.ArgumentParser(description="OpenRouter CLI")
        # addd the user prompt
        self.parser.add_argument("user_prompt", type=str, help="User prompt")
        self.parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
        
        return self.parser