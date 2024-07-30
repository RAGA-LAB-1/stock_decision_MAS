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

from brain.brain_agents import *
from brain.brain_tasks import *

def main():
    # Second_crew에서 ticker를 입력으로 못 받아서 수정 (직접 명시)
    company = "Salesforce"
    ticker = "CRM"  # 회사의 실제 ticker를 사용

    # 첫 번째 Crew 설정 (비동기 실행)
    agents = Agents()
    tasks = Tasks()
    researcher = agents.researcher()
    technical_analyst = agents.technical_analyst()
    financial_analyst = agents.financial_analyst()

    research_task = tasks.research(researcher)
    technical_task = tasks.technical_analysis(technical_analyst)
    financial_task = tasks.financial_analysis(financial_analyst)

    # financial_analyst에게 Key Financial Metrics 도구 사용 강조
    financial_analyst.tools.append(Tools.get_key_metrics)

    first_crew = Crew(
        agents=[researcher, technical_analyst, financial_analyst], 
        tasks=[research_task, technical_task, financial_task],
        process=Process.hierarchical,
        manager_llm=ChatOpenAI(model="gpt-3.5-turbo-0125"), # "gpt-4o"),
        memory=True,
    )

    # 첫 번째 크루 실행 (비동기)
    first_result = asyncio.run(first_crew.kickoff_async(inputs={"company": company, "ticker": ticker}))

    # 두 번째 Crew 설정 (동기 실행)
    second_agents = Brain_agents()
    second_tasks = Brain_tasks()

    left_brain = second_agents.left_brain()
    right_brain = second_agents.right_brain()
    brain_agent = second_agents.brain_agent()

    # left_brain과 right_brain에게 Key Financial Metrics 도구 사용 강조
    left_brain.tools.append(Tools.get_key_metrics)
    right_brain.tools.append(Tools.get_key_metrics)

    # second_crew ticker 직접 입력 수정
    analyze_report_task = second_tasks.analyze_report(left_brain, right_brain, first_result, ticker)

    second_crew = Crew(
        agents=[left_brain, right_brain],
        tasks=[analyze_report_task],
        manager_agent=brain_agent,
        verbose=2,
        process=Process.hierarchical,
        manager_llm=ChatOpenAI(model="gpt-3.5-turbo-0125"), # "gpt-4o"),
        memory=True,
    )

    # 두 번째 크루 실행 (동기)
    # Key financial metric 명확하게 전부 출력하는지 확인하기 위해 로직 추가
    # Key Financial Metrics 가져오기
    second_result = second_crew.kickoff(inputs={"report": first_result, "ticker": ticker}) 

    # Key Financial Metrics 확인
    # 결과에 Key Financial Metrics 섹션이 없으면 직접 추가
    if "Key Financial Metrics:" not in second_result:
        key_metrics = Tools.get_key_metrics(ticker)
        second_result = f"Key Financial Metrics:\n{key_metrics}\n\n{second_result}"

    # 결과 파일에 쓰기
    with open("final_recommendation_report.md", "w") as f:
        f.write(second_result)

    # Key Financial Metrics 확인
    if "Key Financial Metrics:" not in second_result:
        print("Warning: Key Financial Metrics section is missing in the final report.")
    else:
        print("Key Financial Metrics section is present in the final report.")

    return second_result

if __name__ == "__main__":
    final_result = main()
    print(final_result)