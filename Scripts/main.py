import bcrypt
#from string import maketrans as mk 

def banner ():
    
    TEXT = '''
    WELCOME TO PASSWORD HASHING TOOL HOPE YOU WOULD LIKE THIS SHIT :0


 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░        ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░       
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░       ░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░       
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░           ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░       ░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░      
                                                                                                                                                                          
                            AUTHOR Araaap -------CAESAR CYPHER SHIFTING LEFT BY 1----------                                                                                                                                              



'''

    print (f"{TEXT}")



def encode (c):
    encode_String = []
    for i in range (len(c)):
        encode_String.append(chr(ord(c[i])+1))

    encode_String = ''.join(encode_String)
    print (f"{encode_String}")


# def decode (c):
#     decode_string = []
#     for i in range (len(c)):
#         decode_string.append(chr(ord(c[i])-1))

#     decode_string = ''.join(decode_string)
#     print (f"{decode_string}")

def hash (passcode):
      
    passcode = str(input("Enter The passcode to make it hashed :")).encode()
    salt  = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passcode,salt)
#print (hashed)

    if (bcrypt.checkpw(passcode,hashed)):
        print (f"Yeah Fits In\n Encoding...\n The Hashed value is \t{hashed}")

    else:
        print ("Nope NOT Buddy In yOur DrE@m$ ")

def Reverse_Cipher (passcode):
    for i in range (len(passcode)-1,-1,-1):
        print (c[i],end = " ")


    
# def Rot13 (passcode):
#     rot13Text = mk('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
# 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm') # every letter corresponds by shifting 13 places like A->N (A+13) = N and so on ...
#     return passcode.translate (rot13Text)

def Rot13(passcode):
    result = ""
    for char in passcode:
        if 'a' <= char <= 'z':  # Handle lowercase letters
            result += chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':  # Handle uppercase letters
            result += chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        else:
            result += char  # Non-alphabetical characters remain unchanged
    return result


def Letter_Swap(s):
    s1 = []
    for item in s:
        if item.isalpha():
            if item.isupper():
                s1.append(item.lower())
            else:
                s1.append(item.upper())
        else:
            s1.append(item)
    return ''.join(s1[::-1])






if __name__ == '__main__':
    banner ()
    print ("Press'1' For normal  ciphering  text message :\n")
    print ("Press'2' for hashing the password :\n")
    print ("Press'3' Reversing Cipher \n")
    print ("Press'4' Rot_13 \n ")
    print ("Press'5' Letter_Swap:\n ")
    print ("Press'6' exit :\n)
    n = int(input("Enter The Choice :"))
    c = str(input("Enter The String :"))
    match n:
        case 1:
            encode(c)
        case 2:
            hash (c)
        case 3:
            Reverse_Cipher(c)
        case 4:
            print (f"{Rot13(c)}")
        case 5:
            Letter_Swap(c)
        case 6:
            exit (0)
        


    #decode(c)
