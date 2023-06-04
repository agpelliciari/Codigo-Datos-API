import requests
import json

url = "https://v3.football.api-sports.io/teams?league=128&season=2023"

payload = {}
headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "c347da80012545f47dd7ac448d329d83"
    }

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


# Pasar de json a dicc de python

stri_json = response.text
diccionario_equipos = json.loads(stri_json)
#print(diccionario_equipos)

# Serializing json

json_object = json.dumps(diccionario_equipos, indent=4)
 
# Writing to sample.json

with open("planteles.json", "w") as outfile:
    outfile.write(json_object)



#Prueba obtener datos

for response in diccionario_equipos:
     for team in response:
          pass
       







