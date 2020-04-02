# https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    hour = s[0:2]
    minute = s[3:5]
    second = s[6:8]
    is_afternoon = True if s[8:] == "PM" else False
    return convert_to_time(hour, minute, second, is_afternoon)
    
def convert_to_time(hour, minute, second, is_afternoon):
    if hour == "12" and is_afternoon:
        hour = "12"
    elif hour == "12" and not is_afternoon:
        hour = "00"
    else:
        hour = str(int(hour) + 12) if is_afternoon else hour
    return hour + ":" + minute + ":" + second
