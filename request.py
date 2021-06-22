import requests
import main
chunk_size = 100
filename = "Weather Report.txt"
p = {'q':'loction', 'appid':'api_key'}
r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=p)

with open(filename, 'wb') as fd:
     for chunk in r.iter_content(chunk_size):
          fd.write(chunk)