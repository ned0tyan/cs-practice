def main():
    threshold = float(input("Введите порог в градусах цельсия: "))
    n = int(input('Введите количество записей: '))
    errorCounter = 0
    aboveThresholdCounter = 0
    maxScore = None
    scoresSum = 0

    for i in range(n):
        score = input()
        if (score == 'error'):
            errorCounter += 1
            continue

        score = float(score)
        if (maxScore == None):
            maxScore = score
        
        scoresSum += score
        if (score > threshold):
            aboveThresholdCounter += 1

        maxScore = max(maxScore, score)

    averageScore = round(scoresSum / (n - errorCounter), 1)

    print(n)
    print(errorCounter)
    print(aboveThresholdCounter)
    print(round(maxScore, 1))
    print(averageScore)


if __name__ == '__main__':
    main()
