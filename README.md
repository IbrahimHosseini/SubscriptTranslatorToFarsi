
# Language Translator App

A simple Python application to translate text from one language to another. This app uses the [deep-translator](https://pypi.org/project/deep-translator/) package to enable fast and accurate translations. It includes an editable source file, making it flexible and easy to adapt to your specific needs.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [License](#license)

## Introduction

This Python app allows you to easily translate text from any source language to any target language using the `deep-translator` package. It is ideal for handling text or file-based translations, such as `.srt` subtitle files. The source file is editable, enabling users to quickly adapt it to their specific use case.

## Features

- **Multi-language Support**: Translate between any supported languages.
- **Customizable Source and Target**: Configure the languages as needed.
- **Editable Source File**: Modify the script to fit your requirements.
- **File-Based Translation**: Supports working with subtitle files like `.srt`.

## Installation

1. Clone this repository or download the script:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required Python package:
   ```bash
   pip install deep-translator
   ```

## Usage

1. Modify the script as needed:
   - Set the **source language** (`source`) and **target language** (`target`) in the translator configuration.
   - Update file paths or contents based on your use case.

2. Run the script:
   ```bash
   python SubscriptTranslator.py
   ```

3. Check the output file. By default, the translated content will be saved to `dest_sub.srt`.

### Example Configuration

By default:
- **Source Language**: Auto-detected (`source='auto'`).
- **Target Language**: Farsi (`target='fa'`).
- **Source File**: `src_sub.srt`.
- **Output File**: `dest_sub.srt`.

To customize the translation:
```python
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='en', target='es')  # From English to Spanish
```

## Dependencies

This app requires the following package:
- [deep-translator](https://pypi.org/project/deep-translator/)  
  Install it using pip:
  ```bash
  pip install deep-translator
  ```

## Configuration

- **Languages**: Modify the `GoogleTranslator` settings for `source` and `target` languages.
- **File Paths**: Update the file path variables in the script to match your input and output files:
  ```python
  file_path = "./my_directory"
  src_file_name = "my_file.srt"
  dest_file_name = "my_translated_file.srt"
  ```

## License

This project is licensed under the MIT License, allowing you to freely use, modify, and distribute it.
