import hashlib
import os
import time

os.system("clear")
print("				*************PASSWORD CRACKER**********")
print("")
print("")
print("")

pass_found=0
input_hash = input("Enter the hashed password: ")
print("")
pass_doc = input("Enetr the password filename including its path(root / home/): ")
print("")
print("")


try:
	pass_file=open(pass_doc, 'r', encoding='utf-8', errors='ignore')
except:
	print("Error: ")
	print(pass_doc, "is not found.\n Please give the path of file correctly")
	quit()


os.system("sleep 2")
for word in pass_file:
	enc_word = word.strip().encode('utf-8') #converts the string into byte format to convert into hash
	hash_word = hashlib.md5(enc_word.strip()) #convert the byte into md5 hash
	digest = hash_word.hexdigest() #converts the hash into readable format(hexa format)

	if digest == input_hash:
		print("password found.\nThe password is:", word)
		pass_found = 1
		break

if not pass_found:
	print("Password is not found in the", pass_doc, "file")
	print('\n')
print("*********************Thank You********************")
