# PDF Text Search Script

## 📌 Overview
This Python script allows users to search for specific text within PDF files and returns the page numbers containing the text.

## 🔧 Features
- Extracts text from PDF files.
- Searches for a user-specified keyword.
- Outputs page numbers where the keyword is found.
- Handles file errors gracefully.

## 🛠 Installation
1. Install Python 3 if not already installed.
2. Install dependencies using:
   ```bash
    pip install pdfplumber pyinstaller

## ⚡ Convert to `.exe` (Optional)
If you want to create a standalone `.exe` file, follow these steps:
1. Open **Command Prompt** or **Git Bash** and navigate to your project folder:
   ```bash
   cd path/to/your/project

2. Run the following command:
   ```bash
   pyinstaller --onefile search_pdf.py

3. This will create an .exe file inside the dist/ folder.

4. Now, you can run search_pdf.exe without needing Python installed.

💡 Note: This .exe file is Windows-only.