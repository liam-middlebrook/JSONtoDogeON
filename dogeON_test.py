#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from dogeON import colorify

class DogeOnTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_colorify(self):
        string = 'wow such is next'
        self.assertEquals(
            '\x1b[92mwow\x1b[0m \x1b[31msuch\x1b[0m \x1b[32mis\x1b[0m \x1b[34mnext\x1b[0m ',
            colorify(string))

    def test_colorify_empty_string(self):
        string = '    '
        self.assertEquals('', colorify(string))

    def test_colorify_empty_string(self):
        string = ''
        self.assertEquals('', colorify(string))
