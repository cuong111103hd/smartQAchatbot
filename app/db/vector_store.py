import faiss
import numpy as np
import pickle 
from typing import List, Dict

class FAISSVectorStore:
    def __init__(self, dim:int):
        self.index = faiss.IndexFlatIP(dim)
        self.metadata: List[Dict] = []
        self.texts: List[str] = []

    def add(self, embeddings: np.array, texts: List[str], metadata: List[Dict]):
        self.index.add(embeddings)
        self.texts.extend(texts)
        self.metadata.extend(metadata)


    def search(self, query_embedding: np.array, top_k: int =5):
        scores, indices = self.index.search(query_embedding, top_k)

        results = []

        for score, idx in zip(scores[0],indices[0]):
            results.append({
                "score": float(score),
                "text": self.texts[idx],
                "metadata": self.metadata[idx]
            })

        return results

    def save(self, path: str):
        faiss.write_index(self.index, f"{path}.index")
        with open(f"{path}.pkl","wb") as f:
            pickle.dump(
                {
                    "text": self.texts,
                    "metadata":self.metadata
                },
                f
            )
    def load(self,path: str):
        self.index = faiss.read_index(f"{path}.index")
        with open(f"{path}.pkl","rb") as f:
            data = pickle.load(f)
            self.texts = data["text"]
            self.metadata = data["metadata"]