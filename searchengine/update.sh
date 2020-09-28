#!/bin/bash
cd "$(dirname "$0")"
cd ..
./get all
cd searchengine
python3.6 -m index ../db
