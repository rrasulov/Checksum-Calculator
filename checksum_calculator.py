#Coded By Rashad
import hashlib

def checksum(file_name, hasher):
    with open(file_name, 'rb') as file:
        content = file.read()
        hasher.update(content)
    hex_format = hasher.hexdigest()
    return hex_format

file_name = input("Please, Enter File Path: ")
file_name = file_name.replace('"', '')


encrypt_type = int(input(("What Type Of Hash Do You Want ?\n"
      "1. MD5"
      "\r\n2. SHA256"
      "\r\n3. SHA1"
      "\r\n4. SHA512\n\nType Here: ")))
try:
    if encrypt_type == 1:
        hasher = hashlib.md5()
        md5 = checksum(file_name, hasher)
        print("\nYour MD5 Hash Result:", md5)
    elif encrypt_type == 2:
        hasher = hashlib.sha256()
        sha256 = checksum(file_name, hasher)
        print("\nYour SHA256 Hash Result:", sha256)
    elif encrypt_type == 3:
        hasher = hashlib.sha1()
        sha1 = checksum(file_name, hasher)
        print("\nYour SHA1 Hash Result:", sha1)
    elif encrypt_type == 4:
        hasher = hashlib.sha512()
        sha512 = checksum(file_name, hasher)
        print("\nYour SHA512 Hash Result:", sha512)
    else:
        print("\nPlease, Enter A Number From The List.")
except Exception:
    print("Something Went Wrong.")
