import requests
import json


resp = requests.get("https://teamtreehouse.com/library/flask-with-sqlalchemy-basics/read-update-delete")
data = json.loads(resp.content)

print(data)