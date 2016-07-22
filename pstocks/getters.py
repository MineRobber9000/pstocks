import csv,requests;
from urllib import quote_plus as urlencode;

def generatorFromText(text):
	for line in text.splitlines():
		yield line

def getCSVFile(url):
	r = requests.get(url)
	reader = csv.reader(generatorFromText(r.text))
	return reader

def getStocks(symbols,data):
	symbol_string = ""
	if type(symbols) is str:
		symbol_string = symbols
	else:
		symbol_string = "+".join(symbols)
	return getCSVFile("http://finance.yahoo.com/d/quotes.csv?s="+urlencode(symbol_string)+"&f="+data)
