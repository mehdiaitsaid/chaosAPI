def main(openapi_spec_path, population_size, chaos_metrics, max_generations, mutation_rate):
    from load_openapi_spec import load_openapi_spec
    from generate_initial_population import generate_initial_population
    from optimize_and_execute import optimize_and_execute

    endpoints, parameters, methods = load_openapi_spec(openapi_spec_path)
    initial_population = generate_initial_population(endpoints, parameters, methods, population_size)
    optimized_test_suite = optimize_and_execute(initial_population, chaos_metrics, max_generations, mutation_rate)
    return optimized_test_suite

if __name__ == "__main__":
    def latency_metric(response):
        return response.elapsed.total_seconds()

    def error_rate_metric(response):
        return 1 if response.status_code >= 400 else 0

    def response_code_metric(response):
        return 1 if response.status_code == 200 else 0

    chaos_metrics = {
        'latency': latency_metric,
        'error_rate': error_rate_metric,
        'response_code': response_code_metric
    }

    optimized_suite = main(
        openapi_spec_path="path/to/openapi.json",
        population_size=100,
        chaos_metrics=chaos_metrics,
        max_generations=50,
        mutation_rate=0.1
    )
    print(optimized_suite)