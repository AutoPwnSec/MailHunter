.PHONY: install run

# Install dependencies from requirements.txt
install:
	pip install -r requirements.txt

# Run the main Python script (assumed here to be main.py)
run: install
	python MailHunter.py