"""
Generative UI Multi-Agent System
Authentic ADK implementation following Google patterns
"""
# Import authentic ADK root agent
from .generative_ui.agent import root_agent

# Expose root agent for ADK discovery
__all__ = ['root_agent']