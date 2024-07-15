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
            expected_output="Your final answer should be a detailed investment recommendation report to buy or sell a stock, containing a logical and intuitively synthesized analysis of the stock's potential risks and rewards. Clear recommendations for recommendations based on {report} Please provide evidence.",
            agents=[left_brain_agent, right_brain_agent],
            context=sub_tasks,
            output_file="final_report.md",
        )