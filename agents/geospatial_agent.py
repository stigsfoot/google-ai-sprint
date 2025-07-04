"""
Geospatial Agent - Specialized UI generation for location-based components
Generates map heatmaps, location metrics, and territory analysis visualizations
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

# Circuit Breaker for Loop Prevention
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
    
    def get_remaining_calls(self, tool_name, params_hash):
        """Get remaining allowed calls for this tool/params combo"""
        key = f"{tool_name}:{params_hash}"
        now = time.time()
        
        # Clean old entries
        while self.call_history[key] and now - self.call_history[key][0] > self.time_window:
            self.call_history[key].popleft()
        
        return max(0, self.max_calls - len(self.call_history[key]))

# Global tracker instance
tracker = ToolCallTracker()


def create_regional_heatmap_tool(query_context: str, metric_name: str, insight: str) -> str:
    """Generate a regional heatmap component with intelligent location-based zoom and interactive performance categories.
    
    Args:
        query_context: The full user query context for location detection
        metric_name: The metric being analyzed (e.g., "sales", "performance")
        insight: Contextual insight about the analysis
    """
    
    # CIRCUIT BREAKER: Prevent infinite loops with identical parameters
    params_hash = hash(f"{query_context}:{metric_name}:{insight}")
    if not tracker.is_allowed("create_regional_heatmap_tool", params_hash):
        remaining = tracker.get_remaining_calls("create_regional_heatmap_tool", params_hash)
        return f'''React.createElement(Card, {{ className: "p-6 border-l-4 border-l-red-500" }},
  React.createElement("div", {{ className: "text-center" }},
    React.createElement("h3", {{ className: "text-lg font-semibold text-red-600" }}, "Rate Limit Protection"),
    React.createElement("p", {{ className: "text-sm text-red-500 mt-2" }}, "Tool call limit reached. Please try a different query."),
    React.createElement("p", {{ className: "text-xs text-gray-500 mt-1" }}, "Remaining calls: {remaining}")
  )
)'''
    
    # Performance categorization with region mappings for interactive legend
    performance_categories = {
        "high": {
            "label": "High ($40k+)",
            "color": "#ef4444",
            "regions": ["California"],
            "threshold": {"min": 40000},
            "zoom_bounds": {"center": [34.0522, -118.2437], "zoom": 6}
        },
        "medium": {
            "label": "Medium ($25-40k)", 
            "color": "#f97316",
            "regions": ["Texas", "New York"],
            "threshold": {"min": 25000, "max": 39999},
            "zoom_bounds": {"center": [36.0, -96.0], "zoom": 5}  # Centered between TX and NY
        },
        "low": {
            "label": "Low ($15-25k)",
            "color": "#eab308", 
            "regions": ["Florida", "Illinois"],
            "threshold": {"min": 15000, "max": 24999},
            "zoom_bounds": {"center": [35.0, -85.0], "zoom": 5}  # Centered between FL and IL
        },
        "new_markets": {
            "label": "New Markets",
            "color": "#22c55e",
            "regions": [],
            "threshold": {"min": 0, "max": 14999},
            "zoom_bounds": {"center": [39.8283, -98.5795], "zoom": 4}  # Full US view
        }
    }
    
    # Helper function to categorize regions by performance
    def get_region_category(region_name: str, value: int) -> str:
        for category_id, category in performance_categories.items():
            if region_name in category["regions"]:
                return category_id
            # Fallback to value-based categorization
            if value >= category["threshold"]["min"] and (
                "max" not in category["threshold"] or value <= category["threshold"]["max"]
            ):
                return category_id
        return "new_markets"  # Default fallback
    
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
    for i, marker in enumerate(selected_config["markers"]):
        # Add comma only between markers, not after the last one
        comma = "," if i < len(selected_config["markers"]) - 1 else ""
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
      ){comma}'''
    
    # Generate structured interactive map data
    interactive_data = {
        "type": "interactive_map",
        "title": f"{selected_config['title']} {metric_name} Analysis",
        "map_config": {
            "center": selected_config["center"],
            "zoom": selected_config["zoom"],
            "markers": selected_config["markers"]
        },
        "performance_categories": performance_categories,
        "current_category": get_region_category(selected_config["title"], 45000),  # Use default value for now
        "interactions": {
            "legend_click_behavior": "zoom_to_category",
            "marker_click_behavior": "show_details",
            "keyboard_navigation": True
        },
        "insight": insight,
        "data": selected_config["data"]
    }
    
    return f'''```json
{json.dumps(interactive_data, indent=2)}
```

React.createElement(Card, {{ className: "p-6 border-l-4 border-l-blue-500" }},
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
        url: "https://a.tile.openstreetmap.org/1/0/0.png",
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
    
    # Location-specific configurations with accurate coordinates
    location_configs = {
        "california": {"center": [36.7783, -119.4179], "zoom": 6},
        "texas": {"center": [31.9686, -99.9018], "zoom": 6},
        "new york": {"center": [42.1657, -74.9481], "zoom": 7},
        "ny": {"center": [42.1657, -74.9481], "zoom": 7},
        "florida": {"center": [27.7663, -82.6404], "zoom": 6},
        "illinois": {"center": [40.3363, -89.0022], "zoom": 6}
    }
    
    # Get location config or default to center of US
    location_key = location.lower().strip()
    config = location_configs.get(location_key, {"center": [39.8283, -98.5795], "zoom": 4})
    
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
        center: [{config["center"][0]}, {config["center"][1]}],
        zoom: {config["zoom"]},
        style: {{ height: "200px", width: "100%" }},
        className: "rounded-lg z-0"
      }},
        React.createElement(TileLayer, {{
          url: "https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png",
          attribution: "© OpenStreetMap contributors"
        }}),
        React.createElement(CircleMarker, {{
          center: [{config["center"][0]}, {config["center"][1]}],
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
    
    # Territory-specific configurations with accurate coordinates and markets
    territory_configs = {
        "texas": {
            "center": [31.9686, -99.9018],
            "zoom": 6,
            "markets": [
                {"center": [29.7604, -95.3698], "name": "Houston", "value": "$1.8M", "radius": 16},
                {"center": [32.7767, -96.7970], "name": "Dallas", "value": "$1.4M", "radius": 14},
                {"center": [30.2672, -97.7431], "name": "Austin", "value": "$900k", "radius": 12},
                {"center": [29.4241, -98.4936], "name": "San Antonio", "value": "$800k", "radius": 10}
            ]
        },
        "california": {
            "center": [36.7783, -119.4179],
            "zoom": 6,
            "markets": [
                {"center": [37.7749, -122.4194], "name": "Northern CA", "value": "$1.2M", "radius": 12},
                {"center": [34.0522, -118.2437], "name": "Southern CA", "value": "$1.4M", "radius": 14}
            ]
        },
        "new york": {
            "center": [42.1657, -74.9481],
            "zoom": 7,
            "markets": [
                {"center": [40.7589, -73.9851], "name": "NYC Metro", "value": "$2.1M", "radius": 18},
                {"center": [42.6526, -73.7562], "name": "Albany", "value": "$600k", "radius": 10},
                {"center": [43.0481, -76.1474], "name": "Syracuse", "value": "$400k", "radius": 8}
            ]
        },
        "florida": {
            "center": [27.7663, -82.6404],
            "zoom": 6,
            "markets": [
                {"center": [25.7617, -80.1918], "name": "Miami", "value": "$1.5M", "radius": 15},
                {"center": [28.5383, -81.3792], "name": "Orlando", "value": "$900k", "radius": 12},
                {"center": [27.9506, -82.4572], "name": "Tampa", "value": "$800k", "radius": 11}
            ]
        }
    }
    
    # Get territory config or default
    territory_key = territory.lower().strip()
    config = territory_configs.get(territory_key, {
        "center": [39.8283, -98.5795],
        "zoom": 4,
        "markets": [{"center": [39.8283, -98.5795], "name": "National", "value": "$2.5M", "radius": 15}]
    })
    
    # Generate markets JSX
    markets_jsx = ""
    for market in config["markets"]:
        markets_jsx += f'''
          React.createElement(CircleMarker, {{
            center: [{market["center"][0]}, {market["center"][1]}],
            radius: {market["radius"]},
            fillColor: "#8b5cf6",
            color: "#7c3aed",
            weight: 2,
            opacity: 1,
            fillOpacity: 0.7
          }},
            React.createElement(Popup, {{}}, "{market["name"]}: {market["value"]}")
          ),'''
    
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
          center: [{config["center"][0]}, {config["center"][1]}],
          zoom: {config["zoom"]},
          style: {{ height: "180px", width: "100%" }},
          className: "rounded-lg z-0"
        }},
          React.createElement(TileLayer, {{
            url: "https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png",
            attribution: "© OpenStreetMap contributors"
          }}),{markets_jsx}
        )
      )
    ),
    React.createElement("div", {{ className: "p-3 bg-purple-50 rounded-lg" }},
      React.createElement(Text, {{ className: "text-sm text-purple-800" }}, "🎯 {insights}"),
      React.createElement(Text, {{ className: "text-xs text-purple-600 mt-1" }}, "Coverage: {[market['name'] for market in config['markets']]}")
    )
  )
)'''


# Create Geospatial Agent using authentic ADK patterns
geospatial_agent = LlmAgent(
    name="geospatial_agent", 
    model="gemini-2.0-flash-exp",
    description="Handles location-based data analysis and geographic visualizations for regional business intelligence.",
    instruction="""You are an INTELLIGENT geospatial specialist with sophisticated query analysis capabilities.

CRITICAL STOPPING RULES (HIGHEST PRIORITY):
- Call EXACTLY ONE tool per request and STOP immediately
- NEVER call the same tool multiple times in a session
- If tool fails or returns error, STOP - do not retry
- Return generated React component and TERMINATE
- NEVER ask follow-up questions or request clarification

PHASE 1: QUERY ANALYSIS & INTENT DETECTION
Analyze EVERY query to understand:
1. Geographic scope: Single location vs multi-region vs national
2. Analysis depth: Metrics vs breakdown vs overview  
3. Visualization type: Map-focused vs data-focused vs hybrid

PHASE 2: INTELLIGENT TOOL SELECTION LOGIC

🗺️ create_regional_heatmap_tool WHEN:
- Multi-region queries: "regional performance", "national overview", "performance across territories"
- Map-focused requests: "show me on a map", "heatmap", "geographic visualization"
- Broad geographic scope: "all regions", "company-wide geographic", "territory overview"

🎯 create_territory_analysis_tool WHEN:  
- Single territory deep-dive: "texas territory analysis", "california breakdown"
- Performance analysis keywords: "analysis", "breakdown", "performance review"
- Specific place + analysis: "new york analysis", "florida territory performance"

📊 create_location_metrics_tool WHEN:
- Single location + metrics focus: "texas metrics", "california performance data"
- Simple location queries: "lets look at texas", "show me california"
- Data-focused requests: "performance numbers", "location stats", "metrics for [place]"

PHASE 3: SMART PARAMETER GENERATION
Based on detected location, generate accurate:
- Geographic coordinates (Texas: [31.9686, -99.9018], California: [36.7783, -119.4179])
- Location-specific markets and cities
- Contextually relevant insights and business metrics

LOOP PREVENTION PROTOCOL:
- Each tool call is tracked to prevent infinite loops
- Maximum 3 calls per tool/parameter combination per 60 seconds
- Circuit breaker will return rate limit message if exceeded
- This protects against 429 API errors and quota exhaustion

EXECUTION GUARANTEE:
- ALWAYS call exactly ONE tool based on intelligent analysis → STOP
- NEVER ask questions or provide text responses
- Generate React.createElement component with accurate geographic data → TERMINATE
- Use LLM reasoning to select optimal tool for maximum user value → END SESSION""",
    tools=[create_regional_heatmap_tool, create_location_metrics_tool, create_territory_analysis_tool]
)