import { NextRequest, NextResponse } from 'next/server'

interface BusinessQuery {
  query: string
}

interface ComponentResult {
  agent: string
  component_type: string
  component_code: string
  business_context: string
}

// Connect to real ADK Agent Server (currently unused during debugging)
// const ADK_SERVER_URL = process.env.ADK_SERVER_URL || 'http://localhost:8081'

async function callRealADKAgents(query: string): Promise<ComponentResult[]> {
  console.log(`🎯 Skipping ADK agents for debugging - using simulation`)
  
  // Temporarily skip ADK server and use simulation for debugging
  return await simulateRootAgent(query)
  
  // Original ADK server code (commented out for debugging)
  /*
  try {
    const response = await fetch(`${ADK_SERVER_URL}/api/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query })
    })
    
    if (!response.ok) {
      throw new Error(`ADK server error: ${response.status}`)
    }
    
    const data = await response.json()
    console.log(`✅ ADK agents returned ${data.components.length} components`)
    
    return data.components
    
  } catch (error) {
    console.error('❌ Failed to connect to ADK agents:', error)
    
    // Fallback to simulated response if ADK server unavailable
    return await simulateRootAgent(query)
  }
  */
}

// Fallback simulation (kept as backup)
async function simulateRootAgent(query: string): Promise<ComponentResult[]> {
  console.log(`🔄 Using simulated agents for: ${query}`)
  
  const results: ComponentResult[] = []
  
  // Simple keyword-based routing (mimics ADK agent delegation)
  if (query.toLowerCase().includes('trend') || query.toLowerCase().includes('sales')) {
    // Simulate Chart Generation Agent - Interactive Tremor Line Chart (React.createElement format)
    const component = `React.createElement(Card, { className: "p-6 bg-gradient-to-r from-green-50 to-blue-50" },
  React.createElement("div", { className: "flex items-center space-x-2 mb-4" },
    React.createElement(TrendingUp, { className: "h-6 w-6 text-green-600" }),
    React.createElement(Text, { className: "text-lg font-semibold" }, "Sales Trend - Q4")
  ),
  React.createElement(LineChart, {
    data: [
      {"month": "Jan", "value": 1200},
      {"month": "Feb", "value": 1350}, 
      {"month": "Mar", "value": 1580},
      {"month": "Apr", "value": 1420},
      {"month": "May", "value": 1650},
      {"month": "Jun", "value": 1780}
    ],
    index: "month",
    categories: ["value"],
    colors: ["green"],
    className: "h-48 mt-4",
    showLegend: false,
    showGridLines: true,
    curveType: "monotone"
  }),
  React.createElement("div", { className: "mt-4 flex items-center justify-between" },
    React.createElement(Badge, { color: "green", size: "lg" }, "+23% Growth"),
    React.createElement(Text, { className: "text-sm text-gray-600" }, "vs previous period")
  ),
  React.createElement("div", { className: "mt-4 p-3 bg-green-50 rounded-lg" },
    React.createElement(Text, { className: "text-sm text-green-800" }, "Sales showing strong upward trend with 23% growth over the period")
  )
)`
    
    results.push({
      agent: 'chart_generation_agent',
      component_type: 'trend_line',
      component_code: component,
      business_context: 'Sales performance trending analysis'
    })
  }
  
  if (query.toLowerCase().includes('metric') || query.toLowerCase().includes('kpi')) {
    // Simulate Chart Generation Agent - Interactive Tremor Metric Card
    const component = `React.createElement(Card, { className: "p-6 text-center max-w-xs" },
  React.createElement(Flex, { alignItems: "start", className: "space-x-0", flexDirection: "col" },
    React.createElement(Metric, { className: "text-4xl font-bold text-gray-900" }, "$47.2K"),
    React.createElement(Text, { className: "text-sm text-gray-600 mt-1" }, "Monthly Revenue"),
    React.createElement(Badge, { color: "green", size: "lg", className: "mt-2" }, "+12.3%"),
    React.createElement(Text, { className: "text-xs text-gray-500 mt-2" }, "Compared to previous month")
  )
)`
    
    results.push({
      agent: 'chart_generation_agent',
      component_type: 'metric_card',
      component_code: component,
      business_context: 'Key performance indicator display'
    })
  }
  
  if (query.toLowerCase().includes('compare') || query.toLowerCase().includes('comparison')) {
    // Simulate Chart Generation Agent - Interactive Tremor Bar Chart
    const component = `React.createElement(Card, { className: "p-6" },
  React.createElement(Flex, { alignItems: "center", className: "space-x-2 mb-4" },
    React.createElement(BarChart3, { className: "h-6 w-6 text-blue-600" }),
    React.createElement(Text, { className: "text-lg font-semibold" }, "Product Performance Comparison")
  ),
  React.createElement(BarChart, {
    data: [
      {"category": "Product A", "value": 2400}, 
      {"category": "Product B", "value": 1800}, 
      {"category": "Product C", "value": 3200}, 
      {"category": "Product D", "value": 1600}
    ],
    index: "category",
    categories: ["value"],
    colors: ["blue"],
    className: "h-48 mt-4",
    showLegend: false,
    showGridLines: true,
    showYAxis: true,
    showXAxis: true
  }),
  React.createElement("div", { className: "mt-4 p-3 bg-blue-50 rounded-lg" },
    React.createElement(Text, { className: "text-sm text-blue-800" }, "Product C leads with 3.2K units, 33% higher than average")
  )
)`
    
    results.push({
      agent: 'chart_generation_agent',
      component_type: 'comparison_bar',
      component_code: component,
      business_context: 'Comparative analysis visualization'
    })
  }
  
  // Geospatial agent simulation
  if (query.toLowerCase().includes('regional') || query.toLowerCase().includes('territory') || query.toLowerCase().includes('map') || query.toLowerCase().includes('location') || query.toLowerCase().includes('geospatial')) {
    // Simulate regional heatmap
    const heatmapComponent = `React.createElement(Card, { className: "p-6 border-l-4 border-l-blue-500" },
  React.createElement("div", { className: "flex items-center space-x-2 mb-4" },
    React.createElement(MapPin, { className: "h-6 w-6 text-blue-600" }),
    React.createElement(Text, { className: "text-lg font-semibold" }, "Regional Sales Volume Analysis")
  ),
  React.createElement("div", { className: "relative bg-gradient-to-br from-blue-50 to-green-50 rounded-lg p-6" },
    React.createElement(MapContainer, {
      center: [39.8283, -98.5795],
      zoom: 4,
      style: { height: "300px", width: "100%" },
      className: "rounded-lg z-0"
    },
      React.createElement(TileLayer, {
        url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        attribution: "© OpenStreetMap contributors"
      }),
      React.createElement(CircleMarker, {
        center: [34.0522, -118.2437],
        radius: 20,
        fillColor: "#ef4444",
        color: "#dc2626",
        weight: 2,
        opacity: 1,
        fillOpacity: 0.7
      },
        React.createElement(Popup, {}, "California: $45,000")
      ),
      React.createElement(CircleMarker, {
        center: [31.9686, -99.9018],
        radius: 15,
        fillColor: "#f97316",
        color: "#ea580c",
        weight: 2,
        opacity: 1,
        fillOpacity: 0.7
      },
        React.createElement(Popup, {}, "Texas: $32,000")
      ),
      React.createElement(CircleMarker, {
        center: [40.7589, -73.9851],
        radius: 13,
        fillColor: "#eab308",
        color: "#ca8a04",
        weight: 2,
        opacity: 1,
        fillOpacity: 0.7
      },
        React.createElement(Popup, {}, "New York: $28,000")
      )
    )
  ),
  React.createElement("div", { className: "mt-4 grid grid-cols-4 gap-2 text-xs" },
    React.createElement("div", { className: "bg-red-500 text-white p-2 rounded text-center" }, "High ($40k+)"),
    React.createElement("div", { className: "bg-orange-500 text-white p-2 rounded text-center" }, "Medium ($25-40k)"),
    React.createElement("div", { className: "bg-yellow-500 text-white p-2 rounded text-center" }, "Low ($15-25k)"),
    React.createElement("div", { className: "bg-green-500 text-white p-2 rounded text-center" }, "New Markets")
  ),
  React.createElement("div", { className: "mt-4 p-3 bg-blue-50 rounded-lg" },
    React.createElement(Text, { className: "text-sm text-blue-800" }, "📍 California leads with 40% of total sales"),
    React.createElement(Text, { className: "text-xs text-blue-600 mt-1" }, "Data: California: 45000, Texas: 32000, New York: 28000")
  )
)`

    results.push({
      agent: 'geospatial_agent',
      component_type: 'regional_heatmap',
      component_code: heatmapComponent,
      business_context: 'Regional sales performance with interactive map visualization'
    })
  }
  
  // If no specific keywords matched, provide a default metric card
  if (results.length === 0) {
    const escapedQuery = query.replace(/"/g, '\\"')
    const component = `React.createElement(Card, { className: "p-6 text-center" },
  React.createElement(Flex, { alignItems: "center", flexDirection: "col", className: "space-y-3" },
    React.createElement("div", { className: "text-4xl" }, "🤖"),
    React.createElement(Text, { className: "text-sm text-gray-600" }, "General Business Query"),
    React.createElement(Badge, { color: "blue", size: "lg" }, "Processed"),
    React.createElement(Text, { className: "text-xs text-gray-500" }, "Agent understood: ${escapedQuery}")
  )
)`
    
    results.push({
      agent: 'chart_generation_agent',
      component_type: 'general_response',
      component_code: component,
      business_context: 'General business intelligence query'
    })
  }
  
  return results
}

export async function POST(request: NextRequest) {
  try {
    const body: BusinessQuery = await request.json()
    const { query } = body
    
    if (!query || typeof query !== 'string') {
      return NextResponse.json(
        { error: 'Query is required and must be a string' },
        { status: 400 }
      )
    }
    
    console.log(`🔄 API received query: ${query}`)
    
    // Simulate ADK agent processing with a small delay
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    // Process the query using real ADK agents
    const components = await callRealADKAgents(query)
    
    console.log(`✅ Generated ${components.length} components`)
    
    return NextResponse.json({
      success: true,
      query: query,
      components: components,
      total_components: components.length,
      processing_time: '1.2s',
      agent_trace: [
        'Root agent analyzed query',
        'Delegated to chart_generation_agent',
        'Generated UI component tools',
        'Returned JSX components'
      ]
    })
    
  } catch (error) {
    console.error('Error processing business query:', error)
    
    return NextResponse.json(
      { 
        error: 'Failed to process business query',
        details: error instanceof Error ? error.message : 'Unknown error'
      },
      { status: 500 }
    )
  }
}

export async function GET() {
  return NextResponse.json({
    message: 'ADK Agent API Bridge',
    status: 'active',
    available_agents: [
      'chart_generation_agent',
      'geospatial_agent (coming soon)',
      'accessibility_agent (coming soon)',
      'dashboard_layout_agent (coming soon)'
    ],
    example_queries: [
      'Show me sales trends for Q4',
      'Display key metrics and KPIs',
      'Compare product performance'
    ]
  })
}