'''
Created on May 28, 2015

@author: arf1855

This module is meant to be a "non-interactive" main entry point for the program.
It relies on command line switches to start under the right mode and for input of the encrypted/decrypted text,
along with a graphical dialog for receiving the encryption key.
'''
from symbol import arglist
from sys import argv
import SimpleEncrypt

if __name__ == '__main__':
    # Error check
    if (len(argv) != 3):
        print "Usage: python NonInteractiveMain.py [-e|-d] \"encrypted or decrypted text\""
        exit(1)
    
    if (argv[1] == "-e"):
        cipher = SimpleEncrypt.getCipherFromDialog()
        encryptedText = SimpleEncrypt.EncodeAES(cipher, argv[2])
        print encryptedText
        exit(0)
        
    elif (argv[1] == "-d"):
        cipher = SimpleEncrypt.getCipherFromDialog()
        decryptedText = SimpleEncrypt.DecodeAES(cipher, argv[2])
        print decryptedText
        exit(0)
        
    else:
        print "Unsupported switch " + argv[1]
        exit(1)