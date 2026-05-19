# Prgram to Convert all lower cases to upper case in a string.

text=input("Enter text in lowercase: ")
result=""

for char in text:
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)
    else:
        result += char

print("Uppercase Result:", result)
