# 뇌 구조 모방한 모듈
# 뇌 구조간 소통 기능 추가하려다가 실패..

# agents.py (메세지 주고 받으며 소통하게 시도)
# agents.py (메모리 필드 추가)
# import brain agents
from crewai import Agent
from pydantic import Field
from brain.agents import *

# import brain task
from crewai import Task
from brain.tasks import Brain_tasks

# main.py
import os
from dotenv import load_dotenv
from crewai import Crew
from crewai.process import Process
from langchain_openai import ChatOpenAI
from datetime import datetime

# 환경 변수 로드
load_dotenv()

os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo-0125"
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# 테스트를 위한 최종 보고서 로드 , 나중에 crew 병합할 예정
def read_initial_report(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    agents = Brain_agents()
    tasks = Brain_tasks()

    # 에이전트 생성
    left_brain = agents.left_brain()
    right_brain = agents.right_brain()

    # 초기 보고서 파일 경로
    initial_report_path = "total_report.txt"
    # 초기 보고서 읽기
    initial_report = read_initial_report(initial_report_path)

    # 태스크 생성
    analyze_report_task = tasks.analyze_report(left_brain, right_brain, initial_report)

    # Crew 객체 생성 및 태스크 수행
    crew = Crew(
        agents=[
            left_brain,
            right_brain,
        ],
        tasks=[
            analyze_report_task,
        ],
        verbose=2,
        process=Process.hierarchical,
        manager_llm=ChatOpenAI(model="gpt-4o"),
        memory=True,
    )

    # 태스크 실행 및 결과 받기
    result = crew.kickoff(
        inputs=dict(
            report=initial_report,
        ),
    )

    # 메시지 주고받기 (서로 메세지 주고 받으면서 소통하게 하려다 실패함..)
    # 이제 주고 받는건가..? 로그 찍어볼 수 있게 해봐야 겠다.
    # 메시지 기록 파일 자동 생성
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"message_log_{timestamp}.txt"

    with open(log_filename, "w") as log_file:
        log_file.write("Message exchange between Left Brain and Right Brain:\n\n")

        for _ in range(10):  # 최대 10번의 메시지 주고받기
            left_message = left_brain.receive_message("Right Brain", log_file)
            if left_message:
                right_brain.send_message(left_message, log_file)

            right_message = right_brain.receive_message("Left Brain", log_file)
            if right_message:
                left_brain.send_message(right_message, log_file)

            if left_brain.memory.has_task_done() or right_brain.memory.has_task_done():
                break

    # 최종 보고서 출력
    for message in left_brain.memory.get_messages():
        print(f"{message['role']}: {message['content']}")

if __name__ == "__main__":
    main()