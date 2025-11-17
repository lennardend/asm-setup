import sys
import os
import subprocess
import re


def fexe(exe: str) -> str:
    if not (len(exe) == 0 or exe.startswith("./") or exe.startswith("/")):
        exe = f"./{exe}"
    return exe


def run_make(arg: str = "", skip_make: bool = True, debug: bool = False):
    if debug:
        arg = f"gdb --tui {exe_name}"        
    
    print("prepare environment")
    try:
        subprocess.run("cp -a /code/* /compile", shell=True)
        subprocess.run("cd /compile", shell=True)
        if not skip_make:
            print("running make")
            subprocess.run(["make"])
        if len(arg) > 0:
            print(f"running '{arg}'")
            subprocess.run([arg])
        else:
            print("no arg was given, not starting anything")
    except KeyboardInterrupt:
        print("cancelled by user")
    except Exception as ex:
        raise ex
    # end script after make
    exit(0)


exe_name = ""
debug = False
skip_make = False

arguments = sys.argv
for i in range(1, len(arguments)):
    argument = arguments[i]
    if not argument.startswith("-"):
        exe_name = argument
        break

    match argument:
        case "--shell":
            run_make("bash")
        case "--make-test":
            run_make("make test")
        case "--build-only":
            run_make()
        case "--debug":
            debug = True        
        case "--skip-make":
            skip_make = True

if exe_name != "":
    run_make(fexe(exe_name), debug)

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
    matches = re.findall(r"(ld -o (\w+) \w+\.o)|(gcc .*-o (\w+))", content)

    if matches is None or len(matches) > 1:
        print("couldn't find executable name in makefile")
        exit(1)
    
    groups = matches[0]
    if len(groups[1]) > 0:
        exe_name = groups[1]
    if len(groups[3]) > 0:
        exe_name = groups[3]
    print(f"found {exe_name}")
    run_make(fexe(exe_name), skip_make, debug)
