import sys
import requests
import os
import json

year = sys.argv[1]
day = sys.argv[2]
extension = sys.argv[3]

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

if os.path.exists(f'{year}/Day{day}/day{day}.{extension}'):
    overwrite = input(f'{year}/Day{day}/day{day}.{extension} already exists. Overwrite? ')
    if overwrite != 'y':
        print("Aborting")
        quit()

with open(f"{year}/Day{day}/day{day}.{extension}", "w+") as file:
    if extension == "py":
        file.write(f"""with open("input.txt", "r") as file:\n    data = file.read()\n""")

with open(f"{year}/Day{day}/input.txt", "wb+") as file:
    file.write(response.content.strip())
