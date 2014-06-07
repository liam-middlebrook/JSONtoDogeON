#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A JSON parser that converts JSON strings to DogeON"""
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


def colorify(dogeon_string):
    terminal_colors = dict(
        such_='\033[31m',
        is_='\033[32m',
        wow_='\033[92m',
        so_='\033[91m',
        next_='\033[34m',
        many_='\033[89m',
        reset='\033[0m',
    )
    output = ''
    for word in dogeon_string.split(' '):
        word = word.strip()
        if not word:
            continue
        wordkey = "%s_" % word
        if wordkey in terminal_colors.keys():
            output += "%s%s%s " % (terminal_colors[wordkey], word, 
                                   terminal_colors['reset'])
        else:
            output += "%s " % word
    return output


if __name__ == '__main__':
    inQuotes = False
    with open(sys.argv[1], "r") as myfile:
        print colorify(parse(myfile.read().replace('\n', ''), inQuotes))
