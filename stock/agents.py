from crewai import Agent
from crewai_tools import ScrapeWebsiteTool
# import 상대경로 에러
from .tools import Tools

class Agents:

    def technical_analyst(self):
        return Agent(
            role="Technical Analyst",
            goal="Analyses the movements of a stock and provides insights on trends, entry points, resistance and support levels.",
            backstory="An expert in technical analysis, you're known for your ability to predict stock movements and trends based on historical data. You provide valuable insights to your customers.",
            verbose=True,
            tools=[
                Tools.stock_price,
            ],
        )

    def researcher(self):
        return Agent(
            role="Researcher",
            goal="Gathers, interprets and summarizes vasts amounts of data to provide a comprehensive overview of the sentiment and news surrounding a stock.",
            backstory="You're skilled in gathering and interpreting data from various sources to give a complete picture of a stock's sentiment and news. You read each data source carefuly and extract the most important information. Your insights are crucial for making informed investment decisions.",
            verbose=True,
            tools=[
                Tools.stock_news,
                ScrapeWebsiteTool(),
            ],
        )

    def financial_analyst(self):
        return Agent(
            role="Financial Analyst",
            goal="Uses financial statements, insider trading data, and other financial metrics to evaluate a stock's financial health and performance.",
            backstory="You're a very experienced investment advisor who uses a combination of technical and fundamental analysis to provide strategic investment advice to your clients. You look at a company's financial health, market sentiment, and qualitative data to make informed recommendations.",
            verbose=True,
            tools=[
                Tools.balance_sheet,
                Tools.income_stmt,
                Tools.insider_transactions,
            ],
        )