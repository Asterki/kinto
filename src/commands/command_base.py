import abc


# This is an abstract class that all commands must inherit from
class Command(abc.ABC):
    @property
    @abc.abstractmethod
    def description(self):
        pass

    @property
    @abc.abstractmethod
    def usage(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass
