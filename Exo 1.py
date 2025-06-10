import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")


print("code de statut de la réponse : ", response.status_code)
print("contenu de la réponse : ", response.text)



