# Calculator Application

A simple command-line calculator with JSON output formatting.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Command-line interface with expression parsing
- JSON-formatted output for programmatic use
- Comprehensive unit test suite

## Project Structure

```
.
├── main.py              # Entry point, CLI interface
├── calculator.py        # Calculator class implementation
├── render.py            # JSON output formatter
├── tests.py             # Unit tests
├── pkg/
│   ├── calculator.py    # Package version of Calculator
│   └── render.py        # Package version of JSON formatter
└── README.md            # This file
```

## Installation

No external dependencies are required. The application uses only Python standard library modules.

## Usage

Run the calculator from the command line:

```bash
python main.py "3 + 5"
```

### Examples

```bash
# Addition
python main.py "10 + 20"

# Subtraction
python main.py "100 - 35"

# Multiplication
python main.py "7 * 6"

# Division
python main.py "15 / 3"

# Complex expressions
python main.py "2 * 3 + 5"
python main.py "10 / 2 - 4"
```

If no arguments are provided, the program displays usage information:

```bash
python main.py
```

## API

### Calculator Class

The `Calculator` class provides an `evaluate()` method that parses and computes arithmetic expressions.

```python
from calculator import Calculator

calc = Calculator()
result = calc.evaluate("3 + 5 * 2")  # Returns 13
```

### JSON Output

The `render.format_json_output()` function formats the result as JSON:

```python
from render import format_json_output

output = format_json_output("3 + 5", 8)
# {"expression": "3 + 5", "result": 8}
```

## Testing

Run the unit tests with:

```bash
python tests.py
```

All tests should pass, covering basic operations, complex expressions, and error cases.

## License

This project is open source and available under the MIT License.
