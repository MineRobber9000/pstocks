import getters
class StockTicker:
	"""A stock ticker to track certain stocks with."""
	def __init__(self, data=["s","n","l1","c1"], format="{1} ({0}) {2} ({3})"):
		self.symbols = []
		self.data = data
		self.format = format

	def addSymbol(self,symbol):
		self.symbols.append(symbol)

	def removeSymbol(self,symbol):
		self.symbols = [x for x in self.symbols if x != symbol]

	def getTickerValues(self):
		reader = getters.getStocks(self.symbols,"".join(self.data))
		ret = []
		for row in reader:
			ret.append(self.format.format(*row))
		return ret
