import argparse
import datetime
import subprocess
import os
from pathlib import Path
import sys
from languages import Language

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
    parser.add_argument("-f", "--file")

    args = parser.parse_args()
    if args.test:
        args.submit = False

    return args

def get_current_folder(args):
    path = Path(str(args.year), f"Day{args.day}")
    path.mkdir(parents=True, exist_ok=True)
    return path


def run_python(args):
    command = f"python Day{args.day}.py"
    if args.file is not None:
        file = args.file
    elif args.test:
        file = "test.txt"
    else:
        file = "input.txt"

    return subprocess.run(command, file, capture_output=True)

def run_c(args):
    proc = subprocess.run(f"gcc -o out.exe Day{args.day}.c", capture_output=True)
    if proc.returncode != 0:
        return proc
    return subprocess.run("./out.exe", capture_output=True)

def run_rust(args):
    proc = subprocess.run(f"rustc -o out.exe Day{args.day}.rs", capture_output=True)
    if proc.returncode != 0:
        return proc
    return subprocess.run("./out.exe", capture_output=True)
    

def run_program(args):
    os.chdir(get_current_folder(args))
    run_func = None
    if args.lang == Language.PYTHON:
        run_func = run_python
    elif args.lang == Language.C:
        run_func = run_c
    elif args.lang == Language.RUST:
        run_func = run_rust
    
    proc = run_func(args)
    print("Execution interrupted")

    if proc.returncode != 0:
        print(proc.stdout.decode())
        print(proc.stderr.decode(), file=sys.stderr)
        exit(1)
    return proc.stdout.decode().strip().split("\r\n")

def print_output(args, ans):
    if len(ans) == 1:
        ans1 = ans[0]
        ans2 = None
    elif len(ans) == 2:
        ans1, ans2 = ans
    else:
        print("\n".join(ans))
        print("Cannot parse output, exiting")
        exit()

    print(f"{args.year} Day {args.day} Part 1: {ans1}")
    if ans2 is not None:
        print(f"{args.year} Day {args.day} Part 2: {ans2}")

def submit_value(args, value):
    ...

if __name__ == "__main__":
    args = get_args()
    ans = run_program(args)
    print_output(args, ans)
    if args.submit:
        submit_value(args, ans)