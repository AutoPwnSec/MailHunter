import os
import pdfplumber
import re
import json
import csv
import docx

# Function to extract emails from text
def extract_emails(text):
    return re.findall(r"[._+a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+", text)

# Function to process PDF files
def extract_from_pdf(file_path):
    emails = []
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    emails.extend(extract_emails(text))
    except Exception as e:
        print(f"Error processing PDF {file_path}: {e}")
    return list(set(emails))

# Function to process DOCX files
def extract_from_docx(file_path):
    emails = []
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            emails.extend(extract_emails(para.text))
    except Exception as e:
        print(f"Error processing DOCX {file_path}: {e}")
    return list(set(emails))

# Function to process TXT files
def extract_from_txt(file_path):
    emails = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                emails.extend(extract_emails(line))
    except Exception as e:
        print(f"Error processing TXT {file_path}: {e}")
    return list(set(emails))

# Function to process CSV files
def extract_from_csv(file_path):
    emails = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                for cell in row:
                    emails.extend(extract_emails(cell))
    except Exception as e:
        print(f"Error processing CSV {file_path}: {e}")
    return list(set(emails))

# Function to scan selected file type
def scan_files(rootdir, extension, extraction_function):
    email_addresses = {}
    counter = 0

    for subdir, _, files in os.walk(rootdir):
        for file in files:
            if not file.lower().endswith(extension):
                continue

            counter += 1
            full_file_path = os.path.join(subdir, file)
            extracted_emails = extraction_function(full_file_path)

            email_addresses[file] = extracted_emails if extracted_emails else ["-"]

    return email_addresses, counter

# Main menu for file type selection
def main():
    rootdir = input("Enter the folder path to scrape emails from: ").strip()
    
    if not os.path.exists(rootdir):
        print("Error: The provided path does not exist. Please enter a valid folder path.")
        return

    print("\nSelect the file type to scrape emails from:")
    print("1. PDF (.pdf)")
    print("2. Word Document (.docx)")
    print("3. CSV (.csv)")
    print("4. Text File (.txt)")

    choice = input("Enter your choice (1-4): ").strip()

    file_types = {
        "1": (".pdf", extract_from_pdf),
        "2": (".docx", extract_from_docx),
        "3": (".csv", extract_from_csv),
        "4": (".txt", extract_from_txt),
    }

    if choice not in file_types:
        print("Invalid choice! Exiting...")
        return

    extension, extraction_function = file_types[choice]

    print(f"\nScanning for {extension} files in {rootdir}...")
    email_addresses, file_count = scan_files(rootdir, extension, extraction_function)

    # Save results to JSON
    json_file_path = os.path.join(rootdir, "emails.json")
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(email_addresses, json_file, ensure_ascii=False, indent=4)

    # Extract distinct email addresses for CSV
    distinct_emails = set(email for emails in email_addresses.values() for email in emails if email != "-")

    # Save distinct emails to CSV
    csv_file_path = os.path.join(rootdir, "emails.csv")
    with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Email"])
        for email in distinct_emails:
            writer.writerow([email])

    print(f"\n✅ Done! Processed {file_count} files and found {len(distinct_emails)} unique email(s).")
    print(f"📂 Results saved to '{json_file_path}' and '{csv_file_path}'.\n")

if __name__ == "__main__":
    main()
