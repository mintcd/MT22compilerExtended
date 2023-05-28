import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    
    def test1(self):
        input = """int main () {
            int a;
            int b;
            int c;
            int d;
            int e;
            int f;
            int g;
                    
            e = d + a;
            f = b + c;
            f = f + b;
            d = e + f;
            g = d;
        }"""
        expect = """ See 502 for a solution """
        self.assertTrue(TestCodeGen.test(input,expect, 502))