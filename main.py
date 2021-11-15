from random import random
from tabulate import tabulate
import random
from operator import itemgetter


def initialPopFit(lb, up, popSize):
    initPopFit = []
    for j in range(popSize):
        popul = round(random.uniform(lb, up), 4)
        initPopFit.append([j + 1, popul, round(popul ** 2, 4)])
    return initPopFit


def getBestWorstSolution(dataarr):
    data_arr = []
    res = []
    for i in range(len(dataarr)):
        data_arr.append(dataarr[i][2])
    res.append(min(data_arr))
    res.append(max(data_arr))
    return res


def calculateSigma(maxiterations, n, sigmainitial, sigmaend):
    res = ((((maxiterations - n) ** 2)/(maxiterations ** 2)) * (sigmainitial - sigmaend)) + sigmainitial
    return round(res, 4)


if __name__ == '__main__':
    LB = -10  # Нижняя граница
    UP = 10  # Верхняя граница
    maxIterations = 5  # Максимальное кол-во итераций
    populationSizeInitial = 4  # Стартовый размер популяции
    maxPopulationSize = 10  # Максимальный размер популяции
    minSeed = 0  # Минимальное кол-во семян
    maxSeed = 5  # Максимальное кол-во семян
    sigmaInitial = 0.5  # Начальное отклонение
    sigmaEnd = 0.001  # Конечное отклонение
    solutions = []
    for i in range(populationSizeInitial):
        print("------------------ ITERATION NUMBER", i + 1, " ------------------")
        initialPopFitArr = initialPopFit(LB, UP, populationSizeInitial)
        headers_pop = ["Number", "Initial population", "Initial fitness"]
        print(tabulate(initialPopFitArr, headers_pop, tablefmt="grid"))

        bestSolution = getBestWorstSolution(initialPopFitArr)[0]
        print("BEST SOLUTION:", bestSolution)
        worstSolution = getBestWorstSolution(initialPopFitArr)[1]
        print("WORST SOLUTION:", worstSolution)

        sigma = calculateSigma(maxIterations, 1, sigmaInitial, sigmaEnd)
        print("SIGMA", sigma)

        # Фаза репродукции
        newPopFitArr = []
        n = 0
        for j in range(len(initialPopFitArr)):
            ratio = (initialPopFitArr[j][1] - worstSolution) / (bestSolution - worstSolution)  # помеенять на j
            s = int((minSeed + (maxSeed - minSeed) * ratio))
            if s == 0:
                s = int((minSeed + (maxSeed - minSeed) * ratio))
            # print(s)
            for f in range(s):
                n += 1
                # Генерация рандомной локации
                newSolutionPosition = initialPopFitArr[j][1] + (sigma * random.uniform(0.0012, 0.9174))  # помеенять на j
                # Фитнесс значения
                newFitness = round(newSolutionPosition ** 2, 4)
                newPopFitArr.append([n, newSolutionPosition, newFitness])
        headersNewPopFit = ["Number", "New population", "New fitness"]
        print(tabulate(newPopFitArr, headersNewPopFit, tablefmt="grid"))

        # Объединение популяций
        mergedPopFitArr = newPopFitArr
        for x in range(len(initialPopFitArr)):
            mergedPopFitArr.append([len(mergedPopFitArr) + 1, initialPopFitArr[x][1], initialPopFitArr[x][2]])
        headersMergedPopFit = ["Number", "Merged population", "Merged fitness"]
        print(tabulate(mergedPopFitArr, headersMergedPopFit, tablefmt="grid"))

        # Сортировка значений от минимума к масимуму
        mergedPopFitArr = sorted(mergedPopFitArr, key=itemgetter(2))
        print("[ SORTED BY FITNESS ]")
        print(tabulate(mergedPopFitArr, headersMergedPopFit, tablefmt="grid"))

        # Фаза конкурентного исключения
        if len(mergedPopFitArr) > maxPopulationSize:
            mergedPopFitArr = mergedPopFitArr[:maxPopulationSize]
        print("[ COMPETITIVE EXCLUSION ]")
        print(tabulate(mergedPopFitArr, headersMergedPopFit, tablefmt="grid"))

        # Поиск лучшего решения в итерации и добавления в память
        bestSolution = getBestWorstSolution(mergedPopFitArr)[0]
        print("ITERATION", i + 1, "BEST SOLUTION:", bestSolution)
        solutions.append([i + 1, bestSolution])
    print("------------------ SOLUTIONS HISTORY ------------------")
    headHistory = ["Iteration", "Solution"]
    print(tabulate(solutions, headHistory, tablefmt="grid"))
    print("BEST SOLUTION:", min(solutions))
