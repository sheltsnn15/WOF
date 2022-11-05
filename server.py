# @author Shelton Ngwenya, R00203947

from concurrent import futures

import grpc

import guess_that_phrase_pb2
import guess_that_phrase_pb2_grpc
from guess_that_phrase import GuessThatPhrase


class DisplayGuessedLetterServicer(guess_that_phrase_pb2_grpc.DisplayGuessedLetterServicer):
    """The greeting service definition.
    """

    guess_that_phrase = GuessThatPhrase()

    def __init__(self):
        pass

    """
    def SendLetter(self, request, context):
        #Sends a Phrase
        #print("Answer is: " + str(request.letter))
        print("Got request " + str(request.letter))
        if request.letter == 'Y' or 'y':
            return self.guess_that_phrase.starting_point()
        else:
            print("GoodBye")
        return guess_that_phrase_pb2.LetterResponse(message='Hello, %s!' % request.letter)
    """

    def SendUserChoice(self, request, context):
        """Sends a Phrase
        """
        print("Answer is: " + str(request.letter))
        print("Got request " + str(request.letter))
        if request.letter == 'Y' or 'y':
            self.guess_that_phrase.starting_point()
        return guess_that_phrase_pb2.UserChoiceResponse(message='GoodBye, %s!' % request.letter)


def server():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    guess_that_phrase_pb2_grpc.add_DisplayGuessedLetterServicer_to_server(
        DisplayGuessedLetterServicer(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


server()

# build simplest first
# build from there
# look at geek for geeks
