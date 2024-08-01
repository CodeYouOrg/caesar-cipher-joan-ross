# In this exercise we will implement a Caesar cipher with a right shift of 5. This 
#exercise is based on the Caesar cipher exersise in the openSAP Python for 
#Beginners course. If you have already solved it as part of the Learn Python 
#course you can re-use your code here.

#Write a Python program that encrypts text given by the user. The program should 
#ask the user for a plain text sentence and print the encrypted text. The text 
#should be encrypted using a caesar cipher with a right shift of 5.

#Here is an example execution of the program:

#Please enter a senctence: python is fun!
#The encrypted sentence is: udymts nx kzs!

#  E₅ (x) = (x + 5) mod 26 (range 0, 27)

callphrase = input('Please enter a sentence:')
print (callphrase)

def ceaser_cipher(phrase):
    alphabet = range(0, 27)
    cipher_eq = str(phrase) + 5
    for phrase in alphabet:
        return cipher_eq
    
    return('The encrypted sentence is:', ceaser_cipher)
