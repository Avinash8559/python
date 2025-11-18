# work with an web api

# verify if app is responding / working
import requests

response_status = requests.get('https://api.github.com')
print(response_status)