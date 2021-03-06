class enigma:
    inplug = ""
    plug = []
    rotor1 = ""
    rotor2 = ""
    rotor3 = ""
    reflector = ""
    steps = False
    r1_count = 0
    r2_count = 0


    def __init__(self, inplug, plug, rotor1, rotor2, rotor3, reflector, offset1, offset2, offset3, steps):
        self.plug = plug
        self.inplug = inplug
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.reflector = reflector
        self.steps = steps

        ## Setup the rotor with the offset taken into account
        ## If the rotor was "ABCD" with an offset of 2, the new rotor would be "CDAB"
        ## So, the rotor of "ABCD" starts at position 2 of the string, and is looped like a wheel/rotor

        for i in range(0, offset1):
            self.rotor1 = self.stepRotorBack(self.rotor1)

        for i in range(0, offset2):
            self.rotor2 = self.stepRotorBack(self.rotor2)

        for i in range(0, offset3):
            self.rotor3 = self.stepRotorBack(self.rotor3)

    #gets user input for plug board values
    def setPlug(self, plug):
        for x in range(10):
            print("Plugboard connection: " + str(x) + "/10")
            plug.append(input("What letter would you like to swap?\t").upper())
            plug.append(input("What is it being changed to?\t").upper())
        return plug  

    #if uses enters all of the plugbaord values in one line, seperated by comma
    def getvalues(self,inplug, plug):
        valuearaay = inplug.split(',')
        plug = []
        #print(valuearaay)
        for i in range(len(valuearaay)):
            plug.append(valuearaay[i][0])
            plug.append(valuearaay[i][1])
        #print(plug)

        return plug    

    #this swaps the letters in the input text with what the plug board has been changed to
    def swapLetters(self, plug, text, steps):
        swappedtext = ""
        toadd = ''
        if steps == True:
            print("The message before swappins is: " + text)
        for i in range(0, len(text)):
            found = False
            #print("i is" + str(i) + "char at i is " + text[i])
            for x in range(0,(len(plug)-1),2):
                if text[i] == plug[x]:
                    if steps == True:
                        print("Swaping: " + text[i] + " with: " + plug[x+1] + " from the plugboard connections")
                    #print("char in string is "+ text[i] + "char in plug is "+ plug[x])
                    swappedtext += plug[x+1]
                    found = True
                    print(swappedtext)
                elif text[i] == plug[x+1]:
                    if steps == True:
                        print("Swaping: " + text[i] + " with: " + plug[x] + " from the plugboard connections")
                    #print("char in string is "+ text[i] + "char in plug is "+ plug[x+1] + plug[x])
                    swappedtext += plug[x]
                    found = True
                    print(swappedtext)
            if found == False:
                swappedtext += text[i]
        if steps == True:
            print("The message after swapping the plugboard connections is: " + swappedtext)
        return swappedtext

    ## Function to step rotor by 1 position
    ## Input is the rotor string
    ## Each char needs to move right by 1, and the last char needs to go into the first position
    def stepRotor(self, rotor):
        #print("Stepping rotor by 1 place")
        ## Save last char
        lastChar = rotor[25]
        returnString = rotor[25]
        ## Move each char forward 1 position
        for i in range(0, len(rotor) - 1):
            rotorAsList = list(rotor)
            tempChar = rotorAsList[i]
            rotorAsList[i + 1] = tempChar
            returnString += rotorAsList[i + 1]
        #print(returnString)
        return returnString

    def stepRotorBack(self, rotor):
        #print("Stepping rotor back by 1")
        firstChar = rotor[0]
        returnString = ""

        for i in range(1, len(rotor)):
            rotorAsList = list(rotor)
            tempChar = rotorAsList[i]
            rotorAsList[i-1] = tempChar
            returnString += rotorAsList[i-1]
        returnString += firstChar
        return returnString

    def encrypt(self, text):   
        #to get the plugboard values
        # if manually entering it 1 connection at a time
        #self.plug = self.setPlug(self.plug)
        
        #if the user does not enter nay values into the plugbaord
        if(self.inplug == ""):
            pass
        else:
            pass
            #used for GUI
            #splits the combos entered from: "AB,FG,LK" to ['A','B','F','G','L','K'] 
            self.plug = self.getvalues(self.inplug, self.plug)
            if self.steps == True:
                print("Swapping letters with plugboard connections")
            #swaps the letters in the text string with those changes made by the plugbaord
            text = self.swapLetters(self.plug, text, self.steps)
        #print(text)
        
        ## Count for how many times each rotor is stepped. Don't care how many times rotor3 is stepped

        returnString = ""


        if(self.steps):

            print("Rotor I: " + self.rotor1)
            print("Rotor II: " + self.rotor2)
            print("Rotor III: " + self.rotor3)
            print("Initial String: " + text)
            ## Loop through each character of the text provided
            for i in range(0, len(text)):
                ## Step rotor 1 every iteration
                self.rotor1 = self.stepRotorBack(self.rotor1)

                ## Step rotor 2 if rotor 1 has been stepped 26 times
                if(self.r1_count == 25):
                    self.rotor2 = self.stepRotorBack(self.rotor2)
                    r1_count = 0
                    self.r2_count += 1
                ## Step rotor 3 if rotor 2 has been stepped 26 times
                if(self.r2_count == 25):
                    r2_count = 0
                    self.rotor3 = self.stepRotorBack(self.rotor3)

                self.r1_count += 1

                ## Find the index of the current char (CHAR % 65) should give index of an uppercase character
                ## ord(char) returns unicode of character

                ## Find character routing from index of text[i]
                ## charOne is the output from rotor1
                index = ord(text[i]) % 65
                charOne = self.rotor1[index]
                print("Character " + text[i] + " maps to: " + charOne)


                ## Find the character routing from the index of self.rotor1[i]
                ## So input to second rotor will be the output from the first rotor
                index = ord(charOne) % 65
                charTwo = self.rotor2[index]
                print("Character " + charOne + " maps to: " + charTwo)

                index = ord(charTwo) % 65
                charThree = self.rotor3[index]
                print("Character " + charTwo + " maps to: " + charThree)

                ## Right before the reflector. So we've gone through R1, R2, R3

                ## Go back through rotor3
                index = self.reflector.find(charThree)
                charFour = chr(index + 65)
                print("Reflector maps " + charThree + " to: " + charFour)

                ## Go back through rotor2
                index = self.rotor3.find(charFour)
                charFive = chr(index + 65)
                print("Character " + charFour + " maps to: " + charFive)

                ## Go back through rotor1
                index = self.rotor2.find(charFive)
                charSix = chr(index + 65)
                print("Character " + charFive + " maps to: " + charSix)

                index = self.rotor1.find(charSix)
                charSeven = chr(index + 65)
                print("Character " + charSix + " maps to: " + charSeven)
                
                returnString += charSeven
            
            #swaps the letters back - plugboard
            #if no plugboard was entered - skip
            if(self.inplug == ""):
                pass
            #swaps the letters according to the plugboard
            else:
                print("Swapping letters back")
                #swaps the letters in the text string with those chnage smade by the plugbaord
                returnString = self.swapLetters(self.plug, returnString, self.steps)
        else:
            ## Loop through each character of the text provided
            for i in range(0, len(text)):
                ## Step rotor 1 every iteration
                self.rotor1 = self.stepRotorBack(self.rotor1)

                ## Step rotor 2 if rotor 1 has been stepped 26 times
                if(self.r1_count == 25):
                    self.rotor2 = self.stepRotorBack(self.rotor2)
                    r1_count = 0
                    self.r2_count += 1
                ## Step rotor 3 if rotor 2 has been stepped 26 times
                if(self.r2_count == 25):
                    r2_count = 0
                    self.rotor3 = self.stepRotorBack(self.rotor3)

                self.r1_count += 1

                ## Find the index of the current char (CHAR % 65) should give index of an uppercase character
                ## ord(char) returns unicode of character

                ## Find character routing from index of text[i]
                ## charOne is the output from rotor1
                index = ord(text[i]) % 65
                charOne = self.rotor1[index]
                ##print("Character " + text[i] + " maps to: " + charOne)


                ## Find the character routing from the index of self.rotor1[i]
                ## So input to second rotor will be the output from the first rotor
                index = ord(charOne) % 65
                charTwo = self.rotor2[index]
                ##print("Character " + charOne + " maps to: " + charTwo)

                index = ord(charTwo) % 65
                charThree = self.rotor3[index]
                ##print("Character " + charTwo + " maps to: " + charThree)

                ## Right before the reflector. So we've gone through R1, R2, R3

                ## Go back through rotor3
                index = self.reflector.find(charThree)
                charFour = chr(index + 65)
                ##print("Reflector maps " + charThree + " to: " + charFour)

                ## Go back through rotor2
                index = self.rotor3.find(charFour)
                charFive = chr(index + 65)
                ##print("Character " + charFour + " maps to: " + charFive)

                ## Go back through rotor1
                index = self.rotor2.find(charFive)
                charSix = chr(index + 65)
                ##print("Character " + charFive + " maps to: " + charSix)

                index = self.rotor1.find(charSix)
                charSeven = chr(index + 65)
                ##print("Character " + charSix + " maps to: " + charSeven)
                
                returnString += charSeven
            
            #swaps the letters back - plugboard
            #if no plugboard was entered - skip
            if(self.inplug == ""):
                pass
            #swaps the letters according to the plugboard
            else:
                #swaps the letters in the text string with those chnage smade by the plugbaord
                returnString = self.swapLetters(self.plug, returnString, self.steps)

        return returnString


ROTOR_I =   "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_II =  "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"


## A comes out of R3 then goes to the reflector
REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
REFLECTOR_A = "EDCHIJKLMNOPQRSTUVWZYZABGF"
## Reflector returns Y
## Y = 25
## Find position 25 in R3. Thats R3s output


ROTOR_IV = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
ROTOR_V = "VZBRGITYUPSDNHLXAWMJQOFECK"

ROTOR_TEST1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROTOR_TEST2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROTOR_TEST3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#gets the values from the inputed plugboard values. 
#Splits to a single char



def main():

    ## Need two engima machines to both enrypt and decrypt at the same time   

    engimaMachineINPUT = enigma("AB,ER,LP",[], ROTOR_I, ROTOR_II, ROTOR_III, REFLECTOR_B, 0, 0, 0, True)
    engimaMachineOUTPUT = enigma("AB,ER,LP",[], ROTOR_I, ROTOR_II, ROTOR_III, REFLECTOR_B, 0, 0, 0, True)

    inputText = (input("Enter message: ")).upper()
    outputText = engimaMachineINPUT.encrypt(inputText)
    originalMessage = engimaMachineOUTPUT.encrypt(outputText)

    print("Original Message: " + originalMessage)
    print("Encrypted Message: " + outputText)

#main()

## Need to have a function to line up HELLOWORLD to encrypted message. 
## None of the characters can line up to themselves. That new substring is the string we will use to test
