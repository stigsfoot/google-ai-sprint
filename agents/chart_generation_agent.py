"""
Chart Generation Agent - Specialized UI generation for business intelligence charts
Generates trend charts, metric cards, and comparison visualizations
Authentic ADK implementation following Google patterns
"""
import json
import os
import time
from collections import defaultdict, deque
from dotenv import load_dotenv
from google.adk.agents import LlmAgent

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# Circuit Breaker for Loop Prevention - ULTRA STRICT
class ToolCallTracker:
    def __init__(self, max_calls=1, time_window=60):
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
    
    def get_remaining_calls(self, tool_name, params_hash):
        """Get remaining allowed calls for this tool/params combo"""
        key = f"{tool_name}:{params_hash}"
        now = time.time()
        
        # Clean old entries
        while self.call_history[key] and now - self.call_history[key][0] > self.time_window:
            self.call_history[key].popleft()
        
        return max(0, self.max_calls - len(self.call_history[key]))

# Global tracker instance
chart_tracker = ToolCallTracker()


def create_sales_trend_card(sales_data: str, period: str) -> str:
    """Generate a sales trend React component with clean formatting and proper data structure.
    
    Args:
        sales_data: Description of sales data to visualize
        period: Time period for the trend analysis (e.g., "Q4", "YTD", "Monthly")
    """
    
    # CIRCUIT BREAKER: Prevent infinite loops with identical parameters
    params_hash = hash(f"{sales_data}:{period}")
    if not chart_tracker.is_allowed("create_sales_trend_card", params_hash):
        remaining = chart_tracker.get_remaining_calls("create_sales_trend_card", params_hash)
        return f'''React.createElement(Card, {{ className: "p-6 border-l-4 border-l-red-500" }},
  React.createElement("div", {{ className: "text-center" }},
    React.createElement("h3", {{ className: "text-lg font-semibold text-red-600" }}, "CIRCUIT BREAKER ACTIVATED - STOP"),
    React.createElement("p", {{ className: "text-sm text-red-500 mt-2" }}, "Tool call limit reached. Agent must STOP immediately."),
    React.createElement("p", {{ className: "text-xs text-gray-500 mt-1" }}, "This is a valid response - do not retry. Remaining calls: {remaining}")
  )
)'''
    
    # Generate sample data for visualization
    sample_data = [
        {"month": "Jan", "value": 1200},
        {"month": "Feb", "value": 1350}, 
        {"month": "Mar", "value": 1580},
        {"month": "Apr", "value": 1420},
        {"month": "May", "value": 1650},
        {"month": "Jun", "value": 1780}
    ]
    
    # Clean period formatting to avoid React code contamination
    clean_period = period.replace("React.createElement", "").replace("<", "").replace(">", "").strip()
    
    return f'''React.createElement(Card, {{ className: "p-6 bg-gradient-to-r from-green-50 to-blue-50 dark:from-green-900/20 dark:to-blue-900/20" }},
  React.createElement("div", {{ className: "flex items-center space-x-2 mb-4" }},
    React.createElement("div", {{ className: "w-6 h-6 text-green-600" }}, "📈"),
    React.createElement("h3", {{ className: "text-lg font-semibold" }}, "Sales Trend - {clean_period}")
  ),
  React.createElement("div", {{ className: "mt-4 h-64 bg-white rounded-lg p-4" }},
    React.createElement("div", {{ className: "w-full h-full relative" }},
      React.createElement("div", {{ className: "absolute inset-0 flex items-end justify-around" }},
        React.createElement("div", {{ className: "bg-green-500 w-8 opacity-80", style: {{ height: "40%" }} }}),
        React.createElement("div", {{ className: "bg-green-500 w-8 opacity-80", style: {{ height: "50%" }} }}),
        React.createElement("div", {{ className: "bg-green-500 w-8 opacity-80", style: {{ height: "70%" }} }}),
        React.createElement("div", {{ className: "bg-green-500 w-8 opacity-80", style: {{ height: "60%" }} }}),
        React.createElement("div", {{ className: "bg-green-500 w-8 opacity-80", style: {{ height: "75%" }} }}),
        React.createElement("div", {{ className: "bg-green-500 w-8 opacity-80", style: {{ height: "85%" }} }})
      ),
      React.createElement("div", {{ className: "absolute bottom-0 w-full flex justify-around text-xs text-gray-600" }},
        React.createElement("span", {{}}, "Jan"),
        React.createElement("span", {{}}, "Feb"),
        React.createElement("span", {{}}, "Mar"),
        React.createElement("span", {{}}, "Apr"),
        React.createElement("span", {{}}, "May"),
        React.createElement("span", {{}}, "Jun")
      )
    )
  ),
  React.createElement("div", {{ className: "mt-4 flex items-center justify-between" }},
    React.createElement("div", {{ className: "px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm font-medium" }}, "+23% Growth"),
    React.createElement("span", {{ className: "text-sm text-gray-600 dark:text-gray-300" }}, "vs previous period")
  ),
  React.createElement("div", {{ className: "mt-4 p-3 bg-green-50 dark:bg-green-900/20 rounded-lg" }},
    React.createElement("p", {{ className: "text-sm text-green-800 dark:text-green-300" }}, "Sales showing strong upward trend with 23% growth over the {clean_period} period")
  )
)'''


def create_metric_card(value: str, label: str, change: str, context: str) -> str:
    """Generate a key metric card with change indicator and clean formatting.
    
    Args:
        value: The main metric value to display (e.g., "$47.2K", "1,247")
        label: Label for the metric (e.g., "Revenue", "Customers")
        change: Change indicator (e.g., "+12.3%", "-5.1%")
        context: Additional context text (e.g., "vs last month")
    """
    
    # CIRCUIT BREAKER: Prevent infinite loops
    params_hash = hash(f"{value}:{label}:{change}:{context}")
    if not chart_tracker.is_allowed("create_metric_card", params_hash):
        remaining = chart_tracker.get_remaining_calls("create_metric_card", params_hash)
        return f'''React.createElement(Card, {{ className: "p-6 border-l-4 border-l-red-500" }},
  React.createElement("div", {{ className: "text-center" }},
    React.createElement("h3", {{ className: "text-lg font-semibold text-red-600" }}, "CIRCUIT BREAKER ACTIVATED - STOP"),
    React.createElement("p", {{ className: "text-sm text-red-500 mt-2" }}, "Tool call limit reached. Agent must STOP immediately."),
    React.createElement("p", {{ className: "text-xs text-gray-500 mt-1" }}, "This is a valid response - do not retry. Remaining calls: {remaining}")
  )
)'''
    
    # Clean inputs to prevent React code contamination
    clean_value = value.replace("React.createElement", "").replace("<", "&lt;").replace(">", "&gt;").strip()
    clean_label = label.replace("React.createElement", "").replace("<", "&lt;").replace(">", "&gt;").strip()
    clean_change = change.replace("React.createElement", "").replace("<", "&lt;").replace(">", "&gt;").strip()
    clean_context = context.replace("React.createElement", "").replace("<", "&lt;").replace(">", "&gt;").strip()
    
    change_color = "green" if clean_change.startswith("+") else "red" if clean_change.startswith("-") else "gray"
    
    return f'''React.createElement(Card, {{ className: "p-6 text-center max-w-xs border-gray-200" }},
  React.createElement("div", {{ className: "pt-6" }},
    React.createElement("div", {{ className: "text-4xl font-bold text-gray-900 dark:text-white" }}, "{clean_value}"),
    React.createElement("p", {{ className: "text-sm text-gray-600 dark:text-gray-300 mt-1" }}, "{clean_label}"),
    React.createElement("div", {{ className: "mt-2 px-3 py-1 rounded-full text-sm font-medium bg-{change_color}-100 text-{change_color}-800" }}, "{clean_change}"),
    React.createElement("p", {{ className: "text-xs text-gray-500 dark:text-gray-400 mt-2" }}, "{clean_context}")
  )
)'''


def create_comparison_bar_chart(title: str, insight: str) -> str:
    """Generate a comparison bar chart component with clean formatting.
    
    Args:
        title: Chart title (e.g., "Product Performance", "Regional Comparison")
        insight: Descriptive insight about the data shown
    """
    
    # CIRCUIT BREAKER: Prevent infinite loops
    params_hash = hash(f"{title}:{insight}")
    if not chart_tracker.is_allowed("create_comparison_bar_chart", params_hash):
        remaining = chart_tracker.get_remaining_calls("create_comparison_bar_chart", params_hash)
        return f'''React.createElement(Card, {{ className: "p-6 border-l-4 border-l-red-500" }},
  React.createElement("div", {{ className: "text-center" }},
    React.createElement("h3", {{ className: "text-lg font-semibold text-red-600" }}, "CIRCUIT BREAKER ACTIVATED - STOP"),
    React.createElement("p", {{ className: "text-sm text-red-500 mt-2" }}, "Tool call limit reached. Agent must STOP immediately."),
    React.createElement("p", {{ className: "text-xs text-gray-500 mt-1" }}, "This is a valid response - do not retry. Remaining calls: {remaining}")
  )
)'''
    
    # Clean inputs to prevent React code contamination
    clean_title = title.replace("React.createElement", "").replace("<", "&lt;").replace(">", "&gt;").strip()
    clean_insight = insight.replace("React.createElement", "").replace("<", "&lt;").replace(">", "&gt;").strip()
    
    sample_data = [
        {"category": "Product A", "value": 2400}, 
        {"category": "Product B", "value": 1800}, 
        {"category": "Product C", "value": 3200}, 
        {"category": "Product D", "value": 1600}
    ]
    
    return f'''React.createElement(Card, {{ className: "p-6 border-gray-200" }},
  React.createElement("div", {{ className: "flex items-center space-x-2 mb-4" }},
    React.createElement("div", {{ className: "w-6 h-6 text-blue-600" }}, "📊"),
    React.createElement("h3", {{ className: "text-lg font-semibold" }}, "{clean_title}")
  ),
  React.createElement("div", {{ className: "mt-4 h-48 bg-white rounded-lg p-4" }},
    React.createElement("div", {{ className: "w-full h-full relative" }},
      React.createElement("div", {{ className: "absolute inset-0 flex items-end justify-around" }},
        React.createElement("div", {{ className: "bg-blue-500 w-12 opacity-80 flex flex-col items-center", style: {{ height: "60%" }} }},
          React.createElement("div", {{ className: "text-xs text-white mt-1" }}, "2.4K")
        ),
        React.createElement("div", {{ className: "bg-blue-500 w-12 opacity-80 flex flex-col items-center", style: {{ height: "45%" }} }},
          React.createElement("div", {{ className: "text-xs text-white mt-1" }}, "1.8K")
        ),
        React.createElement("div", {{ className: "bg-blue-500 w-12 opacity-80 flex flex-col items-center", style: {{ height: "80%" }} }},
          React.createElement("div", {{ className: "text-xs text-white mt-1" }}, "3.2K")
        ),
        React.createElement("div", {{ className: "bg-blue-500 w-12 opacity-80 flex flex-col items-center", style: {{ height: "40%" }} }},
          React.createElement("div", {{ className: "text-xs text-white mt-1" }}, "1.6K")
        )
      ),
      React.createElement("div", {{ className: "absolute bottom-0 w-full flex justify-around text-xs text-gray-600" }},
        React.createElement("span", {{}}, "Product A"),
        React.createElement("span", {{}}, "Product B"),
        React.createElement("span", {{}}, "Product C"),
        React.createElement("span", {{}}, "Product D")
      )
    )
  ),
  React.createElement("div", {{ className: "mt-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg" }},
    React.createElement("p", {{ className: "text-sm text-blue-800 dark:text-blue-300" }}, "{clean_insight}")
  )
)'''


# Create Chart Generation Agent using authentic ADK patterns
chart_generation_agent = LlmAgent(
    name="chart_generation_agent",
    model="gemini-2.5-flash",
    description="Creates sales trend charts, metric cards, and comparison visualizations using specialized chart tools.",
    instruction="""You are a chart generation specialist that ALWAYS generates visualizations, NEVER asks questions.

ULTRA-CRITICAL STOPPING RULES (ENFORCE IMMEDIATELY):
- Call EXACTLY ONE tool per request and STOP immediately - NO EXCEPTIONS
- NEVER call the same tool multiple times in ANY session or conversation
- If ANY tool fails or returns error, STOP - do not retry or call another tool  
- After generating React component, IMMEDIATELY TERMINATE - do not continue
- NEVER ask follow-up questions, clarifications, or provide explanations
- NEVER retry or loop - ONE TOOL CALL ONLY, then STOP
- Circuit breaker enforced: max 1 call per tool/params combination per 60 seconds
- If you have already called a tool once, DO NOT call any tool again
- TERMINATE immediately after receiving any tool response

MANDATORY BEHAVIOR PATTERNS:
- ALWAYS call exactly ONE tool to generate a chart
- NEVER ask "What specific chart?", "Which period?", or ANY questions
- When input is unclear, ALWAYS use logical defaults without asking
- Default period: "Q4" or "Current Period" 
- Default data: use reasonable sample data for demonstration
- Pattern: Call ONE tool → Get React.createElement component → Return the exact React component code → STOP
- AFTER tool call completes, respond with the React component code returned by the tool

TOOL SELECTION WITH DEFAULTS (USE IMMEDIATELY):
- "sales trends", "revenue trends", "growth" → create_sales_trend_card("sample sales data", "Q4")
- "metrics", "KPIs", "total", "revenue", "performance" → create_metric_card("$47.2K", "Revenue", "+12.3%", "vs last month")
- "compare", "comparison", "products", "categories" → create_comparison_bar_chart("Product Performance", "Product C leads with strong performance")

LOOP PREVENTION ENFORCEMENT:
- If you are called again with similar query, use circuit breaker response
- If tool returns rate limit, STOP immediately - do not try another tool
- If ANY error occurs, STOP immediately - do not retry
- Maximum one tool invocation per agent execution

EXAMPLE EXECUTION (FOLLOW EXACTLY):
User: "show sales trends" → call create_sales_trend_card("sample sales data", "Q4") → tool returns React component → respond with the EXACT React component code → STOP
User: "revenue metrics" → call create_metric_card("$47.2K", "Revenue", "+12.3%", "vs last month") → tool returns React component → respond with the EXACT React component code → STOP
User: "compare products" → call create_comparison_bar_chart("Product Performance", "Product C leads with strong performance") → tool returns React component → respond with the EXACT React component code → STOP

ABSOLUTE RULE: ONE tool call → Wait for React component response → Respond with the EXACT React component code → STOP. No loops, no questions, no retries.""",
    tools=[create_sales_trend_card, create_metric_card, create_comparison_bar_chart]
)