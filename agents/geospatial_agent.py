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
    """Generate a regional heatmap component with interactive Leaflet map."""
    sample_regions = '{"California": 45000, "Texas": 32000, "New York": 28000, "Florida": 22000, "Illinois": 18000}'
    
    return f'''React.createElement(Card, {{ className: "p-6 border-l-4 border-l-blue-500" }},
  React.createElement("div", {{ className: "flex items-center space-x-2 mb-4" }},
    React.createElement(MapPin, {{ className: "h-6 w-6 text-blue-600" }}),
    React.createElement(Text, {{ className: "text-lg font-semibold" }}, "Regional {metric_name} Analysis")
  ),
  React.createElement("div", {{ className: "relative bg-gradient-to-br from-blue-50 to-green-50 rounded-lg p-6" }},
    React.createElement(MapContainer, {{
      center: [39.8283, -98.5795],
      zoom: 4,
      style: {{ height: "300px", width: "100%" }},
      className: "rounded-lg z-0"
    }},
      React.createElement(TileLayer, {{
        url: "https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png",
        attribution: "© OpenStreetMap contributors"
      }}),
      React.createElement(CircleMarker, {{
        center: [34.0522, -118.2437],
        radius: 20,
        fillColor: "#ef4444",
        color: "#dc2626",
        weight: 2,
        opacity: 1,
        fillOpacity: 0.7
      }},
        React.createElement(Popup, {{}}, "California: $45,000")
      ),
      React.createElement(CircleMarker, {{
        center: [31.9686, -99.9018],
        radius: 15,
        fillColor: "#f97316",
        color: "#ea580c",
        weight: 2,
        opacity: 1,
        fillOpacity: 0.7
      }},
        React.createElement(Popup, {{}}, "Texas: $32,000")
      ),
      React.createElement(CircleMarker, {{
        center: [40.7589, -73.9851],
        radius: 13,
        fillColor: "#eab308",
        color: "#ca8a04",
        weight: 2,
        opacity: 1,
        fillOpacity: 0.7
      }},
        React.createElement(Popup, {{}}, "New York: $28,000")
      ),
      React.createElement(CircleMarker, {{
        center: [27.7663, -82.6404],
        radius: 11,
        fillColor: "#22c55e",
        color: "#16a34a",
        weight: 2,
        opacity: 1,
        fillOpacity: 0.7
      }},
        React.createElement(Popup, {{}}, "Florida: $22,000")
      ),
      React.createElement(CircleMarker, {{
        center: [40.3363, -89.0022],
        radius: 9,
        fillColor: "#3b82f6",
        color: "#2563eb",
        weight: 2,
        opacity: 1,
        fillOpacity: 0.7
      }},
        React.createElement(Popup, {{}}, "Illinois: $18,000")
      )
    )
  ),
  React.createElement("div", {{ className: "mt-4 grid grid-cols-4 gap-2 text-xs" }},
    React.createElement("div", {{ className: "bg-red-500 text-white p-2 rounded text-center" }}, "High ($40k+)"),
    React.createElement("div", {{ className: "bg-orange-500 text-white p-2 rounded text-center" }}, "Medium ($25-40k)"),
    React.createElement("div", {{ className: "bg-yellow-500 text-white p-2 rounded text-center" }}, "Low ($15-25k)"),
    React.createElement("div", {{ className: "bg-green-500 text-white p-2 rounded text-center" }}, "New Markets")
  ),
  React.createElement("div", {{ className: "mt-4 p-3 bg-blue-50 rounded-lg" }},
    React.createElement(Text, {{ className: "text-sm text-blue-800" }}, "📍 {insight}"),
    React.createElement(Text, {{ className: "text-xs text-blue-600 mt-1" }}, "Data: {sample_regions}")
  )
)'''


def create_location_metrics_tool(location: str = 'San Francisco', metrics: str = 'multiple', context: str = 'West Coast region') -> str:
    """Generate location-specific metrics card with geographic context and mini map."""
    return f'''React.createElement(Card, {{ className: "p-6 border-2 border-green-200" }},
  React.createElement("div", {{ className: "flex items-center justify-center mb-4" }},
    React.createElement(MapPin, {{ className: "h-8 w-8 text-green-600 mr-2" }}),
    React.createElement(Text, {{ className: "text-xl font-semibold" }}, "{location}")
  ),
  React.createElement(Badge, {{ className: "mb-4 bg-green-100 text-green-800" }}, "{context}"),
  React.createElement("div", {{ className: "grid grid-cols-1 md:grid-cols-2 gap-4 mb-4" }},
    React.createElement("div", {{ className: "space-y-3" }},
      React.createElement("div", {{ className: "bg-green-50 p-3 rounded-lg text-center" }},
        React.createElement(Text, {{ className: "text-2xl font-bold text-green-700" }}, "$2.4M"),
        React.createElement(Text, {{ className: "text-sm text-green-600" }}, "Revenue")
      ),
      React.createElement("div", {{ className: "bg-blue-50 p-3 rounded-lg text-center" }},
        React.createElement(Text, {{ className: "text-2xl font-bold text-blue-700" }}, "1,247"),
        React.createElement(Text, {{ className: "text-sm text-blue-600" }}, "Customers")
      ),
      React.createElement("div", {{ className: "bg-purple-50 p-3 rounded-lg text-center" }},
        React.createElement(Text, {{ className: "text-2xl font-bold text-purple-700" }}, "89%"),
        React.createElement(Text, {{ className: "text-sm text-purple-600" }}, "Satisfaction")
      ),
      React.createElement("div", {{ className: "bg-orange-50 p-3 rounded-lg text-center" }},
        React.createElement(Text, {{ className: "text-2xl font-bold text-orange-700" }}, "15%"),
        React.createElement(Text, {{ className: "text-sm text-orange-600" }}, "Market Share")
      )
    ),
    React.createElement("div", {{ className: "relative" }},
      React.createElement(MapContainer, {{
        center: [37.7749, -122.4194],
        zoom: 10,
        style: {{ height: "200px", width: "100%" }},
        className: "rounded-lg z-0"
      }},
        React.createElement(TileLayer, {{
          url: "https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png",
          attribution: "© OpenStreetMap contributors"
        }}),
        React.createElement(CircleMarker, {{
          center: [37.7749, -122.4194],
          radius: 15,
          fillColor: "#22c55e",
          color: "#16a34a",
          weight: 3,
          opacity: 1,
          fillOpacity: 0.8
        }},
          React.createElement(Popup, {{}}, "{location}: Primary market")
        )
      )
    )
  ),
  React.createElement("div", {{ className: "p-3 bg-gray-50 rounded-lg" }},
    React.createElement(Text, {{ className: "text-sm text-gray-700" }}, "📊 Location analytics for strategic planning")
  )
)'''


def create_territory_analysis_tool(territory: str = 'Western Region', analysis_type: str = 'Sales Performance', insights: str = 'Territory shows 25% growth YoY') -> str:
    """Generate territory analysis component with performance breakdown and territorial map."""
    sample_territories = '["Northern CA", "Southern CA", "Nevada", "Arizona", "Utah"]'
    
    return f'''React.createElement(Card, {{ className: "p-6 border-l-4 border-l-purple-500" }},
  React.createElement("div", {{ className: "flex items-center space-x-2 mb-4" }},
    React.createElement(MapPin, {{ className: "h-6 w-6 text-purple-600" }}),
    React.createElement(Text, {{ className: "text-lg font-semibold" }}, "{territory} - {analysis_type}")
  ),
  React.createElement("div", {{ className: "space-y-4" }},
    React.createElement("div", {{ className: "bg-gradient-to-r from-purple-100 to-blue-100 p-4 rounded-lg" }},
      React.createElement("div", {{ className: "flex justify-between items-center" }},
        React.createElement("div", {{}},
          React.createElement(Text, {{ className: "font-semibold text-purple-800" }}, "Territory Overview"),
          React.createElement(Text, {{ className: "text-sm text-purple-600" }}, "Performance across {territory}")
        ),
        React.createElement("div", {{ className: "text-right" }},
          React.createElement(Text, {{ className: "text-2xl font-bold text-purple-700" }}, "92.4%"),
          React.createElement(Text, {{ className: "text-xs text-purple-600" }}, "Target Achievement")
        )
      )
    ),
    React.createElement("div", {{ className: "grid grid-cols-1 lg:grid-cols-2 gap-4" }},
      React.createElement("div", {{ className: "grid grid-cols-3 gap-3" }},
        React.createElement("div", {{ className: "bg-green-50 p-3 rounded text-center" }},
          React.createElement(Text, {{ className: "text-lg font-bold text-green-700" }}, "$3.2M"),
          React.createElement(Text, {{ className: "text-xs text-green-600" }}, "Total Revenue")
        ),
        React.createElement("div", {{ className: "bg-blue-50 p-3 rounded text-center" }},
          React.createElement(Text, {{ className: "text-lg font-bold text-blue-700" }}, "2,840"),
          React.createElement(Text, {{ className: "text-xs text-blue-600" }}, "Active Accounts")
        ),
        React.createElement("div", {{ className: "bg-orange-50 p-3 rounded text-center" }},
          React.createElement(Text, {{ className: "text-lg font-bold text-orange-700" }}, "18"),
          React.createElement(Text, {{ className: "text-xs text-orange-600" }}, "Sales Reps")
        )
      ),
      React.createElement("div", {{ className: "relative" }},
        React.createElement(MapContainer, {{
          center: [36.7783, -119.4179],
          zoom: 6,
          style: {{ height: "180px", width: "100%" }},
          className: "rounded-lg z-0"
        }},
          React.createElement(TileLayer, {{
            url: "https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png",
            attribution: "© OpenStreetMap contributors"
          }}),
          React.createElement(CircleMarker, {{
            center: [37.7749, -122.4194],
            radius: 12,
            fillColor: "#8b5cf6",
            color: "#7c3aed",
            weight: 2,
            opacity: 1,
            fillOpacity: 0.7
          }},
            React.createElement(Popup, {{}}, "Northern CA: $1.2M")
          ),
          React.createElement(CircleMarker, {{
            center: [34.0522, -118.2437],
            radius: 14,
            fillColor: "#8b5cf6",
            color: "#7c3aed",
            weight: 2,
            opacity: 1,
            fillOpacity: 0.7
          }},
            React.createElement(Popup, {{}}, "Southern CA: $1.4M")
          ),
          React.createElement(CircleMarker, {{
            center: [39.1612, -119.7666],
            radius: 8,
            fillColor: "#a855f7",
            color: "#9333ea",
            weight: 2,
            opacity: 1,
            fillOpacity: 0.7
          }},
            React.createElement(Popup, {{}}, "Nevada: $300k")
          ),
          React.createElement(CircleMarker, {{
            center: [33.4484, -112.0740],
            radius: 10,
            fillColor: "#a855f7",
            color: "#9333ea",
            weight: 2,
            opacity: 1,
            fillOpacity: 0.7
          }},
            React.createElement(Popup, {{}}, "Arizona: $350k")
          ),
          React.createElement(CircleMarker, {{
            center: [40.1500, -111.8947],
            radius: 6,
            fillColor: "#c084fc",
            color: "#a855f7",
            weight: 2,
            opacity: 1,
            fillOpacity: 0.7
          }},
            React.createElement(Popup, {{}}, "Utah: $150k")
          )
        )
      )
    ),
    React.createElement("div", {{ className: "p-3 bg-purple-50 rounded-lg" }},
      React.createElement(Text, {{ className: "text-sm text-purple-800" }}, "🎯 {insights}"),
      React.createElement(Text, {{ className: "text-xs text-purple-600 mt-1" }}, "Coverage: {sample_territories}")
    )
  )
)'''


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