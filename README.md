# MailHunter 🏹 – Extract Emails from Any File Type  

<img src="MailHunter.webp" alt="MailHunter Logo" width="400">

**MailHunter** is a powerful and efficient email scraping tool that hunts and extracts email addresses from various file types, including **PDF, DOCX, CSV, and TXT**. It allows users to **select a directory**, choose a file format, and extract all email addresses from the files within seconds.  
                            
## 🚀 Features  
✅ **Supports Multiple Formats** – Extract emails from PDF, DOCX, CSV, and TXT files.  
✅ **User-Friendly Interface** – Simply enter the folder path and choose the file type.  
✅ **Saves Results** – Stores extracted emails in **JSON and CSV** formats.  
✅ **Fast & Efficient** – Scans hundreds of files quickly.  
✅ **OSINT-Friendly** – Useful for Open-Source Intelligence (OSINT) research.  

## 🔧 Installation  
Make sure you have Python installed. Then, install the required dependencies:  

1. Running the Makefile (Optional)
If you prefer to use the Makefile to automate your setup, follow these steps:
```sh
git clone https://github.com/AutoPwnSec/MailHunter.git
cd MailHunter
```

2. Run the Makefile to install dependencies and start the script:
 ```sh
make run
```
This will first install the required dependencies (if not already installed) and then run the script.


```sh
pip install pdfplumber python-docx pyfiglet
```

📌 Usage
Run the script and follow the prompts:
```sh
python MailHunter.py
```

### 📂 Output Files
emails.json – Stores emails found in each file.
emails.csv – Contains a unique list of all extracted emails.

#### 🎯 Example
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

