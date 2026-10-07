names = ['Аня', 'Боря', 'Вика']
scores = [7.0, 9.0, 9.0]

#Имя участника с наибольшим результатом. При равенстве — тот, кто раньше в списке.
def winner(names: list[str], scores: list[float]) -> str:
    betterResultName = 0
    maxResult = -1
    for i in range(len(scores)):
        if (scores[i] > maxResult):
            maxResult = scores[i]
            betterResultName = names[i]
    return betterResultName

#Средний результат, округлённый до сотых. Для пустого списка — 0.0.
def average(scores: list[float]) -> float:
    if (scores == []):
        return 0
    return sum(scores) / len(scores)

#Имена по убыванию результата. При равенстве — в исходном порядке.
def ranking(names: list[str], scores: list[float]) -> list[str]:
    ranked_names = names.copy()
    ranked_scores = scores.copy()

    for i in range(len(ranked_scores)):
        for j in range(len(ranked_scores) - 1 - i):
            if ranked_scores[j] < ranked_scores[j + 1]:
                ranked_scores[j], ranked_scores[j + 1] = ranked_scores[j + 1], ranked_scores[j]
                ranked_names[j], ranked_names[j + 1] = ranked_names[j + 1], ranked_names[j]

    return ranked_names

#Имена тех, чей результат строго выше среднего. Порядок — как в списке.
def above_average(names: list[str], scores: list[float]) -> list[str]:
    averageScore: float = average(scores)
    aboveAverageNamesList = []

    for i in range(len(names)):
        if (scores[i] > averageScore):
            aboveAverageNamesList.append(names[i])

    return aboveAverageNamesList


