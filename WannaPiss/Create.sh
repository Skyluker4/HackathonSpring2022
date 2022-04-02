#!/bin/sh
base64 -w 0 WannaPiss.7z > 2.txt
cat 1.txt 2.txt 3.txt | tr -d '\n'  > WannaPiss.py
cat main.py >> WannaPiss.py
