from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

class ConceptClusterer:
    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters
        self.vectorizer = TfidfVectorizer()
        self.kmeans = None
        self.data = []

    def cluster(self, new_data):
        self.data.extend(new_data)
        X = self.vectorizer.fit_transform(self.data)
        self.kmeans = KMeans(n_clusters=min(self.n_clusters, len(self.data)), random_state=42)
        self.kmeans.fit(X)
        clusters = {i: [] for i in range(self.kmeans.n_clusters)}
        for idx, label in enumerate(self.kmeans.labels_):
            clusters[label].append(self.data[idx])
        return clusters
