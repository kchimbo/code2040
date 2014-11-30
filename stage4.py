import requests as r
import arrow

payload = {'token':   '4OH4yRBOJq'}

result = r.post("http://challenge.code2040.org/api/time", json=payload)

res = result.json()['result']

datestamp = res['datestamp']

delta = res['interval']

now = (arrow.get(datestamp).replace(seconds=delta))

now = str(now)[:19] + ".000Z"

payload['datestamp'] = now

result = r.post("http://challenge.code2040.org/api/validatetime", json=payload)

print(result.text)