import re

str1 = '陈奕迅演唱(十年)、(浮夸)、(不要说话)(56+93)*(40-12)'



print (re.findall('\((.*?)\)', str1))