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
# Caesar cipher

# given a word or a phrase, return an encrypted word or phrase with an alphabetical offset of 5. Ignore spaces and non-letter characters.

# Examples:
# abc -> efg
# xyz -> def
# aaa! -> eee!

# ask for a word or phrase to be encrypted
# for each character in the word,
	# if the character is not a letter
		# print the character
	# if the character is a letter
		# get the index of that character in the alphabet
		# example: a = 0
		# shift the index + 5
		# if the shifted index is < 26:
			# example shifted a = 5 -> e
			# print the shifted character 
		# else:
			# subtract or mod 26 from the shifted index

# alpha "abcdefghijklmnopqrstuvwxyz"




indexshift = str.index() + 5
callphrase = input('Please enter a sentence to be encrypted:')

print (callphrase)

def ceaser_cipher():

    for str in input:
        if str.isdigit:
            print(input)
        elif str.isalpha:
            return indexshift
        if indexshift < 26:
            print(str.input)
        else: 
            return indexshift - 26 
        
    print('The encrypted sentence is:', ceaser_cipher)
        
    

        
