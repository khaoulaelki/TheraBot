# TheraBot – AI Chatbot Prototype

## 1. Overview

TheraBot is an educational AI chatbot prototype built with Python. It uses a conversational transformer model to generate responses and provides a web interface for interaction.

This project is not a medical service or a substitute for professional mental health support.

## 2. Technologies

- Python 3.13+
- uv – Dependency and build management
- Flask – Backend REST API
- Streamlit – Frontend interface
- Transformers – Pre-trained conversational model
- PyTorch – Deep learning framework
- Requests – HTTP communication
- Pytest – Automated testing

## 3. Project Structure

```text
TheraBot/
├── app.py
├── chatbot.py
├── frontend.py
├── tests/
│   └── test_app.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

## 4. Installation

Install [uv](https://docs.astral.sh/uv/), then clone the repository:

```bash
git clone https://github.com/khaoulaelki/TheraBot.git
cd TheraBot
```

Install the project dependencies using the lockfile:

```bash
uv sync --locked --all-groups
```

## 5. Build

Build the source distribution and Python Wheel:

```bash
uv build
```

The generated files are available in the `dist/` directory.

## 6. Testing

Run the automated tests with:

```bash
uv run pytest
```

The tests verify the Flask chat endpoint, including predefined responses and the fallback chatbot call. The AI model is mocked in the tests to avoid loading it during test execution.

## 7. Code Verification

Check the Python source files for syntax errors:

```bash
uv run python -m compileall -q app.py chatbot.py frontend.py
```

## 8. Run the Application

Start the Flask backend:

```bash
uv run python app.py
```

In a second terminal, start the Streamlit frontend:

```bash
uv run streamlit run frontend.py
```

Open the local URL displayed by Streamlit in your browser.

The first chatbot startup may require an internet connection to download the pre-trained DialoGPT-small model.

## 9. Dependency Management

- `pyproject.toml`: project metadata and dependencies.
- `uv.lock`: exact resolved dependency versions.
- `uv sync --locked --all-groups`: reproducible dependency installation, including development dependencies.
- `uv build`: package generation.