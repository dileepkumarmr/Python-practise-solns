import requests
res = requests.get("http://automatetheboringstuff.com")
res.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(1000):
    playFile.write(chunk)
playFile.close()

