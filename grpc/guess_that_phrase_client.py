import grpc

import guess_that_phrase_pb2
import guess_that_phrase_pb2_grpc


def run():
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = guess_that_phrase_pb2_grpc.DisplayGuessedLetterStub(channel)
        response = stub.SendLetter(
            guess_that_phrase_pb2.LetterRequest(message=""))
        print(response.message)


run()
