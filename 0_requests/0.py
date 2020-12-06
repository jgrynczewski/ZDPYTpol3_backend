import requests

# response = requests.get("https://www.google.pl")
# print(response.content)

res = requests.get("http://data.fixer.io/api/latest?access_key=032053b70cf616de08638aeaeb1cfd1d")
print(res.json().get('rates').get("PLN"))
print(res.json().get("date"))