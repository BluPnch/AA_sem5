import math

import numpy as np
import random
from math import *

def initialize_pheromones(n):
    return [[1 for _ in range(n)] for _ in range(n)]

def calculate_probabilities(pheromones, visibility, visited, current_city, alpha, beta):
    n = len(pheromones)
    probabilities = [0] * n
    for j in range(n):
        if not visited[j]:
            probabilities[j] = (pheromones[current_city][j] ** alpha) * (visibility[current_city][j] ** beta)
    total = sum(probabilities)
    if total == 0:
        probabilities = [1 if not visited[j] else 0 for j in range(n)]
        total = sum(probabilities)
    return [p / total for p in probabilities]

def update_pheromones(distance_matrix, pheromones, routes, lengths, rho, Q, elite_route=None):
    n = len(pheromones)
    for i in range(n):
        for j in range(n):
            pheromones[i][j] *= (1 - rho)

    for route, length in zip(routes, lengths):
        for i in range(len(route) - 1):
            pheromones[route[i]][route[i + 1]] += Q / length

    if elite_route:
        elite_length = sum(distance_matrix[elite_route[i]][elite_route[i + 1]] for i in range(len(elite_route) - 1))
        for i in range(len(elite_route) - 1):
            pheromones[elite_route[i]][elite_route[i + 1]] += Q / elite_length

    return pheromones


def initialize_visibility(distance_matrix):
    n = len(distance_matrix)
    visibility = []

    for i in range(n):
        row = []
        for j in range(n):
            if distance_matrix[i][j] > 0:
                visibility_value = 1 / distance_matrix[i][j]
            else:
                visibility_value = 0
            row.append(visibility_value)
        visibility.append(row)
    return visibility

def calculate_route_length(route, distance_matrix):
    length = 0
    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i + 1]
        distance = distance_matrix[from_city][to_city]
        length += distance
    return length

def ant_colony_optimization(n, distance_matrix, alpha, beta, rho, Q, tmax, n_ants):
    visibility = initialize_visibility(distance_matrix)
    pheromones = initialize_pheromones(n)

    best_route = None
    best_length = float('inf')

    for t in range(tmax):
        routes = []
        lengths = []

        for ant in range(n_ants):
            current_city = random.randint(0, n - 1)
            visited = [False] * n
            visited[current_city] = True
            route = [current_city]

            while len(route) < n:
                probabilities = calculate_probabilities(pheromones, visibility, visited, current_city, alpha, beta)
                r = random.random()
                cumulative = 0
                next_city = None
                for j, prob in enumerate(probabilities):
                    cumulative += prob
                    if r <= cumulative + 1e-5:
                        next_city = j
                        break

                route.append(next_city)
                visited[next_city] = True
                current_city = next_city

            route.append(route[0])
            routes.append(route)

            length = calculate_route_length(route, distance_matrix)
            lengths.append(length)

        min_length = min(lengths)
        if min_length < best_length:
            best_length = min_length
            best_route = routes[lengths.index(min_length)]

        pheromones = update_pheromones(distance_matrix, pheromones, routes, lengths, rho, Q, elite_route=best_route)

    return best_route, best_length

# ПОЛНЫЙ ПЕРЕБОР
def generate_permutations(elements):
    n = len(elements)
    if n == 0:
        return [[]]

    permutations = []
    for i in range(n):
        generated_permutations = generate_permutations(elements[:i] + elements[i+1:])
        for perm in generated_permutations:
            permutations.append([elements[i]] + perm)
    return permutations

def full_check(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    best_length = float('inf')

    perms = generate_permutations(cities)
    for perm in perms:
        cycle = perm + [perm[0]]

        length = 0
        for i in range(n):
            from_city = cycle[i]
            to_city = cycle[i + 1]
            distance = distance_matrix[from_city][to_city]
            length += distance

        if length < best_length:
            best_length = length

    return best_length




cities_5 = [
    {"название": "Вавилон", "широта": 32.536, "долгота": 44.420},
    {"название": "Мемфис", "широта": 29.849, "долгота": 31.254},
    {"название": "Фивы (Египет)", "широта": 25.718, "долгота": 32.645},
    {"название": "Иерусалим", "широта": 31.768, "долгота": 35.213},
    {"название": "Афины", "широта": 37.984, "долгота": 23.728},
    {"название": "Дамаск", "широта": 33.513, "долгота": 36.292},
    {"название": "Урарту", "широта": 38.501, "долгота": 43.370},
    {"название": "Мохенджо-Даро", "широта": 27.327, "долгота": 68.132},
    {"название": "Харран", "широта": 36.867, "долгота": 39.031}
    ]

cities_10 = [
    {"название": "Рим", "широта": 41.902, "долгота": 12.496},
    {"название": "Карфаген", "широта": 36.853, "долгота": 10.323},
    {"название": "Александрия", "широта": 31.200, "долгота": 29.918},
    {"название": "Персеполь", "широта": 29.934, "долгота": 52.891},
    {"название": "Ниневия", "широта": 36.360, "долгота": 43.150},
    {"название": "Троя", "широта": 39.957, "долгота": 26.238},
    {"название": "Спарта", "широта": 37.075, "долгота": 22.429},
    {"название": "Сузиана", "широта": 32.194, "долгота": 48.247},
    {"название": "Кносс", "широта": 35.299, "долгота": 25.162}]

cities_15 = [
    {"название": "Эфес", "широта": 37.941, "долгота": 27.341},
    {"название": "Тир", "широта": 33.273, "долгота": 35.196},
    {"название": "Коринф", "широта": 37.905, "долгота": 22.934},
    {"название": "Пальмира", "широта": 34.551, "долгота": 38.276},
    {"название": "Угарит", "широта": 35.595, "долгота": 35.782},
    {"название": "Сидон", "широта": 33.561, "долгота": 35.375},
    {"название": "Гиза", "широта": 29.978, "долгота": 31.134},
    {"название": "Луксор", "широта": 25.687, "долгота": 32.639},
    {"название": "Тартесс", "широта": 37.191, "долгота": -6.929}]

def haversine(lat_1, lon_1, lat_2, lon_2):
    R = 6371 
    lat_1, lon_1, lat_2, lon_2 = map(radians, [lat_1, lon_1, lat_2, lon_2])
    dlat = lat_2 - lat_1
    dlon = lon_2 - lon_1
    a = sin(dlat / 2) ** 2 + cos(lat_1) * cos(lat_2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


def convert_to_matrix(cities):
    n = len(cities)
    distance_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = haversine(cities[i]["широта"], cities[i]["долгота"], cities[j]["широта"], cities[j]["долгота"])
    return distance_matrix

def generate_graphs():
    graphs = []
    for cities in [cities_5, cities_10, cities_15]:
        graphs.append(convert_to_matrix(cities))
    return graphs


# ПАРАМЕТРИЗАЦИЯ
def run_experiments(graph, alpha, beta, ro, Q, tmax, n_ants, M):

    lengths = []
    for i in range(M):
        length = ant_colony_optimization(len(graph), graph, alpha, beta, ro, Q, tmax, n_ants)
        lengths.append(length)

    return lengths

def parametrization():
    Q = 100
    n_ants = 10
    M = 10

    graph = generate_graphs()[2]
    # for i in range(len(graphs[0])):
    #     for j in range(len(graphs[0])):
    #         print(graphs[0][i][j], end = '\t')
    #     print('\n')

    # for graph in graphs:
    ethalon_decision = full_check(graph)
    print("Ethalon: ", ethalon_decision)

    for alpha in [0.1, 0.25, 0.5, 0.75, 0.9]:
        beta = 1 - alpha
        for ro in [0.1, 0.25, 0.5, 0.75, 0.9]:
            for tmax in [20, 50, 100, 150, 200]:
                results = run_experiments(graph, alpha, beta, ro, Q, tmax, n_ants, M)
                # print(results)
                devs = []
                for result in results:
                    devs.append(abs(result[1] - ethalon_decision))

                max_deviation = max(devs)
                median_deviation = np.median(devs)
                mean_deviation = np.mean(devs)

                print(f"Alpha: {alpha}, ro: {ro}, Tmax: {tmax}, Results: {max_deviation:.3f}, {median_deviation:.3f}, {mean_deviation:.3f}")


parametrization()