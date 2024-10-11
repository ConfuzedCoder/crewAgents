#!/usr/bin/env python
from crewai.llm import LLM
import agentops
agentops.init(default_tags=["crewai"])


import sys
from crewagents.crew import CrewagentsCrew


topic = """Extract topic and references from the given URL below"""
URL = "ADD URL HERE"

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': topic,
        'URL' : URL
    }
    CrewagentsCrew().crew().kickoff(inputs=inputs)

    agentops.end_session(end_state="Success")



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
    