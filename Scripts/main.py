'''Author Arkaaap Implementing Ciphers using python and hashing 
DATE 3/19/2025 
:)
'''

import bcrypt

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



    



if __name__ == '__main__':
    banner ()
    print("Press '1' For normal acesar ciphering your text message :\n")
    print ("Press '2' for hashing the password :\n")
    n = int(input("Enter The Choice :"))
    c = str(input("Enter The String :"))
    match n:
        case 1:
            encode(c)
        case 2:
            hash (c)


    #decode(c)
