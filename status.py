import requests as r

payload = {'token':   '4OH4yRBOJq'}

result = r.post("http://challenge.code2040.org/api/status", json=payload)

print(result.text)
