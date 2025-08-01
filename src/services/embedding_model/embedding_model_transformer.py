import torch
from sentence_transformers import util, SentenceTransformer

from services.embedding_model import EmbeddingModelBase


class EmbeddingModelTransformer(EmbeddingModelBase):
    def __init__(self, config):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = None
        self.model_name_or_path = config['model_name_or_path']
        self.model_dir = config['model_dir']

    def load_model(self):
        self.model = SentenceTransformer(self.model_name_or_path)
        self.model.to(self.device)

    def save_model(self):
        self.model.save(self.model_dir)
        self.model_name_or_path = self.model_dir

    def encode(self, data):
        embeddings = self.model.encode(data, convert_to_tensor=True).to(self.device)
        return embeddings

    def cosine_similarity(self, emb1, emb2):
        similarity = util.cos_sim(emb1, emb2)
        return similarity