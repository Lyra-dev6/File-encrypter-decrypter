# Automated file encrypter and decrypter

An automated file encrypter and decrypter made with Python. Project #2 of Python in my coding journey.

## Overview
This is my fifth project, and I wanted to figure out how to actually protect real files on my computer. Instead of a web app, I made a clean Python script that takes a file, scrambles it into complete gibberish, and can unlock it back to normal. It automatically generates a secure key file and handles the encryption locally. 

## How to Run It
Since this is a Python script, you just need Python installed on your computer to run it:

### Step 1: Install the Requirements
Open your terminal inside the project folder and install the cryptography library:
```bash
pip install cryptography
```

### Step 2: Run the Script
Launch the script by running the main file:
```bash
python main.py
```
*(Note: If you're on a Mac, you might need to type `python3 main.py` instead).*

## Features
* **Fernet Encryption:** Uses super secure cryptography standard to lock files so they can't be cracked.
* **Auto Key Generation:** Automatically creates a unique `encryption.key` file so you don't have to make one yourself.
* **In-Place Swapping:** Directly overwrites the file with encrypted/decrypted data so no extra copies are left floating around.
* **Test Mode:** Automatically creates a test file (`my_secret_document.txt`) right away to show you how it works.

## What I Learned
* **File I/O in Binary:** Figured out how to read and write files in binary mode (`rb` and `wb`) so it can handle more than just standard text.
* **Cryptography Concepts:** Learned how symmetric encryption works and why keeping the key safe is the most important part.
* **The Cryptography Library:** Learned how to import and use the `Fernet` module to handle the heavy math for scrambling data.
* **Conditional Main Blocks:** Used `if __name__ == '__main__':` properly to organize my test code from the main functions.

## Status
Completed

## Author
- Lyra Mgaram


