def load_openapi_spec(openapi_spec_path):
    import json
    with open(openapi_spec_path, 'r') as file:
        spec = json.load(file)
    endpoints = spec.get('paths', {}).keys()
    parameters = [param for path in spec.get('paths', {}).values() for param in path.get('parameters', [])]
    methods = [method for path in spec.get('paths', {}).values() for method in path.keys()]
    return endpoints, parameters, methods
