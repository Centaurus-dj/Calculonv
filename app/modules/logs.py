#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os.path
import subprocess
from pathlib import Path

################################################################################
####
####    LOG MODULE USED FOR CREATING AND MANAGING A LOG FILE FOR DIFFERENTS PURPOSES
####    IT'S MAINLY MADE FOR HELPING THE DEVELOPER IN HIS DEVELOPMENT.
####
################################################################################

class log:
    def __init__(self, ParentFile="main.py", LogFile="log.txt", WriteType="at", SameScript=False): ## differents args given and defaulted letting dev to initate class easely
        self.ParentFile = ParentFile ## File written between [] in log file letting us know in which file the line of the log has been initated
        self.SameScript = SameScript ## Variable letting us know if we need to re-write the log or if we append our lines
        if not self.SameScript:
            self.file = Path(LogFile) ## We define the path of the log as a Path object
            if self.file.is_file():
                self.logfile = open(LogFile, "wt") ## We open the file and re-write it.
            else:
                self.logfile = open(LogFile, WriteType) ## We create the file and starts writing it.
            self.logfile.write(42*"/"+"\n")
            self.logfile.write("Log file created at " + str(datetime.datetime.now()) + "\n") ## We print the date and time
            self.logfile.write("Calculonv | Copyright (c) 2020 Centaurus\n") ## We print the copyright
            self.logfile.write("The software is under MIT License | Read more about it in the README.md\n") ## We print the information about the license
            self.logfile.write(42*"/"+"\n")
            self.info("log file created")
        elif self.SameScript:
            self.file = LogFile ## We also define the selF.file variable for after
            self.logfile = open(LogFile, WriteType) ## We open the file with the type of opening.
            self.info("log file already created")

    ########################################################
    #### Funcs having an effect on self.x variables
    ########################################################
    def infunc(self, func): ## Function used for defining the function when we'll print statements
        self.func = func    ## Practical for debugging
    def outfunc(self): ## Function used to be sure we're not in a function because the function is finished
        self.func = None

    #####################################################
    #### Funcs for Imports system
    #####################################################
    def imported(self, module): ## Function used in order to verify if the module is imported
            self.logfile.write("\n" + "IMPORT: " + f"[{self.ParentFile}] " + "{} module imported".format(module)) ## We say that the module is indeed imported

    def unimported(self, module, exception, StopScript=True): ## Function used in order to verify if the module is imported
        self.logfile.write("\n" + "IMPORT ERROR: " + f"[{self.ParentFile}] " + "{} module couldn't be imported".format(module)) ## We say that the module couldn't be imported
        self.logfile.write("\n" + " because of {}".format(exception)) ## We then print the error
        errors = open("errors.txt", "at") ## We open/create the file with the appending mode
        errors.write("\nError occured the "+str(datetime.datetime.now())+" :")
        errors.write("\n    "+str(exception)+"\n") ## We write the error
        errors.close() ## We close the file to be sure there's no misunderstanding between instances and to be sure we have saved the file and our statement in it.
        if StopScript:
            self.alert() ## We alert the user of the fact there's an error somewhere, more precisely in the import system
            self.end() ## We end the script and the writing of the "log.log" file

    ####################################################################
    #### Funcs for Printing non-critical informations as a redirection
    ####################################################################
    def write(self, txt): ## Function used for continuing to write text if we have something very long to write
        try:
            self.logfile.write("\n" + f"[{self.ParentFile}] " + "{"+f"{self.func}"+"} " + str(txt)) ## We print this statement if the log is in a function
        except:
            self.logfile.write("\n" + f"[{self.ParentFile}] " + str(txt)) ## Otherwise we print this statement without writing the function because the log is not in a function

    def info(self, txt): ## Function used to print informations like a redirection of user, the arrviing of user in function, etc...
        try:
            self.logfile.write("\n" + "INFO: " + f"[{self.ParentFile}] " + "{"+f"{self.func}"+"} " + txt) ## We print this statement if the log is in a function
        except:
            self.logfile.write("\n" + "INFO: " + f"[{self.ParentFile}] " + txt) ## Otherwise we print this statement

    def debug(self, txt): ## Function used to print debugging informations about operations, like the result
        results = open("results.txt", "at") ## We open/create the file with the appending mode
        results.write("\nOperation done the "+str(datetime.datetime.now())+" :") ## We write the date of the operation
        try:
            self.logfile.write("\n" + "DEBUG: " + f"[{self.ParentFile}] " + "{"+f"{self.func}"+"} " + txt) ## We print this statement if the log is in a function
        except:
            self.logfile.write("\n" + "DEBUG: " + f"[{self.ParentFile}] " + txt) ## Otherwise we print this statement
        results.write("\n"+txt+"\n") ## We write the text, mainly the same phrase printed in the console, into the "results.txt" file
        results.close() ## We close the file to be sure there's no misunderstanding between instances and to be sure we have saved the file and our statement in it.

    ############################################################
    #### Funcs for Printing critical informations as errors
    ############################################################
    def error(self, txt): ## Function used to print the fact there's an error somewhere, called in a try/except loop or in a if/else condition for certain cases
        errors = open("errors.txt", "at") ## We open/create the file with the appending mode
        errors.write("\nError occured the "+str(datetime.datetime.now())+" :")
        errors.write("\n"+txt+"\n") ## We write the error
        errors.close() ## We close the file to be sure there's no misunderstanding between instances and to be sure we have saved the file and our statement in it.
        try:
            self.logfile.write("\n" + "ERROR: " + f"[{self.ParentFile}] " + "{"+f"{self.func}"+"} "  + str(txt)) ## We print this statement if the log is in a function
        except:
            self.logfile.write("\n" + "ERROR: " + f"[{self.ParentFile}] " + str(txt)) ## Otherwise we print this statement

    def alert(self): ## Function used for alerting the user/dev that an error occured
        print(65*"/")
        print("An error occured, look at the log for more informations") ## Sentence printed
        print(65*"/")
        print("Wait a minute, we are opening an explorer window to the log file...") ## We add this lign
        print("It can takes a few moments...")  ## Saying that we're opening the folder where there's the log file
        print(" ")  ## And it can take a few moments
        subprocess.Popen(r'explorer /select, {}'.format(self.file))

    ############################################################
    #### Funcs for Ending the script and the log
    ############################################################
    def end(self): ## Function used to end the log file and the script as well
        self.logfile.write("\n\n//////////////////////////////////////////\n") ## We write delimitations using "/" to be sure it's visible by the user/dev looking the log
        self.logfile.write("Log file ended at " + str(datetime.datetime.now()) + "\n") ## We write the time of the end of the script
        self.logfile.write("//////////////////////////////////////////") ## We ends by rewriting our delimitation only for styling the end of the file.
        exit() ## We use the built-in function of python to ends the script
