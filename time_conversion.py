#!/bin/python3

#import os
import sys
import re
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if re.search(r'PM',s).group() == 'PM':
        time_string = re.sub(r'PM','',s)
        time_str_list = time_string.split(':')
        ans = int(time_str_list[0]) + 12
        time_str_list.pop(0)
        time_str_list.insert(0,str(ans))
        return ':'.join(time_str_list)

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
