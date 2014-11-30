import requests as r

payload = {'token':   '4OH4yRBOJq'}

result = r.post("http://challenge.code2040.org/api/getstring", json=payload)

word = result.json()['result']

payload['string'] = word[::-1]

result = r.post("http://challenge.code2040.org/api/validatestring",
                json=payload)

print(result.text)
