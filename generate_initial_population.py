def generate_initial_population(endpoints, parameters, methods, population_size):
    import random
    population = []
    for _ in range(population_size):
        testcase = {
            'endpoint': random.choice(list(endpoints)),
            'parameters': random.sample(parameters, k=min(len(parameters), 3)),
            'method': random.choice(methods)
        }
        population.append(testcase)
    return population