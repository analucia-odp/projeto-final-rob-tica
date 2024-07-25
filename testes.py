import numpy as np
import random

def calculate_distance(route, distance_matrix):
    return sum(distance_matrix[route[i-1], route[i]] for i in range(len(route)))

def fitness(route, distance_matrix):
    return 1 / calculate_distance(route, distance_matrix)

def selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    selected_indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return [population[i] for i in selected_indices]

def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [-1] * size
    child[start:end] = parent1[start:end]
    pointer = 0
    for i in range(size):
        if child[i] == -1:
            while parent2[pointer] in child:
                pointer += 1
            child[i] = parent2[pointer]
    return child

def mutate(route, mutation_rate=0.1):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route

def genetic_algorithm(distance_matrix, population_size=100, generations=500, mutation_rate=0.1):
    num_cities = len(distance_matrix)
    population = [random.sample(range(num_cities), num_cities) for _ in range(population_size)]
    
    for generation in range(generations):
        fitnesses = [fitness(route, distance_matrix) for route in population]
        population = selection(population, fitnesses)
        new_population = []
        
        for i in range(0, population_size, 2):
            parent1, parent2 = population[i], population[i+1]
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            new_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
        
        population = new_population
    
    best_route = min(population, key=lambda route: calculate_distance(route, distance_matrix))
    return best_route, calculate_distance(best_route, distance_matrix)

# Example usage
distance_matrix = np.random.rand(10, 10)  # Replace with your actual distance matrix
best_route, best_distance = genetic_algorithm(distance_matrix)
print("Best route:", best_route)
print("Best distance:", best_distance)
