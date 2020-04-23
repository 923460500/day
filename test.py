# coding:utf-8

import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s:%(message)s')


logging.warning("user [alex] attempted wrong password more than 3 times")
logging.critical("server is down")