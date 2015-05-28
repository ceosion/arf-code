'''
The following is a modification of the code taken from:
http://null-byte.wonderhowto.com/how-to/encrypt-and-decrypt-text-python-0132905/

It is intended to provide a simple way to encrypt and decrypt text fed into
the program.

Noteworth modifications to the program:
 * Original program required secret key to be length 16. To be more flexible for the
     user, I've changed it so that the encryption key is 32 characters long and is
     a repeat of whatever they put in to pad the missing characters. The increase in
     key length should improve the security while also allowing secure-conscious users
     the ability to enter a sufficiently lengthy key.
     
This module relies on Python 2.7 with PyCrypto installed.

Created on Jan 14, 2015

@author: Alex Ford
'''

from Crypto.Cipher import AES
#import Crypto.Cipher
#import string
import base64
import time
from symbol import arglist

import DialogPrompt

PADDING = '{'
BLOCK_SIZE = 32
KEY_SIZE = 32
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
#prepare crypto method
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

'''
This function will always return a key based on the input String of KEY_SIZE.
If the input String is less than KEY_SIZE, then the result will be a truncation
of the original input String. If the input String is greater than KEY_SIZE, then
the result will be a String equal to KEY_SIZE with the input String repeated as
necessary to make up for the missing characters.

Example: if KEY_SIZE = 8
input =  foobar       (6 characters)
output = foobarfo     (8 characters)

input =  foobarworld  (11 characters)
output = foobarwo     (8 characters)
'''
def getPaddedSecret(inputStr):
    retVal = ""
    inputPtr = 0
    while len(retVal) < KEY_SIZE:
        retVal += inputStr[inputPtr]
        inputPtr += 1
        # once we hit the end of input, reset to the beginning
        if inputPtr >= len(inputStr):
            inputPtr = 0
    return retVal

'''
Simple test function for the getPaddedSecret() function.
'''
def testGetPaddedSecret():
    print getPaddedSecret("foobar")
    print getPaddedSecret("foobarworld");

'''
Presents a dialog to the user to enter the secret.
Returns the cipher that can be used with the EncodeAES/DecodeAES methods.
e.g. EncodeAES(cipher, data) or DecodeAES(cipher, data)
'''
def getCipherFromDialog():
    # secret = raw_input("Please Enter An Encryption Key: ")
    dialog = DialogPrompt.DialogPrompt()
    dialog.mainloop()
    secret = dialog.getValue()
    secret = getPaddedSecret(secret)
    countTotal= (len(secret))
    # This checks the encryption key to ensure it matches the correct length
    # It always should, thanks to our padding method
    letter=3
    while letter==3:
        if countTotal==KEY_SIZE:
            cipher = AES.new(secret)
            letter=0
        else:
            print "Please Ensure The Key You Entered Is 64 Characters In Length\n"
            letter=3
    return cipher

'''
Interactive main loop
'''
if __name__ == '__main__':
    arglist
    
    loop=5
    while loop==5:
        #set up loop, so the program can be rerun again if desired, without restarting
        option=raw_input("Would You Like to Encrypt Or Decrypt Text?\nEncrypt: a\nDecrypt: b\n")
        if option=='a':
            cipher = getCipherFromDialog()
            # encode a string
            data=raw_input("Please enter the plain text you'd like encrypted: ")
            encoded = EncodeAES(cipher, data)
            print 'Encrypted string:', encoded
            options=raw_input("Would You Like To Encrypt/Decrypt Again? Y/N\n")
            if options=='y':
                loop=5
            if options=='n':
                loop=0
              
        if option=='b':
            
            ciper = getCipherFromDialog()
            data = raw_input("Please enter the encoded text: ")
            decrypted = DecodeAES(cipher, data)
            print 'Decrypted text: ', decrypted
            options=raw_input("Would You Like To Encrypt/Decrypt Again? Y/N\n")
            if options=='y':
                loop=5
            if options=='n':
                loop=0
                  
        if loop==0:
            print "Goodbye!!"
            time.sleep(2)
            exit
            #exits the program if desired by user
            pass