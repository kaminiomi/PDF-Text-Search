import pdfplumber
import re
import sys

def safe_input(prompt):
    """Safely handle user input to avoid sys.stdin issues in .exe mode."""
    try:
        return input(prompt).strip()
    except (EOFError, AttributeError):
        print(f"{prompt} (input unavailable, skipping)")
        return None

# Take file path and search text as user input
file_path = safe_input("Enter the full PDF file path:")
search_text = safe_input("Enter the text to search for:")

if not file_path or not search_text:
    print("Error: Missing input. Exiting.")
    sys.exit(1)

search_pattern = rf"{search_text}"
page_list = []

try:
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and re.search(search_pattern, text, re.IGNORECASE):
                page_list.append(i + 1)

    if page_list:
        print(f"Pages containing '{search_text}': {page_list}")
    else:
        print(f"No matches found for '{search_text}' in the document.")

except FileNotFoundError:
    print("Error: File not found. Please enter a valid path.")
except Exception as e:
    print(f"An error occurred: {e}")

# Prevent closing in console environments
try:
    input("Press Enter to exit...")
except (EOFError, AttributeError):
    pass
