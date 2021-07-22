import re

def encrypt(p):
    s = ""
    for i in p:
        if i.isalpha() & i.islower():
            s += chr(219 - ord(i))
        else:
            s += i
    return s

def decrypt(c):
    s = ""
    for i in c:
        if i.isalpha() & i.islower():
            s += chr(219 - ord(i))
        else:
            s += i
    return s

def main():
    p = "abcxyzAA"
    c = encrypt(p)
    print(c)
    print(decrypt(c))

if __name__ == "__main__":
    main()
