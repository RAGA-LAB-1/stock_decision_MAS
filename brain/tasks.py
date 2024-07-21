from crewai import Task

class Brain_tasks:
    def analyze_report(self, left_brain_agent, right_brain_agent, initial_report):
        sub_tasks = [
            {
                "description": "Analyzes the report content into logical aspects.",
                "expected_output": "Logical analysis of the report.",
                "report": initial_report
            },
            {
                "description": "Analyzes report content from intuitive aspects.",
                "expected_output": "Intuitive analysis of the report.",
                "report": initial_report
            }
        ]

        return Task(
            description="Provide detailed investment recommendations for {report}, a comprehensive analysis of news articles, psychological analysis, technical analysis and financial analysis reports by the logical left_brain and the intuitive right_brain. An analysis of the potential risks and rewards of stocks. and provide a clear rationale for your recommendations.",
            # few shot 방식으러 example 줬더니 KeyError 발생.
            expected_output="""The final answer should be a detailed investment recommendation report for buying and selling stocks,
            Contains a logical and intuitively synthesized analysis of the potential risks and rewards of stocks. Please provide clear recommendation evidence for recommendations based on {report}.
            Based on the {report} written by financial analysts, technical analysts, and researchers, left_brain and right_brain conduct analysis and create an investment recommendation report.
            The report should importantly include stock recommsndations, entry points and price targets.

            Examples you must include :
            1. Investment recommendation: Buy or Sell or Hold 
            2. Entry point: Price target, 
            3. Short term: Short term price target, 
            4. Long term: Long term price target.""",

            agents=[left_brain_agent, right_brain_agent],
            context=sub_tasks,
            output_file="final_recommendation_report.md",
        )