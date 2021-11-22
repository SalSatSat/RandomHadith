import requests
import json
from Utils import printJSON
from Book import Book

def initBooks() -> []:
    try:
        response = requests.get("https://ahadith-api.herokuapp.com/api/books/en")
        # print(response.status_code)
        # printJSON(response.json())

        booksText = json.dumps(response.json(), sort_keys=True, indent=4)
        booksData = json.loads(booksText)

        books = []
        for bookData in booksData['Books']:
            book = Book(bookData['Book_ID'], bookData['Book_Name'])
            books.append(book)
            
    except requests.exceptions.RequestException as e:
        print(e)
        raise SystemExit(e)

    return books

books = initBooks()
ahadith = books[0].getChapter(1).getAhadith(1)
print(f"Hadith {ahadith.id}")
print(ahadith.sanad)
print(ahadith.text)
