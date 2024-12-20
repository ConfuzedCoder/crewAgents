from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from typing import List
from agentops import record_tool, track_agent, record_action

# Uncomment the following line to use an example of a custom tool
# from crewagents.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool
from crewai_tools import ScrapeWebsiteTool

@CrewBase
class CrewagentsCrew():
	"""Crewagents crew"""

	# @agent
	# def researcher(self) -> Agent:
	# 	return Agent(
	# 	config=self.agents_config['researcher'],
	# 	verbose=True,
	# 	tools=[SerperDevTool()]
	# 	)

	# @agent
	# def reporting_analyst(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['reporting_analyst'],
	# 		verbose=True
	# 	)

	@agent
	def topic_scraper(self) -> Agent:
		return Agent(
		config=self.agents_config['topic_scraper'],
		verbose=True,
		tools=[ScrapeWebsiteTool()],
		max_iter=5
		)

	# @task
	# def research_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['research_task'],
	# 	)

	# @task
	# def reporting_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['reporting_task'],
	# 		output_file='report.md'
	# 	)
	
	@task
	def topic_extractor(self) -> Task:
		return Task(
			config=self.tasks_config['topic_extractor'],
			# output_pydantic=List[TopicData],
			output_file="topics.json",
			verbose=True
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Crewagents crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)