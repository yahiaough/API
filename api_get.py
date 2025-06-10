import requests

nom_ville =input("Veuillez saisir le nom de la ville : ")
code_pays = input("Veuillez saisir le code ISO du pays : ")
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={nom_ville},{code_pays}&appid=c7430fbbf22309097858b612e7387e28&units=metric&lang=fr")
if response.status_code == 200 :
    print("Statut de la réponse :", response.status_code)
    print("Contenu de la réponse : ", response.text)
else :
    print("La ville recherché est inexistante ! \n Statut de la réponse : ", response.status_code )