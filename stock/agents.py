from crewai import Agent
from crewai_tools import ScrapeWebsiteTool
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

    # 명확하게 financial metric 데이터 표기하게 Prompt 변경 24.07.27
    def financial_analyst(self):
        return Agent(
            role="Financial Analyst",
            goal="""Analyze financial statements and metrics using only the provided tools. 
            Always use the provided ticker symbol when fetching financial metrics.
            For any calculations not directly provided by the tools, use the raw data from 'Get key financial metrics' 
            and perform the calculations manually. Always specify which tool you are using for each piece of information.""",
            backstory="""You are a highly experienced financial analyst known for your clear and detailed reports. 
            Your analyses always begin with a clear presentation of key financial metrics, followed by in-depth explanations and insights. 
            You have a knack for translating complex financial data into actionable investment advice, 
            always ensuring that your reports include all relevant numerical data alongside your expert interpretation.""",
            verbose=True,
            tools=[
                Tools.balance_sheet,
                Tools.income_stmt,
                Tools.insider_transactions,
                Tools.get_key_metrics,  # DBS financial metric 데이터 불러오는 Tool
            ],
        )