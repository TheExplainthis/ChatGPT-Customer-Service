from hyperdb import HyperDB
from hyperdb.galaxy_brain_math_shit import cosine_similarity, euclidean_metric, derridaean_similarity, hyper_SVM_ranking_algorithm_sort


class CustomizeHyperDB(HyperDB):
    def __init__(self, similarity_metric='cosine'):
        self.documents = []
        self.vectors = None
        if similarity_metric.__contains__("cosine"):
            self.similarity_metric = cosine_similarity
        elif similarity_metric.__contains__("euclidean"):
            self.similarity_metric = euclidean_metric
        elif similarity_metric.__contains__("derrida"):
            self.similarity_metric = derridaean_similarity
        else:
            raise Exception("Similarity metric not supported. Please use either 'cosine', 'euclidean' or 'derrida'.")

    def query(self, query_vector, top_k=5):
        ranked_results = hyper_SVM_ranking_algorithm_sort(self.vectors, query_vector, top_k=top_k, metric=self.similarity_metric)
        return [self.documents[index] for index in ranked_results]