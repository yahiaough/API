import json 
user = {
    "prenom" :"Paul",
    "age" : 19,
    "email" : "paul@gmail.com",
    "liste de competence" : {
        "competence1":"Python",
        "competence2":"Html",
        "competence3":"Php"
    }
}

fichier_json = json.dumps(user)
print(fichier_json)

with open('FichierJSON.json', 'w',  encoding='utf-8') as f:
    for liste in fichier_json:
        f.write(liste)
f.close()
print("Le fichier à bien été créer ")