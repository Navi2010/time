import random
import time

def x (startdate, enddate):
    numb = random.random()
    dateFormat = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(startdate, dateFormat))
    endTime = time.mktime(time.strptime(enddate, dateFormat))
    randomTime = startTime + numb * (endTime - startTime)
    randomdate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomdate

y = x("1/1/2016", "12/12/2018")
print(y)