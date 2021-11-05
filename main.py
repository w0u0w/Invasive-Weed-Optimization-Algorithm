from random import random
from tabulate import tabulate
import random


def initialPopulation(lb, up, popSize):
    population = []
    for j in range(popSize):
        population.append([[j + 1], [round(random.uniform(lb, up), 2)]])
    return population


def fitnessFunction(population):
    for l in range(len(population)):
        population[l][1][0] *= population[l][1][0]
        population[l][1][0] = round(population[l][1][0], 2)
    return population


def getBestWorstSolution(fitness):
    data_arr = []
    res = []
    for i in range(len(fitness)):
        data_arr.append(fitness[i][1][0])
    res.append(min(data_arr))
    res.append(max(data_arr))
    return res


def calculateSigma(maxiterations, n, sigmainitial, sigmaend):
    res = ((((maxiterations - n) ** 2)/(maxiterations ** 2)) * (sigmainitial - sigmaend)) + sigmainitial
    return round(res, 2)


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
    # bestSolution, worstSolution = float()
    #for i in range(populationSizeInitial):

    begin_population = initialPopulation(LB, UP, populationSizeInitial)  # Инициализация популяции
    headers_pop = ["Number", "Initial population"]
    print(tabulate(begin_population, headers_pop, tablefmt="grid"))

    fitnessInitial = fitnessFunction(begin_population)
    headers_fit = ["Number", "Initial fitness"]
    print(tabulate(fitnessInitial, headers_fit, tablefmt="grid"))

    bestSolution = getBestWorstSolution(fitnessInitial)[0]
    print("BEST SOLUTION:", bestSolution)

    worstSolution = getBestWorstSolution(fitnessInitial)[1]
    print("WORST SOLUTION:", worstSolution)

    sigma = calculateSigma(maxIterations, 1, sigmaInitial, sigmaEnd)
    print("SIGMA", sigma)