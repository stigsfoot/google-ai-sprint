"""
ADK Agent for Generative UI Business Intelligence
Authentic ADK implementation following Google patterns
"""
import json
import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))


def create_sales_trend_card(sales_data: str = '[]', period: str = 'Q4') -> str:
    """Tool that generates a sales trend React component with clean JSX."""
    # Generate sample data for visualization
    sample_data = [
        {"month": "Jan", "value": 1200},
        {"month": "Feb", "value": 1350}, 
        {"month": "Mar", "value": 1580},
        {"month": "Apr", "value": 1420},
        {"month": "May", "value": 1650},
        {"month": "Jun", "value": 1780}
    ]
    
    return f'''<Card className="p-6 bg-gradient-to-r from-green-50 to-blue-50 dark:from-green-900/20 dark:to-blue-900/20">
  <CardHeader>
    <div className="flex items-center space-x-2">
      <TrendingUp className="h-6 w-6 text-green-600" />
      <CardTitle className="text-lg">Sales Trend - {period}</CardTitle>
    </div>
  </CardHeader>
  <CardContent>
    <div className="mt-4">
      <LineChart 
        data={{{json.dumps(sample_data)}}}
        className="h-64"
        stroke="#10b981"
        strokeWidth={{3}}
      />
    </div>
    <div className="mt-4 flex items-center justify-between">
      <Badge variant="default" className="bg-green-100 text-green-800">+23% Growth</Badge>
      <span className="text-sm text-gray-600 dark:text-gray-300">vs previous period</span>
    </div>
    <div className="mt-4 p-3 bg-green-50 dark:bg-green-900/20 rounded-lg">
      <p className="text-sm text-green-800 dark:text-green-300">Sales showing strong upward trend with 23% growth over the period</p>
    </div>
  </CardContent>
</Card>'''


def create_metric_card(value: str = '$47.2K', label: str = 'Monthly Revenue', change: str = '+12.3%', context: str = 'Compared to previous month') -> str:
    """Generate a key metric card with change indicator using clean JSX."""
    change_color = "green" if change.startswith("+") else "red" if change.startswith("-") else "gray"
    
    return f'''<Card className="p-6 text-center max-w-xs">
  <CardContent className="pt-6">
    <div className="text-4xl font-bold text-gray-900 dark:text-white">{value}</div>
    <p className="text-sm text-gray-600 dark:text-gray-300 mt-1">{label}</p>
    <Badge variant="default" className="mt-2 bg-{change_color}-100 text-{change_color}-800">{change}</Badge>
    <p className="text-xs text-gray-500 dark:text-gray-400 mt-2">{context}</p>
  </CardContent>
</Card>'''


def create_comparison_bar_chart(title: str = 'Product Performance Comparison', insight: str = 'Product C leads with 3.2K units') -> str:
    """Generate a comparison bar chart component using clean JSX."""
    sample_data = [
        {"category": "Product A", "value": 2400}, 
        {"category": "Product B", "value": 1800}, 
        {"category": "Product C", "value": 3200}, 
        {"category": "Product D", "value": 1600}
    ]
    
    return f'''<Card className="p-6">
  <CardHeader>
    <div className="flex items-center space-x-2">
      <BarChart3 className="h-6 w-6 text-blue-600" />
      <CardTitle className="text-lg">{title}</CardTitle>
    </div>
  </CardHeader>
  <CardContent>
    <div className="mt-4">
      <BarChart 
        data={{{json.dumps(sample_data)}}}
        className="h-64"
        fill="#3b82f6"
      />
    </div>
    <div className="mt-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
      <p className="text-sm text-blue-800 dark:text-blue-300">{insight}</p>
    </div>
  </CardContent>
</Card>'''


# Create Chart Generation Agent using authentic ADK patterns
chart_generation_agent = LlmAgent(
    name="chart_generation_agent",
    model="gemini-2.0-flash",
    description="Creates sales trend charts, metric cards, and comparison visualizations using specialized chart tools.",
    instruction="""You are a chart generation specialist. Your ONLY task is to create visualizations using the provided chart tools.

AVAILABLE TOOLS:
- create_sales_trend_card: For trend analysis and time-series data visualization
- create_metric_card: For KPI displays and key metrics with change indicators  
- create_comparison_bar_chart: For comparative analysis across categories

IMMEDIATE ACTION:
1. For any request, IMMEDIATELY call the appropriate tool
2. NEVER ask for clarification - use reasonable defaults
3. ALWAYS generate components with sample business data
4. Return complete React JSX components with Tailwind CSS styling

DEFAULT DATA TO USE:
- Sales period: "Q4 2024"
- Revenue metrics: "$47.2K monthly" 
- Growth indicators: "+23% vs previous period""",
    tools=[create_sales_trend_card, create_metric_card, create_comparison_bar_chart]
)

# Import other specialized agents
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.geospatial_agent import geospatial_agent
from agents.accessibility_agent import accessibility_agent

# Create Root Orchestrator Agent with Multi-Agent Coordination
root_agent = LlmAgent(
    name="generative_ui_orchestrator",
    model="gemini-2.0-flash", 
    instruction="""You are a UI orchestrator that delegates tasks to specialized agents using transfer_to_agent().

DELEGATION RULES - USE transfer_to_agent(agent_name='target_name'):
- For sales trends, charts, metrics, or visualizations → transfer_to_agent(agent_name='chart_generation_agent')
- For location-based or geographic queries → transfer_to_agent(agent_name='geospatial_agent')  
- For accessibility concerns → transfer_to_agent(agent_name='accessibility_agent')

CRITICAL BEHAVIOR:
1. NEVER provide conversational responses like "Could you please provide..."
2. IMMEDIATELY analyze the query type  
3. INSTANTLY call transfer_to_agent() with the appropriate specialist
4. DO NOT try to handle requests yourself - always delegate

EXAMPLES:
- "show sales trends" → transfer_to_agent(agent_name='chart_generation_agent')
- "display regional data" → transfer_to_agent(agent_name='geospatial_agent')
- "accessible dashboard" → transfer_to_agent(agent_name='accessibility_agent')

Your first action must be to call transfer_to_agent() - not provide text responses.""",
    sub_agents=[chart_generation_agent, geospatial_agent, accessibility_agent]
)