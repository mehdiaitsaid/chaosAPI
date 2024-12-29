def crossover(parent_population):
    import random
    offspring_population = []
    for _ in range(len(parent_population) // 2):
        parent1, parent2 = random.sample(parent_population, 2)
        child1 = {
            'endpoint': parent1['endpoint'],
            'parameters': parent2['parameters'],
            'method': random.choice([parent1['method'], parent2['method']])
        }
        child2 = {
            'endpoint': parent2['endpoint'],
            'parameters': parent1['parameters'],
            'method': random.choice([parent1['method'], parent2['method']])
        }
        offspring_population.extend([child1, child2])
    return offspring_population