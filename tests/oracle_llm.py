import requests

ORACLE_CACHE = {}

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "l5_exactly_one_1"

PROMPT_TEMPLATE = """You are a formal language membership oracle.

Language definition:
A binary string over the alphabet {{0,1}} is ACCEPTED if and only if
it contains an EVEN number of symbol '1'.

Task:
Given a string, decide whether it belongs to the language.

Rules:
- Count ALL occurrences of '1'
- Accept if the count is EVEN (including zero)
- Reject otherwise

Output format:
Return exactly one character.
Return "1" if the string is ACCEPTED.
Return "0" if the string is REJECTED.
Do not write anything else.
Do not add words, explanations or punctuation.

Answer with 1 or 0 only.

Input string:
"{word}"
"""

def membership_query(word: str, k=3) -> bool:
    if word in ORACLE_CACHE:
        return ORACLE_CACHE[word]

    votes = []

    for _ in range(k):
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": PROMPT_TEMPLATE.format(word=word),
                "stream": False,
                "options": {"temperature": 0}
            },
            timeout=30
        )
        raw = response.json()["response"].strip()

        if raw == "1":
            votes.append(True)
        elif raw == "0":
            votes.append(False)

    # majority vote
    if votes:
        decision = votes.count(True) > votes.count(False)
    else:
        decision = False

    ORACLE_CACHE[word] = decision
    return decision
