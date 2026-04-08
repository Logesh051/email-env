def grade(action, correct):
    score = 0

    for i in range(len(correct["classification"])):
        if action["classification"][i] == correct["classification"][i]:
            score += 0.3

        if action["priority"][i] == correct["priority"][i]:
            score += 0.3

    if correct["summary"].lower() in action["summary"].lower():
        score += 0.4

    return min(score, 1.0)