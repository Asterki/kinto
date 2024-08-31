import abc


# This is an abstract class that all commands must inherit from
class Command(abc.ABC):
    @property
    @abc.abstractmethod
    def run(self, *args):
        pass

    @property
    @abc.abstractmethod
    def info(self) -> dict:
        pass