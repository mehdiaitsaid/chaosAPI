def optimize_and_execute(population, chaos_metrics, max_generations, mutation_rate):
    for _ in range(max_generations):
        fitness_scores = [evaluate_fitness(testcase, chaos_metrics) for testcase in population]
        selected_population = selection(population, fitness_scores)
        offspring_population = crossover(selected_population)
        population = mutation(offspring_population, mutation_rate)
    return population