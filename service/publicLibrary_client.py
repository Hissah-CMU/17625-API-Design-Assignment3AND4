from __future__ import print_function

import logging

import grpc
import publicLibrary_pb2
import publicLibrary_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = publicLibrary_pb2_grpc.InventoryServiceStub(channel)
        #test create book service
        print("-------------- Create Book --------------")
        response = stub.CreateBook(publicLibrary_pb2.CreateBookRequest(book={
        "ISBN": "0377209944",
        "title": "The NonFiction Book!",
        "author": "Steve L. AAA",
        "genre": "NonFiction",
        "publishingYear": 2020
        }))
        print(response.confirmationMessage)

        #test get book service
        print("-------------- Get Book --------------")
        response2= stub.GetBook(publicLibrary_pb2.GetBookRequest(ISBN='0964001172'))
        print("Book Title: "+ response2.book.title +
              "\nAuthor: "+ response2.book.author +
              "\nGenre: "+ str(response2.book.genre) +
              "\nPublishing Year: "+ str(response2.book.publishingYear)
        )


if __name__ == '__main__':
    logging.basicConfig()
    run()