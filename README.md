# AI Agent Practice Project

A small Python practice project for exploring how coding agents are built. It contains an OpenRouter-backed prompt CLI, filesystem and Python-execution helper functions intended for a restricted working directory, and a standalone arithmetic calculator.

> **Current state:** The CLI currently sends a prompt to OpenRouter and prints the model response. The helper functions are not yet connected to an agent/tool-calling loop, and the system prompt is a placeholder. This is a learning project, not a production-ready coding agent.

## Requirements

- Python 3.13 or later
- [`uv`](https://docs.astral.sh/uv/) for dependency and environment management
- An OpenRouter API key

## Setup

Clone the repository, enter its directory, install dependencies, and create a local `.env` file:

```bash
uv sync
printf 'OPENAI_API_KEY=your_openrouter_api_key\n' > .env
```

The application reads `OPENAI_API_KEY` from `.env`. Keep this secret out of source control.

## Run the prompt CLI

Pass the prompt as a positional argument; use `--verbose` to print token usage:

```bash
uv run python lib/main.py "What is a coding agent?"
uv run python lib/main.py --verbose "Explain this project"
```

The CLI uses the OpenAI Python client with OpenRouter's API endpoint and the `openrouter/free` model route. Availability and the specific model serving that route are controlled by OpenRouter.

## Project components

- `lib/` — CLI entry point, configuration, prompt, and argument parsing.
- `functions/` — helpers to list files, read file contents, write files, and run Python files.
- `calculator/` — a separate command-line arithmetic calculator and its tests.
- `test/` — tests for the filesystem and Python-execution helpers.

The helper functions accept a working-directory argument and are intended to limit operations to that directory. They are not a secure sandbox: in particular, running a Python file executes its code with the current user's permissions. Use only with trusted code and do not rely on these path checks as a security boundary.

## Calculator

Run an arithmetic expression from the calculator directory:

```bash
cd calculator
python main.py "3 * 4 + 5"
```

The result is printed as JSON. The calculator supports basic arithmetic expressions; see `calculator/tests.py` for examples.

## Tests

Run the helper-function tests from the repository root:

```bash
uv run python -m unittest discover -s test
```

Run the calculator tests:

```bash
uv run python calculator/tests.py
```

## License

No license has been specified for this repository yet.
