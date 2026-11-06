# AI Agent Practice Project

A small Python project for exploring coding-agent concepts. It combines an OpenRouter-backed command-line interface with filesystem and Python-execution tools, plus a standalone arithmetic calculator.

> **Project status:** The CLI sends a prompt to OpenRouter and can dispatch tool calls returned by the model. It currently handles the initial response only; it does not send tool results back to the model for a follow-up response, so this is not yet a complete agent loop.

## Requirements

- Python 3.13 or later
- [`uv`](https://docs.astral.sh/uv/) for dependency and environment management
- An OpenRouter API key

## Setup

Clone the repository, enter its directory, install dependencies, and add your API key to a local `.env` file:

```bash
uv sync
printf 'OPENAI_API_KEY=your_openrouter_api_key\n' > .env
```

The application reads `OPENAI_API_KEY` from `.env`. Keep this secret out of source control. **Note:** the current CLI prints the final four characters of the configured key when it starts; avoid sharing terminal output or logs that may contain this value.

## Run the AI CLI

Run `main.py` from the repository root and pass a prompt as a positional argument. Add `--verbose` to show token usage and tool output:

```bash
uv run python main.py "What is a coding agent?"
uv run python main.py --verbose "List the files in the working directory"
```

The CLI uses the OpenAI Python client with OpenRouter's API endpoint and the `openrouter/free` model route. OpenRouter controls route availability and which model serves a request. The current tool dispatcher sets its working directory to `./calculator`, so the model's filesystem and Python tools operate there rather than across the repository.

## Available tools and safety

The model can request these helper operations:

- `get_files_info` — list entries in a directory.
- `get_file_content` — read a file, up to 10,000 characters.
- `write_file` — write a file and create parent directories as needed.
- `run_python_file` — execute a Python file, with optional arguments and a 30-second timeout.

The helpers are intended to constrain paths to their working directory, but they are **not a secure sandbox**. In particular, executing a Python file runs its code with the current user's permissions. Only run this project and its tools with code and files you trust.

## Calculator

The calculator is a separate command-line program. Run it from its directory with an arithmetic expression in quotes:

```bash
cd calculator
python main.py "3 * 4 + 5"
```

It prints the result as JSON. See `calculator/tests.py` for examples of supported expressions.

## Tests

Run the helper-function tests from the repository root:

```bash
uv run python -m unittest discover -s test
```

Run the calculator tests:

```bash
uv run python calculator/tests.py
```

## Project layout

- `main.py` — AI CLI entry point.
- `config.py` — loads the OpenRouter API key from `.env`.
- `lib/` — prompt, command-line argument parsing, and tool dispatch.
- `functions/` — filesystem and Python-execution tool implementations.
- `calculator/` — standalone calculator application and tests.
- `test/` — tests for the helper functions.

## License

No license has been specified for this repository yet.
