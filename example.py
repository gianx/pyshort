#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyshort import pyshort
myshort = pyshort("sites_archive.json")
try:
    print myshort.generate(astring="http://www.gianlucanieri.com",checksite=False)[0]
except myshort.SiteConnectionError, e:
    print "beccato!"