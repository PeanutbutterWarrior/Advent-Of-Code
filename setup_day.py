import requests
import json
import argparse
import datetime
from enum import Enum, auto
from pathlib import Path
from bs4 import BeautifulSoup

class Language(Enum):
    PYTHON = auto(), "py"
    C = auto(), "c"

    def __init__(self, _, extension):
        self.ext = extension

    @classmethod
    def _missing_(cls, value):
        return language_abbr.get(value, None)

language_abbr = {"py": Language.PYTHON, "python": Language.PYTHON, "c": Language.C}

def get_args():
    today = datetime.date.today()
    parser = argparse.ArgumentParser(prog="day_setup.py", description="Sets up files for each day of Advent of Code")
    
    parser.add_argument("-y", "--year", type=int, default=today.year)
    parser.add_argument("-d", "--day", type=int, default=today.day)
    parser.add_argument(
        "-l", "--language",
        choices=list(language_abbr.keys()),
        default=Language.PYTHON,
        type=Language,
        dest="lang"
    )
    parser.add_argument("--headers", default="headers.json")

    return parser.parse_args()

def load_headers(args):
    with open(args.headers, "r") as file:
        return json.load(file)

def make_request(url):
    headers = load_headers(args)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Request failed. Status: {response.status_code}")
        print(response.content)
        quit()
    return response.content.decode().strip()

def get_input_file(args):
    url = f"https://adventofcode.com/{args.year}/day/{args.day}/input"
    return make_request(url)

def get_test_file(args):
    url = f"https://adventofcode.com/{args.year}/day/{args.day}"
    data = make_request(url)
    data = data[data.find("<pre>"):data.find("</pre>") + 7]
    soup = BeautifulSoup(data, "html.parser")
    code_block = soup.find("pre").find("code")
    return code_block.get_text()

def get_current_folder(args):
    path = Path(str(args.year), f"Day{args.day}")
    path.mkdir(parents=True, exist_ok=True)
    return path

def get_template(args):
    with open(Path("templates", f"{args.lang.ext}.txt")) as file:
        data = file.read()
    
    data = data.replace("{{day}}", str(args.day)).replace("{{year}}", str(args.year))
    return data

def write_files(args):
    folder = get_current_folder(args)
    day_name = f"Day{args.day}"
    (folder / f"{day_name}.{args.lang.ext}").write_text(get_template(args))
    (folder / "input.txt").write_text(get_input_file(args))
    (folder / "test.txt").write_text(get_test_file(args))

if __name__ == "__main__":
    args = get_args()
    write_files(args)