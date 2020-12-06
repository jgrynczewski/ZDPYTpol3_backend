# Command-line application
import requests

base = input("Pierwsz waluta: ")
other = input("Druga waluta: ")

res = requests.get("http://data.fixer.io/api/latest?access_key=032053b70cf616de08638aeaeb1cfd1d")

if res.status_code != 200:
    raise Exception("Error: API request unsuccessful")

data = res.json()