#!/usr/bin/env python

import urllib2
import json

GET_MARKET_SUMMARIES = "https://bittrex.com/api/v1.1/public/getmarketsummaries"

json_marketsummaries = urllib2.urlopen(GET_MARKET_SUMMARIES)
marketsummaries = json.load(json_marketsummaries)

######### TOP COIN ###########
markt = marketsummaries["result"]
config = open("topcoins.txt", "w")

# NUR BTC PAARE
for pair in marketsummaries["result"]:
    if pair["MarketName"].startswith("BTC-") and pair["BaseVolume"] > 200:
        paar = pair["MarketName"]
        configausgabe = ('"' + paar.strip() + '": {"strategy": "bb", "override": {}},')
        config.write("\t\t\t" + configausgabe + '\n')
        print configausgabe
config.close()

print "#################"
print "#Config updated!#"
print "#################"