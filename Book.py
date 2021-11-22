import requests
import json
import Utils
from Chapter import Chapter

class Book:
    def __init__(self, bookID: int, bookName: str):
        self.id = bookID
        self.name = bookName
        self.chapters = self.getChapters()
        self.chaptersCount = len(self.chapters)

    def getChapters(self) -> []:
        chapterEndpoint: str = f"https://ahadith-api.herokuapp.com/api/chapter/{self.id}/en"
        try:
            response = requests.get(chapterEndpoint)
            # printJSON(response.json())
            chaptersText = json.dumps(response.json(), sort_keys=True, indent=4)
            chaptersData = json.loads(chaptersText)
        except requests.exceptions.RequestException as e:
            print(e)
            raise SystemExit(e)

        chapters = []
        for item in chaptersData['Chapter']:
            chapter = Chapter(self.id, item['Chapter_ID'], item['Chapter_Name'])
            # print(f"{chapter.id}, {chapter.name}")
            chapters.append(chapter)
            break
        return chapters

    def getChapter(self, chapterID: int):
        index: int = chapterID - 1
        if index < 0 or index >= self.chaptersCount:
            raise Exception(f"Unable to get chapter {chapterID}")
        else:
            return self.chapters[index]