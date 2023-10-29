#!/bin/bash

./downloader.sh

python3 parse.py
python3 mentos.py
python3 map.py