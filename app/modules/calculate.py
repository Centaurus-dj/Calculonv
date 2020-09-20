#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
####
#### CALCULATE MODULE (IN DEVELOPMENT) CONTAINS CLASSES FOR ANY KIND OF OPERATIONS
#### BETWEEN SOME TYPE OF OBJECTS. EVERY CLASS IS SPECIALISED FOR ONE TYPE OF OBJECT
####
################################################################################

class Operations: ## Class for Integers
    def __init__(self, warn=True):
        self.warning = "This class only support int() objects" ## Warning written

    def Add(self, x, y, step=False): ## Function used to add two integers
        if type(x) is int and type(y) is int:
            r = x+y
        elif type(x) is str and type(y) is str:
            r = "This class don't support the strings"
        elif type(x) is int and type(y) is str or type(x) is str and type(y) is int:
            r = "One element is a number but the other one isn't"
        if step:
            return(r)
        else:
            print("{} plus {} is {}".format(x, y, r))

    def Min(self, x, y, step=False): ## Function used to minus two integers
        if type(x) is int and type(y) is int:
            r = x-y
        elif type(x) is str and type(y) is str:
            r = "This class don't support the strings"
        elif type(x) is int and type(y) is str or type(x) is str and type(y) is int:
            r = "One element is a number but the other one isn't"
        if step:
            return(r)
        else:
            print("{} minus {} is {}".format(x, y, r))

    def Multiply(self, x, y, step=False): ## Function used to multiply two integers
        if type(x) is int and type(y) is int:
            r = x*y
        elif type(x) is str and type(y) is str:
            r = "This class don't support the strings"
        elif type(x) is int and type(y) is str or type(x) is str and type(y) is int:
            r = "One element is a number but the other one isn't"
        if step:
            return(r)
        else:
            print("{} multiplied by {} is {}".format(x, y, r))

    def Divide(self, x, y, step=False): ## Function used to divide two integers
        if type(x) is int and type(y) is int:
            r = x/y
            s = int(r)
            if 2*s == x:
                r = s
        elif type(x) is str and type(y) is str:
            r = "This class don't support the strings"
        elif type(x) is int and type(y) is str or type(x) is str and type(y) is int:
            r = "One element is a number but the other one isn't"
        if step:
            return(r)
        else:
            print("{} divided by {} is {}".format(x, y, r))

class BinOperations:
    def __init__(self, warn=True):
        super().__init__()
        self.warning = "This class only support bin() objects" ## Warning written

    def Add(self, x, y=1, step=False): ## We add two binaries, in theory
        if y == 1:                     ## For now we just add 1 to a binary number
            carry = y
        else:
            carry = 0
        x = str(x)
        l = []
        t = 0
        while t < len(x):
            for i in x:
                if int(i) + int(carry) == 2:
                    i = "0"
                elif int(i) + int(carry) == 1:
                    i = "1"
                    carry = 0
                t = t + 1
                l.append(i)
        r = "".join(l[::-1])
        if not step:
            print("{Add} Result: "+r)
        else:
            return r

    def Inverse(self, nbr, step=False): ## We inverse the number
        l = []                          ## Used if we want to have the inverse one.
        for i in nbr:
            if i == "0":
                i = "1"
            elif i == "1":
                i = "0"
            l.append(i)
            lc = "".join(l)
        if not step:
            print("The inverse of " + nbr + " is " + lc)
        return lc
