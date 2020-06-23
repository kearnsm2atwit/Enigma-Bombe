#Enigma code

import array

#array for the alphabet
alphabet = {(i,j): 0 for i in range(2) for j in range(26)}

#to get the upper case letter corresponding to each num of the alphabet
charnum = 65
for x in range(26):
    alphabet[0, int(x)] = chr(charnum)
    alphabet[1, int(x)] = chr(charnum)
    charnum+=1

def printalphabet(num):
    for x in range(26):
        print(alphabet[num,x])

def plugboard(ogletter, swapedletter):
    print("Plugboard section")
    print("Swapping letter: " + ogletter + " with: " + swapedletter)
    #swap the letters
    ogletterindex = 0
    swapletterindex = 0
    #search for the index of letters to swap
    for x in range(26):
        if (alphabet[1, x] == ogletter):
            ogletterindex = x
            #print(str(ogletterindex))
        if (alphabet[1, x] == swapedletter):
            swapletterindex = x
    #swap the two in the array
    alphabet[1, ogletterindex] = swapedletter
    alphabet[1, swapletterindex] = ogletter
    #prints cipher alphabet to check that the swap worked
    printalphabet(1)

#menu
#get input message
plainTextMessage = input("What is the message you would like to input")
#get rid of spaces
#make uppercase so chars match with the alphabet

#get settings 
#plug board
for x in range(10):
    print("Plugboard connection: " + str(x) + "/10")
    OrigLetter = input("What letter would you like to swap?").upper()
    ChangeLetter = input("What is it being changed to?").upper()
    plugboard(OrigLetter, ChangeLetter)
#rotors
rotorarray = []
for x in range(3):
    rotornum = input("What is the " + x + " you would like to use?")
    rotorarray.append(rotornum)
#reflector
reflector = input("Please choose the reflector")

print("The encoded message is: ")
