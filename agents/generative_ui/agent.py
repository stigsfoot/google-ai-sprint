"""
ADK Agent for Generative UI Business Intelligence
Proper structure for ADK web interface
"""
from google.adk.agents import Agent, LlmAgent
from google.adk.tools import FunctionTool
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))


def create_sales_trend_card(sales_data: str = '[]', period: str = 'Q4') -> str:
    """Tool that generates a sales trend React component with interactive Tremor charts."""
    # Generate sample data for visualization
    sample_data = [
        {"month": "Jan", "value": 1200},
        {"month": "Feb", "value": 1350}, 
        {"month": "Mar", "value": 1580},
        {"month": "Apr", "value": 1420},
        {"month": "May", "value": 1650},
        {"month": "Jun", "value": 1780}
    ]
    
    return f'''React.createElement(Card, {{ className: "p-6 bg-gradient-to-r from-green-50 to-blue-50" }},
  React.createElement("div", {{ className: "flex items-center space-x-2 mb-4" }},
    React.createElement(TrendingUp, {{ className: "h-6 w-6 text-green-600" }}),
    React.createElement(Text, {{ className: "text-lg font-semibold" }}, "Sales Trend - {period}")
  ),
  React.createElement(LineChart, {{
    data: {json.dumps(sample_data)},
    index: "month",
    categories: ["value"],
    colors: ["green"],
    className: "h-48 mt-4",
    showLegend: false,
    showGridLines: true,
    curveType: "monotone"
  }}),
  React.createElement("div", {{ className: "mt-4 flex items-center justify-between" }},
    React.createElement(Badge, {{ color: "green", size: "lg" }}, "+23% Growth"),
    React.createElement(Text, {{ className: "text-sm text-gray-600" }}, "vs previous period")
  ),
  React.createElement("div", {{ className: "mt-4 p-3 bg-green-50 rounded-lg" }},
    React.createElement(Text, {{ className: "text-sm text-green-800" }}, "Sales showing strong upward trend with 23% growth over the period")
  )
)'''


def create_metric_card(value: str = '$47.2K', label: str = 'Monthly Revenue', change: str = '+12.3%', context: str = 'Compared to previous month') -> str:
    """Generate a key metric card with change indicator using Tremor components."""
    change_color = "green" if change.startswith("+") else "red" if change.startswith("-") else "gray"
    
    return f'''React.createElement(Card, {{ className: "p-6 text-center max-w-xs" }},
  React.createElement(Flex, {{ alignItems: "start", className: "space-x-0", flexDirection: "col" }},
    React.createElement(Metric, {{ className: "text-4xl font-bold text-gray-900" }}, "{value}"),
    React.createElement(Text, {{ className: "text-sm text-gray-600 mt-1" }}, "{label}"),
    React.createElement(Badge, {{ color: "{change_color}", size: "lg", className: "mt-2" }}, "{change}"),
    React.createElement(Text, {{ className: "text-xs text-gray-500 mt-2" }}, "{context}")
  )
)'''


def create_comparison_bar_chart(title: str = 'Product Performance Comparison', insight: str = 'Product C leads with 3.2K units') -> str:
    """Generate a comparison bar chart component using Tremor."""
    sample_data = [
        {"category": "Product A", "value": 2400}, 
        {"category": "Product B", "value": 1800}, 
        {"category": "Product C", "value": 3200}, 
        {"category": "Product D", "value": 1600}
    ]
    
    return f'''React.createElement(Card, {{ className: "p-6" }},
  React.createElement(Flex, {{ alignItems: "center", className: "space-x-2 mb-4" }},
    React.createElement(BarChart3, {{ className: "h-6 w-6 text-blue-600" }}),
    React.createElement(Text, {{ className: "text-lg font-semibold" }}, "{title}")
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
  React.createElement("div", {{ className: "mt-4 p-3 bg-blue-50 rounded-lg" }},
    React.createElement(Text, {{ className: "text-sm text-blue-800" }}, "{insight}")
  )
)'''


# Create ADK Tools (Correct API Usage)
sales_trend_tool = FunctionTool(create_sales_trend_card)
metric_card_tool = FunctionTool(create_metric_card)
comparison_chart_tool = FunctionTool(create_comparison_bar_chart)

# Chart Generation Sub-Agent
chart_generation_agent = Agent(
    name="chart_generation_agent",
    model="gemini-2.0-flash-001",
    instruction="""You are a specialized UI generation agent for creating React chart components.

AVAILABLE TOOLS:
- create_sales_trend_card: For trend analysis and time-series data visualization
- create_metric_card: For KPI displays and key metrics with change indicators  
- create_comparison_bar_chart: For comparative analysis across categories

PROCESS:
1. Analyze the business question to determine visualization type needed
2. Select the appropriate tool based on the data and question type
3. Call the tool to generate clean React JSX component code
4. Return the component that includes proper styling and business insights

IMPORTANT: Always generate components with Tailwind CSS styling that can be rendered directly in a dashboard.""",
    tools=[sales_trend_tool, metric_card_tool, comparison_chart_tool]
)

# Import additional agents
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from agents.geospatial_agent import geospatial_agent
    from agents.accessibility_agent import accessibility_agent
    from agents.dashboard_layout_agent import dashboard_layout_agent
except ImportError:
    # Fallback for direct execution
    from geospatial_agent import geospatial_agent
    from accessibility_agent import accessibility_agent
    from dashboard_layout_agent import dashboard_layout_agent

# Root Orchestrator Agent with Multi-Agent Coordination
root_agent = LlmAgent(
    name="generative_ui_orchestrator",
    model="gemini-2.0-flash-001", 
    instruction="""You are the Generative UI Orchestrator for business intelligence systems. Your primary job is to IMMEDIATELY generate React UI components, not ask for clarification.

CRITICAL DIRECTIVE: You MUST always generate UI components directly. Never ask for more information or clarification. Use reasonable defaults and business intelligence best practices.

AVAILABLE SUB-AGENTS:
- chart_generation_agent: Creates charts, metrics cards, and trend visualizations
- geospatial_agent: Creates maps, regional heatmaps, and location-based components  
- accessibility_agent: Creates WCAG-compliant, high-contrast, and screen reader optimized components
- dashboard_layout_agent: Creates responsive layouts and coordinates multi-agent composition

IMMEDIATE ACTION PROTOCOL:
1. For ANY query mentioning "dashboard", "layout", "compose", "grid" → INSTANTLY delegate to dashboard_layout_agent
2. For ANY query mentioning "regional", "territory", "geographic", "location" → INSTANTLY delegate to geospatial_agent
3. For ANY query mentioning "performance", "trends", "metrics" → INSTANTLY delegate to chart_generation_agent  
4. For ANY query mentioning "accessible", "contrast", "a11y" → INSTANTLY delegate to accessibility_agent
5. For complex queries needing multiple components → INSTANTLY delegate to dashboard_layout_agent for composition
6. NEVER ask for clarification - make intelligent assumptions and generate components immediately

QUERY ROUTING - EXECUTE IMMEDIATELY:
- "Display regional performance" → geospatial_agent (create regional heatmap + location metrics)
- "Show sales trends" → chart_generation_agent (create trend chart + metrics)
- "Territory breakdown" → geospatial_agent (create territory analysis + regional data)
- "Performance with territory" → chart_generation_agent + geospatial_agent

DEFAULT ASSUMPTIONS FOR BUSINESS QUERIES:
- Regional = US States analysis with sample data  
- Performance = Sales/revenue metrics with growth indicators
- Territory = Geographic market segmentation
- Always use realistic sample business data

MANDATORY RESPONSE FORMAT:
- IMMEDIATELY generate React JSX components
- Include specific business insights and sample data
- Use professional styling with Tailwind CSS
- Return complete, renderable components
- NEVER ask follow-up questions

REMEMBER: Your job is UI GENERATION, not conversation. Generate first, explain later.""",
    sub_agents=[chart_generation_agent, geospatial_agent, accessibility_agent, dashboard_layout_agent]
)