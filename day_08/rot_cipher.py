# decode or encrypt
#
# get code
#
# run code


def getMethod():
    while True:
        method = input('Do you want to encrypt or decrypt a message?: ').lower()
        if method in 'encrypt e decrypt d'.split():
            return method
        else:
            print("Not a valid option.")


def getMessage():
    message = input('What is your message?: ')
    return message


def processMessage(meth, mess):
    if meth == 'd' or meth == 'decrypt':
        pass
    elif meth == 'e' or meth == 'encrypt':
        pass


cipher_method = getMethod()
cipher_message = getMessage()
final_message = processMessage(cipher_method, cipher_message)
print(final_message)

