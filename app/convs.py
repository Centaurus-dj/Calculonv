#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def CreateIndependantLog():
    import datetime; import os.path; from pathlib import Path
    file = Path("log.log");
    if file.is_file(): logfile = open("log.log", "wt")
    else: logfile = open(LogFile, "at")
    logfile.write("//////////////////////////////////////////\n"); logfile.write("Log file created at " + str(datetime.datetime.now()) + "\n"); logfile.write("//////////////////////////////////////////\n")
    logfile.write("\nlogs module coudln't be imported, script stoped because module is needed")
    logfile.write("\nfor a good processing")



################################################################################
#### Imports
################################################################################

try: import modules.logs; log = modules.logs.log("convs.py", "log.log", "at", True);
except Exception as e: print("[convs.py] logs module couldn't be imported"); exit();
try: import modules.typos; log.imported("typos"); t = modules.typos.typo()
except Exception as e: log.unimported("typos", e); exit();
try: import modules.conversions; log.imported("conversions"); c = modules.conversions.Conversions()
except Exception as e: log.unimported("conversions", e); exit();
try: import modules.calculate; log.imported("calculate");
except Exception as e: log.unimported("calculate", e); exit()
try: import module.intclass; log.imported("intclass");
except Exception as e: log.unimported("intclass", e); exit()
try: import lists; log.imported("lists");l = lists;
except Exception as e: log.unimported("lists", e); exit();

bcl = modules.calculate.BinOperations()

################################################################################
#### Functions
################################################################################

def Input():
    log.infunc("Input")
    log.info("function used")
    def AskOne():
        x = input("Enter your number: ")
        return x
    try:
        HelpCommands()
        entry = input("Input: ")
        if "help" in entry:
            HelpCommands()
            Input()
        if entry in l.quitlist:
            print("You decided to stop this script using", entry)
            log.info("User stoped the script")
            exit()
        if entry == "a" or entry == "A":
            n1 = AskOne()
            try:
                test = int(n1)
            except:
                t.vspace("What you've entered isn't a number.... Please Retry")
                log.error("string entered into input isn't a number...")
                log.write("We redirect him to re-enter a number")
                n1 = AskOne()
            HelpConvert("b")
            n2 = input("What is the format you want to convert to? ")
            if n2 in l.dec:
                log.info("User sent to {ConvertBinToDec}")
                try: c.ConvertBinToDec(n1)
                except Exception as e: log.error(e)
            elif n2 in l.hex:
                log.info("User sent to {ConvertBinToHex}")
                c.ConvertBinToHex(n1)
                Input()
        elif entry == "z" or entry == "Z":
            n1 = AskOne()
            try:
                test = int(n1)
            except:
                t.vspace("What you've entered isn't a number.... Please Retry")
                log.error("string entered into input isn't a number...")
                log.write("We redirect him to re-enter a number")
                n1 = AskOne()
            HelpConvert("d")
            n2 = input("What is the format you want to convert to? ")
            if n2 in l.hex:
                log.info("User sent to {ConvertDecToHex}")
                c.ConvertDecToHex(n1)
                Input()
            elif n2 in l.bin:
                log.info("User sent to {ConvertDecToBin}")
                cs = c.ConvertDecToBin(n1, True, 8, True)
                if cs == "neg":
                    subentry = input("What's the encoding you want? ")
                    if subentry == "":
                        cn = c.ConvertDecToBin(n1, True)
                        c.ConvertDecToBin(n1)
                    else:
                        cn = c.ConvertHexToBin(n1, True, int(subentry))
                        c.ConvertDecToBin(n1, False, int(subentry))
                    try:
                        HelpComplement()
                        subentry = input("What complement do you want? ")
                        if subentry == "a":
                            one = BinComplement1(cn, True)
                            t.barsep("\nWe have as complement {}".format(one))
                            print(one)
                        elif subentry == "z":
                            two = BinComplement12(cn, True)
                            t.barsep("We have as 1st complement {} and as 2nd {}".format(two[0], two[1]))
                        Input()
                    except Exception as e:
                        log.error(e)
                        print(e)
                elif cs == "pos":
                    subentry = input("What's the encoding you want? ")
                    if subentry == "":
                        c.ConvertDecToBin(n1)
                    else:
                        c.ConvertDecToBin(n1, False, int(subentry))
                else:
                    print("something went wrong....")
                Input()

        elif entry == "e" or entry == "E":
            n1 = AskOne()
            HelpConvert("h")
            n2 = input("What is the format you want to convert to? ")
            if n2 in l.dec:
                log.info("User sent to {ConvertHexToDec}")
                c.ConvertHexToDec(n1)
                Input()
            elif n2 in l.bin:
                log.info("User sent to {ConvertHexToBin}")
                cs = c.ConvertHexToBin(n1, True, 8, True)
                if cs == "neg":
                    subentry = input("What's the encoding you want? ")
                    if subentry == "":
                        cn = c.ConvertHexToBin(n1, True)
                        c.ConvertHexToBin(n1)
                    else:
                        cn = c.ConvertHexToBin(n1, True, int(subentry))
                        c.ConvertHexToBin(n1, False, int(subentry))
                    try:
                        HelpComplement()
                        subentry = input("What complement do you want? ")
                        if subentry == "a":
                            one = BinComplement1(cn, True)
                            t.barsep("\nWe have as complement {}".format(one))
                            print(one)
                        elif subentry == "z":
                            two = BinComplement12(cn, True)
                            t.barsep("We have as 1st complement {} and as 2nd {}".format(two[0], two[1]))
                        Input()
                    except Exception as e:
                        log.error(e)
                        print(e)
                elif cs == "pos":
                    subentry = input("What's the encoding you want? ")
                    if subentry == "":
                        c.ConvertHexToBin(n1)
                    else:
                        c.ConvertHexToBin(n1, False, int(subentry))
                else:
                    print("something went wrong....")
                log.outfunc()
                Input()
    except KeyboardInterrupt:
        t.vspace("You stoped to script using ctrl+c")
        log.outfunc()
        log.end()
    except Exception as e:
        log.error(e)
        log.outfunc()
        log.end()


def BinComplement1(n1, step=False):
    log.infunc("BinComplement1")
    x = bcl.Inverse(n1, True); log.info("step one done")
    if not step:
        t.barsep("Complement to 1 : "+x)
        log.outfunc()
    else:
        log.outfunc()
        return(x)

def BinComplement12(n1, step=False):
    log.infunc("BinComplement12")
    x = bcl.Inverse(n1, True); log.info("step one done")
    y = bcl.Add(x, 1, True); log.info("step two done")
    if not step:
        t.barsep("Complement to 1 : "+x)
        t.barsep("Complement to 2 : "+y)
        log.outfunc()
    else:
        log.outfunc()
        return(x, y)

################################################################################
#### We define the Help Functions
################################################################################
def HelpComplement():
    print(" ")
    print("Available Complements: ")
    print(" ")
    print(" - a:    Complement to 1")
    print(" - z:    Complement to 1 and 2")
    print(" ")

def HelpConvert(arg):
    print(" ")
    print("Available Conversions: ")
    print(" ")
    if arg == "b":
        print(" - d:    Convert to decimal")
        print(" - h:    Convert to hexadecimal")
    elif arg == "d":
        print(" - h:    Convert to hexadecimal")
        print(" - b:    Convert to binary")
    elif arg == "h":
        print(" - b:    Convert to binary")
        print(" - d:    Convert to decimal")
    else:
        print("None valid argument has been given")
    print(" ")

def HelpCommands():
    print(" ")
    print("Usage: Input: <command shortcut>")
    print(" ")
    print("Shortcuts for commands:")
    print(" ")
    print("     - a:     Conversion from Binary")
    print("     - z:     Conversion from Decimal")
    print("     - e:     Conversion from Hexadecmial")
    print(" ")
