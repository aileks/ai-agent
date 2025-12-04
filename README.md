# AI Agent

An AI-powered code assistant that uses Google's Gemini API to perform file operations and execute Python code within a restricted working directory.

## Features

- **File Operations**: List files and directories, read file contents, and write/overwrite files
- **Code Execution**: Run Python files with optional arguments
- **Secure Sandbox**: All operations are restricted to a configurable working directory
- **Function Calling**: Uses Gemini's function calling capabilities to perform actions based on natural language prompts

## Requirements

- Python >= 3.11
- `uv` >= 0.9
- Google Gemini API key

## Installation

1. Clone this repository:

```bash
git clone https://github.com/aileks/ai-agent
cd ai-agent
```

2. Install dependencies using `uv` (or your preferred package manager):

```bash
uv sync
```

## Configuration

1. Create a `.env` file in the project root:

```bash
GEMINI_API_KEY=your_api_key_here
```

2. Configure the working directory and other settings in `config.py`:
   - `WORKING_DIR`: The directory where file operations are allowed (default: `./calculator`)
   - `MAX_ITERS`: Maximum number of iterations for the agent loop (default: `20`)
   - `MAX_FILE_CONTENT_LENGTH`: Maximum file content length to read (default: `10000`)

## Usage

Run the agent with a natural language prompt:

```bash
python main.py "your prompt here"
```

For verbose output (showing function calls and token usage):

```bash
python main.py "your prompt here" --verbose
```

### Example

```bash
python main.py "List all files in the current directory and read the main.py file"
```

## Available Functions

The agent can call the following functions:

- **get_files_info**: List files and directories in the working directory
- **get_file_content**: Read the contents of a file
- **write_file**: Write or overwrite a file
- **run_python_file**: Execute a Python script

All paths are relative to the configured working directory for security.

## Project Structure

```
ai-agent/
├── main.py              # Main entry point
├── config.py            # Configuration settings
├── prompts.py           # System prompt for the AI agent
├── call_function.py     # Function calling logic
├── functions/           # Available function implementations
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── calculator/          # Default working directory
└── pyproject.toml       # Project dependencies
```

## Development

Install development dependencies:

```bash
uv sync --group dev
```

Run linting:

```bash
ruff check .
```
