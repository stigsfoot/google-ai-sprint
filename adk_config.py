"""
ADK Configuration for Web Interface
"""
from agents.generative_ui.agent import root_agent, chart_generation_agent

# Export agents for ADK web interface
__all__ = ['root_agent', 'chart_generation_agent']