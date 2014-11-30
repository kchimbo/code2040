import requests as r

payload = {'email':   'oaf7862@rit.edu',
           'github':  'http://github.com/oaf7862/code2040/'}

result = r.post("http://challenge.code2040.org/api/register", json=payload)

print(result.text)
