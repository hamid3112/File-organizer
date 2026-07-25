<p align="center">
  <img src="./assets/file-organizer-banner.svg" alt="File Organizer" width="100%">
</p>

<p align="center">
  A lightweight Python script that automatically organizes files by their extensions.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Dependencies-None-success" alt="No Dependencies">
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows" alt="Windows">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License">
</p>

---

## About the Project

**File Organizer** is a simple Python automation tool that scans the Downloads directory and copies files into categorized folders based on their extensions.

It helps keep cluttered directories clean and structured without requiring any external Python packages.

## Features

- Recursively scans files and subdirectories
- Automatically detects file types by extension
- Creates category folders when they do not exist
- Preserves file metadata during copying
- Supports uppercase and lowercase extensions
- Prevents files inside the output directory from being processed again
- Uses only Python's standard library

## Supported Categories

| Category | Supported Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`, `.webp` |
| Documents | `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv` |
| Audio | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg` |
| Archives | `.zip`, `.rar`, `.tar`, `.gz`, `.7z` |

## How It Works

The script scans the selected base directory:

```text
Downloads/
```

It then creates a structured output directory:

```text
Downloads/
└── sorted/
    ├── images/
    ├── documents/
    ├── videos/
    ├── audio/
    └── archives/
```

Each supported file is copied into its corresponding category folder.

## Requirements

- Python 3.14 or newer
- No third-party dependencies

Check your Python version:

```bash
python --version
```

## Installation

Clone the repository:

```bash
git clone https://github.com/hamid3112/File-organizer.git
```

Navigate to the project directory:

```bash
cd File-organizer
```

## Usage

Run the script:

```bash
python file_organizer.py
```

By default, the script organizes files located in:

```text
C:\Users\iTop_Store\Downloads
```

To use another directory, update this line:

```python
base_directory = Path(r"C:\Users\YourUsername\Downloads")
```

## Customisation

New extensions can be added to the `FILE_CATEGORIES` dictionary:

```python
FILE_CATEGORIES = {
    "images": [".jpg", ".png", ".webp"],
    "documents": [".pdf", ".docx", ".txt"],
    "code": [".py", ".js", ".html", ".css"]
}
```

You can also create completely new categories by adding another dictionary entry.

## Important Note

The current version **copies** files into the `sorted` directory and keeps the original files unchanged.

Files with identical names may overwrite each other when they are copied into the same category folder.

## Future Improvements

- Handle duplicate filenames automatically
- Add a graphical user interface
- Allow users to select the source directory
- Add support for moving files instead of copying
- Add logging and operation reports
- Organize files by creation date

## Author

Developed by [Hamid](https://github.com/hamid3112).

## License

This project is available under the MIT License.

---

<p align="center">
  Made with Python and a desire for cleaner folders.
</p>
