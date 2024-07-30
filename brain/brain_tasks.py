from crewai import Task

class Brain_tasks:
    def analyze_report(self, left_brain_agent, right_brain_agent, initial_report, ticker):
        context = [
            {
                "description": f"Analyze the comprehensive report for {ticker} and provide a logical investment recommendation.",
                "expected_output": "Logical analysis including price targets and entry points.",
                "initial_report": initial_report,
                "ticker": ticker
            },
            {
                "description": f"Analyze the comprehensive report for {ticker} and provide an intuitive investment recommendation.",
                "expected_output": "Intuitive analysis including price targets and entry points.",
                "initial_report": initial_report,
                "ticker": ticker
            }
        ]
        
        # Key Financial Metrics 확실히 출력하도록 명시
        # {ticker} 직접 사용할 수 있게 명시
        return Task(
            description=f"""Begin your analysis by using the 'Get key financial metrics' tool with the ticker symbol {ticker}. 
            Copy and paste the ENTIRE output from this tool at the very beginning of your report under a section titled 'Key Financial Metrics:'.
            Then, analyze the comprehensive {initial_report} provided by the financial analyst, technical analyst, and researcher for {ticker}. 
            Provide a detailed investment recommendation based on this analysis.""",

            expected_output="""Your report MUST include the following sections in this order:

            1. Key Financial Metrics: [Copy and paste the ENTIRE output from the 'Get key financial metrics' tool here]

            2. Left Brain Analysis:
            - 12-month Target Price: [Insert specific price]
            - Rationale for the target price
            - Key factors considered in the logical analysis

            3. Right Brain Analysis:
            - 12-month Target Price: [Insert specific price]
            - Rationale for the target price
            - Key intuitive factors and market sentiments considered

            4. Consolidated Recommendation:
            - Final Investment Recommendation: Buy / Hold / Sell
            - Consolidated Target Price: [Insert specific price]
            - Entry Point: [Insert specific price or price range]
            - Short-term Price Target: [Insert specific price]
            - Long-term Price Target: [Insert specific price]

            5. Consolidated Recommendation:
            - Final Investment Recommendation: Buy / Hold / Sell
            - Consolidated Target Price (if different from individual predictions)
            - Entry Point
            - Short-term Price Target
            - Long-term Price Target

            6. Risk Analysis:
            - Potential risks to the investment thesis
            - Factors that could significantly alter the recommendation

            7. Additional Insights:
            - Any other relevant information or analysis

            Ensure that ALL financial metrics are clearly presented at the beginning of the report exactly as provided by the 'Get key financial metrics' tool, 
            and that both the Left Brain and Right Brain analyses are thoroughly explained and justified.""",
            agents=[left_brain_agent, right_brain_agent],
            context=context,
            output_file="final_recommendation_report.md",
        )
