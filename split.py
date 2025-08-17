"""
split.py

This script takes a raw pubs CSV file thats in the format (pubs,tag1,tag2,...,tagn)
and splits it into two normalized csv files:
- pubs.csv : mapping pub_id to pub_name
- tags.csv : mapping pub_id to multiple tags
"""

import csv
from pathlib import Path

raw_csv = Path("data/york_pubs.csv")
pubs_csv = Path("data/pubs.csv")
tags_csv = Path("data/tags.csv")

# This will rewrite both pubs_csv and tag_csv each time split.py is run
with open(raw_csv, newline="", encoding="utf-8") as rawfile, \
     open(pubs_csv, "w", newline="", encoding="utf-8") as pubfile, \
     open(tags_csv, "w", newline="", encoding="utf-8") as tagfile:

    # Reads the rawfile
    reader = csv.reader(rawfile)
    pub_writer = csv.writer(pubfile)
    tag_writer = csv.writer(tagfile)

    # Write the headers
    pub_writer.writerow(["pub_id", "pub_name"])
    tag_writer.writerow(["pub_id", "tag"])

    # Enumerate gives each pub a unique ID starting at 1
    for pub_id, row in enumerate(reader, start=1):
        pub_name = row[0]
        pub_writer.writerow([pub_id, pub_name])

        # Goes through each tag and removes spaces and writes to tags_csv
        for tag in row[1:]:
            clean_tag = tag.strip()
            if clean_tag:
                tag_writer.writerow([pub_id,clean_tag])
