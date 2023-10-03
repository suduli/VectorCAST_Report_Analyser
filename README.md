# Directory Tree Generator and File Extractor

This Python script generates a directory tree of the current directory and extracts specific filenames based on given patterns. The extracted data is then saved to an Excel file.

## Features

- Generates a directory tree of the current directory.
- Extracts filenames based on specific patterns (e.g., `.Full_Report.html`, `.Metrics_Report.html`, and `.Testcase_Management_Report.html`).
- Saves the extracted data to an Excel file named `output.xlsx`.

## Requirements

- Python 3.9+
- Pandas
- openpyxl (for saving to Excel)

You can install the required packages using pip:

```bash
pip install pandas openpyxl
```

## Usage

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Run the script:

```bash
python <script-name>.py
```

3. The script will generate a directory tree of the current directory, extract specific filenames, and save the data to `output.xlsx`.

## Functions

- `extract_file_names(content, pattern)`: Extracts filenames from content based on a given pattern.
- `generate_tree(directory, output_file)`: Generates a directory tree and saves it to an output file.
- `pad_lists_to_same_length(*lists)`: Pads lists with `None` until they all have the same length.

## Contribution

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss the proposed change.

---
