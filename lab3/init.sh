#!/usr/bin/env bash

# create a virtual environment and specify venv folder
python3 -m venv venv

# activate a Python virtual environment
source venv/bin/activate

# install lib
pip3 install -r https://www.comp.hkbu.edu.hk/~mandel/comp7510/pkg.txt