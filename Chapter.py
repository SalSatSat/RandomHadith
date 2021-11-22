import requests
import json
import Utils
from Ahadith import Ahadith

class Chapter:
    def __init__(self, bookID: int, chapterID: int, chapterName: str):
        self.id = chapterID
        self.name = chapterName
        self.ahadiths = self.getAhadiths(bookID)
        self.ahadithsCount = len(self.ahadiths)

    def getAhadiths(self, bookID: int) -> []:
        ahadithEndpoint: str = f"https://ahadith-api.herokuapp.com/api/ahadith/{bookID}/{self.id}/en"
        try:
            response = requests.get(ahadithEndpoint)
            # printJSON(response.json())
            ahadithsText = json.dumps(response.json(), sort_keys=True, indent=4)
            ahadithsData = json.loads(ahadithsText)
        except requests.exceptions.RequestException as e:
            print(e)
            raise SystemExit(e)

        ahadiths = []
        for item in ahadithsData['Chapter']:
            ahadith = Ahadith(item['Hadith_ID'], item['En_Sanad'], item['En_Text'])
            # print(f"{ahadith.id}, {ahadith.sanad}, {ahadith.text}")
            ahadiths.append(ahadith)

        return ahadiths

    def getAhadith(self, ahadithID: int):
        index: int = ahadithID - 1
        if index < 0 or index >= self.ahadithsCount:
            raise Exception(f"Unable to get ahadith {ahadithID}")
        else:
            return self.ahadiths[index]