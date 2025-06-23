"""
Generative UI Multi-Agent System
Simplified structure for demo
"""
# Import mock root agent for ADK Web UI compatibility
from .agent import root_agent

# Expose root agent for ADK discovery
__all__ = ['root_agent']