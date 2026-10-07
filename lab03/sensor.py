def main():
    threshold = float(input("Введите порог в градусах цельсия: "))
    n = int(input('Введите количество записей: '))
    errorCounter = 0
    aboveThresholdCounter = 0
    maxScore = -1
    averageScore = 0

    for i in range(n):
        score = input()

        if (score != 'error'):
            score = float(score)
            averageScore += score
            if (score > threshold):
                aboveThresholdCounter += 1

            maxScore = max(maxScore, score)
        else:
            errorCounter += 1
    
    print(n)
    print(errorCounter)
    print(aboveThresholdCounter)
    print(round(maxScore, 1))
    print(round(averageScore / (n - errorCounter), 1))


if __name__ == '__main__':
    main()
