# Python URL Validator

A lightweight Python-based URL validator that checks URL formats, protocols, and hostnames through an interactive command-line interface.

## Features

- Validate URL formats.
- Check HTTP and HTTPS protocols.
- Validate hostname and domain presence.
- Detect invalid URL formats.
- Display validation results.
- Support multiple URL checks.
- Interactive command-line interface.

## Technologies Used

- Python
- urllib
- Colorama

## Project Structure

```text
python-url-validator/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone this repository:

```bash
git clone https://github.com/pradipta-web/python-url-validator.git
```

2. Navigate to the project directory:

```bash
cd python-url-validator
```

3. Create a virtual environment:

```bash
py -m venv venv
```

4. Install dependencies:

```bash
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Usage

Run the application:

```bash
.\venv\Scripts\python.exe app.py
```

Enter a URL to check whether its format is valid.

Type `exit` to close the application.

## Example

```text
Enter URL (or type 'exit' to quit):
> https://google.com

Status: VALID
Message: URL format is valid.
```

## Author

**Kinervaaa**

GitHub: https://github.com/pradipta-web