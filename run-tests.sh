#!/usr/bin/env bash
flake8 battleship tests
nosetests --with-coverage tests
