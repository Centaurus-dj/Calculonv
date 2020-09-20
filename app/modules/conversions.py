#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try: import modules.logs as lg; log = lg.log("modules.conversions.py", "log.log", "at", True); log.imported("modules.logs");
except Exception as e:
    log.unimported("modules.logs", e, False);
    log.write("We try to import \"modules.logs\" as \"logs\"");
    try:
        import logs as lg; log.imported("logs");
    except Exception as e:
        log.unimported("logs", e);
try: import modules.typos as ty; log.imported("modules.typos");
except Exception as e: import typos as ty; log.unimported("modules.typos", e);
try: import modules.intclass as mic; log.imported("modules.intclass");
except Exception as e: log.unimported("modules.intclass", e);
try: import modules.calculate as mc; log.imported("modules.calculate");
except Exception as e: log.unimported("modules.calculate", e);
try: import lists as l; log.imported("lists");
except Exception as e: log.unimported("lists", e);

t = ty.typo(False)

#####################################################################################################
####
#### CONVERSIONS MODULE IS USED TO CONVERT NUMBER FROM BINARY, DECIMAL, HECADECIMAL FORMATS
#### TO ONE OF THE TWO TOHERS FORMAT. IT TAKES NATURAL INTEGERS AS WELL AS THE NEGATIVE NUMBERS
#### // ATTENTION // FOR NOW, IT'S NOT SUPPORTING FLOAT NUMBERS. IN THE FUTURE, IF NEEDED AND WANTED
#### IT WILL BE IMPLEMENTED.
####
####################################################################################################

class Conversions:
    def __init__(self):
        log.info("Conversions class initiated")

    ###########################################
    #### Conversions from Bin to x
    ###########################################
    def ConvertBinToDec(self, x, step=False):
        log.infunc("ConvertBinToDec")
        try:
            r = 0
            int(x)
            for digit in x:
                r = r*2 + int(digit)
            if not step:
                t.barsep("The decimal value for "+str(x)+" is "+str(r))
                log.debug("The decimal value for "+str(x)+" is "+str(r))
                log.outfunc()
                self.ConvertContinue()
            else:
                log.debug("The decimal value for "+str(x)+" is "+str(r))
                log.outfunc()
                return(r)
        except KeyboardInterrupt:
            t.vspace("You stoped the script using ctrl+c")
            log.error("User stoped script using ctrl+c")
            log.outfunc()
            log.end()
        except Exception as e:
            log.error(e)
            log.outfunc()
            log.end()

    def ConvertBinToHex(self, x):
        log.infunc("ConvertBinToHex")
        try:
            xs = x
            log.info("First step started")
            x = self.ConvertBinToDec(x, True)
            log.info("First step done")
            log.info("Second step started")
            x = self.ConvertDecToHex(x, True)
            log.info("Second step done")
            r = "".join(x)
            print(f"The Hexadecimal value for the binary "+str(xs)+f" is {r}")
            log.debug(f"The Hexadecimal value for the binary "+str(xs)+f" is {r}")
            log.outfunc()
            self.ConvertContinue()
        except KeyboardInterrupt:
            t.vspace("You stoped the script using ctrl+c")
            log.error("User stoped the script using ctrl+c")
            log.outfunc()
            log.end()
        except Exception as e:
            log.error(e)
            log.outfunc()
            log.end()

    ###########################################
    #### Conversions from Decimal to x
    ###########################################
    def ConvertDecToBin(self, x, step=False, encoding=None, signstep=False):
        log.infunc("ConvertDecToBin")
        mt = mic.number(x)
        mt.TestSign(True)
        if signstep:
            return(mt.sign)
        try:
            binary = []
            xs = int(mt.dn)
            x = int(mt.pn)
            while x > 0:
                s1 = str(int(x%2))
                binary.append(s1)
                x //= 2
            r = "".join(binary[::-1])
            if encoding == 8 or encoding == "8":
                while len(r) < 8:
                    r = "0" + r
            elif encoding == "" or encoding == None:
                pass
            else:
                while len(r) < encoding:
                    r = "0" + r
            if not step:
                t.barsep(f"The Binary value for "+ str(xs)+ " is "+ r)
                log.debug(f"The Binary value for "+ str(xs)+ " is "+ r)
                subentry = input("Do you want the number in signed binary? ")
                if subentry in l.yeslist or subentry in l.ouilist:
                    if mt.dn >= -127 and mt.dn <= 127:
                        sb = mt.SignBin(r, True)
                        t.barsep("The signed binary is : {}".format(sb))
                    else:
                        t.barsep("{} can't be transformed in signed binary".format(n1))
                        log.error("{} can't be transformed in signed binary".format(n1))
                        log.outfunc()
                        log.end()
                log.outfunc()
            else:
                log.debug(f"The Binary value for "+ str(xs)+ " is "+ r)
                log.outfunc()
                return r
        except KeyboardInterrupt:
            t.vspace("You stoped the script using ctrl+c")
            log.error("User stoped the script using ctrl+c")
            log.outfunc()
            log.end()
        except Exception as e:
            log.error(e)
            log.outfunc()
            log.end()

    def ConvertDecToHex(self, x, step=False):
        log.infunc("ConvertDecToHex")
        try:
            hexa = []
            xs = int(x)
            x = int(x)
            while x > 0:
                s1 = self.CheckHexEqua(int(x%16))
                hexa.append(str(s1))
                x //= 16
            if not step:
                t.barsep("The hexadecimal value for "+ str(xs)+ " is "+"".join(hexa[::-1]))
                log.debug("The hexadecimal value for "+ str(xs)+ " is "+"".join(hexa[::-1]))
                log.outfunc()
                self.ConvertContinue()
            else:
                log.debug("The hexadecimal value for "+ str(xs)+ " is "+"".join(hexa[::-1]))
                log.outfunc()
                return(hexa[::-1])

        except KeyboardInterrupt:
            t.vspace("You stoped the script using ctrl+c")
            log.error("User stoped script using ctrl+c")
            log.outfunc()
            log.end()
        except Exception as e:
            log.error(e)
            log.outfunc()
            log.end()

    ###########################################
    #### Conversions from Hexadecimal to x
    ###########################################
    def ConvertHexToDec(self, x, step=False):
        log.infunc("ConvertHexToDec")
        xs = x
        x = int(x, 16)
        if not step:
            print("The Decimal value for", str(xs), "is", str(x))
            log.debug("The Decimal value for "+str(xs)+" is "+str(x))
            log.outfunc()
            self.ConvertContinue()
        else:
            log.debug("The Decimal value for "+str(xs)+" is "+str(x))
            log.outfunc()
            return(x)

    def ConvertHexToBin(self, x, encoding=None):
        log.infunc("ConvertHexToBin")
        xs = x
        log.info("first step started")
        x = ConvertHexToDec(x, True)
        log.info("first step done")
        log.info("second step started")
        if encoding != None:
            x = self.ConvertDecToBin(x, True, encoding)
        else:
            x = self.ConvertDecToBin(x, True)
        log.info("second step done")
        t.barsep("The Binary value for "+str(xs)+" is "+ str(x))
        log.debug("The Binary value for "+str(xs)+" is "+ str(x))
        log.outfunc()
        self.ConvertContinue()

    ###########################################
    #### Check Hexadecimal values
    ###########################################
    def CheckHexEqua(self, x):
        log.infunc("CheckHexEqua")
        if x == 10:
            x = "A"
            log.info("10 transformed into A")
        elif x == 11:
            x = "B"
            log.info("11 transformed into B")
        elif x == 12:
            x = "C"
            log.info("12 transformed into C")
        elif x == 13:
            x = "D"
            log.info("13 transformed into D")
        elif x == 14:
            x = "E"
            log.info("14 transformed into E")
        elif x == 15:
            x = "F"
            log.info("15 transformed into F")
        else:
            x = x
        log.outfunc()
        return x

    ###########################################
    #### Asking to Continue
    ##########################################
    def ConvertContinue(self):
        log.infunc("ConvertContinue")
        try:
            quest = "Do you want to continue to convert? y/n"
            if quest in l.yeslist or quest in l.ouilist:
                log.outfunc()
                return(True)
            elif quest in l.nolist or quest in l.nonlist:
                log.outfunc()
                log.end()
        except Exception:
            log.error(Exception)
            log.outfunc()
            log.end()
