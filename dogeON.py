#!/usr/bin/python
#dogeON.py
#A JSON parser that converts JSON strings to DogeON

import sys

jsonFile = sys.argv[1]

#retrieve the JSON data from specified file
with open (jsonFile, "r") as myfile:
    jsonString=myfile.read().replace('\n', '')

inQuotes = False

def parse(jsonString):
    inQuotes = False
    for i, char in enumerate(jsonString):
        if char == '\"':
            inQuotes = not inQuotes
        if not inQuotes:
            if char == '{':
                jsonString = jsonString[:i] + " such "+ jsonString[1+i:]
                return parse(jsonString)
            if char == '}':
                jsonString = jsonString[:i] + " wow "+ jsonString[i+1:]
                return parse(jsonString)
            if char == ':':
                jsonString = jsonString[:i] + " is "+ jsonString[i+1:]
                return parse(jsonString)
    return jsonString

jsonString = parse(jsonString)
print jsonString
            
