import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

config = {
    # Embedding Models Vars
    "model_name_or_path": os.environ.get('MODEL_NAME_OR_PATH', 'sentence-transformers/all-MiniLM-L6-v2'),
    "model_dir": os.environ.get('MODEL_DIR', './services/embedding_model/model'),
}