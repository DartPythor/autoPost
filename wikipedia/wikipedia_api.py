import requests

import wikipedia.fileManager
import wikipedia.interface_wikipedia_api


class WikipediaException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)


class BackupError(WikipediaException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class WikipediaApi(
    wikipedia.interface_wikipedia_api.InterfaceWikipediaApi,
    wikipedia.fileManager.FileManager,
):
    url = "https://{0}.wikipedia.org/w/api.php"
    source_url = "https://ru.wikipedia.org/wiki/{0}"

    def __init__(self, lang: str = "ru"):
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

    def get_content_page(self, titles):
        """return content(small) page wikipedia with title"""
        params = {
            "action": "query",
            "prop": "extracts",
            "exlimit": "max",
            "explaintext": "",
            "exintro": "",
            "redirects": "",
            "exchars": str(150),
        }
        params.update(
            {"titles": titles if isinstance(titles, str) else "|".join(titles)},
        )
        response = self._get(params)
        pages_id = tuple(response["query"]["pages"].keys())
        pages_title = [titles] if isinstance(titles, str) else titles

        return {
            pages_title[i]: response["query"]["pages"][pages_id[i]]["extract"]
            for i in range(len(pages_id))
        }

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
            raise BackupError("Error backup return")
        data = self.load()
        data["pages"].insert(0, self.backup)
        self.save(data)


__all__ = ()
