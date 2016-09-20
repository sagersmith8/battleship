#!/bin/sh
set -ex

flake8 battleship tests
nosetests --with-coverage tests
