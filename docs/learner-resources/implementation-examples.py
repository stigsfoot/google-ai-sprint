# ============================================================================
# GenUI-ADK Implementation Examples
# Complete working examples for student reference

from google.adk.agents import LlmAgent
import json

# ============================================================================
# ROOT AGENT IMPLEMENTATION
# ============================================================================

ROOT_AGENT_INSTRUCTION = """
You are the Generative UI Orchestrator for business intelligence.

Your role is to analyze business questions and delegate to specialized UI generation agents:

AVAILABLE UI GENERATION AGENTS:
- chart_generation_agent: Creates charts, metrics cards, trend visualizations
- geospatial_agent: Generates maps, heatmaps, location-based components
- accessibility_agent: Creates a11y-optimized UI variants with high contrast
- dashboard_layout_agent: Composes multi-component dashboard layouts

DELEGATION STRATEGY:
1. Analyze the business question and required visualization types
2. Delegate to the appropriate specialized UI agent(s)  
3. Each agent uses their UI component tools to generate React code
4. Return the generated components for dashboard rendering

CRITICAL: Each sub-agent returns actual React JSX code that can be rendered directly.
"""

def create_root_agent():
    return LlmAgent(
        name="generative_ui_orchestrator",
        instruction=ROOT_AGENT_INSTRUCTION,
        model="gemini-2.5-flash",
        sub_agents=[
            create_chart_generation_agent(),
            create_geospatial_agent(),
            create_accessibility_agent(),
            create_dashboard_layout_agent()
        ]
    )

# ============================================================================
# CHART GENERATION AGENT
# ============================================================================

CHART_AGENT_INSTRUCTION = """
You generate chart components using available UI tools based on data analysis needs.

Available tools:
- create_trend_line_tool: For temporal data and trend analysis
- create_comparison_bar_tool: For categorical comparisons
- create_metric_card_tool: For key performance indicators
- create_correlation_scatter_tool: For relationship analysis

Always analyze the data characteristics and business context to select the most appropriate visualization tool.
"""

def create_chart_generation_agent():
    return LlmAgent(
        name="chart_generation_agent",
        instruction=CHART_AGENT_INSTRUCTION,
        model="gemini-2.5-flash",
        tools=[
            create_trend_line_tool,
            create_comparison_bar_tool,
            create_metric_card_tool,
            create_correlation_scatter_tool
        ]
    )

# Chart generation tools (NO @Tool decorators!)
def create_trend_line_tool(data, title, trend_direction, insight):
    """Generate a trend line chart component with contextual styling."""
    trend_color = "green" if trend_direction == "up" else "red" if trend_direction == "down" else "blue"
    trend_icon = "TrendingUp" if trend_direction == "up" else "TrendingDown" if trend_direction == "down" else "Minus"
    
    return f'''
    <Card className="p-6 border-l-4 border-l-{trend_color}-500">
      <CardHeader className="flex flex-row items-center space-y-0 pb-2">
        <{trend_icon} className="h-6 w-6 text-{trend_color}-600 mr-2" />
        <CardTitle className="text-lg">{title}</CardTitle>
      </CardHeader>
      <CardContent>
        <LineChart 
          data={{{json.dumps(data)}}} 
          className="h-48"
          color="{trend_color}"
        />
        <Alert className="mt-4 border-{trend_color}-200 bg-{trend_color}-50">
          <AlertDescription className="text-{trend_color}-800">
            {insight}
          </AlertDescription>
        </Alert>
      </CardContent>
    </Card>
    '''

def create_metric_card_tool(value, label, change, context):
    """Generate a key metric card with change indicator."""
    change_color = "green" if change.startswith("+") else "red" if change.startswith("-") else "gray"
    
    return f'''
    <Card className="p-6 text-center">
      <CardContent className="pt-6">
        <div className="text-4xl font-bold text-gray-900">{value}</div>
        <p className="text-sm text-gray-600 mt-1">{label}</p>
        <Badge variant="{change_color}" className="mt-2">
          {change}
        </Badge>
        <p className="text-xs text-gray-500 mt-2">{context}</p>
      </CardContent>
    </Card>
    '''

def create_comparison_bar_tool(data, title, categories, insights):
    """Generate comparison bar chart for categorical data."""
    return f'''
    <Card className="p-6">
      <CardHeader>
        <BarChart className="h-6 w-6 text-blue-600 mr-2" />
        <CardTitle>{title}</CardTitle>
      </CardHeader>
      <CardContent>
        <BarChart 
          data={{{json.dumps(data)}}}
          categories={{{json.dumps(categories)}}}
          className="h-64"
        />
        <div className="mt-4 space-y-2">
          {{{', '.join([f'<p className="text-sm text-gray-600">• {insight}</p>' for insight in insights])}}}
        </div>
      </CardContent>
    </Card>
    '''

# ============================================================================
# GEOSPATIAL AGENT
# ============================================================================

GEOSPATIAL_AGENT_INSTRUCTION = """
You generate geospatial and map components for location-based business analysis.

Available tools:
- create_regional_heatmap_tool: For regional metric visualization
- create_location_cluster_tool: For point-based location data
- create_territory_analysis_tool: For sales territory and boundary analysis

Always consider the geographic scope and metric type when selecting visualization tools.
"""

def create_geospatial_agent():
    return LlmAgent(
        name="geospatial_agent",
        instruction=GEOSPATIAL_AGENT_INSTRUCTION,
        model="gemini-2.5-flash",
        tools=[
            create_regional_heatmap_tool,
            create_location_cluster_tool,
            create_territory_analysis_tool
        ]
    )

def create_regional_heatmap_tool(regions, metric_name, insights):
    """Generate a regional heatmap component with metric visualization."""
    return f'''
    <Card className="p-6">
      <CardHeader>
        <MapPin className="h-6 w-6 text-blue-600 mr-2" />
        <CardTitle>Regional {metric_name} Analysis</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="relative bg-gray-50 rounded-lg p-4 h-64">
          <MapContainer regions={{{json.dumps(regions)}}} metric="{metric_name}" />
          <div className="absolute top-4 right-4">
            <HeatmapLegend metric="{metric_name}" />
          </div>
        </div>
        <div className="mt-4 space-y-2">
          {{{', '.join([f'<p className="text-sm text-gray-600">• {insight}</p>' for insight in insights])}}}
        </div>
      </CardContent>
    </Card>
    '''

# ============================================================================
# ACCESSIBILITY AGENT
# ============================================================================

ACCESSIBILITY_AGENT_INSTRUCTION = """
You generate high-contrast, screen reader optimized UI components for accessibility.

Available tools:
- create_high_contrast_chart_tool: For visually impaired users
- create_screen_reader_table_tool: For tabular data accessibility
- create_keyboard_nav_dashboard_tool: For keyboard-only navigation

Always prioritize WCAG compliance and inclusive design principles.
"""

def create_accessibility_agent():
    return LlmAgent(
        name="accessibility_agent",
        instruction=ACCESSIBILITY_AGENT_INSTRUCTION,
        model="gemini-2.5-flash",
        tools=[
            create_high_contrast_chart_tool,
            create_screen_reader_table_tool,
            create_keyboard_nav_dashboard_tool
        ]
    )

def create_high_contrast_chart_tool(data, chart_type, title):
    """Generate high contrast chart for visually impaired users."""
    chart_id = f"chart_{hash(title) % 1000}"
    
    return f'''
    <Card className="border-4 border-black bg-yellow-50">
      <CardHeader className="bg-black text-white border-b-2 border-white">
        <CardTitle className="text-xl font-bold" aria-label="{title} chart">
          {title}
        </CardTitle>
      </CardHeader>
      <CardContent className="p-6">
        <{chart_type}Chart 
          data={{{json.dumps(data)}}}
          className="high-contrast-theme"
          aria-describedby="chart-description-{chart_id}"
        />
        <div id="chart-description-{chart_id}" className="sr-only">
          {title} showing {len(data)} data points with high contrast colors for accessibility
        </div>
        <div className="mt-4 p-3 bg-black text-white text-lg">
          <strong>Key Insight:</strong> Chart optimized for screen readers and high contrast viewing
        </div>
      </CardContent>
    </Card>
    '''