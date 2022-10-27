import random


class Wof_Phrases_Dao:
    __instance = None
    
    @staticmethod
    def get_instance():
        if Wof_Phrases_Dao.__instance is None:
            Wof_Phrases_Dao()
        return Wof_Phrases_Dao.__instance
    
    def __init__(self):
        if Wof_Phrases_Dao.__instance is not None:
            raise Exception("This is a singleton!")
        else:
            Wof_Phrases_Dao.__instance = self
            self.phrases = []
            with open("phrases.txt", 'r') as file:
                for line in file:
                    self.phrases.append(line.rstrip())
            # pick random phrase
            random.shuffle(self.phrases)
