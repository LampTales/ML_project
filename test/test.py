import logging
import time
import os

if os.path.exists('output.log'):
    os.remove('output.log')

logging.basicConfig(filename='output.log', level=logging.INFO)

for i in range(1, 100):
    logging.info(i)
    time.sleep(1)