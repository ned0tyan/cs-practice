names = ['Аня', 'Боря', 'Вика']
scores = [7.0, 9.0, 9.0]

def winner(names: list[str], scores: list[float]) -> int:
    betterResultIndex = 0
    maxResult = -1
    for i in scores.count():
        if (scores[i] > maxResult):
            maxResult = scores[i]
            betterResultIndex = i
    return betterResultIndex

def average(scores: list[float]) -> float:
    if (scores == []):
        return 0
    return sum(scores) / scores.count()

