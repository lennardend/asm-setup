# Assembly M1 Setup

To build the container image, run:
```shell
docker build --platform linux/amd64 -t "local/asm" .
```

To build and execute your current project, run:
```shell
docker run --rm -ti --platform linux/amd64 -v $(pwd):/code:ro local/asm
```

## Documentation

When the container is started, the [get_executable.py](get_executable.py) python script is run. If you give a command with the `docker run` command, that is treated as the executable name. If not, it tries to find the name of the generated executable with this regex: `ld -o (\w+) \w+\.o`.

After a executable name is found (or given), [make.sh](make.sh) is run with the executable name as an argument. This small shell script copies all files from the given read-only directory and runs the `make` command.