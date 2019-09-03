from logger_base import Logger

logger = Logger('my.log')
logger.write_log('Loggin with a classin singelton pattern')
logger2 = Logger("***ignored message****")
logger2.write_log('Another log record')

logger.close_log()

with open('my.log','r') as f:
    for line in f:
        print("pritning the log file")
        print(line,end='')