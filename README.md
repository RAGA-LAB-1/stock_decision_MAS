# stock_decision_MAS in RAGA Lab
## MAS : Multi Agent System  

<p align="center">
 <img src = "./img/Autonomous Agent Brain archi.png">
</p>  

---
## Team Role & Team members  

### 1. code develop : 코드 최적화를 위한 개발팀  
　　　a. member : 최현우, 김지우, 김대선  

### 2. Prompt engineering : metric 설정과 보다 나은 결과를 위한 프롬프트 테스트 팀  
　　　a. member : 최현우, 김지우, 박현아, 변상규  

### 3. Tuned sLLM develop : 뇌 모듈 및 Agent 별 튜닝된 sLLM 적용을 위한 개발팀  
　　　a. member : 최현우, 김한솔, 최성은  

---  
## 실행 방법  
　　　1. Run requirment.txt   
　　　2. Setting OPENAI_API_KEY   
　　　(X) 3. Run brain_module.py (Input : total_report.txt)     
　　　>>> Crew1 & Crew2 통합 후 main.py 실행 가능하게 개선중 통합 완료  

　　　3. Run run.py  
　　　4. Result : stock_news.md & technical_analysis.md & financial_analysis.md & final_recommendation_report.md  
　　　5. final_report.md : 1. key_financial_metrics, 2. Left Target Price, 3. Right Target Price, 4. Integrate Target Price, 5. Add Insights  

---  

## Component

### 1. Agent  
　　　a. Researcher  
　　　b. Technical_analyst  
　　　c. Financial_analyst  
  
  ###  **> 뇌모듈**
　　　d. Left_brain  
　　　e. Right_brain    
　　　f. brain_agent  
   

### 2. Task
　　　a. research : 최신 뉴스 기사에서 내용 분석 및 시장 심리 분석 (Yahoo Finance)  

　　　b. technical_analysis : 가격 변동에 대한 기술 분석  
　　　　　　(추세, 향후 성과 및 영향, 주요 지지/저항 수준, 차트 패턴 및 기술지표. 진입점, 가격 목표에 대한 통찰)  

　　　c. financial_analysis : 재무 건전성과 실적 평가  
　　　　　　(내부자 거래, 수익, 현금흐름, 재무 지표에 대한 통찰, 주식의 가치 & 성장 잠재력 평가)  

　　　d. analyze_report : 하위 Task의 Report들을 입력으로 좌/우뇌가 최종 투자 추천 보고서 출력    

### 3. Tool  
　　　stock_news : arg(ticker), 주식 관련 뉴스 기사 URL를 얻는 도구  
　　　stock_price : arg(ticker), 예: 한달치, 주가 데이터를 csv로 가져오는 도구  
　　　incom_stmt : arg(ticker), 주식의 손익계산서를 csv로 가져오는 도구  
　　　balance_sheet : arg(ticker), 주식의 대차대조표를 csv로 가져오는 도구  
　　　insider_tranaction : arg(ticker), 주식의 내부 거래를 csv로 가져오는 도구  
　　　get_key_metric : arg(ticker), DBS의 Key Financial Metrics 지표를 불러오는 도구  

### 4. Update (이전 기록 확인 후 추가 예정)  

　　　a. 24.07.23 : Integrate Crew 1 + Crew 2, Changed async Crew 1

　　　b. 24.07.29 : Integrate Hyunwoo & Daesun' code

　　　c. 24.07.30 : Add DBS's Metrics, Update Prompt, Update Data Process 

