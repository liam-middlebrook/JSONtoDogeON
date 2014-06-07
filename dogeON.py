#!/usr/bin/python
#dogeON.py
#A JSON parser that converts JSON strings to DogeON
import sys


def parse(jsonString, inQuotes=False):
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
            if char == '[':
                jsonString = jsonString[:i] + " so "+ jsonString[i+1:]
                return parse(jsonString)
            if char == ',':
                jsonString = jsonString[:i] + " next "+ jsonString[i+1:]
                return parse(jsonString)
            if char == ']':
                jsonString = jsonString[:i] + " many "+ jsonString[i+1:]
                return parse(jsonString)
    return jsonString


if __name__ == '__main__':
    inQuotes = False
    with open(sys.argv[1], "r") as myfile:
        print parse(myfile.read().replace('\n', ''), inQuotes)
