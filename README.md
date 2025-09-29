# Assembly M1 Setup

To build the container image, run:
```shell
docker build --platform linux/amd64 -t "local/asm" .
```

To build and execute your current project, run:
```shell
docker run --rm -ti --platform linux/amd64 -v $(pwd):/code:ro local/asm <path to executable>
```

## Documentation

When the container is started, [make.sh](make.sh) is executed. In the script, all files from the current project folder, as bound in the documented `docker run` command, are copied to a seperate directory. There, the `make` command is run. After that, the `<path to executable>` or `./main` is run.