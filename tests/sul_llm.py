from aalpy.base import SUL
from oracle_llm import membership_query

class LLMOracleSUL(SUL):

    def __init__(self):
        super().__init__()

    def pre(self):
        pass

    def post(self):
        pass

    def step(self, letter):
        # Not used, required by interface
        return 0

    def query(self, word):
        if len(word) == 0:
            return [1 if membership_query("") else 0]

        outputs = []

        for i in range(len(word)):
            prefix = word[:i+1]
            outputs.append(1 if membership_query(prefix) else 0)

        return outputs
