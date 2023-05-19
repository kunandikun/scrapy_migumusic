import os.path

from scrapy.cmdline import execute
#import logging
#logging.getLogger('scrapy').propagate = False

import sys
import os

sys.path.append(os.path.dirname((__file__)))
execute(["scrapy","crawl","demo_test"])
