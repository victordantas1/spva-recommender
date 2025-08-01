from abc import ABC, abstractmethod
class EmbeddingModelBase(ABC):
    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def save_model(self):
        pass

    @abstractmethod
    def encode(self, data):
        pass

    @abstractmethod
    def cosine_similarity(self, emb1, emb2):
        pass