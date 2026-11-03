import argparse


class Parser:
    _instance = None

    # Implement the singleton pattern
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Parser, cls).__new__(cls)
        return cls._instance

    def __init__(self, data):
        self.data = data

    def setup_argparse(self):
        self.parser = argparse.ArgumentParser(description="OpenRouter CLI")
        # addd the user prompt
        self.parser.add_argument("user_prompt", type=str, help="User prompt")
        self.parser.add_argument(
            "--verbose", action="store_true", help="Enable verbose output"
        )
        return self.parser
