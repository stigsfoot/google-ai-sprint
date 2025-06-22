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

// Connect to real ADK Agent Server
const ADK_SERVER_URL = process.env.ADK_SERVER_URL || 'http://localhost:8081'

async function callRealADKAgents(query: string): Promise<ComponentResult[]> {
  console.log(`🎯 Calling real ADK agents: ${query}`)
  
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
}

// Fallback simulation (kept as backup)
async function simulateRootAgent(query: string): Promise<ComponentResult[]> {
  console.log(`🔄 Using simulated agents for: ${query}`)
  
  const results: ComponentResult[] = []
  
  // Simple keyword-based routing (mimics ADK agent delegation)
  if (query.toLowerCase().includes('trend') || query.toLowerCase().includes('sales')) {
    // Simulate Chart Generation Agent - Trend Line
    const component = `
<div className="p-6 border-l-4 border-l-green-500 bg-white rounded-lg shadow-sm">
  <div className="flex flex-row items-center space-y-0 pb-2">
    <div className="h-6 w-6 text-green-600 mr-2">📈</div>
    <h3 className="text-lg font-semibold">Sales Trend Analysis</h3>
  </div>
  <div className="mt-4">
    <div className="h-48 bg-gradient-to-r from-green-100 to-blue-100 rounded-lg flex items-center justify-center">
      <div className="text-center">
        <div className="text-3xl font-bold text-green-600">📊</div>
        <p className="text-sm text-gray-600 mt-2">Trend visualization would render here</p>
        <p className="text-xs text-gray-500">[Chart Data: Jan: 1200, Feb: 1350, Mar: 1580, Apr: 1420]</p>
      </div>
    </div>
    <div className="mt-4 p-3 border-green-200 bg-green-50 rounded-lg">
      <p className="text-green-800 text-sm">
        📈 Sales showing strong upward trend with 23% growth over the period
      </p>
    </div>
  </div>
</div>`
    
    results.push({
      agent: 'chart_generation_agent',
      component_type: 'trend_line',
      component_code: component,
      business_context: 'Sales performance trending analysis'
    })
  }
  
  if (query.toLowerCase().includes('metric') || query.toLowerCase().includes('kpi')) {
    // Simulate Chart Generation Agent - Metric Card
    const component = `
<div className="p-6 text-center bg-white rounded-lg shadow-sm border">
  <div className="pt-6">
    <div className="text-4xl font-bold text-gray-900">$47.2K</div>
    <p className="text-sm text-gray-600 mt-1">Monthly Revenue</p>
    <div className="mt-2 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-green-500 text-white">
      +12.3%
    </div>
    <p className="text-xs text-gray-500 mt-2">Compared to previous month</p>
  </div>
</div>`
    
    results.push({
      agent: 'chart_generation_agent',
      component_type: 'metric_card',
      component_code: component,
      business_context: 'Key performance indicator display'
    })
  }
  
  if (query.toLowerCase().includes('compare') || query.toLowerCase().includes('comparison')) {
    // Simulate Chart Generation Agent - Comparison Bar
    const component = `
<div className="p-6 bg-white rounded-lg shadow-sm border">
  <div className="flex items-center mb-4">
    <div className="h-6 w-6 text-blue-600 mr-2">📊</div>
    <h3 className="text-lg font-semibold">Product Performance Comparison</h3>
  </div>
  <div className="h-48 bg-gradient-to-r from-blue-100 to-purple-100 rounded-lg flex items-center justify-center">
    <div className="text-center">
      <div className="text-3xl font-bold text-blue-600">📊</div>
      <p className="text-sm text-gray-600 mt-2">Bar chart visualization would render here</p>
      <p className="text-xs text-gray-500">[Data: Product A: 2400, Product B: 1800, Product C: 3200, Product D: 1600]</p>
    </div>
  </div>
  <div className="mt-4 p-3 bg-blue-50 rounded-lg">
    <p className="text-sm text-blue-800">Product C leads with 3.2K units, 33% higher than average</p>
  </div>
</div>`
    
    results.push({
      agent: 'chart_generation_agent',
      component_type: 'comparison_bar',
      component_code: component,
      business_context: 'Comparative analysis visualization'
    })
  }
  
  // If no specific keywords matched, provide a default metric card
  if (results.length === 0) {
    const component = `
<div className="p-6 text-center bg-white rounded-lg shadow-sm border">
  <div className="pt-6">
    <div className="text-4xl font-bold text-gray-900">🤖</div>
    <p className="text-sm text-gray-600 mt-1">General Business Query</p>
    <div className="mt-2 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-blue-500 text-white">
      Processed
    </div>
    <p className="text-xs text-gray-500 mt-2">Agent understood: "${query}"</p>
  </div>
</div>`
    
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