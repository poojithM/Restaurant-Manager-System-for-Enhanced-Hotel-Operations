from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool
from pydantic import BaseModel, Field
from typing import Dict, List


# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

file_writter = FileWriterTool()

class SentimentOutput(BaseModel):
    sentiment: str = Field( ..., description="Overall sentiment derived from the analysis, e.g., 'positive', 'negative', or 'neutral'." )
    sentiments_percentage: Dict[str, int] = Field(..., description="Dictionary showing the sentiment percentages, e.g., {'positive': 90, 'negative': 10, 'neutral': 20}.")
    


class ExtractedKeywordsOutput(BaseModel):
    extracted_keywords: List[str] = Field(...,description="List of extracted keywords from the summary. For example: ['food is good', 'service is bad', 'interior is good'].")


@CrewBase
class hotel_manager:
    """Poem Crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # If you would lik to add tools to your crew, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def summerizer(self) -> Agent:
        return Agent(
            config=self.agents_config["summerizer"],
            memory = True
        )
    
    @agent
    def sentiment_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config["sentiment_analyzer"],
            memory = True
        )
        
    @agent
    def keyword_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config["keyword_extractor"],
            memory = True
        )
    
    @agent
    def reporter(self) -> Agent:
        return Agent(
            config=self.agents_config["reporter"],
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def summerizer_task(self) -> Task:
        return Task(
            config=self.tasks_config["summerizer_task"],
        )
    
    @task
    def sentiment_task(self) -> Task:
        return Task(
            config=self.tasks_config["sentiment_task"],
            output_pydantic = SentimentOutput,
            async_execution = True, 
            
        )
        
    @task
    def extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config["extraction_task"],
            output_pydantic = ExtractedKeywordsOutput,
            async_execution = True
        )
        
    @task
    def reporter_task(self) -> Task:
        return Task(
            config=self.tasks_config["reporter_task"],
            
            tools = [file_writter],
            output_file = "report.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
