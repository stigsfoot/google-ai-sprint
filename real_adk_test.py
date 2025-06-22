#!/usr/bin/env python3
"""
Test Real Google ADK Implementation
Replace our mock framework with actual ADK
"""
import asyncio
from google.adk.agents import Agent, LlmAgent
from google.adk.tools import FunctionTool


def create_sales_trend_card(sales_data: list, period: str) -> str:
    """Tool that generates a sales trend React component."""
    return f'''
    <Card className="p-6 bg-gradient-to-r from-green-50 to-blue-50">
      <CardHeader>
        <TrendingUp className="h-6 w-6 text-green-600" />
        <CardTitle>Sales Trend - {period}</CardTitle>
      </CardHeader>
      <CardContent>
        <LineChart data={sales_data} className="h-48" />
        <Badge variant="success">+23% Growth</Badge>
      </CardContent>
    </Card>
    '''


def create_metric_card(value: str, label: str, change: str, context: str) -> str:
    """Generate a key metric card with change indicator."""
    return f'''
    <Card className="p-6 text-center">
      <CardContent className="pt-6">
        <div className="text-4xl font-bold text-gray-900">{value}</div>
        <p className="text-sm text-gray-600 mt-1">{label}</p>
        <Badge variant="success" className="mt-2">{change}</Badge>
        <p className="text-xs text-gray-500 mt-2">{context}</p>
      </CardContent>
    </Card>
    '''


# Create Real ADK Agent
chart_generation_agent = Agent(
    name="chart_generation_agent",
    model="gemini-2.0-flash-001",
    instruction="Generate chart components using available UI tools based on data analysis needs. Use the provided tools to create React JSX components for business intelligence visualizations.",
    tools=[FunctionTool(create_sales_trend_card), FunctionTool(create_metric_card)]
)

# Create Root Agent with Sub-Agents
root_agent = LlmAgent(
    name="generative_ui_orchestrator",
    model="gemini-2.0-flash-001",
    instruction="""
    You are the Generative UI Orchestrator for business intelligence.
    
    Your role is to analyze business questions and delegate to specialized UI generation agents:
    
    AVAILABLE UI GENERATION AGENTS:
    - chart_generation_agent: Creates charts, metrics cards, trend visualizations
    
    DELEGATION STRATEGY:
    1. Analyze the business question and required visualization types
    2. Delegate to the appropriate specialized UI agent(s)
    3. Each agent uses their UI component tools to generate React code
    4. Return the generated components for dashboard rendering
    
    CRITICAL: Each sub-agent returns actual React JSX code that can be rendered directly.
    """,
    sub_agents=[chart_generation_agent]
)


async def test_real_adk():
    """Test the real Google ADK implementation"""
    print("🎯 Testing Real Google ADK...")
    
    try:
        # Test direct tool call
        print("\n--- Test 1: Direct Tool Call ---")
        result = await chart_generation_agent.call_function_tool(
            "create_sales_trend_card",
            sales_data=[{"month": "Jan", "value": 1200}, {"month": "Feb", "value": 1350}],
            period="Q1"
        )
        print(f"Tool Result: {result}")
        
        # Test agent interaction
        print("\n--- Test 2: Agent Query ---")
        response = await root_agent.run_interactive_session("Show me sales trends for Q4")
        print(f"Agent Response: {response}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("🚀 Real Google ADK Test")
    print("=" * 40)
    asyncio.run(test_real_adk())