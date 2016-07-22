# pstocks
Uses Yahoo APIs to get the latest on stocks.

## Usage
Make a ticker:

    ticker = pstocks.StockTicker()

Add some stocks:

    ticker.addSymbol("GOOG")
    ticker.addSymbol("YHOO")
    ticker.addSymbol("MSFT")
    ticker.addSymbol("F") # woops!

Then, finally, get the results:

    ticker.getTickerValues()

If you accidentally added a symbol you don't need, you can remove all instances of it from your ticker:

    ticker.removeSymbol("F")

Have fun using pstocks in your projects!
