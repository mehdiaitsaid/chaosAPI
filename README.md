# ChaosAPI: Chaos Engineering Automation for API Testing

**ChaosAPI** is a Python-based framework that automates chaos engineering for API testing using the OpenAPI Specification and Genetic Algorithms. The framework generates, optimizes, and executes API test cases to identify edge cases, potential faults, and improve system robustness.

## Features

- **OpenAPI Specification Integration**: Automatically parses OpenAPI specs to identify endpoints, methods, and parameters.
- **Genetic Algorithm-Based Optimization**: Utilizes selection, crossover, and mutation to optimize test cases over multiple generations.
- **Chaos Injection**: Introduces faults, unexpected inputs, and edge cases to simulate real-world failures.
- **Highly Modular Architecture**: Each functionality is encapsulated in standalone modules for flexibility and scalability.
- **Customizable Metrics**: Define your own chaos metrics (e.g., latency, error rate) to guide optimization.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mehdiaitsaid/chaosAPI.git
   cd ChaosAPI
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the framework:
   ```bash
   python main.py
   ```

---

## Usage

### OpenAPI Specification
Provide the path to your OpenAPI JSON file. For example:
```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Example API",
    "version": "1.0.0"
  },
  "paths": {
    "/users": {
      "get": {
        "parameters": [
          { "name": "page", "in": "query", "schema": { "type": "integer" } },
          { "name": "limit", "in": "query", "schema": { "type": "integer" } }
        ]
      }
    }
  }
}
```

### Running the Framework
1. Edit the `main.py` file to specify:
   - `openapi_spec_path`: Path to your OpenAPI spec.
   - `population_size`: Number of test cases in each generation.
   - `chaos_metrics`: Custom metrics for evaluating test case fitness.
   - `max_generations`: Number of generations for optimization.
   - `mutation_rate`: Probability of test case mutation.

2. Execute the main script:
   ```bash
   python main.py
   ```

### Example Output

Optimized test suite:
```json
[
  {
    "endpoint": "/users",
    "parameters": { "page": 3, "limit": 20 },
    "method": "get"
  },
  {
    "endpoint": "/users/{id}",
    "parameters": { "id": "test_id_789" },
    "method": "get"
  }
]
```

---

## Project Structure

```
ChaosAPI/
├── load_openapi_spec.py          # Module for loading OpenAPI specification
├── generate_initial_population.py # Module for generating initial population of test cases
├── evaluate_fitness.py           # Module for evaluating test case fitness
├── apply_chaos.py                # Module for introducing chaos
├── selection.py                  # Module for selecting top test cases
├── crossover.py                  # Module for performing crossover on test cases
├── mutation.py                   # Module for mutating test cases
├── optimize_and_execute.py       # Module for optimizing and executing tests
├── main.py                       # Main script to run the framework
├── requirements.txt              # Python dependencies
└── README.md                     # Documentation
```

---

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push:
   ```bash
   git commit -m "Add feature"
   git push origin feature-name
   ```
4. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions or support, please open an issue in the repository or contact [m.aitsaid@uhp.ac.ma].

