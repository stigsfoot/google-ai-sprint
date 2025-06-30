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


def create_sales_trend_card(sales_data: str, period: str) -> str:
    """Tool that generates a sales trend React component with React.createElement format."""
    # Generate sample data for visualization
    sample_data = [
        {"month": "Jan", "value": 1200},
        {"month": "Feb", "value": 1350}, 
        {"month": "Mar", "value": 1580},
        {"month": "Apr", "value": 1420},
        {"month": "May", "value": 1650},
        {"month": "Jun", "value": 1780}
    ]
    
    return f'''React.createElement(Card, {{ className: "p-6 bg-gradient-to-r from-green-50 to-blue-50 dark:from-green-900/20 dark:to-blue-900/20" }},
  React.createElement("div", {{ className: "flex items-center space-x-2 mb-4" }},
    React.createElement(TrendingUp, {{ className: "h-6 w-6 text-green-600" }}),
    React.createElement("h3", {{ className: "text-lg font-semibold" }}, "Sales Trend - {period}")
  ),
  React.createElement("div", {{ className: "mt-4" }},
    React.createElement(LineChart, {{
      data: {json.dumps(sample_data)},
      index: "month",
      categories: ["value"],
      colors: ["green"],
      className: "h-64",
      showLegend: false,
      showGridLines: true,
      curveType: "monotone",
      yAxisLabel: "Sales ($)",
      autoMinValue: true
    }})
  ),
  React.createElement("div", {{ className: "mt-4 flex items-center justify-between" }},
    React.createElement(Badge, {{ color: "green", size: "lg" }}, "+23% Growth"),
    React.createElement("span", {{ className: "text-sm text-gray-600 dark:text-gray-300" }}, "vs previous period")
  ),
  React.createElement("div", {{ className: "mt-4 p-3 bg-green-50 dark:bg-green-900/20 rounded-lg" }},
    React.createElement("p", {{ className: "text-sm text-green-800 dark:text-green-300" }}, "Sales showing strong upward trend with 23% growth over the period")
  )
)'''


def create_metric_card(value: str, label: str, change: str, context: str) -> str:
    """Generate a key metric card with change indicator using React.createElement format."""
    change_color = "green" if change.startswith("+") else "red" if change.startswith("-") else "gray"
    
    return f'''React.createElement(Card, {{ className: "p-6 text-center max-w-xs" }},
  React.createElement("div", {{ className: "pt-6" }},
    React.createElement("div", {{ className: "text-4xl font-bold text-gray-900 dark:text-white" }}, "{value}"),
    React.createElement("p", {{ className: "text-sm text-gray-600 dark:text-gray-300 mt-1" }}, "{label}"),
    React.createElement(Badge, {{ color: "{change_color}", size: "lg", className: "mt-2" }}, "{change}"),
    React.createElement("p", {{ className: "text-xs text-gray-500 dark:text-gray-400 mt-2" }}, "{context}")
  )
)'''


def create_comparison_bar_chart(title: str, insight: str) -> str:
    """Generate a comparison bar chart component using React.createElement format."""
    sample_data = [
        {"category": "Product A", "value": 2400}, 
        {"category": "Product B", "value": 1800}, 
        {"category": "Product C", "value": 3200}, 
        {"category": "Product D", "value": 1600}
    ]
    
    return f'''React.createElement(Card, {{ className: "p-6" }},
  React.createElement("div", {{ className: "flex items-center space-x-2 mb-4" }},
    React.createElement(BarChart3, {{ className: "h-6 w-6 text-blue-600" }}),
    React.createElement("h3", {{ className: "text-lg font-semibold" }}, "{title}")
  ),
  React.createElement(BarChart, {{
    data: {json.dumps(sample_data)},
    index: "category",
    categories: ["value"],
    colors: ["blue"],
    className: "h-48 mt-4",
    showLegend: false,
    showGridLines: true,
    showYAxis: true,
    showXAxis: true
  }}),
  React.createElement("div", {{ className: "mt-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg" }},
    React.createElement("p", {{ className: "text-sm text-blue-800 dark:text-blue-300" }}, "{insight}")
  )
)'''


# Create Chart Generation Agent using authentic ADK patterns
chart_generation_agent = LlmAgent(
    name="chart_generation_agent",
    model="gemini-2.0-flash",
    description="Creates sales trend charts, metric cards, and comparison visualizations using specialized chart tools.",
    instruction="""You are a chart generation specialist.

CRITICAL STOPPING RULE:
- Call ONE tool that matches the request
- Return the JSX result immediately after successful generation
- NEVER call multiple tools for a single request
- STOP after generating one component

TOOL SELECTION (choose EXACTLY ONE):
- Sales/revenue/trends/growth → create_sales_trend_card
- Metrics/KPIs/single values/totals → create_metric_card  
- Comparisons/categories/products → create_comparison_bar_chart

EXECUTION PATTERN:
1. Analyze request to identify ONE primary visualization need
2. Call the appropriate tool ONCE with reasonable defaults
3. Return the generated JSX component immediately
4. STOP - do not generate additional components

EXAMPLE FLOWS:
User: "show sales trends" → call create_sales_trend_card → STOP
User: "revenue metrics" → call create_metric_card → STOP  
User: "compare products" → call create_comparison_bar_chart → STOP

CRITICAL: Never call tools multiple times. One request = One tool call = One component.""",
    tools=[create_sales_trend_card, create_metric_card, create_comparison_bar_chart]
)

# Import other specialized agents
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.geospatial_agent import geospatial_agent
from agents.accessibility_agent import accessibility_agent

# Create Root Orchestrator Agent with Multi-Agent Delegation
root_agent = LlmAgent(
    name="generative_ui_orchestrator",
    model="gemini-2.0-flash", 
    instruction="""You are a UI orchestrator that delegates tasks to specialized agents using transfer_to_agent().

MULTI-AGENT DELEGATION STRATEGY:
1. Analyze business intelligence queries for visualization requirements
2. Delegate to the most appropriate specialized agent using transfer_to_agent()
3. Let sub-agents handle the actual UI component generation
4. Return their output directly to maintain clean delegation

AVAILABLE SPECIALIZED AGENTS:
- chart_generation_agent: Sales trends, metrics, comparisons, business charts
- geospatial_agent: Maps, regional data, location-based visualizations  
- accessibility_agent: WCAG-compliant components, keyboard navigation

DELEGATION RULES:
- Sales, revenue, trends, metrics, KPIs, comparisons → transfer_to_agent(chart_generation_agent)
- Maps, regional, geographic, territory, location → transfer_to_agent(geospatial_agent)
- Accessibility, WCAG, keyboard, screen reader, high-contrast → transfer_to_agent(accessibility_agent)

CRITICAL ORCHESTRATION REQUIREMENTS:
- ALWAYS use transfer_to_agent() for delegation - never do work yourself
- Let sub-agents generate the actual JSX components
- Maintain clean separation of concerns across the multi-agent system
- Trust specialized agents to handle their domain expertise

EXAMPLE MULTI-AGENT FLOW:
User: "show sales trends for Q4"
You: transfer_to_agent(chart_generation_agent) 
chart_generation_agent: [generates sales trend JSX component]
Output: Complete JSX from specialized chart agent""",
    tools=[],  # Root agent has no tools - only delegates
    sub_agents=[chart_generation_agent, geospatial_agent, accessibility_agent]
)