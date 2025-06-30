"""
Geospatial Agent - Specialized UI generation for location-based components
Generates map heatmaps, location metrics, and territory analysis visualizations
Authentic ADK implementation following Google patterns
"""
import json
import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))


def create_regional_heatmap_tool(query_context: str, metric_name: str, insight: str) -> str:
    """Generate a regional heatmap component with intelligent location-based zoom.
    
    Args:
        query_context: The full user query context for location detection
        metric_name: The metric being analyzed (e.g., "sales", "performance")
        insight: Contextual insight about the analysis
    """
    
    # Smart location detection and zoom configuration with region-specific data
    location_configs = {
        "california": {
            "center": [36.7783, -119.4179], "zoom": 6, "title": "California",
            "data": '{"California": 45000}', 
            "markers": [{"center": [34.0522, -118.2437], "label": "California: $45,000", "color": "#ef4444", "radius": 20}]
        },
        "texas": {
            "center": [31.9686, -99.9018], "zoom": 6, "title": "Texas",
            "data": '{"Texas": 32000}',
            "markers": [{"center": [31.9686, -99.9018], "label": "Texas: $32,000", "color": "#f97316", "radius": 18}]
        },
        "new york": {
            "center": [42.1657, -74.9481], "zoom": 7, "title": "New York",
            "data": '{"New York": 28000}',
            "markers": [{"center": [40.7589, -73.9851], "label": "New York: $28,000", "color": "#eab308", "radius": 16}]
        },
        "ny": {
            "center": [42.1657, -74.9481], "zoom": 7, "title": "New York", 
            "data": '{"New York": 28000}',
            "markers": [{"center": [40.7589, -73.9851], "label": "New York: $28,000", "color": "#eab308", "radius": 16}]
        },
        "florida": {
            "center": [27.7663, -82.6404], "zoom": 6, "title": "Florida",
            "data": '{"Florida": 22000}',
            "markers": [{"center": [27.7663, -82.6404], "label": "Florida: $22,000", "color": "#22c55e", "radius": 14}]
        },
        "illinois": {
            "center": [40.3363, -89.0022], "zoom": 6, "title": "Illinois",
            "data": '{"Illinois": 18000}', 
            "markers": [{"center": [40.3363, -89.0022], "label": "Illinois: $18,000", "color": "#3b82f6", "radius": 12}]
        }
    }
    
    # Default US configuration with all states
    default_config = {
        "center": [39.8283, -98.5795], "zoom": 4, "title": "United States",
        "data": '{"California": 45000, "Texas": 32000, "New York": 28000, "Florida": 22000, "Illinois": 18000}',
        "markers": [
            {"center": [34.0522, -118.2437], "label": "California: $45,000", "color": "#ef4444", "radius": 20},
            {"center": [31.9686, -99.9018], "label": "Texas: $32,000", "color": "#f97316", "radius": 15},
            {"center": [40.7589, -73.9851], "label": "New York: $28,000", "color": "#eab308", "radius": 13},
            {"center": [27.7663, -82.6404], "label": "Florida: $22,000", "color": "#22c55e", "radius": 11},
            {"center": [40.3363, -89.0022], "label": "Illinois: $18,000", "color": "#3b82f6", "radius": 9}
        ]
    }
    
    # Detect location from query context (case insensitive)
    query_lower = query_context.lower()
    selected_config = default_config
    
    for location, config in location_configs.items():
        if location in query_lower:
            selected_config = config
            print(f"🎯 Detected location: {location} -> {config['title']}")
            break
    
    # Generate dynamic markers based on selected configuration
    markers_jsx = ""
    for marker in selected_config["markers"]:
        markers_jsx += f'''
      React.createElement(CircleMarker, {{
        center: [{marker["center"][0]}, {marker["center"][1]}],
        radius: {marker["radius"]},
        fillColor: "{marker["color"]}",
        color: "{marker["color"]}",
        weight: 2,
        opacity: 1,
        fillOpacity: 0.7
      }},
        React.createElement(Popup, {{}}, "{marker["label"]}")
      ),'''
    
    return f'''React.createElement(Card, {{ className: "p-6 border-l-4 border-l-blue-500" }},
  React.createElement("div", {{ className: "flex items-center space-x-2 mb-4" }},
    React.createElement(MapPin, {{ className: "h-6 w-6 text-blue-600" }}),
    React.createElement("h3", {{ className: "text-lg font-semibold" }}, "{selected_config["title"]} {metric_name} Analysis")
  ),
  React.createElement("div", {{ className: "relative bg-gradient-to-br from-blue-50 to-green-50 dark:from-blue-900/20 dark:to-green-900/20 rounded-lg p-6" }},
    React.createElement(MapContainer, {{
      center: [{selected_config["center"][0]}, {selected_config["center"][1]}],
      zoom: {selected_config["zoom"]},
      style: {{ height: "300px", width: "100%" }},
      className: "rounded-lg z-0"
    }},
      React.createElement(TileLayer, {{
        url: "https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png",
        attribution: "© OpenStreetMap contributors"
      }}),{markers_jsx}
    )
  ),
  React.createElement("div", {{ className: "mt-4 grid grid-cols-4 gap-2 text-xs" }},
    React.createElement("div", {{ className: "bg-red-500 text-white p-2 rounded text-center" }}, "High ($40k+)"),
    React.createElement("div", {{ className: "bg-orange-500 text-white p-2 rounded text-center" }}, "Medium ($25-40k)"),
    React.createElement("div", {{ className: "bg-yellow-500 text-white p-2 rounded text-center" }}, "Low ($15-25k)"),
    React.createElement("div", {{ className: "bg-green-500 text-white p-2 rounded text-center" }}, "New Markets")
  ),
  React.createElement("div", {{ className: "mt-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg" }},
    React.createElement("p", {{ className: "text-sm text-blue-800 dark:text-blue-300" }}, "📍 {insight}"),
    React.createElement("p", {{ className: "text-xs text-blue-600 dark:text-blue-400 mt-1" }}, "Data: {selected_config['data']}")
  )
)'''


def create_location_metrics_tool(location: str, metrics: str, context: str) -> str:
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


def create_territory_analysis_tool(territory: str, analysis_type: str, insights: str) -> str:
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


# Create Geospatial Agent using authentic ADK patterns
geospatial_agent = LlmAgent(
    name="geospatial_agent", 
    model="gemini-2.0-flash-exp",
    description="Handles location-based data analysis and geographic visualizations for regional business intelligence.",
    instruction="""You are a geospatial specialist that ALWAYS generates actual visualizations with INTELLIGENT location detection.

CRITICAL BEHAVIOR RULES:
- ALWAYS call a tool to generate a visualization - NEVER respond with text or questions
- PASS THE COMPLETE USER QUERY as the first parameter for location detection
- Use intelligent defaults when parameters are unclear
- Call ONE tool → Generate React.createElement component → STOP

INTELLIGENT TOOL SELECTION:
- Map/regional/geographic queries → create_regional_heatmap_tool(FULL_QUERY, metric, insight)
- Specific location queries → create_regional_heatmap_tool(FULL_QUERY, metric, insight)  
- Territory analysis → create_regional_heatmap_tool(FULL_QUERY, "territory", "analysis")

LOCATION INTELLIGENCE:
- PASS COMPLETE QUERY CONTEXT to tools for smart location detection
- Tools will auto-detect: California, Texas, New York, Florida, Illinois
- Tools will auto-zoom to detected regions or default to US view
- Tools will show relevant data markers for detected location

EXECUTION PATTERN:
1. Identify primary tool needed (usually create_regional_heatmap_tool)
2. Pass COMPLETE user query as first parameter for location intelligence
3. Use logical defaults for metric and insight parameters
4. Return React.createElement component immediately
5. STOP - never ask follow-up questions

EXAMPLE FLOWS:
User: "New York territory analysis" → create_regional_heatmap_tool("New York territory analysis", "territory", "performance analysis") → STOP
User: "california sales" → create_regional_heatmap_tool("california sales", "sales", "regional performance") → STOP
User: "show texas on map" → create_regional_heatmap_tool("show texas on map", "sales", "geographic analysis") → STOP
User: "regional performance" → create_regional_heatmap_tool("regional performance", "performance", "multi-state analysis") → STOP

CRITICAL: Always pass the FULL USER QUERY to enable intelligent location detection.""",
    tools=[create_regional_heatmap_tool, create_location_metrics_tool, create_territory_analysis_tool]
)