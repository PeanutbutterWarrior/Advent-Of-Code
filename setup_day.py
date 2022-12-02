import sys
import requests
import os
import json

year = sys.argv[1]
day = sys.argv[2]

with open("headers.json", "r") as file:
    headers = json.load(file)

url = f"https://adventofcode.com/{year}/day/{day}/input"
response = requests.get(url, **headers)
if response.status_code != 200:
    print(f"Request failed. Status: {response.status_code}")
    print(response.content)
    quit()

if not os.path.isdir(year):
    os.mkdir(year)
if not os.path.isdir(f"{year}/Day{day}"):
    os.mkdir(f"{year}/Day{day}")

with open(f"{year}/Day{day}/Day{day}.py", "w+") as file:
    file.write(f"""with open("Day{day}.txt", "r") as file:
    data = file.read()
""")

with open(f"{year}/Day{day}/Day{day}.txt", "wb+") as file:
    file.write(response.content)
