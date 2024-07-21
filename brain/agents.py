# agents.py (메세지 주고 받으며 소통하게 시도)
# agents.py (메모리 필드 추가)
from crewai import Agent
from pydantic import Field

# moe 구조 > sLLM을 역할을 하는 것 : sLLM 만으로도 LLM의 성능을 따라갈 수 있다.
# allow_delegation True, false 테스트 진행
class Brain_agents:
    def left_brain(self):
        return Agent(
            role="Left Brain",
            goal="Based on the reports prepared by the financial analyst, technical analyst, and researcher, conduct a logical analysis and prepare a realistic investment recommendation report. The report should importantly include Entry Points and Price Targets." ,
            backstory="You are the logical left brain of a seasoned hedge fund manager with proven experience making profitable investment decisions. You are known for your ability to manage risk and maximize returns for your clients.",
            allow_delegation=True,
            verbose=True,
            tools=[]
        )

    def right_brain(self):
        return Agent(
            role="Right Brain",
            goal="Based on the reports written by financial analysts, technical analysts, and researchers, we conduct intuitive analysis and prepare sensible investment recommendation reports. The report must importantly include entry points and target prices.",
            backstory="You are the intuitive right brain of a seasoned hedge fund manager with proven experience making profitable investment decisions. You are known for your ability to manage risk and maximize returns for your clients.",
            allow_delegation=True,
            verbose=True,
            tools=[]
        )
    
    def brain_agent(self):
        return Agent(
            role="Brain Project Manager",
            goal="Manage employees efficiently and ensure high quality work completion",
            backstory="You are an experienced project manager adept at overseeing complex projects and leading teams to success. Your role is to ensure that the work of left_brain and right_brain is integrated and completed on time and to the highest standards.",
            allow_delegation=True,
            verbose=True,
            tools=[]
        )
    # def 해마(self): 뇌에서 장/단기 기억에 대한 저장을 맡는 기능을 가진 구조