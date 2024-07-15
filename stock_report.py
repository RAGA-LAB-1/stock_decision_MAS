import os
from dotenv import load_dotenv

load_dotenv

os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo-0125"

# 각자의 API KEY 사용하세요!
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

from crewai import Crew
from crewai.process import Process
from langchain_openai import ChatOpenAI

from stock.agents import *
from stock.tasks import *

agents = Agents()
tasks = Tasks()

researcher = agents.researcher()
technical_analyst = agents.technical_analyst()
financial_analyst = agents.financial_analyst()
hedge_fund_manager = agents.hedge_fund_manager()

research_task = tasks.research(researcher)
technical_task = tasks.technical_analysis(technical_analyst)
financial_task = tasks.finacial_analysis(financial_analyst)
recommend_task = tasks.investment_recommendation(
    hedge_fund_manager,
    [
        research_task,
        technical_task,
        financial_task,
    ],
)

crew = Crew(
    agents=[
        researcher,
        technical_analyst,
        financial_analyst,
        hedge_fund_manager,
    ],
    tasks=[
        research_task,
        technical_task,
        financial_task,
        recommend_task,
    ],
    verbose=2,
    process=Process.hierarchical,
    manager_llm=ChatOpenAI(model="gpt-4o"),
    memory=True,
)

result = crew.kickoff(
    inputs=dict(
        company="Salesforce",
    ),
)

# 각 Task에서 나오는 report.md 들을 append > list, txt.. 포맷으로 저장 > 굳이 저장 안하고 메모리 저장 후 연쇄적 처리하고 싶다