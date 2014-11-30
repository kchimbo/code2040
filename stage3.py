import requests as r

payload = {'token':   '4OH4yRBOJq'}

result = r.post("http://challenge.code2040.org/api/prefix", json=payload)

res = result.json()['result']

words = res['array']

prefix = res['prefix']

words_noprefix = []

for word in words:
    if prefix != word[:len(prefix)]:
        words_noprefix.append(word)

payload['array'] = words_noprefix

req = r.post("http://challenge.code2040.org/api/validateprefix", json=payload)

print(req.text)
