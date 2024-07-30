from crewai_tools import tool
import yfinance as yf

class Tools:

    @tool("One month stock price history")
    def stock_price(ticker):
        """
        Useful to get a month's worth of stock price data as CSV.
        The input of this tool should a ticker, for example AAPL, NET, TSLA etc...
        """
        stock = yf.Ticker(ticker)
        return stock.history(period="1mo").to_csv()

    @tool("Stock news URLs")
    def stock_news(ticker):
        """
        Useful to get URLs of news articles related to a stock.
        The input to this tool should be a ticker, for example AAPL, NET
        """
        stock = yf.Ticker(ticker)
        return list(map(lambda x: x["link"], stock.news))

    @tool("Company's income statement")
    def income_stmt(ticker):
        """
        Useful to get the income statement of a stock as CSV.
        The input to this tool should be a ticker, for example AAPL, NET
        """
        stock = yf.Ticker(ticker)
        return stock.income_stmt.to_csv()

    @tool("Balance sheet")
    def balance_sheet(ticker):
        """
        Useful to get the balance sheet of a stock as CSV.
        The input to this tool should be a ticker, for example AAPL, NET
        """
        stock = yf.Ticker(ticker)
        return stock.balance_sheet.to_csv()

    @tool("Get insider transactions")
    def insider_transactions(ticker):
        """
        Useful to get insider transactions of a stock as CSV.
        The input to this tool should be a ticker, for example AAPL, NET
        """
        stock = yf.Ticker(ticker)
        return stock.insider_transactions.to_csv()
    
    # DBS metric 지표를 가져오는 tool 구현
    @tool("Get key financial metrics")
    def get_key_metrics(ticker):
        """
        Useful to get key financial metrics for a stock.
        The input to this tool should be a ticker.
        """
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
                
            market_cap = info.get('marketCap', 'N/A')
            if market_cap != 'N/A':
                market_cap = f"{market_cap / 1e9:.1f}"  # Convert to billions
                
            volume = info.get('volume', 'N/A')
            if volume != 'N/A':
                volume = f"{volume / 1e6:.1f}"  # Convert to millions
                
            # Yahoo Finance Rating: {rating} 제외    
            metric = f"""
            Key Financial Data:
                
            Bloomberg Ticker: {ticker} US
            Sector: {info.get('sector', 'N/A')}
            Share Price (USD): {info.get('currentPrice', 'N/A')}
            12-mth Target Price (USD): {info.get('targetMeanPrice', 'N/A')}
            Market Cap (USDb): {market_cap}
            Volume (m shares): {volume}
            Free float (%): {info.get('floatShares', 'N/A') / info.get('sharesOutstanding', 1) * 100:.1f}
            Dividend yield (%): {info.get('dividendYield', 0) * 100:.1f}
            Net Debt to Equity (%): {info.get('debtToEquity', 'N/A')}
            Fwd. P/E (x): {info.get('forwardPE', 'N/A')}
            P/Book (x): {info.get('priceToBook', 'N/A')}
            ROE (%): {info.get('returnOnEquity', 0) * 100:.1f}
            """
            return metric
        except Exception as e:
            return f"Error fetching data for ticker {ticker}: {str(e)}"
