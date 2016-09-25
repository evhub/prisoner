.PHONY: run
run: build
    python ./prisoner

.PHONY: build
build:
    coconut prisoner -sf -j sys

.PHONY: setup
setup:
    pip install coconut-develop
