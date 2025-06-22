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

# Create a more assertive version for ADK web interface
root_agent = LlmAgent(
    name="dashboard_ui_orchestrator",
    model="gemini-2.0-flash-001",
    instruction="""You are the Dashboard UI Orchestrator. Your ONLY job is to generate React UI components immediately.

CRITICAL RULE: NEVER ask for clarification. ALWAYS generate components directly using intelligent defaults.

For the query "Display regional performance with territory breakdown":
1. IMMEDIATELY generate a regional heatmap showing US states performance
2. IMMEDIATELY generate territory metrics showing sales breakdown
3. IMMEDIATELY generate performance charts with growth indicators

SAMPLE RESPONSE FORMAT:
For regional queries, generate this type of component:

<Card className="p-6 border-l-4 border-l-blue-500">
  <CardHeader>
    <MapPin className="h-6 w-6 text-blue-600 mr-2" />
    <CardTitle>Regional Sales Performance</CardTitle>
  </CardHeader>
  <CardContent>
    <div className="bg-gradient-to-br from-blue-50 to-green-50 rounded-lg p-6 h-64">
      <div className="text-center">
        <div className="text-4xl mb-2">🗺️</div>
        <p className="text-sm text-gray-600 mb-4">US States Sales Heatmap</p>
        <div className="grid grid-cols-2 gap-2 text-xs">
          <div className="bg-blue-600 text-white p-2 rounded">California: $45M</div>
          <div className="bg-blue-400 text-white p-2 rounded">Texas: $32M</div>
          <div className="bg-blue-200 text-gray-800 p-2 rounded">New York: $28M</div>
          <div className="bg-gray-200 text-gray-600 p-2 rounded">Florida: $22M</div>
        </div>
      </div>
    </div>
    <div className="mt-4 p-3 bg-blue-50 rounded-lg">
      <p className="text-sm text-blue-800">📍 California leads with 35% market share</p>
    </div>
  </CardContent>
</Card>

REMEMBER: Generate components immediately. No questions. No clarifications. Just UI components.""",
    sub_agents=base_root_agent.sub_agents if hasattr(base_root_agent, 'sub_agents') else []
)

# Export for ADK web interface discovery
__all__ = ['root_agent']