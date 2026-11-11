# AI Agent Practice Project

This repository is a small, educational project for understanding how a coding agent can operate inside a constrained working directory. It uses an LLM via OpenRouter, exposes a small set of file and execution tools, and demonstrates how an agent can read files, write files, and run Python code in a controlled environment.

The goal is to make the internals of agent/tool orchestration explicit and easy to study rather than hiding them behind a large framework.

## What this project does

- Sends a user prompt to OpenRouter
- Lets the model decide whether it needs tool calls
- Invokes a few helper functions to inspect or modify files
- Runs Python code from the project workspace
- Keeps the agent focused on a working directory instead of unrestricted filesystem access

## Current capabilities

The agent currently exposes these tools:

- `get_files_info` — list files and directories
- `get_file_content` — read file contents up to a limit
- `write_file` — create or overwrite a file
- `run_python_file` — execute a Python file with optional arguments

These tools are intentionally simple and are designed for experimentation. They are not a secure sandbox and should not be used with untrusted code.

## Requirements

- Python 3.13+
- [`uv`](https://docs.astral.sh/uv/)
- An OpenRouter API key

## Setup

Clone the repository and install dependencies:

```bash
uv sync
```

Create a local `.env` file with your API key:

```bash
printf 'OPENAI_API_KEY=your_openrouter_api_key\n' > .env
```

The app reads `OPENAI_API_KEY` from `.env` using `pydantic-settings`.

## Running the agent

From the repository root:

```bash
uv run python main.py "What is a coding agent?"
```

Verbose mode shows tool calls and token information:

```bash
uv run python main.py --verbose "List the files in the working directory"
```

This project uses the OpenAI Python client pointed at OpenRouter's API endpoint and the `openrouter/free` model route.

## Project structure

- `main.py` — CLI entry point
- `agent.py` — agent loop and tool orchestration
- `call_functions.py` — mapping between model tool calls and Python helpers
- `config.py` — loads environment configuration
- `functions/` — filesystem and execution tools
- `lib/` — prompt and CLI-related utilities
- `calculator/` — standalone calculator example used as a simple test target
- `test/` — unit tests for helper functionality

## Safety notes

This project is an educational prototype, not a hardened production agent runtime.

Important caveats:

- Tool use is constrained to a working directory, but the implementation is not a secure sandbox.
- Running Python code executes within the current user's environment and permissions.
- Sensitive values such as API keys should never be committed to source control.

## Calculator example

There is also a small calculator app in `calculator/`.

Run it from the repository root:

```bash
uv run python calculator/main.py "3 * 4 + 5"
```

## Tests

Run helper tests:

```bash
uv run python -m unittest discover -s test
```

Run the calculator tests:

```bash
uv run python calculator/tests.py
```

## Notes

This project is intentionally small and explicit. It is useful for learning:

- how model tool calls are structured
- how a tool layer can be injected around an LLM
- how to keep a coding agent inside a working directory
- how to build a toy agent loop without depending on a large framework

## License

No license has been specified for this repository yet.
