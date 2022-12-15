from concurrent import futures
import logging
import grpc
import publicLibrary_pb2
import publicLibrary_pb2_grpc
import json
#import publicLibrary_DB


#  define function to return list of books from json file
def read_publicLibrary_database():
    """Reads the publicLibrary database.
  Returns:
    The list of books in the  database as a sequence of
      publicLibrary_pb2.Book.
  """
    book_list = []
    with open("publicLibrary_DB.json") as publicLibrary_db_file:
        for item in json.load(publicLibrary_db_file):
            book = publicLibrary_pb2.Book(
                ISBN=item["book"]["ISBN"],
                title=item["book"]["title"],
                author=item["book"]["author"],
                genre=item["book"]["genre"],
                publishingYear=item["book"]["publishingYear"]
                )
            book_list.append(book)
    return book_list

#  InventoryServiceServicer class
class InventoryService(publicLibrary_pb2_grpc.InventoryServiceServicer):
    """Provides methods that implement functionality of inventory service server."""

    #  initiate the books db
    def __init__(self):
        self.db = read_publicLibrary_database()

    # create book implementation:
    def CreateBook(self, request, context):
        #Store the book in the db:
        self.db.append(request.book)
        return publicLibrary_pb2.CreateBookResponse(confirmationMessage= 'The book of title: '+ request.book.title +
                                                                         '  is created!')
    # get book implementation:
    def GetBook(self, request, context):
        bookIndex= -1
        for item in self.db:
            if item.ISBN == request.ISBN:
                bookIndex= self.db.index(item)
        returnedBook= self.db[bookIndex]
        return publicLibrary_pb2.GetBookResponse(book=returnedBook)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    publicLibrary_pb2_grpc.add_InventoryServiceServicer_to_server(
        InventoryService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()