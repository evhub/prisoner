.PHONY: build
build:
	coconut prisoner -sf -j sys

.PHONY: run
run:
	python ./prisoner

.PHONY: test
test: build run

.PHONY: setup
setup:
	pip install coconut-develop
