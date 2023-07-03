from abc import ABCMeta
from abc import abstractmethod


class InterfaceVkApi(metaclass=ABCMeta):
    @abstractmethod
    def _post(self, *args, **kwargs):
        pass

    @abstractmethod
    def wall_post(self, *args, **kwargs):
        pass
