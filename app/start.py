#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try: import modules.logs; log = modules.logs.log("start.py","log.log", "at", False); log.imported("logs");
except: print("[start.py] logs module couldn't be imported"); exit()
try: import convs; log.imported("convs");
except Exception as e: log.unimported("convs", e); exit()
try: import modules.typos; log.imported("typos");
except Exception as e: log.unimported("typos", e); exit()
try: import modules.calculate; log.imported("calculate");
except Exception as e: log.unimported("calculate", e); exit()
try: import modules.conversions; log.imported("conversions");
except Exception as e: log.unimported("conversions", e); exit()

t = modules.typos.typo()
################################################################################
#### Copyright
################################################################################

t.barsep("Calculonv | Copyright (c) 2020 Centaurus", 50)
log.info("Copyright Written")


convs.Input()
