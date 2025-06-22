"""
Generative UI Multi-Agent System
ADK-compliant agent package structure
"""
from .generative_ui.agent import root_agent

# ADK discovery: expose root_agent for web interface
__all__ = ['root_agent']