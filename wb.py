import requests

res = requests.get("https://autoatetheboringstuff.com/files/rj.txt")
type(res)
res.status_code== requests.codes.ok
len(res.text)
print(res.text[:250])
