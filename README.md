# MailHunter 🏹 – Extract Emails from Any File Type  

**MailHunter** is a powerful and efficient email scraping tool that hunts and extracts email addresses from various file types, including **PDF, DOCX, CSV, and TXT**. It allows users to **select a directory**, choose a file format, and extract all email addresses from the files within seconds.  

## 🚀 Features  
✅ **Supports Multiple Formats** – Extract emails from PDF, DOCX, CSV, and TXT files.  
✅ **User-Friendly Interface** – Simply enter the folder path and choose the file type.  
✅ **Saves Results** – Stores extracted emails in **JSON and CSV** formats.  
✅ **Fast & Efficient** – Scans hundreds of files quickly.  
✅ **OSINT-Friendly** – Useful for Open-Source Intelligence (OSINT) research.  

## 🔧 Installation  
Make sure you have Python installed. Then, install the required dependencies:  

```sh
pip install pdfplumber python-docx
```
📌 Usage
Run the script and follow the prompts:
```sh
python mailhunter.py
```

Enter the folder path where the files are located.
Select the file type to scan.
MailHunter will extract all email addresses and save them in:
emails.json – Emails categorized by file.
emails.csv – A list of unique emails.
📂 Output Files
emails.json – Stores emails found in each file.
emails.csv – Contains a unique list of all extracted emails.

🎯 Example
Enter the folder path to scrape emails from: /Users/John/Documents
Select the file type to scrape emails from:
1. PDF (.pdf)
2. Word Document (.docx)
3. CSV (.csv)
4. Text File (.txt)
Enter your choice (1-4): 2

✅ Done! Processed 5 files and found 12 unique email(s).
📂 Results saved to '/Users/John/Documents/emails.json' and '/Users/John/Documents/emails.csv'.
⚠️ Disclaimer
This tool is designed for educational and legal use only. Misuse for illegal purposes is strictly prohibited.

🛠 Contributing
Feel free to submit issues or feature requests!

📜 License
MIT License


### **📌 Steps to Upload on GitHub**  
1. Create a **new repository** on GitHub (e.g., `MailHunter`).  
2. Clone the repository:  
   ```sh
   git clone https://github.com/your-username/MailHunter.git
   cd MailHunter
   ```

