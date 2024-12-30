import argparse
import datetime
import subprocess
import os
from pathlib import Path
import sys
from languages import Language

class TextBuffer:
    def __init__(self):
        self.data = ""
        self.position = 0
    
    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return self.data
    
    def __repr__(self):
        return self.data
    
    def write(self, data):
        self.data += data
    
    def read(self):
        return self.data[self.position:]
    
    def read_line(self):
        newline_pos = self.data.find("\n", self.position)
        if newline_pos == -1:
            return ""
        output = self.data[self.position:newline_pos]
        self.position = newline_pos + 1
        return output
    
    def has_line(self):
        return "\n" in self.data[self.position:]

def get_args():
    today = datetime.date.today()
    parser = argparse.ArgumentParser(prog="submit.py", description="Submits the answer from a specific day")
    
    parser.add_argument("-y", "--year", type=int, default=today.year)
    parser.add_argument("-d", "--day", type=int, default=today.day)
    parser.add_argument(
        "-l", "--language",
        default=Language.PYTHON,
        type=Language,
        dest="lang"
    )
    parser.add_argument("--headers", default="headers.json")
    parser.add_argument("--no-submit", action="store_false", dest="submit")
    parser.add_argument("--test", action="store_true")
    parser.add_argument("-f", "--file", default="input.txt")
    parser.add_argument("-s", "--stream-output,", action="store_true", dest="stream") 

    args = parser.parse_args()
    if args.test:
        args.submit = False
        if args.file == "input.txt":
            args.file = "test.txt"
    return args

def get_current_folder(args):
    path = Path(str(args.year), f"Day{args.day}")
    path.mkdir(parents=True, exist_ok=True)
    return path

def get_command(args):
    match args.lang:
        case Language.PYTHON:
            return "python"
        case _:
            return "echo"

def run_program(args):
    os.chdir(get_current_folder(args))

    command = get_command(args)
    filename = f"Day{args.day}.{args.lang.ext}"
    proc = subprocess.Popen((command, filename, args.file), bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env={"PYTHONUNBUFFERED": "1"})

    if not args.stream:
        stdout_data, stderr_data = proc.communicate(timeout=1)
        if stdout_data.count("\n") > 2:
            print(stdout_data, end="")
        print(stderr_data, file=sys.stderr, end="")
        return proc.returncode, stdout_data

    stdout = []

    try:
        for output_line in iter(proc.stdout.readline, ""):
            stdout.append(output_line)
            print(output_line, end="", flush=True)
    except KeyboardInterrupt:
        proc.terminate()
    
    stderr = proc.stderr.read()

    proc.stdout.close()
    proc.stderr.close()

    print(stderr, file=sys.stderr, end="")

    return proc.returncode, "".join(stdout)

def print_output(args, ans):
    ans = ans.split("\n")
    if len(ans) == 0:
        return
    elif len(ans) == 1:
        ans1 = ans[0]
        ans2 = None
    elif len(ans) >= 2:
        ans1, ans2, *_ = ans

    print(f"{args.year} Day {args.day} Part 1: {ans1}")
    if ans2 is not None:
        print(f"{args.year} Day {args.day} Part 2: {ans2}")

def submit_value(args, value):
    ...

if __name__ == "__main__":
    args = get_args()
    returncode, output = run_program(args)
    print_output(args, output)
    if args.submit and returncode == 0:
        submit_value(args, output)