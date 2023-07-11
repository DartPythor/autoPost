if __name__ != "__main__":
    from wikipediaApi.interfaceWikipediaApi import InterfaceWikipediaApi
    from wikipediaApi.fileManager import FileManager
else:
    from interfaceWikipediaApi import InterfaceWikipediaApi
    from fileManager import FileManager

import requests
import os
import logging
import pprint
from typing import Dict, List, Any

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler(os.path.join(os.getcwd(), "logs", "WikipediApi.log"), mode="w")
format_handler = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
handler.setFormatter(format_handler)
logger.addHandler(handler)


class WikipediaApi(InterfaceWikipediaApi, FileManager):
    url = "https://{0}.wikipedia.org/w/api.php"
    source_url = "https://ru.wikipedia.org/wiki/{0}"

    def __init__(self, lang: str = "ru"):
        super().__init__()
        self.path_file = ""
        self.lang = lang

    def _get(self, params: dict) -> dict:
        """Getting get requests on wiki"""

        params.update({"format": "json"})
        return requests.get(url=self.url.format(self.lang), params=params).json()

    def get_pages_list(self, apcontinue: str = "", limit: int = 500) -> dict[str, str, list[Any] | Any]:
        """возращает все русскоязычные страницы, limit - сколько придет в json ответе(макс. 500)"""

        params = {"action": "query", "list": "allpages", "aplimit": str(limit)}
        if apcontinue:
            params.update({"apcontinue": apcontinue})

        pages_list = self._get(params)
        result = {
            "pages": [i["title"] for i in pages_list["query"]["allpages"]],
            "apcontinue": pages_list["continue"]["apcontinue"]
                  }
        return result

    def get_content_page(self, titles: str | List[str]) -> Dict[str, str]:
        """return content(small) page wikipedia with title"""
        params = {
            "action": "query", "prop": "extracts",
            "exlimit": "max", "explaintext": "",
            "exintro": "", "redirects": "",
            "exchars": str(1200)
                  }
        params.update({"titles": titles if isinstance(titles, str) else "|".join(titles)})
        response = self._get(params)
        pages_id = tuple(response["query"]["pages"].keys())
        pages_title = [titles] if isinstance(titles, str) else titles

        return {pages_title[i]: response["query"]["pages"][pages_id[i]]["extract"] for i in range(len(pages_id))}

    def get_formate_page(self, title: str, data: str) -> str:
        """formatting datas for post"""

        return "\n".join((data, "Источник: " + self.source_url.format(title)))


if __name__ == '__main__':
    wiki = WikipediaApi()
    pprint.pprint(wiki.get_content_page("(1367) Нонгома"))
    # print(wiki._get_lang_from_dict(wiki.get_lang("'eiki")))
