#!/usr/bin/env python
from crewai.llm import LLM
import agentops
agentops.init(default_tags=["crewai"])


import sys
from crewagents.crew import CrewagentsCrew


topic = """Extract Information about openai swarm from the below URLs. URLs are separated by ,"""
URL = ["https://x.com/shyamalanadkat/status/1844888546014052800", "https://x.com/search?q=openai%20%20swarm&src=recent_search_click"]

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': topic,
        'URL': URL
    }
    CrewagentsCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": topic,
    }
    try:
        CrewagentsCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewagentsCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": topic
    }
    try:
        CrewagentsCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
    

if __name__ == "__main__":
    run()