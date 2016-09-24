.PHONY: run
run: build
    python ./prisoner

.PHONY: build
build:
    coconut prisoner -fps -j sys

.PHONY: setup
setup:
    pip install coconut-develop
