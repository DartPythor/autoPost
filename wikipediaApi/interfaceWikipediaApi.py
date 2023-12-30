from abc import abstractmethod
from abc import ABCMeta


class InterfaceWikipediaApi(metaclass=ABCMeta):
    @abstractmethod
    def get_pages_list(self, *args, **kwargs):
        pass

    # @abstractmethod
    # def get_image_title(self, *args, **kwargs):
    #     pass
