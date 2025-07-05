"""
Dashboard Layout Agent - Phase 3.1
Composes complex layouts by orchestrating multiple specialized agents
Includes accessibility tools for cross-cutting accessibility features
"""

from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
from .accessibility_tools import create_high_contrast_chart_tool, create_screen_reader_table_tool, create_keyboard_nav_dashboard_tool


def create_responsive_grid_layout(data_types: str, user_preference: str) -> str:
    """Generate responsive grid layout based on data types and user preferences"""
    
    # Set default values within function
    if not user_preference:
        user_preference = "default"
    
    # Determine grid structure based on data complexity
    layout_configs = {
        "charts_only": {
            "grid": "grid-cols-1 lg:grid-cols-2 gap-6",
            "container": "max-w-7xl mx-auto p-6"
        },
        "charts_and_maps": {
            "grid": "grid-cols-1 lg:grid-cols-3 gap-6",
            "container": "max-w-7xl mx-auto p-6"
        },
        "full_dashboard": {
            "grid": "grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6",
            "container": "max-w-full mx-auto p-6"
        },
        "accessibility_focus": {
            "grid": "grid-cols-1 lg:grid-cols-2 gap-8",
            "container": "max-w-6xl mx-auto p-8"
        }
    }
    
    config = layout_configs.get(data_types, layout_configs["full_dashboard"])
    
    return f"""
<div className="{config['container']} bg-gradient-to-br from-slate-50 to-blue-50 min-h-screen">
  <!-- Dashboard Header -->
  <div className="mb-8">
    <div className="flex items-center justify-between">
      <div>
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Business Intelligence Dashboard</h1>
        <p className="text-gray-600">Generated components with responsive layout optimization</p>
      </div>
      <div className="flex items-center space-x-3">
        <div className="flex items-center space-x-2">
          <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
          <span className="text-sm text-gray-500">Live Data</span>
        </div>
        <button className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
          Export Dashboard
        </button>
      </div>
    </div>
  </div>

  <!-- Responsive Grid Container -->
  <div className="{config['grid']}">
    <!-- Components will be inserted here by sub-agents -->
    COMPONENT_SLOTS_PLACEHOLDER
  </div>

  <!-- Dashboard Footer -->
  <div className="mt-12 pt-8 border-t border-gray-200">
    <div className="flex items-center justify-between text-sm text-gray-500">
      <div>Generated with Google ADK • AgenticBI System</div>
      <div>Last updated: {{new Date().toLocaleTimeString()}}</div>
    </div>
  </div>
</div>"""


def compose_multi_agent_dashboard(query: str, complexity: str) -> str:
    """Compose a complete dashboard by coordinating multiple specialized agents"""
    
    # Set default values within function
    if not complexity:
        complexity = "medium"
    
    # Analyze query to determine which agents to invoke
    query_lower = query.lower()
    
    # Determine component mix based on query analysis
    needs_charts = any(word in query_lower for word in ['trend', 'sales', 'revenue', 'growth', 'chart', 'graph'])
    needs_maps = any(word in query_lower for word in ['regional', 'geographic', 'territory', 'location', 'map'])
    needs_accessibility = any(word in query_lower for word in ['accessible', 'screen reader', 'high contrast', 'wcag'])
    
    # Generate composition instructions for sub-agents
    if needs_charts and needs_maps and needs_accessibility:
        layout_type = "full_dashboard"
        component_slots = """
    <!-- Chart Components (Top Row) -->
    <div className="col-span-1 lg:col-span-2">
      {/* CHART_AGENT_SLOT */}
    </div>
    
    <!-- Map Component (Top Right) -->
    <div className="col-span-1 lg:col-span-2">
      {/* GEOSPATIAL_AGENT_SLOT */}
    </div>
    
    <!-- Accessibility Components (Bottom Row) -->
    <div className="col-span-1 md:col-span-2 xl:col-span-4">
      {/* ACCESSIBILITY_AGENT_SLOT */}
    </div>"""
    
    elif needs_charts and needs_maps:
        layout_type = "charts_and_maps"
        component_slots = """
    <!-- Chart Component -->
    <div className="col-span-1 lg:col-span-2">
      {/* CHART_AGENT_SLOT */}
    </div>
    
    <!-- Map Component -->
    <div className="col-span-1">
      {/* GEOSPATIAL_AGENT_SLOT */}
    </div>"""
    
    elif needs_accessibility:
        layout_type = "accessibility_focus"
        component_slots = """
    <!-- High Contrast Chart -->
    <div className="col-span-1">
      {/* ACCESSIBILITY_AGENT_SLOT */}
    </div>
    
    <!-- Screen Reader Table -->
    <div className="col-span-1">
      {/* ACCESSIBILITY_AGENT_SLOT_2 */}
    </div>"""
    
    else:
        layout_type = "charts_only"
        component_slots = """
    <!-- Primary Chart -->
    <div className="col-span-1">
      {/* CHART_AGENT_SLOT */}
    </div>
    
    <!-- Secondary Chart -->
    <div className="col-span-1">
      {/* CHART_AGENT_SLOT_2 */}
    </div>"""
    
    # Generate the complete layout
    grid_layout = create_responsive_grid_layout(layout_type)
    composed_dashboard = grid_layout.replace("COMPONENT_SLOTS_PLACEHOLDER", component_slots)
    
    return f"""
{composed_dashboard}

<!-- Layout Metadata for Agent Coordination -->
<script type="application/json" id="layout-metadata">
{{
  "layout_type": "{layout_type}",
  "query": "{query}",
  "components_needed": {{
    "charts": {str(needs_charts).lower()},
    "maps": {str(needs_maps).lower()},
    "accessibility": {str(needs_accessibility).lower()}
  }},
  "complexity": "{complexity}",
  "responsive_breakpoints": ["sm", "md", "lg", "xl"],
  "generated_at": "{{new Date().toISOString()}}"
}}
</script>"""


def create_comprehensive_business_dashboard(query: str, focus_area: str) -> str:
    """Generate a comprehensive business intelligence dashboard based on the provided mockup"""
    
    # Set default values within function
    if not focus_area:
        focus_area = "regional_sales"
    
    return '''React.createElement("div", { className: "min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 p-6" },
  React.createElement(Card, { className: "w-full max-w-7xl mx-auto bg-white/95 backdrop-blur-sm border-0 shadow-2xl" },
    React.createElement("div", { className: "p-8" },
      
      // Tab Navigation Header
      React.createElement("div", { className: "mb-8" },
        React.createElement("div", { className: "flex items-center justify-between mb-6" },
          React.createElement("h1", { className: "text-3xl font-bold text-gray-900" }, "Business Intelligence Dashboard"),
          React.createElement("div", { className: "flex items-center space-x-2" },
            React.createElement("div", { className: "w-2 h-2 bg-green-500 rounded-full animate-pulse" }),
            React.createElement("span", { className: "text-sm text-gray-500" }, "Live Data")
          )
        ),
        React.createElement("div", { className: "flex space-x-1 bg-gray-900 p-2 rounded-xl w-fit" },
          React.createElement("button", {
            className: "px-6 py-2 rounded-lg font-medium transition-all bg-purple-600 text-white"
          }, "Regional Sales"),
          React.createElement("button", {
            className: "px-6 py-2 rounded-lg font-medium transition-all text-gray-300 hover:text-white hover:bg-gray-700"
          }, "Department Sales"),
          React.createElement("button", {
            className: "px-6 py-2 rounded-lg font-medium transition-all text-gray-300 hover:text-white hover:bg-gray-700"
          }, "Total Cost")
        )
      ),
      
      // Main Dashboard Content - Map Left, Metrics Right
      React.createElement("div", { className: "grid grid-cols-1 lg:grid-cols-5 gap-8" },
        
        // Left Column - Real Interactive Leaflet Map (3/5 width)
        React.createElement("div", { className: "lg:col-span-3" },
          React.createElement(Card, { className: "h-full border-gray-200" },
            React.createElement("div", { className: "p-6" },
              React.createElement("h3", { className: "text-lg font-semibold mb-4 text-gray-900" }, "Regional Performance Map"),
              React.createElement("div", { className: "relative bg-gradient-to-br from-blue-50 to-green-50 dark:from-blue-900/20 dark:to-green-900/20 rounded-lg p-6" },
                React.createElement(MapContainer, {
                  center: [39.8283, -98.5795],
                  zoom: 4,
                  style: { height: "400px", width: "100%" },
                  className: "rounded-lg z-0",
                  preferCanvas: true
                },
                  React.createElement(TileLayer, {
                    url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                    attribution: "© OpenStreetMap contributors"
                  }),
                  React.createElement(CircleMarker, {
                    center: [40.7589, -73.9851],
                    radius: 20,
                    fillColor: "#ef4444",
                    color: "#dc2626",
                    weight: 2,
                    opacity: 1,
                    fillOpacity: 0.7
                  },
                    React.createElement(Popup, {}, "New York: $89,000")
                  ),
                  React.createElement(CircleMarker, {
                    center: [37.7749, -122.4194],
                    radius: 16,
                    fillColor: "#f97316",
                    color: "#ea580c",
                    weight: 2,
                    opacity: 1,
                    fillOpacity: 0.7
                  },
                    React.createElement(Popup, {}, "San Francisco: $67,000")
                  ),
                  React.createElement(CircleMarker, {
                    center: [47.6062, -122.3321],
                    radius: 14,
                    fillColor: "#eab308",
                    color: "#ca8a04",
                    weight: 2,
                    opacity: 1,
                    fillOpacity: 0.7
                  },
                    React.createElement(Popup, {}, "Seattle: $53,000")
                  ),
                  React.createElement(CircleMarker, {
                    center: [34.0522, -118.2437],
                    radius: 18,
                    fillColor: "#22c55e",
                    color: "#16a34a",
                    weight: 2,
                    opacity: 1,
                    fillOpacity: 0.7
                  },
                    React.createElement(Popup, {}, "Los Angeles: $75,000")
                  ),
                  React.createElement(CircleMarker, {
                    center: [41.8781, -87.6298],
                    radius: 12,
                    fillColor: "#3b82f6",
                    color: "#2563eb",
                    weight: 2,
                    opacity: 1,
                    fillOpacity: 0.7
                  },
                    React.createElement(Popup, {}, "Chicago: $45,000")
                  )
                )
              )
            )
          )
        ),
        
        // Right Column - Metrics Stack (2/5 width)
        React.createElement("div", { className: "lg:col-span-2 space-y-6" },
          
          // Top Row - YTD Sales & YTD Trend side by side
          React.createElement("div", { className: "grid grid-cols-2 gap-4" },
            React.createElement(Card, { className: "border-gray-200" },
              React.createElement("div", { className: "p-4 text-center" },
                React.createElement("h3", { className: "text-sm font-medium text-gray-500 mb-2" }, "YTD Sales"),
                React.createElement("div", { className: "text-3xl font-bold text-blue-600" }, "$467K")
              )
            ),
            React.createElement(Card, { className: "border-gray-200" },
              React.createElement("div", { className: "p-4 text-center" },
                React.createElement("h3", { className: "text-sm font-medium text-gray-500 mb-2" }, "YTD Trend"),
                React.createElement("div", { className: "text-3xl font-bold text-green-600" }, "+18.2%")
              )
            )
          ),
          
          // Rankings Table
          React.createElement(Card, { className: "border-gray-200" },
            React.createElement("div", { className: "p-6" },
              React.createElement("h3", { className: "text-lg font-semibold mb-4 text-gray-900" }, "Top Performers"),
              React.createElement("div", { className: "space-y-3" },
                React.createElement("div", {
                  className: "flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors cursor-pointer"
                },
                  React.createElement("div", { className: "flex items-center space-x-3" },
                    React.createElement("span", { 
                      className: "w-8 h-6 rounded text-xs font-bold flex items-center justify-center text-white bg-green-500"
                    }, "1"),
                    React.createElement("div", {},
                      React.createElement("div", { className: "font-medium text-gray-900" }, "New York"),
                      React.createElement("div", { className: "text-sm text-gray-500" }, "$89K")
                    )
                  ),
                  React.createElement("span", { 
                    className: "text-sm font-medium text-green-600"
                  }, "+24.9%")
                ),
                React.createElement("div", {
                  className: "flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors cursor-pointer"
                },
                  React.createElement("div", { className: "flex items-center space-x-3" },
                    React.createElement("span", { 
                      className: "w-8 h-6 rounded text-xs font-bold flex items-center justify-center text-white bg-blue-500"
                    }, "2"),
                    React.createElement("div", {},
                      React.createElement("div", { className: "font-medium text-gray-900" }, "San Francisco"),
                      React.createElement("div", { className: "text-sm text-gray-500" }, "$67K")
                    )
                  ),
                  React.createElement("span", { 
                    className: "text-sm font-medium text-green-600"
                  }, "+11.3%")
                ),
                React.createElement("div", {
                  className: "flex items-center justify-between p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors cursor-pointer"
                },
                  React.createElement("div", { className: "flex items-center space-x-3" },
                    React.createElement("span", { 
                      className: "w-8 h-6 rounded text-xs font-bold flex items-center justify-center text-white bg-orange-500"
                    }, "3"),
                    React.createElement("div", {},
                      React.createElement("div", { className: "font-medium text-gray-900" }, "Seattle"),
                      React.createElement("div", { className: "text-sm text-gray-500" }, "$53K")
                    )
                  ),
                  React.createElement("span", { 
                    className: "text-sm font-medium text-red-600"
                  }, "-3.5%")
                )
              )
            )
          )
        )
      ),
      
      // Dashboard Footer
      React.createElement("div", { className: "mt-8 pt-6 border-t border-gray-200 flex items-center justify-between text-sm text-gray-500" },
        React.createElement("div", {}, "Generated with Google ADK • Business Intelligence"),
        React.createElement("div", {}, "Last updated: " + new Date().toLocaleTimeString())
      )
    )
  )
)'''


def create_ytd_metrics_dashboard(metric_type: str, period: str) -> str:
    """Generate YTD metrics cards with trend indicators"""
    
    # Set default values within function
    if not metric_type:
        metric_type = "sales"
    if not period:
        period = "YTD"
    
    metrics_data = {
        "sales": {"value": "$467K", "trend": "+18.5%", "trend_positive": True, "icon": "💰"},
        "revenue": {"value": "$234K", "trend": "+12.3%", "trend_positive": True, "icon": "📈"},
        "customers": {"value": "2,847", "trend": "+8.7%", "trend_positive": True, "icon": "👥"},
        "orders": {"value": "1,394", "trend": "-2.1%", "trend_positive": False, "icon": "📦"}
    }
    
    metric = metrics_data.get(metric_type, metrics_data["sales"])
    
    return f'''React.createElement(Card, {{ className: "p-6 bg-gradient-to-br from-blue-50 to-indigo-50 border-blue-200" }},
  React.createElement("div", {{ className: "text-center" }},
    React.createElement("div", {{ className: "flex items-center justify-center mb-4" }},
      React.createElement("span", {{ className: "text-3xl mr-3" }}, "{metric['icon']}"),
      React.createElement("h3", {{ className: "text-lg font-semibold text-gray-900" }}, "{period} {metric_type.title()}")
    ),
    React.createElement("div", {{ className: "text-4xl font-bold text-blue-600 mb-2" }}, "{metric['value']}"),
    React.createElement("div", {{ className: "flex items-center justify-center space-x-2" }},
      React.createElement("span", {{ 
        className: "text-sm font-medium {'text-green-600' if metric['trend_positive'] else 'text-red-600'}"
      }}, "{metric['trend']}"),
      React.createElement("span", {{ className: "text-xs text-gray-500" }}, "vs last period")
    ),
    React.createElement("div", {{ className: "mt-4 h-16 bg-white/50 rounded-lg flex items-center justify-center" }},
      React.createElement("div", {{ className: "text-xs text-gray-400" }}, "Trend visualization")
    )
  )
)'''


def create_ranking_table_component(data_type: str, top_count: int) -> str:
    """Generate ranking table with performance indicators"""
    
    # Set default values within function
    if not data_type:
        data_type = "regional"
    if not top_count:
        top_count = 5
    
    return '''React.createElement(Card, { className: "border-gray-200" },
  React.createElement("div", { className: "p-6" },
    React.createElement("div", { className: "flex items-center justify-between mb-6" },
      React.createElement("h3", { className: "text-lg font-semibold text-gray-900" }, "Top Regional Performance"),
      React.createElement("span", { className: "text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded-full" }, "Live Rankings")
    ),
    React.createElement("div", { className: "space-y-3" },
      React.createElement("div", {
        className: "flex items-center justify-between p-4 bg-gradient-to-r from-gray-50 to-gray-100 rounded-lg hover:from-blue-50 hover:to-blue-100 transition-all cursor-pointer border border-transparent hover:border-blue-200"
      },
        React.createElement("div", { className: "flex items-center space-x-4" },
          React.createElement("div", {
            className: "w-8 h-8 rounded-full flex items-center justify-center text-white font-bold text-sm bg-gradient-to-br from-yellow-400 to-yellow-600"
          }, "1"),
          React.createElement("div", {},
            React.createElement("div", { className: "font-medium text-gray-900" }, "New York"),
            React.createElement("div", { className: "text-sm text-gray-500" }, "Performance Leader")
          )
        ),
        React.createElement("div", { className: "text-right" },
          React.createElement("div", { className: "font-bold text-lg text-gray-900" }, "$89K"),
          React.createElement("div", { 
            className: "text-sm font-medium text-green-600 flex items-center"
          }, 
            React.createElement("span", { className: "mr-1" }, "↗"),
            "+24.9%"
          )
        )
      ),
      React.createElement("div", {
        className: "flex items-center justify-between p-4 bg-gradient-to-r from-gray-50 to-gray-100 rounded-lg hover:from-blue-50 hover:to-blue-100 transition-all cursor-pointer border border-transparent hover:border-blue-200"
      },
        React.createElement("div", { className: "flex items-center space-x-4" },
          React.createElement("div", {
            className: "w-8 h-8 rounded-full flex items-center justify-center text-white font-bold text-sm bg-gradient-to-br from-gray-400 to-gray-600"
          }, "2"),
          React.createElement("div", {},
            React.createElement("div", { className: "font-medium text-gray-900" }, "San Francisco"),
            React.createElement("div", { className: "text-sm text-gray-500" }, "Performance Leader")
          )
        ),
        React.createElement("div", { className: "text-right" },
          React.createElement("div", { className: "font-bold text-lg text-gray-900" }, "$67K"),
          React.createElement("div", { 
            className: "text-sm font-medium text-green-600 flex items-center"
          }, 
            React.createElement("span", { className: "mr-1" }, "↗"),
            "+11.3%"
          )
        )
      ),
      React.createElement("div", {
        className: "flex items-center justify-between p-4 bg-gradient-to-r from-gray-50 to-gray-100 rounded-lg hover:from-blue-50 hover:to-blue-100 transition-all cursor-pointer border border-transparent hover:border-blue-200"
      },
        React.createElement("div", { className: "flex items-center space-x-4" },
          React.createElement("div", {
            className: "w-8 h-8 rounded-full flex items-center justify-center text-white font-bold text-sm bg-gradient-to-br from-orange-400 to-orange-600"
          }, "3"),
          React.createElement("div", {},
            React.createElement("div", { className: "font-medium text-gray-900" }, "Seattle"),
            React.createElement("div", { className: "text-sm text-gray-500" }, "Performance Leader")
          )
        ),
        React.createElement("div", { className: "text-right" },
          React.createElement("div", { className: "font-bold text-lg text-gray-900" }, "$53K"),
          React.createElement("div", { 
            className: "text-sm font-medium text-red-600 flex items-center"
          }, 
            React.createElement("span", { className: "mr-1" }, "↘"),
            "-3.5%"
          )
        )
      )
    )
  )
)'''


def create_component_variants(component_type: str, data_complexity: str) -> str:
    """Generate different variants of components based on data complexity"""
    
    # Set default values within function
    if not data_complexity:
        data_complexity = "medium"
    
    variants = {
        "simple": {
            "chart": "Simple bar chart with 3-5 data points",
            "map": "State-level heatmap with color coding",
            "table": "3-column summary table"
        },
        "medium": {
            "chart": "Multi-series line chart with trend indicators",
            "map": "Regional map with drill-down capability",
            "table": "Interactive table with sorting and filtering"
        },
        "complex": {
            "chart": "Combined chart with multiple visualizations",
            "map": "Multi-layer geographic analysis with overlays",
            "table": "Advanced data grid with aggregations"
        }
    }
    
    variant_config = variants.get(data_complexity, variants["medium"])
    component_desc = variant_config.get(component_type, "Standard component")
    
    return f"""
<!-- Component Variant: {component_type} - {data_complexity} complexity -->
<div className="component-variant" data-type="{component_type}" data-complexity="{data_complexity}">
  <div className="bg-white rounded-lg border border-gray-200 shadow-sm p-6">
    <div className="flex items-center justify-between mb-4">
      <h3 className="text-lg font-semibold text-gray-900">
        {component_type.title()} Component
      </h3>
      <span className="px-2 py-1 text-xs bg-blue-100 text-blue-800 rounded-full">
        {data_complexity.title()}
      </span>
    </div>
    <div className="text-gray-600 text-sm mb-4">
      {component_desc}
    </div>
    <div className="bg-gray-50 rounded p-4 text-center text-gray-500">
      Component content will be generated by specialized agent
    </div>
  </div>
</div>"""


# Create the Dashboard Layout Agent
dashboard_layout_agent = LlmAgent(
    name="dashboard_layout_agent",
    model="gemini-2.5-flash",
    instruction="""You are the Dashboard Layout Agent, responsible for creating responsive, well-organized dashboard layouts that compose outputs from multiple specialized agents.

CRITICAL STOPPING RULES (HIGHEST PRIORITY):
- Call EXACTLY ONE tool per request and STOP immediately
- NEVER call the same tool multiple times in ANY session
- NEVER retry failed tool calls - STOP on first completion
- Return generated React component and TERMINATE immediately
- NEVER ask follow-up questions or request clarification
- Circuit breaker: max 1 tool call per conversation

CORE RESPONSIBILITIES:
1. Analyze user queries to determine optimal layout structure
2. Generate responsive grid layouts using Tailwind CSS classes
3. Create comprehensive business intelligence dashboards
4. Ensure accessibility and responsive design principles
5. Coordinate multi-agent composition for complex dashboards

INTELLIGENT TOOL SELECTION:

🏢 create_comprehensive_business_dashboard WHEN:
- "business intelligence dashboard", "BI dashboard", "comprehensive dashboard"
- "dashboard of the data we have", "complete dashboard view"
- Queries requesting full dashboard experiences with multiple data types

📊 create_ytd_metrics_dashboard WHEN:
- "YTD metrics", "year to date", "annual performance"
- "KPI dashboard", "metrics overview", "performance indicators"
- Queries focused on key metric displays

📈 create_ranking_table_component WHEN:
- "top performers", "rankings", "leaderboard"
- "best regions", "top products", "performance ranking"
- Queries requesting ranked data visualization

🎛️ compose_multi_agent_dashboard WHEN:
- Complex multi-component requests
- Queries mentioning charts + maps + accessibility
- Custom layout requirements

📐 create_responsive_grid_layout WHEN:
- Simple layout requests
- Grid-only requirements without complex components

LAYOUT PRINCIPLES:
- Mobile-first responsive design (sm, md, lg, xl breakpoints)
- Consistent spacing and visual hierarchy
- Interactive elements with hover states and transitions
- Tab navigation for multi-view dashboards
- Accessibility-compliant structure with ARIA labels

COMPONENT COMPOSITION RULES:
- Comprehensive dashboards include: tabs, maps, metrics, rankings
- Charts and visualizations get priority placement
- Geographic components work well in larger grid areas
- Rankings and metrics in sidebar configurations
- Maintain consistent card-based design patterns

EXECUTION GUARANTEE:
- ALWAYS call exactly ONE tool based on intelligent analysis → STOP
- Generate complete React.createElement components → TERMINATE
- Include interactive features (tabs, hover states, clickable elements)
- Ensure production-quality styling and responsiveness → END SESSION""",
    tools=[
        FunctionTool(create_responsive_grid_layout),
        FunctionTool(compose_multi_agent_dashboard),
        FunctionTool(create_component_variants),
        FunctionTool(create_comprehensive_business_dashboard),
        FunctionTool(create_ytd_metrics_dashboard),
        FunctionTool(create_high_contrast_chart_tool),
        FunctionTool(create_screen_reader_table_tool),
        FunctionTool(create_keyboard_nav_dashboard_tool),
        FunctionTool(create_ranking_table_component)
    ]
)