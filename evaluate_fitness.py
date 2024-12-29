def evaluate_fitness(testcase, chaos_metrics):
    import requests
    try:
        response = requests.request(testcase['method'], testcase['endpoint'], params=testcase['parameters'])
        fitness_score = sum([chaos_metrics[metric](response) for metric in chaos_metrics])
    except Exception as e:
        fitness_score = -1  # Penalize test cases that fail to execute
    return fitness_score