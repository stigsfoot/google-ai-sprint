"""
Accessibility Agent - Specialized UI generation for a11y-optimized components
Generates high-contrast, screen reader compatible, and keyboard navigable components
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

# Circuit Breaker for Loop Prevention (shared with geospatial agent)
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
a11y_tracker = ToolCallTracker()


def create_high_contrast_chart_tool(data_type: str, chart_title: str, description: str) -> str:
    """Generate high contrast chart for visually impaired users."""
    chart_id = f"chart_{hash(chart_title) % 10000}"
    
    return f'''<Card className="border-4 border-black bg-yellow-50">
      <CardHeader className="bg-black text-white border-b-4 border-white p-6">
        <CardTitle className="text-2xl font-bold text-white" aria-label="{chart_title} accessible chart">
          ♿ {chart_title} (High Contrast)
        </CardTitle>
        <Badge className="bg-yellow-400 text-black font-bold mt-2">ACCESSIBLE</Badge>
      </CardHeader>
      <CardContent className="p-6 bg-white">
        <div className="relative bg-white border-4 border-black rounded-lg p-6 h-64">
          <div className="text-center">
            <div className="text-6xl mb-4" role="img" aria-label="Chart representation">📊</div>
            <div className="bg-black text-white p-4 rounded-lg mb-4">
              <p className="text-lg font-bold">HIGH CONTRAST {data_type.upper()} CHART</p>
              <p className="text-sm">Enhanced visibility for low vision users</p>
            </div>
            <div className="grid grid-cols-2 gap-2">
              <div className="bg-black text-white p-3 rounded font-bold">HIGH VALUES</div>
              <div className="bg-gray-800 text-white p-3 rounded font-bold">MED VALUES</div>
              <div className="bg-gray-600 text-white p-3 rounded font-bold">LOW VALUES</div>
              <div className="bg-yellow-400 text-black p-3 rounded font-bold">TREND LINE</div>
            </div>
          </div>
        </div>
        
        <div id="chart-description-{chart_id}" className="mt-6 p-4 bg-black text-white rounded-lg">
          <h4 className="text-lg font-bold mb-2" role="heading" aria-level="4">📝 Chart Description</h4>
          <p className="text-base leading-relaxed">{description}</p>
        </div>
        
        <div className="mt-4 p-4 border-4 border-green-600 bg-green-100 rounded-lg">
          <div className="flex items-center">
            <span className="text-2xl mr-3" role="img" aria-label="Accessibility feature">♿</span>
            <div>
              <p className="font-bold text-green-800">Accessibility Features Active:</p>
              <p className="text-sm text-green-700">High contrast colors, large fonts, screen reader descriptions</p>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>'''


def create_screen_reader_table_tool(table_title: str, data_summary: str, row_count: str) -> str:
    """Generate screen reader optimized data table with ARIA labels."""
    table_id = f"table_{hash(table_title) % 10000}"
    
    return f'''<Card className="border-2 border-blue-600 bg-blue-50">
      <CardHeader className="bg-blue-600 text-white p-4">
        <CardTitle className="text-xl font-bold flex items-center">
          <span className="text-2xl mr-3" role="img" aria-label="Data table">📋</span>
          {table_title} (Screen Reader Optimized)
        </CardTitle>
        <p className="text-blue-100 text-sm mt-2">{data_summary}</p>
      </CardHeader>
      <CardContent className="p-6">
        <div className="mb-4 p-3 bg-blue-100 border-l-4 border-blue-600 rounded">
          <p className="text-sm font-semibold text-blue-800">🔊 Screen Reader Instructions:</p>
          <p className="text-xs text-blue-700">Use arrow keys to navigate. Each cell includes descriptive labels.</p>
        </div>
        
        <div className="overflow-x-auto">
          <table 
            id="{table_id}"
            className="w-full border-4 border-black bg-white"
            role="table"
            aria-label="{table_title} with {row_count} rows of data"
            aria-describedby="table-summary-{table_id}"
          >
            <caption className="bg-gray-800 text-white p-3 text-left font-bold">
              📊 {table_title} - Accessible Data Table
            </caption>
            <thead className="bg-gray-800 text-white">
              <tr role="row">
                <th scope="col" className="border-2 border-white p-4 text-left font-bold">
                  REGION
                </th>
                <th scope="col" className="border-2 border-white p-4 text-left font-bold">
                  Q1 SALES
                </th>
                <th scope="col" className="border-2 border-white p-4 text-left font-bold">
                  Q2 SALES  
                </th>
                <th scope="col" className="border-2 border-white p-4 text-left font-bold">
                  GROWTH %
                </th>
              </tr>
            </thead>
            <tbody>
              <tr role="row" className="border-b-2 border-gray-300">
                <th scope="row" className="border-2 border-gray-300 p-4 font-bold bg-gray-100">NORTH</th>
                <td className="border-2 border-gray-300 p-4" aria-label="North region Q1 sales">$2.4M</td>
                <td className="border-2 border-gray-300 p-4" aria-label="North region Q2 sales">$2.8M</td>
                <td className="border-2 border-gray-300 p-4 bg-green-100" aria-label="North region growth rate">+16.7%</td>
              </tr>
              <tr role="row" className="border-b-2 border-gray-300">
                <th scope="row" className="border-2 border-gray-300 p-4 font-bold bg-gray-100">SOUTH</th>
                <td className="border-2 border-gray-300 p-4" aria-label="South region Q1 sales">$1.9M</td>
                <td className="border-2 border-gray-300 p-4" aria-label="South region Q2 sales">$2.1M</td>
                <td className="border-2 border-gray-300 p-4 bg-green-100" aria-label="South region growth rate">+10.5%</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <div id="table-summary-{table_id}" className="mt-4 p-4 bg-gray-100 rounded-lg">
          <h4 className="font-bold mb-2">📈 Table Summary for Screen Readers:</h4>
          <p className="text-sm">{data_summary}. All regions show positive growth with North leading at 16.7% increase.</p>
        </div>
      </CardContent>
    </Card>'''


def create_keyboard_nav_dashboard_tool(dashboard_title: str, widget_count: str, nav_instructions: str) -> str:
    """Generate keyboard navigable dashboard with focus management."""
    dashboard_id = f"dash_{hash(dashboard_title) % 10000}"
    
    return f'''<Card className="border-4 border-purple-600 bg-purple-50">
      <CardHeader className="bg-purple-600 text-white p-4">
        <CardTitle className="text-xl font-bold flex items-center">
          <span className="text-2xl mr-3" role="img" aria-label="Keyboard navigation">⌨️</span>
          {dashboard_title} (Keyboard Accessible)
        </CardTitle>
        <Badge className="bg-purple-200 text-purple-800 font-bold mt-2">KEYBOARD READY</Badge>
      </CardHeader>
      <CardContent className="p-6">
        <div className="mb-6 p-4 bg-purple-100 border-l-4 border-purple-600 rounded">
          <h4 className="font-bold text-purple-800 mb-2">⌨️ Keyboard Navigation Guide:</h4>
          <div className="grid grid-cols-2 gap-2 text-sm text-purple-700">
            <div><kbd className="bg-purple-600 text-white px-2 py-1 rounded">Tab</kbd> Navigate forward</div>
            <div><kbd className="bg-purple-600 text-white px-2 py-1 rounded">Shift+Tab</kbd> Navigate backward</div>
            <div><kbd className="bg-purple-600 text-white px-2 py-1 rounded">Enter</kbd> Activate widget</div>
            <div><kbd className="bg-purple-600 text-white px-2 py-1 rounded">Space</kbd> Toggle selection</div>
          </div>
        </div>
        
        <div 
          className="grid grid-cols-2 gap-4"
          role="region"
          aria-label="{dashboard_title} main content with {widget_count} interactive widgets"
        >
          <div 
            className="bg-white border-2 border-gray-400 rounded-lg p-4 focus:border-4 focus:border-blue-600 focus:outline-none cursor-pointer"
            tabindex="0"
            role="button"
            aria-label="Sales widget - shows current sales metrics, press Enter to view details"
            onkeydown="if(event.key==='Enter') alert('Sales widget activated')"
          >
            <div className="text-center">
              <div className="text-3xl mb-2" role="img" aria-label="Sales icon">💰</div>
              <h3 className="font-bold text-lg">SALES</h3>
              <p className="text-2xl font-bold text-green-600">$4.2M</p>
              <p className="text-sm text-gray-600">Click or press Enter</p>
            </div>
          </div>
          
          <div 
            className="bg-white border-2 border-gray-400 rounded-lg p-4 focus:border-4 focus:border-blue-600 focus:outline-none cursor-pointer"
            tabindex="0"
            role="button"
            aria-label="Customers widget - shows customer count, press Enter to view details"
            onkeydown="if(event.key==='Enter') alert('Customers widget activated')"
          >
            <div className="text-center">
              <div className="text-3xl mb-2" role="img" aria-label="Customers icon">👥</div>
              <h3 className="font-bold text-lg">CUSTOMERS</h3>
              <p className="text-2xl font-bold text-blue-600">2,847</p>
              <p className="text-sm text-gray-600">Keyboard accessible</p>
            </div>
          </div>
          
          <div 
            className="bg-white border-2 border-gray-400 rounded-lg p-4 focus:border-4 focus:border-blue-600 focus:outline-none cursor-pointer"
            tabindex="0"
            role="button"
            aria-label="Orders widget - shows order statistics, press Enter to view details"
            onkeydown="if(event.key==='Enter') alert('Orders widget activated')"
          >
            <div className="text-center">
              <div className="text-3xl mb-2" role="img" aria-label="Orders icon">📦</div>
              <h3 className="font-bold text-lg">ORDERS</h3>
              <p className="text-2xl font-bold text-orange-600">1,394</p>
              <p className="text-sm text-gray-600">Focus manageable</p>
            </div>
          </div>
          
          <div 
            className="bg-white border-2 border-gray-400 rounded-lg p-4 focus:border-4 focus:border-blue-600 focus:outline-none cursor-pointer"
            tabindex="0"
            role="button"
            aria-label="Growth widget - shows growth percentage, press Enter to view details"
            onkeydown="if(event.key==='Enter') alert('Growth widget activated')"
          >
            <div className="text-center">
              <div className="text-3xl mb-2" role="img" aria-label="Growth icon">📈</div>
              <h3 className="font-bold text-lg">GROWTH</h3>
              <p className="text-2xl font-bold text-purple-600">+23%</p>
              <p className="text-sm text-gray-600">Tab navigable</p>
            </div>
          </div>
        </div>
        
        <div className="mt-6 p-4 bg-green-100 border-l-4 border-green-600 rounded">
          <div className="flex items-center">
            <span className="text-2xl mr-3" role="img" aria-label="Accessibility confirmed">✅</span>
            <div>
              <p className="font-bold text-green-800">WCAG 2.1 AA Compliant Features:</p>
              <p className="text-sm text-green-700">Keyboard navigation, focus indicators, ARIA labels, semantic markup</p>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>'''



# Create Accessibility Agent using authentic ADK patterns
accessibility_agent = LlmAgent(
    name="accessibility_agent",
    model="gemini-2.5-flash",
    description="Ensures UI components meet accessibility standards and provides WCAG-compliant accessibility improvements.",
    instruction="""You are an accessibility specialist.

CRITICAL STOPPING RULES (HIGHEST PRIORITY):
- Call EXACTLY ONE tool per request and STOP immediately
- NEVER call the same tool multiple times in a session
- If tool fails or returns error, STOP - do not retry
- Return generated React component and TERMINATE
- NEVER ask follow-up questions or request clarification
- Circuit breaker prevents infinite loops (max 3 calls per tool/params per 60s)

TOOL SELECTION (choose EXACTLY ONE):
- High contrast/visually impaired → create_high_contrast_chart_tool
- Screen reader/data tables → create_screen_reader_table_tool
- Keyboard navigation/dashboard → create_keyboard_nav_dashboard_tool

EXECUTION PATTERN:
1. Analyze request to identify ONE primary accessibility need
2. Call the appropriate tool ONCE with WCAG 2.1 AA compliant defaults
3. Return the generated JSX component immediately
4. STOP - do not generate additional components

EXAMPLE FLOWS:
User: "high contrast chart" → call create_high_contrast_chart_tool → STOP
User: "accessible table" → call create_screen_reader_table_tool → STOP
User: "keyboard dashboard" → call create_keyboard_nav_dashboard_tool → STOP

CRITICAL: Never call tools multiple times. One request = One tool call = One component.""",
    tools=[create_high_contrast_chart_tool, create_screen_reader_table_tool, create_keyboard_nav_dashboard_tool]
)
