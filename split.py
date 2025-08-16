"""
split.py

This script takes a raw pubs CSV file thats in the format (pubs,tag1,tag2,...,tagn)
and splits it into two normalized csv files:
- pubs.csv : mapping pub_id to pub_name
- tags.csv : mapping pub_id to multiple tags
"""

import csv
from pathlib import Path



with open("data/york_pubs.csv", newline="", encoding="utf-8") as rawfile, \
     open("data/pubs.csv", "w", newline="", encoding="utf-8") as pubfile, \
     open("data/tags.csv", "w", newline="", encoding="utf-8") as tagfile:

    reader = csv.DictReader(infile)
    pub_writer = csv.writer(pubfile)
    tag_writer = csv.writer(tagfile)

