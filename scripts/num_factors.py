#!/usr/bin/env python

# Written by Karolis Uziela in 2013

import sys
from sets import Set
from collections import Counter
import multiprocessing
from IPython.parallel import Client

################################ Usage ################################

script_name = sys.argv[0]

usage_string = """
Usage:

    %s <mode>
    
<mode> :
    s - serial
    m - multiprocessing
    i - IPython.parallel
""" % script_name

if len(sys.argv) != 2:
    sys.exit(usage_string)

################################ Functions ################################

def factorize(n):
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors
        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            p += 2
        else:
            p += 1

def count_unique_factors(n):
    factors = factorize(n)
    return len(Set(factors))

################################ Variables ################################

# Constants
MODE = sys.argv[1]

################################ Main script ################################
    
if MODE == "s":
    print "Running %s in serial mode" % script_name
    uniq_list = []
    for i in xrange(2, 500001):
        uniq_list.append(count_unique_factors(i))
    print(dict(Counter(uniq_list)))
elif MODE == "m":
    print "Running %s in multiprocessing mode" % script_name
    pool = multiprocessing.Pool(processes=4)
    results = pool.map_async(count_unique_factors, xrange(2, 500001))
    uniq_list = results.get()
    print(dict(Counter(uniq_list)))
elif MODE == "i":
    print "Running %s in IPython.parallel mode" % script_name
    cli = Client()
    dview = cli[:]

    ########### does not work... But how do I make it work?.. ##########
    #@dview.parallel(block=True)
    #def count_unique_factors_interactive(n):
    #    return count_unique_factors(n)

    @dview.parallel(block=True)
    def factorize_interactive(n):
        if n < 2:
            return []
        factors = []
        p = 2 

        while True:
            if n == 1:
                return factors
            r = n % p 
            if r == 0:
                factors.append(p)
                n = n / p 
            elif p * p >= n:
                factors.append(n)
                return factors
            elif p > 2:
                p += 2
            else:
                p += 1 

    result = factorize_interactive.map(range(2, 500001))
    uniq_list = []
    for elem in result:
        uniq_list.append(len(Set(elem)))
    print(dict(Counter(uniq_list)))

