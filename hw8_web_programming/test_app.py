import requests

response = requests.get('http://localhost:5000/api/recipes/')

print(response.json())

response = requests.get('http://localhost:5000/api/recipes/1')

print(response.status_code)

sample = {
    # 'id': request.json['id'] or RECIPES[-1]['id'] + 1,
    'meal': 'Lasagna',
    'description': 'Really delicious',
    'ingredients': 'Potatoes, cheese, tomatoes',
    'directions': 'Cook them',
}

response = requests.post('http://localhost:5000/api/recipes/', json=sample)

print(response.json())

response = requests.put('http://localhost:5000/api/recipes/update/1', json=sample)

print(response.json())

response = requests.delete('http://localhost:5000/api/recipes/delete/2', json=sample)

print(response)
