#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try: import modules.typo_colors as c;
except Exception as e: print(e)

##############################################################################
####
####    CLASS OF TYPOS USED FOR WRITING
####
##############################################################################
class typo:
    def __init__(self, warning=False):
        self.type = self
        self.warn = warning
        if self.warn: ## We print this warning if self.warn is True
            print("You initialised a typo class, be sure to understand the fact that it creates spaces only in the vertical alignment")
            print("If you don't want it to appear again enter")
            print(" ")

    def vspace(self, text=None, times=33):  ## It creates a space letting the dev
        print(" ")                          ## to have spaces between text.
        if text != None:                    ## We can also write some text
            print(text)                     ## to write some informations.
        print(" ")

    def hashsep(self, text=None, times=33): ## It creates a div with hash.
        times = int(times)                  ## It adds spaces between this div
        print("  ")                         ## the text before and after him.
        print(times*"#")                    ## We have the possibility to write
        if text != None:                    ## some text as args to write informations
            print(text)
        print(times*"#")
        print("  ")

    def barsep(self, text=None, times=33): ## It creates a div with bars.
        times = int(times)                 ## It adds spaces between this div
        print("  ")                        ## the text before and after him.
        print(times*"/")                   ## We have the possibility to write
        if text != None:                   ## some text as args to write informations
            print(text)
        print(times*"/")
        print("  ")

    ### Functions for printing text

    def printg(self, text="Text Sample"):        ## It's still in development
        try:
            print(c.color.bold + ' Hello World ! ' + c.color.end) ##Normally, it prints the text in bold
        except Exception as e:                          ## It's actually not working
            self.ErrorPrecisedPrint(e)

    def ErrorPrint(self):
        print(" ")                          ## It's executed if any error occurs
        print("We're sorry but an error occured.... Please retry")
        print("If this error persists or if you encounter another error")
        print("please contact us at unknowngamesoff@gmail.com")
        print(" ")

    def ErrorPrecisedPrint(self, error):
        print(" ")                         ## It's executed if any error occurs
        print("We're sorry but this error occured:")    ## and if we want more informations
        print(error)
        print("If this error persists or if you encounter another error")
        print("please contact us at unknowngamesoff@gmail.com")
        print(" ")
