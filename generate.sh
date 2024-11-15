#!/bin/sh 

set -e

gen-json-schema hello.yaml > hello.schema.json

gen-python hello.yaml > hello.py
gen-sqla hello.yaml > hello_sqla.py

