import grpc

import guess_that_phrase
import guess_that_phrase_pb2
import guess_that_phrase_pb2_grpc
from guess_that_phrase import Guess_That_Phrase_DAO


class DisplayGuessedLetterServicer(guess_that_phrase_pb2_grpc.DisplayGuessedLetterServicer):
    """The greeting service definition.
    """

    def __int__(self):
        pass

    def SendLetter(self, request, context):
        """Sends a Phrase
        """
        guess_that_phrase.guess_vowel()
        return guess_that_phrase_pb2_grpc.DisplayGuessedLetter(message='Hello, %s!' % request.name)

    def SendPhrase(self, request, context):
        """Sends a Phrase
        """
        guess_that_phrase.guess_phrase(request.letter)

        return helloworld_pb2.HelloReply(message='Hello again, %s!' % request.name)

