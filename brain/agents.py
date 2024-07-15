# agents.py (메세지 주고 받으며 소통하게 시도)
# agents.py (메모리 필드 추가)
from crewai import Agent
from pydantic import Field
from brain.memory import Memory

class CustomAgent(Agent):
    memory: Memory = Field(default_factory=Memory)

    def __init__(self, role, goal, backstory, verbose, tools):
        super().__init__(role=role, goal=goal, backstory=backstory, verbose=verbose, tools=tools)
        self.memory = Memory()

    def send_message(self, content, log_file=None):
        self.memory.add_message(self.role, content)
        if log_file:
            log_file.write(f"{self.role}: {content}\n")

    def receive_message(self, role, log_file=None):
        message = self.memory.get_last_message(role)
        if message and log_file:
            log_file.write(f"Received by {self.role}: {message}\n")
        return message

# moe 구조 > sLLM을 역할을 하는 것 : sLLM 만으로도 LLM의 성능을 따라갈 수 있다.
class Brain_agents:
    def left_brain(self):
        return CustomAgent(
            role="Left Brain",
            goal="Manage your stock portfolio and collaborate with right_brain to make investment decisions based on logical analysis, taking as input a strategic final report to maximize returns made using insights from financial analysts, technical analysts and researchers.",
            backstory="You are the logical left brain of a seasoned hedge fund manager with proven experience making profitable investment decisions. You are known for your ability to manage risk and maximize returns for your clients.",
            verbose=True,
            tools=[]
        )

    def right_brain(self):
        return CustomAgent(
            role="Right Brain",
            goal="Manage your stock portfolio and collaborate with left_brain to make investment decisions based on intuitive analysis, taking as input a strategic final report to maximize returns made using the insights of financial analysts, technical analysts and researchers.",
            backstory="You are the intuitive right brain of a seasoned hedge fund manager with proven experience making profitable investment decisions. You are known for your ability to manage risk and maximize returns for your clients.",
            verbose=True,
            tools=[]
        )
    # def 해마(self): 뇌에서 장/단기 기억에 대한 저장을 맡는 기능을 가진 구조