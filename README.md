# Assembly M1 Setup

Make sure you have [Docker](https://www.docker.com/) installed (`brew install docker`). Also install Docker desktop if you are not planning to use the debugger (see chapter [Debugger](#debugger)).

To build and execute your current project, run:
```sh
docker run --rm -ti --platform linux/amd64 -v "$(pwd)":/code:ro lennardend/x86-asm
```

To build and start the gdb debugger, run:
```sh
docker run --rm -ti --platform linux/amd64 --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -v "$(pwd)":/code:ro lennardend/x86-asm --debug
```

## Documentation

When the container is started, the [get_executable.py](get_executable.py) python script is run. If an argument with the `docker run` command is given, that is treated as the executable name. If not, it tries to find the name of the generated executable with this regex: `ld -o (\w+) \w+\.o`.

After a executable name is found (or given), [make.sh](make.sh) is run with the executable name as an argument. This small shell script copies all files from the given read-only directory and runs the `make` command.

### Flags

> [!NOTE]
> There is no `man` page and therefore no `-h` or `--help` at the moment. It will be added later.

To start a [`gdb`](https://www.sourceware.org/gdb/) session, include the `--debug` flag in your `docker run` command.

To go into the shell of the container, use `/bin/sh` as argument or add the `--shell` flag in your `docker run` command.

To test your project easily, add a target `test` to your `Makefile`. Run this target with the `--make-test` flag in your `docker run` command.

To only build your project and not run anything, add the `--build-only` flag in your `docker run` command.

### Debugger

If you want to use the debugger, make sure to use [colima](https://github.com/abiosoft/colima) as your container runtime. Colima runs Docker inside a emulated linux VM. The Docker ARM runtime corrently has an issue where they cannot correctly access the memory, which means `gdb` cannot access the register values (see this [GitHub issue](https://github.com/docker/for-mac/issues/6921)).

```sh
brew install colima qemu lima-additional-guestagents
colima start --arch x86_64
```
