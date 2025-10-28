import sys
import os
import subprocess
import re

debug = False
test = False
exe_name = ""

def run_make():
    if debug:
        exe_name = f"gdb --tui {exe_name}"
    elif test:
        exe_name = "make test"
    elif not (exe_name.startswith("./") or exe_name.startswith("/")):
        exe_name = f"./{exe_name}"
    
    print(f"starting make.sh with argument '{exe_name}'")
    try:
        subprocess.run(["/scripts/make.sh", exe_name])
    except KeyboardInterrupt:
        print("cancelled by user")
    except Exception as ex:
        raise ex

arguments = sys.argv
for i in range(1, len(arguments)):
    argument = arguments[i]
    if argument == "--shell":
        debug = False
        exe_name = "/bin/sh"
        break
    if argument == "--debug":
        debug = True
    if argument == "--make-test":
        test = True
    else:
        exe_name = argument

if exe_name != "" or test:
    run_make()
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
    
    exe_name = groups[0]
    print(f"found {exe_name}")
    run_make()
