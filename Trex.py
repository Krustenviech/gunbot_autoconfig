#GUNBOT AUTOCONFIG v.1.0 Alpha version!
#
# by Krustenviech Mail: krustenviech@gmail.com Tele: https://t.me/Krustenviech
#
#if this helped you, how about a coffee for me?
# BTC: 12Qy1qxd5RqwCc47cPtRL4off1KPFKzKom
# ETH: 0xd01295bB1845A8d7e1643702E42ceC2e9e96dF9F
#
#more info: https://github.com/Krustenviech/gunbot_autoconfig

#!/usr/bin/env python

import urllib2
import json

GET_MARKET_SUMMARIES = "https://bittrex.com/api/v1.1/public/getmarketsummaries"
override = {'GAIN': 0.6, 'HIGH_BB': 60, 'LOW_BB': -40, 'DOUBLE_UP': true} #Override settings for old pairs u want to sell off, please enter u´r own, if u wish so.

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

######################################################################################################################### NEW
#conf = json.loads(open('config.js').read())
#conf['pairs']['poloniex'] = {}

######################################################################################################################### Vorher FEHLERANALYSE?

#for pair in marketsummaries["result"]:
#    if pair["MarketName"].startswith("BTC-") and pair["BaseVolume"] > 200:
#        conf['pairs']['bittrex'][pair] = {'strategy': 'bb', 'override': {}}

######################################################################################################################### Paare die nicht neu sind "override" ?

 #       for e in balances:
  #          if float(balances[e]) > 0 and e != 'BTC':
   #             if 'BTC_' + e not in conf['pairs']['bittrex']:
    #                conf['pairs']['bittrex']['BTC_' + e] = {'strategy': 'bb', 'override': override}
######################################################################################################################### ? Balances

     #   with open('config.js', 'w') as f:
      #      f.write(json.dumps(conf, sort_keys=False, indent=4))

print "#################"
print "#Config updated!#"
print "#################"