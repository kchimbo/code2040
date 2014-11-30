import requests as r

payload = {'token':   '4OH4yRBOJq'}

result = r.post("http://challenge.code2040.org/api/haystack", json=payload)

res = result.json()['result']

haystack = res['haystack']

needle = res['needle']

counter = 0
for text in haystack:
        if text == needle:
            break
        counter += 1
        
payload['needle'] = counter

result = r.post("http://challenge.code2040.org/api/validateneedle",
                json=payload)

print(result.text)
