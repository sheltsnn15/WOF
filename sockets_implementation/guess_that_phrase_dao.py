import random
from functools import cache
import time


# The class will manage when/whether the instance needs to be created 
class Guess_That_Phrase_DAO:
    # class var to keep track if instance has been created
    # set to null to keep track if it's been created
    __instance = None

    # method associated to the class only
    @staticmethod
    def get_instance():
        # create the object if not created
        if Guess_That_Phrase_DAO.__instance is None:
            Guess_That_Phrase_DAO()
        # return the value (singleton object)
        return Guess_That_Phrase_DAO.__instance

    @cache
    # constructor method, given a reference of the singleton object
    def __init__(self):
        # if singleton has already been called, catch this
        if Guess_That_Phrase_DAO.__instance is not None:
            raise Exception("DAO already instantiated!")
        # else, we good. Read from the text file
        else:
            #start = time.time()
            Guess_That_Phrase_DAO.__instance = self
            self.phrases = []
            # read phrases.txt
            with open("phrases.txt", 'r') as file:
                for line in file:
                    # append phrases to a list
                    self.phrases.append(line.rstrip())
            # pick random phrase
            random.shuffle(self.phrases)
            #end = time.time()

            #print(end - start, "\n\n")
