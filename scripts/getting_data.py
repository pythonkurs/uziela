#!/usr/bin/env python

# Written by Karolis Uziela in 2013

from uziela import parse_outages

XML_file = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"

fraction = parse_outages(XML_file)

print "Fraction of outages that are under repair: %0.2f" % fraction

