import publicLibrary_pb2_grpc, publicLibrary_pb2
import grpc


class Inventory:
    def __init__(self):
        with grpc.insecure_channel('localhost:50051') as channel:
            self.stub = publicLibrary_pb2_grpc.InventoryServiceStub(channel)
            print(channel)

    def getBookByISBN(self, isbn):
        with grpc.insecure_channel('localhost:50051') as channel:
            self.stub = publicLibrary_pb2_grpc.InventoryServiceStub(channel)
            return self.stub.GetBook(publicLibrary_pb2.GetBookRequest(ISBN=isbn))
