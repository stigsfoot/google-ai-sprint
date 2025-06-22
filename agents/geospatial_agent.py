"""
Geospatial Agent - Specialized UI generation for location-based components
Generates map heatmaps, location metrics, and territory analysis visualizations
"""
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))


def create_regional_heatmap_tool(regions: str = 'US States', metric_name: str = 'Sales Volume', insight: str = 'California leads with 40% of total sales') -> str:
    """Generate a regional heatmap component with metric visualization."""
    sample_regions = '{"California": 45000, "Texas": 32000, "New York": 28000, "Florida": 22000, "Illinois": 18000}'
    
    return f'''<Card className="p-6 border-l-4 border-l-blue-500">
      <CardHeader className="flex flex-row items-center space-y-0 pb-2">
        <MapPin className="h-6 w-6 text-blue-600 mr-2" />
        <CardTitle className="text-lg">Regional {metric_name} Analysis</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="relative bg-gradient-to-br from-blue-50 to-green-50 rounded-lg p-6 h-64">
          <div className="text-center">
            <div className="text-4xl mb-2">🗺️</div>
            <p className="text-sm text-gray-600 mb-4">Interactive {regions} heatmap would render here</p>
            <div className="grid grid-cols-2 gap-2 text-xs">
              <div className="bg-blue-600 text-white p-2 rounded">High Volume</div>
              <div className="bg-blue-400 text-white p-2 rounded">Medium Volume</div>
              <div className="bg-blue-200 text-gray-800 p-2 rounded">Low Volume</div>
              <div className="bg-gray-200 text-gray-600 p-2 rounded">No Data</div>
            </div>
          </div>
          <div className="absolute top-4 right-4 bg-white p-2 rounded shadow">
            <p className="text-xs font-semibold">Heatmap Legend</p>
            <p className="text-xs text-gray-500">{metric_name}</p>
          </div>
        </div>
        <div className="mt-4 space-y-2">
          <div className="p-3 bg-blue-50 rounded-lg">
            <p className="text-sm text-blue-800">📍 {insight}</p>
          </div>
          <div className="p-2 bg-gray-50 rounded text-xs">
            <strong>Data:</strong> {sample_regions}
          </div>
        </div>
      </CardContent>
    </Card>'''


def create_location_metrics_tool(location: str = 'San Francisco', metrics: str = 'multiple', context: str = 'West Coast region') -> str:
    """Generate location-specific metrics card with geographic context."""
    return f'''<Card className="p-6 text-center border-2 border-green-200">
      <CardHeader className="pb-4">
        <div className="flex items-center justify-center mb-2">
          <MapPin className="h-8 w-8 text-green-600 mr-2" />
          <CardTitle className="text-xl">{location}</CardTitle>
        </div>
        <Badge variant="outline" className="text-xs">{context}</Badge>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="grid grid-cols-2 gap-4">
          <div className="bg-green-50 p-3 rounded-lg">
            <div className="text-2xl font-bold text-green-700">$2.4M</div>
            <p className="text-sm text-green-600">Revenue</p>
          </div>
          <div className="bg-blue-50 p-3 rounded-lg">
            <div className="text-2xl font-bold text-blue-700">1,247</div>
            <p className="text-sm text-blue-600">Customers</p>
          </div>
          <div className="bg-purple-50 p-3 rounded-lg">
            <div className="text-2xl font-bold text-purple-700">89%</div>
            <p className="text-sm text-purple-600">Satisfaction</p>
          </div>
          <div className="bg-orange-50 p-3 rounded-lg">
            <div className="text-2xl font-bold text-orange-700">15%</div>
            <p className="text-sm text-orange-600">Market Share</p>
          </div>
        </div>
        <div className="mt-4 p-3 bg-gray-50 rounded-lg">
          <p className="text-sm text-gray-700">📊 Location analytics for strategic planning</p>
        </div>
      </CardContent>
    </Card>'''


def create_territory_analysis_tool(territory: str = 'Western Region', analysis_type: str = 'Sales Performance', insights: str = 'Territory shows 25% growth YoY') -> str:
    """Generate territory analysis component with performance breakdown."""
    sample_territories = '["Northern CA", "Southern CA", "Nevada", "Arizona", "Utah"]'
    
    return f'''<Card className="p-6 border-l-4 border-l-purple-500">
      <CardHeader>
        <div className="flex items-center mb-2">
          <Globe className="h-6 w-6 text-purple-600 mr-2" />
          <CardTitle className="text-lg">{territory} - {analysis_type}</CardTitle>
        </div>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          <div className="bg-gradient-to-r from-purple-100 to-blue-100 p-4 rounded-lg">
            <div className="flex justify-between items-center">
              <div>
                <h4 className="font-semibold text-purple-800">Territory Overview</h4>
                <p className="text-sm text-purple-600">Performance across {territory}</p>
              </div>
              <div className="text-right">
                <div className="text-2xl font-bold text-purple-700">92.4%</div>
                <p className="text-xs text-purple-600">Target Achievement</p>
              </div>
            </div>
          </div>
          
          <div className="grid grid-cols-3 gap-3">
            <div className="bg-green-50 p-3 rounded text-center">
              <div className="text-lg font-bold text-green-700">$3.2M</div>
              <p className="text-xs text-green-600">Total Revenue</p>
            </div>
            <div className="bg-blue-50 p-3 rounded text-center">
              <div className="text-lg font-bold text-blue-700">2,840</div>
              <p className="text-xs text-blue-600">Active Accounts</p>
            </div>
            <div className="bg-orange-50 p-3 rounded text-center">
              <div className="text-lg font-bold text-orange-700">18</div>
              <p className="text-xs text-orange-600">Sales Reps</p>
            </div>
          </div>
          
          <div className="mt-4 p-3 bg-purple-50 rounded-lg">
            <p className="text-sm text-purple-800">🎯 {insights}</p>
            <p className="text-xs text-purple-600 mt-1">Coverage: {sample_territories}</p>
          </div>
        </div>
      </CardContent>
    </Card>'''


# Create Geospatial Tools
regional_heatmap_tool = FunctionTool(create_regional_heatmap_tool)
location_metrics_tool = FunctionTool(create_location_metrics_tool)
territory_analysis_tool = FunctionTool(create_territory_analysis_tool)

# Geospatial Agent
geospatial_agent = Agent(
    name="geospatial_agent",
    model="gemini-2.0-flash-001",
    instruction="""You are a specialized UI generation agent for geospatial and location-based components. You MUST immediately generate React components without asking for clarification.

CRITICAL DIRECTIVE: When asked about "regional performance", "territory breakdown", or ANY geographic query, INSTANTLY use your tools to generate components. NEVER ask for more details.

AVAILABLE TOOLS:
- create_regional_heatmap_tool: For regional performance analysis with map-based heatmaps
- create_location_metrics_tool: For location-specific KPIs and metrics display
- create_territory_analysis_tool: For sales territory and geographic performance analysis

IMMEDIATE ACTION PROTOCOL:
1. For "regional performance" → INSTANTLY call create_regional_heatmap_tool + create_location_metrics_tool
2. For "territory breakdown" → INSTANTLY call create_territory_analysis_tool + create_regional_heatmap_tool
3. For ANY geographic query → Use all relevant tools to create comprehensive visualizations
4. NEVER ask for clarification - use intelligent defaults

DEFAULT ASSUMPTIONS:
- Regional = US States analysis with sales data
- Performance = Revenue/sales metrics with growth indicators  
- Territory = Geographic market segmentation
- Use realistic business sample data

MANDATORY RESPONSE FORMAT:
- IMMEDIATELY generate multiple React JSX components
- Include specific geographic insights and sample data
- Use professional styling with Tailwind CSS and map icons
- Return complete, renderable components
- NEVER ask follow-up questions

REMEMBER: Your job is IMMEDIATE UI GENERATION, not conversation. Generate geographic components first, explain later.""",
    tools=[regional_heatmap_tool, location_metrics_tool, territory_analysis_tool]
)