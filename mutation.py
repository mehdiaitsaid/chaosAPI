def mutation(population, mutation_rate):
    import random
    mutated_population = []
    for testcase in population:
        if random.random() < mutation_rate:
            testcase['parameters'] = {key: random.choice(["MUTATION", value]) for key, value in testcase['parameters'].items()}
        mutated_population.append(testcase)
    return mutated_population