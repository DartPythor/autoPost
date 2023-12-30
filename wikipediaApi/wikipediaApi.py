import fileManager
import interfaceWikipediaApi
import requests


class WikipediaApi(
    interfaceWikipediaApi.InterfaceWikipediaApi,
    fileManager.FileManager,
):
    url = "https://{0}.wikipedia.org/w/api.php"
    source_url = "https://ru.wikipedia.org/wiki/{0}"

    def __init__(self, lang: str = "en"):
        super().__init__()
        self.lang = lang
        self.backup = None

    def _get(self, params):
        params.update({"format": "json"})
        return requests.get(url=self.url.format(self.lang), params=params).json()

    def get_pages_list(self, apcontinue="", limit=500):
        params = {
            "action": "query",
            "list": "allpages",
            "aplimit": str(limit),
        }
        if apcontinue:
            params.update({"apcontinue": apcontinue})

        pages_list = self._get(params)
        result = {
            "pages": [i["title"] for i in pages_list["query"]["allpages"]],
            "apcontinue": pages_list["continue"]["apcontinue"],
        }
        return result

    def get_title(self):
        data = self.load()
        if not data["pages"]:
            data = self.get_pages_list(data["apcontinue"])
        title = data["pages"].pop(0)
        self.backup = title
        self.save(data)
        return title

    def set_backup(self):
        if self.backup is None:
            ...
        data = self.load()
        data["pages"].append(self.backup)
        self.save(data)


__all__ = ()
