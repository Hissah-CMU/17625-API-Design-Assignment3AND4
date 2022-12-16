from __future__ import print_function
import logging
import inventory_client

def getBookTitleByISBN(ISBNs, client):
    title_list = []
    for item in ISBNs:
        response = client.getBookByISBN(item)
        if response is not None:
            title_list.append(response.book.title)

    return title_list

def initClient():
    return inventory_client.Inventory()

def run():
    client= initClient()
    ISBN_list= ["0321543254", "0377209000", "0964001172"]
    response= getBookTitleByISBN(ISBN_list, client)
    print("-------------- Get Books Titles --------------")
    for title in response:
        print(title)


if __name__ == '__main__':
    logging.basicConfig()
    run()