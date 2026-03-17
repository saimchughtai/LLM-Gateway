def detect_injection(prompt):

    keywords = [
        "ignore instructions",
        "reveal system prompt",
        "bypass rules",
        "act as",
        "pretend you are"
    ]

    score = 0

    for word in keywords:
        if word in prompt.lower():
            score += 1

    return score