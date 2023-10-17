from tkinter import *

root = Tk()
root.title("Security")
root.geometry("500x500")
root.resizable(0,0)
root.config(bg="#0d0d0d")

def encrypt_fuc():
	en_root = Tk()
	en_root.title("ENCRYPT")
	en_root.geometry("500x500")
	en_root.resizable(0,0)
	en_root.config(bg="#0d0d0d")

	
	def xor_encrypt(key, plaintext):
		ciphertext = ""
		for char in plaintext:
			encrypted_char = chr(ord(char)^key)
			ciphertext += encrypted_char
		return ciphertext

	def do():
		word = en_word.get('1.0','end')
		key = int(key_word.get())
		plaintext = word
		ciphertext = xor_encrypt(key,plaintext)

		en_lab_word = Label(en_root, text="Your encrypted text:", font = ('Helvetica', 10),fg="#008000", bg="#0d0d0d")
		en_lab_word.grid(row=5, column = 0)

		den_word = Text(en_root,height=5, width=30, font = ('Helvetica', 20),fg="#008000", bg="#0d0d0d")
		den_word.grid(row=6, column=0, columnspan=2, padx=20,pady=5)
		den_word.insert('1.0', ciphertext)

	en_wel_word = Label(en_root, text="Welcome to make ENCRYPT", font = ('Helvetica', 25),fg="#008000", bg="#0d0d0d")
	en_wel_word.grid(row=0, column = 0, columnspan=2)
	
	en_key_word = Label(en_root, text="Please input 3 number as a key:", font = ('Helvetica', 10),fg="#008000", bg="#0d0d0d")
	en_key_word.grid(row=1, column = 0)

	key_word = Entry(en_root, font = ('Helvetica', 20),fg="#008000", bg="#0d0d0d")
	key_word.grid(row=2, column=0, pady=15, padx=25)
	
	sumbit_but = Button(en_root, text="Submit", border=0, bg="#008000",font = ('Helvetica', 20), command=do)
	sumbit_but.grid(row=2, column=1)

	den_lab_word = Label(en_root, text="Please input your text to encrypt:", font = ('Helvetica', 10),fg="#008000", bg="#0d0d0d")
	den_lab_word.grid(row=3, column = 0)

	en_word = Text(en_root, height=5, width=30, font = ('Helvetica', 20),fg="#008000", bg="#0d0d0d")
	en_word.grid(row=4, column=0, columnspan=2, padx=20,pady=5)

	


def decrypt_func():

	den_root = Tk()
	den_root.title("DECRYPT")
	den_root.geometry("500x500")
	den_root.resizable(0,0)
	den_root.config(bg="#0d0d0d")

	def xor_decrypt(key, ciphertext):
		plaintext = ""
		for char in ciphertext:
			decrypted_char =chr(ord(char)^key)
			plaintext += decrypted_char
		return plaintext

	def do():
		word = den_word.get('1.0','end')
		key = int(key_word.get())
		plaintext = word
		ciphertext = xor_decrypt(key,plaintext)

		den_lab_word = Label(den_root, text="Your decrypted text:", font = ('Helvetica', 10),fg="#008000", bg="#0d0d0d")
		den_lab_word.grid(row=5, column = 0)

		en_word = Text(den_root,height=5, width=30, font = ('Helvetica', 20),fg="#008000", bg="#0d0d0d")
		en_word.grid(row=6, column=0, columnspan=2, padx=20,pady=5)
		en_word.insert('1.0', ciphertext)


	den_wel_word = Label(den_root, text="Welcome to make DECRYPT", font = ('Helvetica', 25),fg="#008000", bg="#0d0d0d")
	den_wel_word.grid(row=0, column = 0, columnspan=2)

	en_key_word = Label(den_root, text="Please input 3 number as a key:", font = ('Helvetica', 10),fg="#008000", bg="#0d0d0d")
	en_key_word.grid(row=1, column = 0)

	key_word = Entry(den_root, font = ('Helvetica', 20),fg="#008000", bg="#0d0d0d")
	key_word.grid(row=2, column=0, pady=15, padx=25)
	
	sumbit_but = Button(den_root, text="Submit", border=0, bg="#008000",font = ('Helvetica', 20), command=do)
	sumbit_but.grid(row=2, column=1)

	en_lab_word = Label(den_root, text="Please input your text to decrypt:", font = ('Helvetica', 10),fg="#008000", bg="#0d0d0d")
	en_lab_word.grid(row=3, column = 0)

	den_word = Text(den_root, height=5, width=30, font = ('Helvetica', 20),fg="#008000", bg="#0d0d0d")
	den_word.grid(row=4, column=0, columnspan=2, padx=20,pady=5)




wel_word_lab =Label(root, text="Welcome to Security Text App!", font = ('Helvetica', 25),fg="#008000", bg="#0d0d0d")
wel_word_lab.grid(row=0, column=0, columnspan=4 ,pady=30, padx=15)

en_but = Button(root, text="ENCRYPT", border=0, bg="#008000",font = ('Helvetica', 20), command=encrypt_fuc)
de_but = Button(root, text="DECRYPT", border=0, bg="#008000",font = ('Helvetica', 20), command=decrypt_func)

en_but.grid(row = 1 , column=1, pady=25)
de_but.grid(row = 1 , column=2)
about_en ="This program is designed for text security, \n enabling encryption and decryption. You can utilize a simple key to \nencrypt your text and subsequently use the same\n key to decrypt it."
about_zh ="这个程序是为文本安全而设计的，可以进行加密和解密。\n您可以使用一个简单的密钥来加密您的文本，\n并使用同一个密钥对其进行解密"

word_lab =Label(root, text="About", font = ('Helvetica', 25),fg="#008000", bg="#0d0d0d")
word_lab.grid(row=2, column=0, columnspan=4 ,pady=15, padx=15)

word_lab =Label(root, text=about_en, font = ('Helvetica', 11),fg="#008000", bg="#0d0d0d")
word_lab.grid(row=3, column=0, columnspan=4 ,pady=5, padx=15)

word_lab1 =Label(root, text=about_zh, font = ('Helvetica', 12),fg="#008000", bg="#0d0d0d")
word_lab1.grid(row=4, column=0, columnspan=4 ,pady=5, padx=15)


root.mainloop()