# Assembly M1 Setup

Make sure you have [Docker](https://www.docker.com/) installed (`brew install docker`). Also install Docker desktop if you are not planning to use the debugger (see chapter [Debugger](#debugger)).

To build the container image, run:
```sh
docker build --platform linux/amd64 -t "local/asm" .
```

To build and execute your current project, run:
```sh
docker run --rm -ti --platform linux/amd64 -v $(pwd):/code:ro local/asm
```

To build and start the gdb debugger, run:
```sh
docker run --rm -ti --platform linux/amd64 --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -v $(pwd):/code:ro local/asm --debug
```

## Documentation

When the container is started, the [get_executable.py](get_executable.py) python script is run. If you give a command with the `docker run` command, that is treated as the executable name. If not, it tries to find the name of the generated executable with this regex: `ld -o (\w+) \w+\.o`.

After a executable name is found (or given), [make.sh](make.sh) is run with the executable name as an argument. This small shell script copies all files from the given read-only directory and runs the `make` command.

To start a [`gdb`](https://www.sourceware.org/gdb/) session, include the `--debug` flag in your `docker run` command.

To go into the shell of the container, use `/bin/sh` as argument or add the `--shell` flag in your `docker run` command.

### Debugger

If you want to use the debugger, make sure to use [colima](https://github.com/abiosoft/colima) as your container runtime. Colima runs Docker inside a emulated linux VM. The Docker ARM runtime corrently has an issue where they cannot correctly access the memory, which means `gdb` cannot access the register values (see this [GitHub issue](https://github.com/docker/for-mac/issues/6921)).

```sh
brew install colima qemu lima-additional-guestagents
colima start --arch x86_64
```
