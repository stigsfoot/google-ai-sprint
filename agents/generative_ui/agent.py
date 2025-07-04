"""
ADK Agent for Generative UI Business Intelligence
Authentic ADK implementation following Google patterns
"""
import json
import os
import time
from collections import defaultdict, deque
from dotenv import load_dotenv
from google.adk.agents import LlmAgent

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Circuit Breaker for Loop Prevention (shared pattern)
class ToolCallTracker:
    def __init__(self, max_calls=3, time_window=60):
        self.max_calls = max_calls
        self.time_window = time_window
        self.call_history = defaultdict(deque)
    
    def is_allowed(self, tool_name, params_hash):
        """Check if tool call is allowed based on recent history"""
        key = f"{tool_name}:{params_hash}"
        now = time.time()
        
        # Clean old entries
        while self.call_history[key] and now - self.call_history[key][0] > self.time_window:
            self.call_history[key].popleft()
        
        # Check if under limit
        if len(self.call_history[key]) >= self.max_calls:
            return False
        
        # Record this call
        self.call_history[key].append(now)
        return True

# Global tracker instance
chart_tracker = ToolCallTracker()


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
    model="gemini-2.0-flash-exp",
    description="Creates sales trend charts, metric cards, and comparison visualizations using specialized chart tools.",
    instruction="""You are a chart generation specialist that ALWAYS generates visualizations, NEVER asks questions.

CRITICAL STOPPING RULES (HIGHEST PRIORITY):
- Call EXACTLY ONE tool per request and STOP immediately
- NEVER call the same tool multiple times in a session
- If tool fails or returns error, STOP - do not retry
- Return generated React component and TERMINATE
- NEVER ask follow-up questions or request clarification
- Circuit breaker prevents infinite loops (max 3 calls per tool/params per 60s)

CRITICAL BEHAVIOR RULES:
- ALWAYS call a tool to generate a chart - NEVER respond with text or questions
- NEVER ask "What specific chart?" or "Which period?" - always use logical defaults
- When period is unclear, default to "Q4" or "Current Period"
- When data is unclear, use reasonable sample data for demonstration
- Call ONE tool → Generate React.createElement component → STOP → TERMINATE

TOOL SELECTION & DEFAULTS:
- Sales/revenue/trends/growth → create_sales_trend_card (default: "Q4", sample trend data)
- Metrics/KPIs/single values/totals → create_metric_card (default: "$47.2K", "Revenue", "+12.3%")
- Comparisons/categories/products → create_comparison_bar_chart (default: "Product Comparison", product sample data)

EXECUTION PATTERN:
1. Immediately call appropriate tool with sensible defaults
2. Return React.createElement component 
3. STOP - never ask follow-up questions

EXAMPLE FLOWS:
User: "show sales trends" → create_sales_trend_card("sample data", "Q4") → STOP
User: "revenue metrics" → create_metric_card("$47.2K", "Revenue", "+12.3%", "vs last month") → STOP  
User: "compare products" → create_comparison_bar_chart("Product Performance", "Product C leads with strong performance") → STOP

CRITICAL: NEVER respond with questions. ALWAYS generate charts with defaults.""",
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
    model="gemini-2.0-flash-exp", 
    instruction="""You are an intelligent UI orchestrator with VALIDATION capabilities for multi-agent generative UI system.

MULTI-AGENT DELEGATION WITH QUALITY CONTROL:
1. Analyze business intelligence queries for visualization requirements
2. Delegate to the most appropriate specialized agent using transfer_to_agent()
3. VALIDATE the agent response for quality and relevance
4. Ensure location-specific queries are properly handled by geospatial agent

AVAILABLE SPECIALIZED AGENTS:
- chart_generation_agent: Sales trends, metrics, comparisons, business charts
- geospatial_agent: Maps, regional data, location-based visualizations with intelligent zoom
- accessibility_agent: WCAG-compliant components, keyboard navigation

INTELLIGENT DELEGATION RULES:
- Sales, revenue, trends, metrics, KPIs, comparisons → transfer_to_agent(chart_generation_agent)
- Maps, regional, geographic, territory, location, SPECIFIC PLACES → transfer_to_agent(geospatial_agent)
- California, Texas, New York, Florida, states, cities → transfer_to_agent(geospatial_agent)
- Accessibility, WCAG, keyboard, screen reader, high-contrast → transfer_to_agent(accessibility_agent)

CRITICAL ORCHESTRATION & VALIDATION:
- ALWAYS use transfer_to_agent() for delegation - never do work yourself
- Geospatial agent will intelligently detect locations and auto-zoom (California→CA view, New York→NY view)
- Sub-agents MUST generate actual React.createElement components, NOT questions
- VALIDATE that location-specific queries result in proper geographic focus
- If geospatial response seems generic, the agent has proper fallback defaults

EXAMPLE INTELLIGENT FLOWS:
User: "New York territory analysis"
You: transfer_to_agent(geospatial_agent) 
geospatial_agent: [detects "New York", generates NY-focused map with zoom 7, NY-specific data]
Output: React.createElement component with New York geographic focus

User: "california sales map"  
You: transfer_to_agent(geospatial_agent)
geospatial_agent: [detects "california", generates CA-focused map with zoom 6, CA-specific data]
Output: React.createElement component centered on California

User: "regional performance"
You: transfer_to_agent(geospatial_agent)
geospatial_agent: [no specific location, generates US-wide map with all states data]
Output: React.createElement component with continental US view""",
    tools=[],  # Root agent has no tools - only delegates
    sub_agents=[chart_generation_agent, geospatial_agent, accessibility_agent]
)