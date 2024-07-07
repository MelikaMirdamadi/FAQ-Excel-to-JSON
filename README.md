
<<<<<<< HEAD
=======

>>>>>>> b3382e4ae3dee7c926680007f223a9f2dbe2817d
---

# FAQ Excel to JSON Converter

## Description
The FAQ Excel to JSON Converter is a Python script designed to automate the conversion of Frequently Asked Questions (FAQ) data from an Excel file into a structured JSON format. This tool is particularly useful for managing and processing bulk FAQ data, enabling easy integration with web applications, databases, or other systems that utilize JSON.

## Features
- **Excel to JSON Conversion:** Reads data from an Excel file and converts it into JSON format.
- **Chunking:** Groups FAQs into chunks for better organization and management.
- **Language Support:** Handles multiple languages, making it suitable for internationalization.
- **Customizable:** Allows easy adjustment of chunk size and other parameters to fit specific needs.

## Requirements
- Python 3.x
- pandas
- openpyxl

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/MelikaMirdamadi/faq-excel-to-json.git
    cd faq-excel-to-json
    ```

2. Install the required Python packages:
    ```sh
    pip install pandas openpyxl
    ```

## Usage
1. Place your Excel file (`Export.xlsx`) in the same directory as the script.
2. Run the script:
    ```sh
    python convert_faq.py
    ```
3. The JSON output will be saved as `faqs.json` in the same directory.

## Example
Given an Excel file (`Export.xlsx`) with columns "سوال" (Question) and "پاسخ" (Answer), the script will process these entries and generate a JSON file structured as follows:
```json
{
    "file_name": "FAQ",
    "languages": "eng+fas",
    "CHUNK__": [
        "Question : ... -> Answer : ...",
        ...
    ]
}
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<<<<<<< HEAD
---
=======
---

>>>>>>> b3382e4ae3dee7c926680007f223a9f2dbe2817d
