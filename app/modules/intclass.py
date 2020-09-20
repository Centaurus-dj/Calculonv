#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
####
####    INTCLASS MODULE (IN DEVELOPMENT), IT'S CREATED WITH THE ONLY PURPOSE OF HELPING
####    DEVELOPER WITH OPERATIONS USING AN INT() OBJECT IN PYTHON
####
################################################################################

class number:
    def __init__(self, nbr): ## We initiate the class, we asks the number as an argument
        self.dn = int(nbr) ## self.dn == "self.decimal-number"
        self.sign = "null" ## We default the sign property of number because, for now, the sign is null (number=0)

    def TestSign(self, step=False): ## Function called to test the sign of an int() number
        if self.dn < 0:
            self.sign = "neg" ## We update the sign property
            if not step:
                print(f"{self.dn} is negative") ## If the function is not a step of another one, we print an answer
            self.pn = self.dn-(self.dn*2) ## We create self.pn as "self.positive-number" used for any operations needing the positive version of the number
        else:
            self.sign = "pos" ## We update the sign property
            if not step:
                print(f"{self.dn} is positive") ## If the function is not a step of another one, we print an answer
            self.pn = self.dn ## We create self.pn as "self.positive-number" used for any operations needing the number.

    def SignBin(self, nbr, step=False, encoding=4): ## Function called to sign a Binary // The method will surely be put in a Bin() class in the future
        l = []
        if len(nbr) == 4:
            for i in nbr:
                l.append(i)
            if self.sign == "pos":
                l[0] = "0"
            elif self.sign == "neg":
                l[0] = "1"
            else:
                pass
            nbr = "".join(l)
        else:
            if self.sign == "pos":
                nbr = "0"+nbr ## 0 is the signing form to say it's a positive number
            elif self.sign == "neg":
                nbr = "1"+nbr ## 1 is the signing form to say it's a negative number
            else:
                pass
        if not step:
            print(" ")
            print("The signed binary is :", nbr) ## If the function is not a step of another one, we print the answer
            print(" ")
        else:
            return nbr ## Otherwise we return the signed number, ATTENTION: because of the
                    ## return statement, the function is needed to call as a variation of a variable.
                    ## Ex:  x = number.SignBin(01, True)
                    ## It will cause an error if it's not called like this.
