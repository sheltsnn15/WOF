# @author Shelton Ngwenya, R00203947

import grpc

import guess_that_phrase_pb2
import guess_that_phrase_pb2_grpc
import logging


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = guess_that_phrase_pb2_grpc.DisplayGuessedLetterStub(channel)
        response = stub.SendUserChoice(
            guess_that_phrase_pb2.UserChoiceRequest(letter=str(input("\nPlay game [Y\'N]: "))))
    print("Greeter client received: " + response.message)


run()
