import json

data = [
    {
        'name': 'Fuiz',
        'age': 19
    },
    {
        'name': 'Filipy',
        'age': 15
    },
    {
        'name': 'Araujo',
        'age': 23
    }
]

json_str = json.dumps(data, sort_keys=True, indent=4)
print(json_str)

json_dict = json.loads(json_str)
print(json_dict)
