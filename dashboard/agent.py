"""
ADK Agent Bridge for Dashboard App
Exposes the root agent from the main agents directory with enhanced instructions
"""
import sys
import os

# Add the parent directory to sys.path to access agents
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

# Import the real root agent from the agents directory
from agents.generative_ui.agent import root_agent as base_root_agent
from google.adk.agents import LlmAgent

# Use the updated root agent directly - no override needed
root_agent = base_root_agent

# Export for ADK web interface discovery
__all__ = ['root_agent']