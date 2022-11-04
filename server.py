from concurrent import futures

import grpc

import guess_that_phrase_pb2
import guess_that_phrase_pb2_grpc
import guess_that_phrase


class DisplayGuessedLetterServicer(guess_that_phrase_pb2_grpc.DisplayGuessedLetterServicer):
    """The greeting service definition.
    """

    def __init__(self):
        pass

    def SendLetter(self, request, context):
        """Sends a Phrase
        """
        guess_that_phrase.Guess_That_Phrase.guess_letter(request.letter)
        return guess_that_phrase_pb2.LetterResponse(message='{0}'.format(request.letter))

    def SendPhrase(self, request, context):
        """Sends a Phrase
        """
        guess_that_phrase.Guess_That_Phrase.guess_phrase(request.letter)
        return guess_that_phrase_pb2.PhraseResponse(message='{0}'.format(request.letter))

    # define server


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    guess_that_phrase_pb2_grpc.add_DisplayGuessedLetterServicer_to_server(
        DisplayGuessedLetterServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC starting")
    server.start()
    server.wait_for_termination()

    server()

    # build simplest first
    # build from there
    # look at geek for geeks
