from abc import ABC, abstractmethod


class Repository(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def put(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class SqlRepository(Repository):

    def __init__(self, session):
        self.session = session

    def create(self):
        pass

    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
