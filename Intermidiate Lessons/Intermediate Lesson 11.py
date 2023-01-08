"""
2023 1/7
1444  جُمَادَىٰ ٱلثَّانِي 14

Logging
"""
# every system produces a lot of msg statement, error and many more, and this need to be store somewhere
# Basically knowing the saving status or future warning and printing it to admin(moy)

# Logging
# help find + avoid + understand problem - https://www.geeksforgeeks.org/logging-in-python/

"""
security level

Debug - testing == ex. checking output 
Info - Information data == ex. 17 user online, 5 new msg
Warning - indicates nothing bad yet but about to == ex. running low on space/battery
Error - classical exception == ex. couldn't do something because of xyz - system still running
Critical - crucial component/part of system break down == ex. server is down 
"""

import logging

# default rout logger - pre_made
# own logger - customizable

logging.basicConfig(level=logging.DEBUG)  # setting level -> see comment line 33 and 34

logging.info("$185,950 was transferred to mercedes-Tokyo")
logging.critical("AI is angry") # ㅋㅋㅋㅋㅋ

# python has default security level of warning - security level work in to critical -> debug
# if you want to see critical it will only show critical, if you want to see debug it will show all 5 security level

# customizing logger
logger = logging.getLogger("moy logger")
logger.info("moy 1.0 logger created")
logger.critical("Moy is lost grind-set streak")

# other way to do it
logger.log(logging.ERROR,"Error?")

# making a log file - saving logs into file
handler = logging.FileHandler("moylog.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")  # have to use specific keywords
# .log file doesn't have structured format if you open -using specific keyword to make
handler.setFormatter(formatter)  # telling handler to save data using format defines in formatter

logger.addHandler(handler)  # giving access to moy logger data from code here below
logger.info("Moy is doing python")

"""
Quick 日記
우와ㅏㅏㅏㅏ
이제 프로젝트 할수 있다
솔직히 이번에 많이 기대 된다 레벨업 을 
많이 해 가지고 ㅋㅋㅋㅋㅋ
"""