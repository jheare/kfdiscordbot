import os
import random
import string
import re
from re import search


class SanitizeInput:

    def __init__(self):
        self.input = ""
        self.nicknames = {
            "dubbs": "paul joseph watson",
            "stevie": "steve pieczenik",
            "sweary": "kerry cassidy",
            "squatch": "solomon berg"
        }
        
    # this function checks for common nicknames and replaces them with the correct name
    
    def isnickname(self, input):
        for people in self.nicknames:
            if people in input:
                print("We are printing people " + people)
                self.input = self.nicknames[people]
        # if the input isn't a common nickname then we just revert to the original name typed
        if len(self.input) == 0:
            print("Self.input is empty")
            self.input = input

    def output(self, input):
        #Removing punctuation from the input
        minuspunctuation = input.translate(str.maketrans('','',string.punctuation))
        #Making every letter lowercase
        lowercase = minuspunctuation.lower()
        #Moving on to checking to see if a common nickname is in the formatted input
        self.isnickname(lowercase)
        print("This is self.input after running isnickname " + self.input)
        return self.input





