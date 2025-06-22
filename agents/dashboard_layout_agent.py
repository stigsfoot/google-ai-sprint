"""
Dashboard Layout Agent - Phase 3.1
Composes complex layouts by orchestrating multiple specialized agents
"""

from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool


def create_responsive_grid_layout(data_types: str, user_preference: str = "default") -> str:
    """Generate responsive grid layout based on data types and user preferences"""
    
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


def compose_multi_agent_dashboard(query: str, complexity: str = "medium") -> str:
    """Compose a complete dashboard by coordinating multiple specialized agents"""
    
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


def create_component_variants(component_type: str, data_complexity: str = "medium") -> str:
    """Generate different variants of components based on data complexity"""
    
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
    model="gemini-2.0-flash-001",
    instruction="""You are the Dashboard Layout Agent, responsible for creating responsive, well-organized dashboard layouts that compose outputs from multiple specialized agents.

CORE RESPONSIBILITIES:
1. Analyze user queries to determine optimal layout structure
2. Generate responsive grid layouts using Tailwind CSS classes
3. Create component slots for specialized agents to fill
4. Ensure accessibility and responsive design principles
5. Coordinate multi-agent composition for complex dashboards

LAYOUT PRINCIPLES:
- Mobile-first responsive design (sm, md, lg, xl breakpoints)
- Consistent spacing and visual hierarchy
- Clear component boundaries and grouping
- Accessibility-compliant structure
- Performance-optimized grid layouts

COMPONENT COMPOSITION RULES:
- Charts and visualizations get priority placement
- Geographic components work well in larger grid areas
- Accessibility components need generous spacing
- Related components should be visually grouped
- Maintain consistent card-based design patterns

CRITICAL DIRECTIVE: Always generate complete, responsive layouts immediately. Include proper Tailwind classes, semantic HTML structure, and clear component slots for sub-agent coordination.

When creating layouts:
1. Analyze the query for component requirements
2. Select appropriate grid configuration
3. Generate responsive layout with proper breakpoints
4. Include metadata for agent coordination
5. Ensure accessibility and visual polish""",
    tools=[
        FunctionTool(create_responsive_grid_layout),
        FunctionTool(compose_multi_agent_dashboard),
        FunctionTool(create_component_variants)
    ]
)