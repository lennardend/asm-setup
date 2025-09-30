import sys
import os
import subprocess
import re

arguments = sys.argv
if len(arguments) > 1:
    subprocess.run(["/scripts/make.sh", arguments[1]])
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
    subprocess.run(["/scripts/make.sh", f"./{groups[0]}"])
