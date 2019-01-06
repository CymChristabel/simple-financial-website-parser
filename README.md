# simple-financial-website-parser
A simple financial website fetcher and parser in python

## Dependencies
- [xlsxwriter](https://xlsxwriter.readthedocs.io/)

## Description
This is a simple financial website fetcher parser that handling data of securities and fund in Asset Management Association of China. After successfully fetching, data would be saved as xlsx file.

## Usage
After clone the repo, simply call

    python crawler.py START_DATE END_DATE OUTPUT_FILENAME MODE

Where MODE stands has:
- Securities(0)
- Fund(1)
