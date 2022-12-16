from unittest.mock import MagicMock, patch
import unittest
from public_library.service import publicLibrary_pb2
from  inventory_client import Inventory
import get_book_titles
# Data Declaration will be used in testing
# Declare book 1
test_book = publicLibrary_pb2.Book(
    ISBN="0377209000",
    title= "The Social Science Book!",
    author="Jhon V. XYZ",
    genre="SocialScience",
    publishingYear=2015
    )

test_book2 = publicLibrary_pb2.GetBookResponse(
    book= test_book
)

# inventory class mocking
client_mock = Inventory()
client_mock.__init__= None
client_mock.getBookByISBN = MagicMock(return_value=test_book2)
client_mock.getBookByISBN(test_book.ISBN)
client_mock.getBookByISBN.assert_called_with(test_book.ISBN)


#unit test of get_book_titles
class TestStringMethods(unittest.TestCase):
    #test with mock
    def test_book_titles(self):
        ISBN_list = {test_book.ISBN}
        return_list = [test_book.title]
        call= get_book_titles.getBookTitleByISBN(ISBN_list, client_mock)
        self.assertEqual(call, return_list, None)

    #test with server
    def  test_book_titles2(self):
        ISBN_list = {test_book.ISBN}
        return_list = [test_book.title]
        client = Inventory()
        call = get_book_titles.getBookTitleByISBN(ISBN_list, client)
        self.assertEqual(call, return_list, None)

if __name__ == '__main__':
    unittest.main()