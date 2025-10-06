import sys
import os
import subprocess
import re

def run_make(exe_name: str, debug: bool):
    if debug:
        exe_name = f"gdb --tui {exe_name}"
    elif not (exe_name.startswith("./") or exe_name.startswith("/")):
        exe_name = f"./{exe_name}"
    
    print(f"starting make.sh with argument {exe_name}")
    try:
        subprocess.run(["/scripts/make.sh", exe_name])
    except KeyboardInterrupt:
        print("cancelled by user")
    except Exception as ex:
        raise ex

debug = False
exe_name = ""

arguments = sys.argv
for i in range(1, len(arguments)):
    argument = arguments[i]
    if argument == "--debug":
        debug = True
    else:
        exe_name = argument

if exe_name != "":
    run_make(exe_name, debug)
    exit(0)

print("trying to get executable name from makefile")

code_dir = "/code"

makefiles = ["GNUmakefile", "makefile", "Makefile"]
makefile = ""
for item in os.listdir(code_dir):
    if not os.path.isfile(f"{code_dir}/{item}"):
        continue
    
    if item in makefiles:
        makefile = f"{code_dir}/{item}"
        break

if makefile == "":
    print("no makefile was found")
    exit(1)

print(f"found {makefile}, trying to get name of generated executable")
with open(makefile) as file:
    content = file.read()
    groups = re.findall(r"ld -o (\w+) \w+\.o", content)

    if groups is None or len(groups) == 0:
        print("couldn't find executable name in makefile")
        exit(1)
    
    print(f"found {groups[0]}")
    run_make(groups[0], debug)
