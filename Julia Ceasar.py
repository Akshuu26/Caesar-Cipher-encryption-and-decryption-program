#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

#check the above function
def decrypt(text,s):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result
i='y'
while i=='y':
    z=input('do you want to encrypt or decrypt?(e/d):')
    if z=='e' or z=="E":
        x=input("Enter text to encrypt:")
        t=int(input("Enter letter shift(1 to 26):"))
        L=x.split(" ")
        L1=[]
        #print(L)
        for j in L:
            L1.append(encrypt(j,t))
        print("Encrypted text:")
        for i in L1:
            print(i,end=" ")
    else:
        c=input("Enter text to decrypt:")
        v=int(input("Enter letter shift(1 to 26):"))
        L=c.split(" ")
        L1=[]
        #print(L)
        for j in L:
            L1.append(decrypt(j,v))
        print("Decrypted text:")
        for i in L1:
            print(i,end=" ")
    i=input("\ndo you want to continue(y/n):")
exit()
    