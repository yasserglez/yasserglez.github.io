#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)
from develop_conf import *

SITEURL = 'http://yassergonzalez.com'
FEED_DOMAIN = SITEURL

PLUGINS += ['minify']
