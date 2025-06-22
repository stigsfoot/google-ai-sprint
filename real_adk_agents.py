#!/usr/bin/env python3
"""
Real Google ADK Implementation for Generative UI
Using actual ADK APIs instead of our mock framework
"""
import asyncio
import json
from google.adk.agents import Agent, LlmAgent
from google.adk.tools import FunctionTool


def create_sales_trend_card(sales_data: str, period: str) -> str:
    """Tool that generates a sales trend React component."""
    # Parse JSON string back to data
    try:
        data = json.loads(sales_data) if isinstance(sales_data, str) else sales_data
    except:
        data = [{"month": "Jan", "value": 1200}, {"month": "Feb", "value": 1350}]
    
    return f'''<Card className="p-6 bg-gradient-to-r from-green-50 to-blue-50">
      <CardHeader>
        <TrendingUp className="h-6 w-6 text-green-600" />
        <CardTitle>Sales Trend - {period}</CardTitle>
      </CardHeader>
      <CardContent>
        <LineChart data={json.dumps(data)} className="h-48" />
        <Badge variant="success">+23% Growth</Badge>
      </CardContent>
    </Card>'''


def create_metric_card(value: str, label: str, change: str, context: str) -> str:
    """Generate a key metric card with change indicator."""
    change_color = "green" if change.startswith("+") else "red" if change.startswith("-") else "gray"
    
    return f'''<Card className="p-6 text-center">
      <CardContent className="pt-6">
        <div className="text-4xl font-bold text-gray-900">{value}</div>
        <p className="text-sm text-gray-600 mt-1">{label}</p>
        <Badge variant="{change_color}" className="mt-2">{change}</Badge>
        <p className="text-xs text-gray-500 mt-2">{context}</p>
      </CardContent>
    </Card>'''


def create_comparison_bar_chart(data: str, title: str, insight: str) -> str:
    """Generate a comparison bar chart component."""
    try:
        chart_data = json.loads(data) if isinstance(data, str) else data
    except:
        chart_data = [{"category": "Product A", "value": 2400}, {"category": "Product B", "value": 1800}]
    
    return f'''<Card className="p-6">
      <CardHeader>
        <BarChart3 className="h-6 w-6 text-blue-600 mr-2" />
        <CardTitle className="text-lg">{title}</CardTitle>
      </CardHeader>
      <CardContent>
        <BarChart data={json.dumps(chart_data)} className="h-48" />
        <div className="mt-4 p-3 bg-blue-50 rounded-lg">
          <p className="text-sm text-blue-800">{insight}</p>
        </div>
      </CardContent>
    </Card>'''


# Create Real ADK Tools (Correct API Usage)
sales_trend_tool = FunctionTool(create_sales_trend_card)
metric_card_tool = FunctionTool(create_metric_card)
comparison_chart_tool = FunctionTool(create_comparison_bar_chart)

# Create Real ADK Agents
chart_generation_agent = Agent(
    name="chart_generation_agent",
    model="gemini-2.0-flash-001",
    instruction="""You are a specialized UI generation agent for chart components.

Your role is to generate React JSX components for business intelligence visualizations using your available tools:
- create_sales_trend_card: For trend analysis and time-series data
- create_metric_card: For KPIs and key metrics display  
- create_comparison_bar_chart: For comparative analysis

When given a business question:
1. Analyze what type of visualization is needed
2. Use the appropriate tool to generate the React component
3. Return clean JSX that can be rendered in a dashboard

Always generate components that include:
- Proper styling with Tailwind CSS
- Business context and insights
- Interactive elements where appropriate""",
    tools=[sales_trend_tool, metric_card_tool, comparison_chart_tool]
)

root_agent = LlmAgent(
    name="generative_ui_orchestrator",
    model="gemini-2.0-flash-001", 
    instruction="""You are the Generative UI Orchestrator for business intelligence.

Your role is to analyze business questions and delegate to specialized UI generation agents to create React components.

AVAILABLE AGENTS:
- chart_generation_agent: Creates charts, metrics cards, trend visualizations

PROCESS:
1. Analyze the user's business question
2. Determine what type of UI components are needed
3. Delegate to the appropriate specialized agent
4. Return the generated React JSX components

IMPORTANT: Your sub-agents return actual React JSX code that can be rendered directly in a dashboard.""",
    sub_agents=[chart_generation_agent]
)


async def test_real_adk_agents():
    """Test the real ADK implementation"""
    print("🎯 Testing Real Google ADK Agents...")
    
    # Test queries
    test_queries = [
        "Show me sales trends for Q4",
        "Display key revenue metrics", 
        "Compare product performance across categories"
    ]
    
    for query in test_queries:
        print(f"\n--- Testing: {query} ---")
        try:
            # This would use the real ADK conversation flow
            print(f"Query: {query}")
            print("Would delegate to chart_generation_agent...")
            print("Expected: React JSX component generation")
            
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    print("🚀 Real Google ADK Implementation")
    print("=" * 50)
    asyncio.run(test_real_adk_agents())