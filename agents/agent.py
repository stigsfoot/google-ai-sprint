"""
Root agent for ADK Web Interface
Duck-typed agent that works with ADK CLI requirements
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# Create a simple agent class with all required ADK attributes
class GenerativeUIOrchestrator:
    def __init__(self):
        # Required ADK attributes
        self.name = "generative_ui_orchestrator"
        self.model = "gemini-2.0-flash-001"
        self.instruction = """You are the Generative UI Orchestrator for business intelligence systems.

IMPORTANT: This agent runs in the ADK Web UI for demonstration purposes. 
For full functionality with actual UI generation, please use the FastAPI server at http://localhost:8081

You can process business queries and explain how the system would generate UI components:
- Sales trends → Line charts with trend analysis
- Regional data → Interactive maps with geographic visualization  
- Accessibility → High-contrast charts and screen reader tables
- Comparisons → Bar charts with comparative insights

Respond with explanations of what UI components would be generated for the given query."""
        
        # ADK-specific attributes
        self._type = "agent"
        self.tools = []
        self.sub_agents = []
        
        # Additional compatibility attributes
        self._name = self.name
        self._model = self.model
        self._agent_type = "llm_agent"
    
    # Methods that ADK expects
    async def run(self, query: str):
        return f"""For query: "{query}"

This system would generate the following UI components:

1. **Component Analysis**: Based on keywords, the system would delegate to specialized agents:
   - Chart Generation Agent: For trends, metrics, comparisons
   - Geospatial Agent: For regional, location-based queries  
   - Accessibility Agent: For high-contrast, screen reader optimized components

2. **Generated Components**: Real UI components would be created as React JSX and rendered in the dashboard.

3. **Live Demo**: Visit http://localhost:3002 to see the actual working system with real chart generation!

NOTE: This ADK Web UI shows the agent architecture. The actual UI generation happens via the FastAPI server at http://localhost:8081"""

    # Additional ADK compatibility methods
    def __str__(self):
        return f"GenerativeUIOrchestrator(name={self.name})"
    
    def __repr__(self):
        return self.__str__()
    
    # Properties ADK might check
    @property 
    def agent_type(self):
        return "llm_agent"

# Create the root agent instance
root_agent = GenerativeUIOrchestrator()