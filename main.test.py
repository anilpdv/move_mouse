import requests

response = requests.get('https://quotesappapi.herokuapp.com/quotes')
print(response.status_code)


