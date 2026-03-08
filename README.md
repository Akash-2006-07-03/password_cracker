# Password Cracker (Dictionary Attack) – Python

## Description

This is a simple Python script that performs a **dictionary-based password cracking attack**.
It attempts to find the original password from an **MD5 hash** by comparing it with passwords stored in a wordlist file.

The script reads each password from the provided file, converts it into an MD5 hash, and compares it with the hash entered by the user. If a match is found, the corresponding password is displayed.

---

## Features

* Accepts an **MD5 hashed password** as input.
* Reads passwords from a **wordlist file**.
* Converts each word into an **MD5 hash** using Python's `hashlib`.
* Compares generated hashes with the input hash.
* Displays the password if a match is found.
* Handles file errors if the wordlist path is incorrect.

---

## How It Works

1. The user enters the **hashed password**.
2. The user provides the **path to a password wordlist file**.
3. The script reads each password from the file.
4. Each password is:

   * cleaned using `strip()` to remove newline characters
   * converted to bytes using UTF-8 encoding
   * hashed using the MD5 algorithm
5. The generated hash is compared with the input hash.
6. If a match is found, the original password is displayed.

---

Example input:

```
Enter the hashed password: 5f4dcc3b5aa765d61d8327deb882cf99
Enter the password filename including its path(root / home/): /home/kali/Desktop/rockyou.txt
```

Example output:

```
password found.
The password is: password
```

---

## Important Notes

* This script only works with **MD5 hashes**.
* It uses a **dictionary attack**, so the password must exist in the provided wordlist.
* For educational purposes only (cybersecurity learning and testing environments).

---
