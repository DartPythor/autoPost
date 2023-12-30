import abc


class InterfaceWikipediaApi(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_pages_list(self, *args, **kwargs):
        pass


__all__ = ()
