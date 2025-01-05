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
    parser.add_argument("--full-output,", action="store_false", dest="condense") 
    parser.add_argument("--stream", action="store_true")

    args = parser.parse_args()
    if args.test:
        args.submit = False
        if args.file == "input.txt":
            args.file = "test.txt"
    
    if args.year < 2000:
        args.year += 2000

    return args

def get_current_folder(args):
    path = Path(str(args.year), f"Day{args.day}")
    path.mkdir(parents=True, exist_ok=True)
    return path

def get_command(args):
    match args.lang:
        case Language.PYTHON:
            return sys.executable
        case _:
            return "echo"

def run_program(args):
    os.chdir(get_current_folder(args))

    command = get_command(args)
    filename = f"Day{args.day}.{args.lang.ext}"
    proc = subprocess.Popen((command, filename, args.file), bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env={"PYTHONUNBUFFERED": "1", "PATH": "", "PYGAME_HIDE_SUPPORT_PROMPT": "1"})

    stdout = []
    try:
        for output_line in iter(proc.stdout.readline, ""):
            stdout.append(output_line)
            if args.stream:
                print(output_line, end="", flush=True)
    except KeyboardInterrupt:
        print("Keyboard interrupt recieved, killing program")
        proc.terminate()
    
    proc.wait()
    stderr = proc.stderr.read()

    proc.stdout.close()
    proc.stderr.close()

    if len(stderr) > 0:
        print(stderr, file=sys.stderr, end="")

    return proc.returncode, "".join(stdout)

def print_formatted_output(args, returncode, output):
    output = output.strip()
    num_lines = output.count("\n") + 1
    if num_lines == 0:
        return
    elif num_lines == 1:
        ans1, *_ = output.split("\n", maxsplit=1)
        print(f"{args.year} Day {args.day} Part 1: {ans1}")
    elif num_lines == 2:
        ans1, ans2, *_ = output.split("\n", maxsplit=2)
        print(f"{args.year} Day {args.day} Part 1: {ans1}")
        print(f"{args.year} Day {args.day} Part 2: {ans2}")
    elif num_lines <= 10 or not args.condense:
        print(output)
    else:
        *head, output = output.split("\n",maxsplit=5)
        output, *tail = output.rsplit("\n",maxsplit=5)
        print("\n".join(head))
        print(f"*** Ommited {num_lines - 10} lines ***")
        print("\n".join(tail))

def submit_value(args, value):
    ...

if __name__ == "__main__":
    args = get_args()
    returncode, output = run_program(args)
    if not args.stream:
        print_formatted_output(args, returncode, output)
    if args.submit and returncode == 0:
        submit_value(args, output)