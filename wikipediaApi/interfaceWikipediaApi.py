from abc import abstractmethod
from abc import ABCMeta


class InterfaceWikipediaApi(metaclass=ABCMeta):
    @abstractmethod
    def get_pages_list(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_content_page(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_formate_page(self, *args, **kwargs):
        pass
