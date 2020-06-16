import json

data = [
    {
        'name': 'Luiz',
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

# converte um dicionário em uma string, ordenando as chaves (sort_keys=True) e identando com 4 espaços (indent=4)
json_str = json.dumps(data, sort_keys=True, indent=4)
print(type(json_str))
print(json_str)

# transforma uma string em um dict, neste caso, em uma lista de dicionários
json_dict = json.loads(json_str)
print(type(json_dict))
print(json_dict)
