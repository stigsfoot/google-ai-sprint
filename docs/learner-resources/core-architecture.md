# GenUI-ADK Core Architecture Reference

## Overview
GenUI-ADK treats React UI components as callable tools within Google ADK agents. Instead of building traditional UIs, specialized agents generate components dynamically through intelligent tool composition.

## Key Innovation
```python
# Traditional React Component
def SalesDashboard(props):
    return <Card><LineChart data={props.data} /></Card>

# GenUI ADK Tool (NO @Tool decorator!)
def create_sales_dashboard_tool(data, insights, trend_direction):
    """Tool that generates sales dashboard component"""
    return f'''
    <Card className="p-6 border-l-4 border-l-{trend_direction}-500">
      <CardHeader>
        <CardTitle>Sales Performance</CardTitle>
      </CardHeader>
      <CardContent>
        <LineChart data={{{json.dumps(data)}}} />
        <Alert className="mt-4">
          <AlertDescription>{insights[0]}</AlertDescription>
        </Alert>
      </CardContent>
    </Card>
    '''
Agent Hierarchy
Root Agent: generative_ui_orchestrator
├── chart_generation_agent
│   ├── create_trend_line_tool()
│   ├── create_metric_card_tool()
│   └── create_comparison_bar_tool()
├── geospatial_agent  
│   ├── create_regional_heatmap_tool()
│   └── create_location_cluster_tool()
├── accessibility_agent
│   ├── create_high_contrast_chart_tool()
│   └── create_screen_reader_table_tool()
└── dashboard_layout_agent
    ├── create_grid_layout_tool()
    └── create_responsive_container_tool()
Technology Stack

Agent Framework: Google ADK + Gemini 2.0 Flash
UI Generation: React components as ADK tools returning JSX strings
Dashboard: Next.js for rendering agent-generated components
Development: ADK Web Interface for tracing and evaluation

Core Learning Objectives

Understand UI components as callable ADK tools
Design specialized agents with focused responsibilities
Implement tool composition for complex UI generation
Master ADK delegation and evaluation patterns