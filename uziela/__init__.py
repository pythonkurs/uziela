#!/usr/bin/env python

# Written by Karolis Uziela in 2013

def parse_outages(XML_file):
    import untangle

    doc = untangle.parse(XML_file)
    outages = doc.NYCOutages.outage
    N = len(outages)
    repair_count = 0

    for i in range(N):
        if outages[i].reason.cdata == "REPAIR":
            repair_count += 1

    fraction = float(repair_count) / N
    
    return fraction

