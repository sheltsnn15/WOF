from concurrent import futures

import grpc

import guess_that_phrase_pb2
import guess_that_phrase_pb2_grpc
from guess_that_phrase import GuessThatPhrase


class DisplayGuessedLetterServicer(guess_that_phrase_pb2_grpc.DisplayGuessedLetterServicer):
    """The greeting service definition.
    """

    def __init__(self):
        pass

    def SendLetter(self, request, context):
        """Sends a Phrase
        """
        print("Got request " + str(request.letter))
        GuessThatPhrase.starting_point()
        return guess_that_phrase_pb2.LetterResponse(message='Hello, %s!' % request.letter)

    def SendPhrase(self, request, context):
        """Sends a Phrase
        """
        # guess_that_phrase.Guess_That_Phrase.guess_phrase(request.letter)
        print("Got request " + str(request.phrase))
        return guess_that_phrase_pb2.PhraseResponse(message='Hello, %s!' % request.phrase)

    # define server


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
