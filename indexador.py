import msvcrt
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json
print("Bienvenidos a el indexador de Google Api.") 
print("Un Proyecto de Samuel Castillo") 

url = input("Ingrese la URL a procesar: ")

option = input("""Que deseas hacer: 
    1. Indexar
    2. eliminar URL (Cuidado con esta opcion)
""") 

SERVICE_KEY = "service_account.json" 
SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
GETMETADATA = "https://indexing.googleapis.com/v3/urlNotifications/metadata"
content = {}
content['url'] = url
 
credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_KEY, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())

if option == "1":
    print("Procesando...")
    content['type'] = "URL_UPDATED"
    json_content = json.dumps(content)
    response, content = http.request(ENDPOINT, method="POST", body=json_content)
    result = json.loads(content.decode())
    print(result)
elif option == "2":
    print("Procesando...")
    content['type'] = "URL_DELETED"
    json_content = json.dumps(content)
    response, content = http.request(ENDPOINT, method="POST", body=json_content)
    result = json.loads(content.decode())
    print(result)
msvcrt.getch()