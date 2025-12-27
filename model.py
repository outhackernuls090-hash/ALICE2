from .clustering import ConceptClusterer
from .vector_memory import VectorMemory
import random

class BottomUpModel:
    def __init__(self):
        self.clusterer = ConceptClusterer()
        self.memory = VectorMemory()

    def learn(self, concept):
        self.memory.add(concept)
        return self.clusterer.cluster(self.memory.memory)

    def recall(self, query):
        return self.memory.search(query)

    def respond(self, query):
        matches = self.recall(query)
        if matches:
            return random.choice(matches)
        else:
            generic_responses = [
                "Interesting, tell me more!",
                "I see, go on...",
                "Hmm, could you explain that?",
                "Got it, what else?"
            ]
            return random.choice(generic_responses)
