{
	"pairs": {
		"bittrex": {
			"BTC-NEO": {"strategy": "bb", "override": {}},
			"BTC-XEM": {"strategy": "bb", "override": {}},
			"BTC-BAT": {"strategy": "bb", "override": {}},
			"BTC-ZEC": {"strategy": "bb", "override": {}},
			"BTC-ETH": {"strategy": "bb", "override": {}},
			"BTC-BCC": {"strategy": "bb", "override": {}},
			"BTC-ETC": {"strategy": "bb", "override": {}}
		}
	},

	"exchanges": {
		"poloniex": {
			"key": "",
			"secret": ""
		},
		"kraken": {
			"key": "",
			"secret": ""
		},
		"bittrex": {
			"key": "",
			"secret": ""
		}
	},

	"bot": {
		"debug": true,

		"period_storage_ticker": 300,
		"interval_ticker_update": 10000,

		"timeout_buy": 60000,
		"timeout_sell": 60000,

		"MIN_VOLUME_TO_BUY": 0.0005,

		"WATCH_MODE": false
	},

	"strategies": {
		"bb": {
			"BTC_TRADING_LIMIT": 0.001,
			"PERIOD": 15,
			"BUY_LEVEL": 2,
			"GAIN": 2.5,
			"HIGH_BB": 60,
			"LOW_BB": 33,
			"PANIC_SELL": false,
			"DOUBLE_UP": true
		}
	}


}