import os
import string
import re
from re import search

class FindNicknames():

    def __init__(self):
        self.nicknames = {
            "dubbs": ["paul joseph watson", "pjw", "pjdubbs", "pj dubbs"],
            "stevie": ["steve pieczenik", "stevie p"],
            "sweary": ["kerry cassidy", "sweary kerry"],
            "squatch": ["solomon berg", "squatch"]
        }
        
    # this function checks for common nicknames and replaces them with the correct name

    def isnickname(self, string):
        nicknames_to_pass_along = []
        for i in self.nicknames:
            if string in self.nicknames[i]:
                print(self.nicknames[i])
                return self.nicknames[i]
            else:
                nicknames_to_pass_along = [string]
        print(nicknames_to_pass_along)
        return nicknames_to_pass_along


    def checknames(self, input):
        #Removing punctuation from the input
        minuspunctuation = input.translate(str.maketrans('','',string.punctuation))
        #Making every letter lowercase
        lowercase = minuspunctuation.lower()
        #Moving on to checking to see if a common nickname is in the formatted input
        name_array = self.isnickname(lowercase)
        return name_array


# addnames = FindNicknames()
# addnames.output('PJDUBBS')
# addnames.output('David')
# addnames.output('Squatch')