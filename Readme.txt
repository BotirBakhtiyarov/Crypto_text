# Security Text App Documentation

## Overview

The Security Text App is a Tkinter-based graphical user interface (GUI) application designed to encrypt and decrypt text using a simple XOR encryption method. The application allows users to input text and a numeric key to secure their text data and retrieve it when needed.

## Table of Contents

1. [Setup and Installation](#setup-and-installation)
2. [Application Layout](#application-layout)
3. [Encryption Functionality](#encryption-functionality)
4. [Decryption Functionality](#decryption-functionality)
5. [Main Window](#main-window)
6. [About Section](#about-section)
7. [Running the Application](#running-the-application)

## Setup and Installation

### Prerequisites

- Python 3.x installed on your system.
- Tkinter library (usually comes with Python installation).

### Installation

1. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/BotirBakhtiyarov/Crypto_text.git
   cd security-text-app
   ```

2. **Install Dependencies**: No external dependencies are required other than Tkinter.

## Application Layout

The application consists of a main window and two secondary windows for encryption and decryption. Each window has a black background (`#0d0d0d`) with green text (`#008000`).

### Main Window

The main window contains:
- A welcome label.
- Two buttons for opening the encryption and decryption windows.
- An "About" section that provides information about the application in both English and Chinese.

### Encryption Window

The encryption window contains:
- A welcome label.
- An entry field for the encryption key.
- A text area for the plaintext to be encrypted.
- A submit button to perform the encryption.
- A text area to display the encrypted text.

### Decryption Window

The decryption window contains:
- A welcome label.
- An entry field for the decryption key.
- A text area for the encrypted text to be decrypted.
- A submit button to perform the decryption.
- A text area to display the decrypted text.

## Encryption Functionality

The encryption functionality uses a simple XOR encryption method with a numeric key.

### XOR Encryption Method
```python
def xor_encrypt(key, plaintext):
    ciphertext = ""
    for char in plaintext:
        encrypted_char = chr(ord(char) ^ key)
        ciphertext += encrypted_char
    return ciphertext
```

### Encryption Process
1. The user inputs the plaintext and a numeric key.
2. When the "Submit" button is clicked, the plaintext is encrypted using the `xor_encrypt` function.
3. The encrypted text is displayed in a text area.

### Encryption Function in the GUI
```python
def encrypt_fuc():
    # ... (create encryption window and widgets)
    
    def do():
        word = en_word.get('1.0', 'end')
        key = int(key_word.get())
        plaintext = word
        ciphertext = xor_encrypt(key, plaintext)
        
        en_lab_word = Label(en_root, text="Your encrypted text:", font=('Helvetica', 10), fg="#008000", bg="#0d0d0d")
        en_lab_word.grid(row=5, column=0)
        
        den_word = Text(en_root, height=5, width=30, font=('Helvetica', 20), fg="#008000", bg="#0d0d0d")
        den_word.grid(row=6, column=0, columnspan=2, padx=20, pady=5)
        den_word.insert('1.0', ciphertext)
```

## Decryption Functionality

The decryption functionality also uses a simple XOR method with a numeric key, identical to the encryption key.

### XOR Decryption Method
```python
def xor_decrypt(key, ciphertext):
    plaintext = ""
    for char in ciphertext:
        decrypted_char = chr(ord(char) ^ key)
        plaintext += decrypted_char
    return plaintext
```

### Decryption Process
1. The user inputs the ciphertext and the numeric key.
2. When the "Submit" button is clicked, the ciphertext is decrypted using the `xor_decrypt` function.
3. The decrypted text is displayed in a text area.

### Decryption Function in the GUI
```python
def decrypt_func():
    # ... (create decryption window and widgets)
    
    def do():
        word = den_word.get('1.0', 'end')
        key = int(key_word.get())
        plaintext = xor_decrypt(key, word)
        
        den_lab_word = Label(den_root, text="Your decrypted text:", font=('Helvetica', 10), fg="#008000", bg="#0d0d0d")
        den_lab_word.grid(row=5, column=0)
        
        en_word = Text(den_root, height=5, width=30, font=('Helvetica', 20), fg="#008000", bg="#0d0d0d")
        en_word.grid(row=6, column=0, columnspan=2, padx=20, pady=5)
        en_word.insert('1.0', plaintext)
```

## Main Window

### Welcome Label
```python
wel_word_lab = Label(root, text="Welcome to Security Text App!", font=('Helvetica', 25), fg="#008000", bg="#0d0d0d")
wel_word_lab.grid(row=0, column=0, columnspan=4, pady=30, padx=15)
```

### Buttons
```python
en_but = Button(root, text="ENCRYPT", border=0, bg="#008000", font=('Helvetica', 20), command=encrypt_fuc)
de_but = Button(root, text="DECRYPT", border=0, bg="#008000", font=('Helvetica', 20), command=decrypt_func)
en_but.grid(row=1, column=1, pady=25)
de_but.grid(row=1, column=2)
```

## About Section

### About Text in English and Chinese
```python
about_en = "This program is designed for text security, \n enabling encryption and decryption. You can utilize a simple key to \nencrypt your text and subsequently use the same\n key to decrypt it."
about_zh = "这个程序是为文本安全而设计的，可以进行加密和解密。\n您可以使用一个简单的密钥来加密您的文本，\n并使用同一个密钥对其进行解密"

word_lab = Label(root, text="About", font=('Helvetica', 25), fg="#008000", bg="#0d0d0d")
word_lab.grid(row=2, column=0, columnspan=4, pady=15, padx=15)
word_lab = Label(root, text=about_en, font=('Helvetica', 11), fg="#008000", bg="#0d0d0d")
word_lab.grid(row=3, column=0, columnspan=4, pady=5, padx=15)
word_lab1 = Label(root, text=about_zh, font=('Helvetica', 12), fg="#008000", bg="#0d0d0d")
word_lab1.grid(row=4, column=0, columnspan=4, pady=5, padx=15)
```

## Running the Application

To run the application, execute the Python script containing the code:
```bash
python security_text_app.py
```

This will launch the main window of the Security Text App. From here, you can access the encryption and decryption functionalities and view information about the application.

## Conclusion

This documentation provides a comprehensive overview of the Security Text App, including setup, functionality, and usage. The application is designed to be user-friendly and secure, making it easy to encrypt and decrypt text using a simple XOR method.
