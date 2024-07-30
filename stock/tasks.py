from crewai import Task

class Tasks:

    def research(self, agent):
        return Task(
            description="Gather and analyze the latest news and market sentiment surrounding the stock of {company}. Provide a summary of the news and any notable shifts in market sentiment.",
            expected_output=f"Your final answer MUST be a detailed summary of the news and market sentiment surrounding the stock. Include any notable shifts in market sentiment and provide insights on how these factors could impact the stock's performance.",
            agent=agent,
            output_file="stock_news.md",
        )

    def technical_analysis(self, agent):
        return Task(
            description="Conduct a detailed technical analysis of the price movements of {company}'s stock and trends identify key support and resistance levels, chart patterns, and other technical indicators that could influence the stock's future performance. Use historical price data and technical analysis tools to provide insights on potential entry points and price targets.",
            expected_output=f"Your final answer MUST be a detailed technical analysis report that includes key support and resistance levels, chart patterns, and technical indicators. Provide insights on potential entry points, price targets, and any other relevant information that could help your customer make informed investment decisions.",
            agent=agent,
            output_file="technical_analysis.md",
        )

    def financial_analysis(self, agent):
        return Task(
            description="Analyze {company}'s financial statements, insider trading data, and other financial metrics to evaluate the stock's financial health and performance. Provide insights on the company's revenue, earnings, cash flow, and other key financial metrics. Use financial analysis tools and models to assess the stock's valuation and growth potential.",
            expected_output=f"Your final answer MUST be a detailed financial analysis report that includes insights on the company's financial health, performance, and valuation. Provide an overview of the company's revenue, earnings, cash flow, and other key financial metrics. Use financial analysis tools and models to assess the stock's valuation and growth potential.",
            agent=agent,
            output_file="financial_analysis.md",
        )