import grpc

import guess_that_phrase_pb2
import guess_that_phrase_pb2_grpc
import logging


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = guess_that_phrase_pb2_grpc.DisplayGuessedLetterStub(channel)
        response = stub.SendLetter(
            guess_that_phrase_pb2.LetterRequest(letter=input("Enter name: ")))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
