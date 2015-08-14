# coding: utf-8

from pytrends.py2GTrends import pyGTrends, parse_data
import re
import time
from random import randint
import getpass
import pprint


def pp(obj, encoding='utf-8'):
    pp_ = pprint.PrettyPrinter(indent=2)
    s = pp_.pformat(obj)
    s = re.sub(r'\\u([0-9a-f]{4})', lambda x: unichr(int('0x' + x.group(1), 16)), s)
    s = s.encode(encoding) if encoding else s
    return s

google_username = raw_input('username (Google)? ')
google_password = getpass.getpass('passwd? ')
path = ""

#connect to Google
connector = pyGTrends(google_username, google_password)

#make request
connector.request_report("寿司,天ぷら", geo='JP')

#wait a random amount of time between requests to avoid bot detection
#time.sleep(randint(5,10))

#download file
connector.save_csv(path, "sushi_tempura")

#parse data
data = connector.get_data()
parsed_data = parse_data(data)

print pp(parsed_data)
