import os, asyncio
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo-0125"
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

from crewai import Crew
from crewai.process import Process
from langchain_openai import ChatOpenAI

from stock.agents import *
from stock.tasks import *

from brain.agents import *
from brain.tasks import *

def main():
    # 첫 번째 Crew 설정 (비동기 실행)
    agents = Agents()
    tasks = Tasks()
    researcher = agents.researcher()
    technical_analyst = agents.technical_analyst()
    financial_analyst = agents.financial_analyst()
    hedge_fund_manager = agents.hedge_fund_manager()

    research_task = tasks.research(researcher)
    technical_task = tasks.technical_analysis(technical_analyst)
    financial_task = tasks.financial_analysis(financial_analyst)
    recommend_task = tasks.investment_recommendation(hedge_fund_manager, [research_task, technical_task, financial_task])

    first_crew = Crew(
        agents=[researcher, technical_analyst, financial_analyst, hedge_fund_manager],
        tasks=[research_task, technical_task, financial_task, recommend_task],
        verbose=2,
        process=Process.hierarchical,
        manager_llm=ChatOpenAI(model="gpt-4o"),
        memory=True,
    )

    # 첫 번째 크루 실행 (비동기)
    first_result = asyncio.run(first_crew.kickoff_async(inputs={"company": "Salesforce"}))

    # 두 번째 Crew 설정 (동기 실행)
    second_agents = Brain_agents()
    second_tasks = Brain_tasks()

    left_brain = second_agents.left_brain()
    right_brain = second_agents.right_brain()

    analyze_report_task = second_tasks.analyze_report(left_brain, right_brain, first_result)

    second_crew = Crew(
        agents=[left_brain, right_brain],
        tasks=[analyze_report_task],
        verbose=2,
        process=Process.hierarchical,
        manager_llm=ChatOpenAI(model="gpt-4o"),
        memory=True,
    )

    # 두 번째 크루 실행 (동기)
    second_result = second_crew.kickoff(inputs={"report": first_result})

    return second_result

if __name__ == "__main__":
    final_result = main()
    print(final_result)