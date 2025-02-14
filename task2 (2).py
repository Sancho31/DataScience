def typeBasedTransformer(**kwargs):
    transformed_data = {}

    for key, value in kwargs.items():
        if isinstance(value, (int, float)):  
            transformed_data[key] = value ** 2
        elif isinstance(value, str):  
            transformed_data[key] = value[::-1]
        elif isinstance(value, bool):  
            transformed_data[key] = not value
        elif isinstance(value, (list, tuple)):  
            transformed_data[key] = value[::-1]
        elif isinstance(value, dict):  
            if len(set(value.values())) == len(value):  
                transformed_data[key] = {v: k for k, v in value.items()}
            else:
                transformed_data[key] = value  
        else:  
            transformed_data[key] = value

    return transformed_data
