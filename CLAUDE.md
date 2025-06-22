# CLAUDE.md - Generative UI with ADK Agent Tool Architecture
**Engineering Requirements & Specification Document**

## Project Overview

**System Name**: AgenticBI - Generative UI through ADK Tool Composition  
**Target**: Educational demonstration of UI components as ADK tools  
**Core Innovation**: React components as callable tools within ADK agent framework  
**Architecture**: Specialized UI generation agents with component tool libraries

## Vision: UI Components as ADK Tools

### Core Concept
```python
# React UI components become callable tools in ADK agents
@Tool
def create_sales_trend_card(self, sales_data: list, period: str) -> str:
    """Tool that generates a sales trend React component."""
    return '''
    <Card className="p-6 bg-gradient-to-r from-green-50 to-blue-50">
      <CardHeader>
        <TrendingUp className="h-6 w-6 text-green-600" />
        <CardTitle>Sales Trend - {period}</CardTitle>
      </CardHeader>
      <CardContent>
        <LineChart data={sales_data} className="h-48" />
        <Badge variant="success">+23% Growth</Badge>
      </CardContent>
    </Card>
    '''
```

### Architecture Philosophy
1. **UI-as-Tools**: React components are callable tools within ADK agents
2. **Specialized Agents**: Each agent focuses on specific UI generation domains  
3. **Tool Composition**: Agents combine multiple UI tools to create complex layouts
4. **Educational Transparency**: Students see how agents compose UI through tool calling

## Simplified Technical Stack

```
Agent Framework:  Google ADK + Gemini 2.0 Flash (Option A)
Fallback:         ADK + Ollama + Gemma 3 + LiteLLM (Option B)
UI Generation:    React components as ADK tools returning JSX strings
Dashboard:        Next.js for rendering agent-generated components
Development UI:   ADK Web Interface (tool tracing, agent delegation)
```

## Core Agent Architecture

### Root Agent: Generative UI Orchestrator
```python
# para_agent/root_agent.py
from google.adk.agents import LlmAgent
from .agents import (
    create_chart_generation_agent,
    create_geospatial_agent,
    create_accessibility_agent,
    create_dashboard_layout_agent
)

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

def create_root_agent() -> LlmAgent:
    return LlmAgent(
        name="generative_ui_orchestrator", 
        instruction=ROOT_AGENT_INSTRUCTION,
        model="gemini-2.0-flash",  # Option A
        sub_agents=[
            create_chart_generation_agent(),
            create_geospatial_agent(),
            create_accessibility_agent(), 
            create_dashboard_layout_agent()
        ]
    )
```

### Specialized UI Generation Agents

#### 1. Chart Generation Agent
```python
# para_agent/agents/chart_generation_agent.py
from google.adk.agents import LlmAgent
from google.adk.tools import Tool

class ChartGenerationAgent(LlmAgent):
    """Specialized agent for generating chart components via tool calling."""
    
    def __init__(self):
        super().__init__(
            name="chart_generation_agent",
            instruction="Generate chart components using available UI tools based on data analysis needs.",
            model="gemini-2.0-flash"
        )
        
        self.tools = [
            self.create_trend_line_tool,
            self.create_comparison_bar_tool,
            self.create_metric_card_tool,
            self.create_correlation_scatter_tool
        ]

    @Tool
    def create_trend_line_tool(self, data: list, title: str, trend_direction: str, insight: str) -> str:
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

    @Tool  
    def create_metric_card_tool(self, value: str, label: str, change: str, context: str) -> str:
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
```

#### 2. Geospatial Agent  
```python
# para_agent/agents/geospatial_agent.py
class GeospatialAgent(LlmAgent):
    """Specialized agent for generating map and location-based components."""
    
    def __init__(self):
        super().__init__(
            name="geospatial_agent",
            instruction="Generate geospatial and map components for location-based business analysis.",
            model="gemini-2.0-flash"
        )
        
        self.tools = [
            self.create_regional_heatmap_tool,
            self.create_location_metrics_tool,
            self.create_territory_analysis_tool
        ]

    @Tool
    def create_regional_heatmap_tool(self, regions: dict, metric_name: str, insights: list) -> str:
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
```

#### 3. Accessibility Agent
```python
# para_agent/agents/accessibility_agent.py  
class AccessibilityAgent(LlmAgent):
    """Specialized agent for generating accessibility-optimized UI components."""
    
    def __init__(self):
        super().__init__(
            name="accessibility_agent", 
            instruction="Generate high-contrast, screen reader optimized UI components for accessibility.",
            model="gemini-2.0-flash"
        )
        
        self.tools = [
            self.create_high_contrast_chart_tool,
            self.create_screen_reader_table_tool,
            self.create_keyboard_nav_dashboard_tool
        ]

    @Tool
    def create_high_contrast_chart_tool(self, data: list, chart_type: str, title: str) -> str:
        """Generate high contrast chart for visually impaired users."""
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
              aria-describedby="chart-description-{{{id}}}"
            />
            <div id="chart-description-{{{id}}}" className="sr-only">
              Detailed chart description for screen readers would go here
            </div>
            <div className="mt-4 p-3 bg-black text-white text-lg">
              <strong>Key Insight:</strong> Chart shows data trends with high contrast colors
            </div>
          </CardContent>
        </Card>
        '''
```

## Dashboard Integration: Rendering Generated Components

### Next.js Dynamic Component Renderer
```typescript
// app/dashboard/page.tsx
'use client'

import { useState, useEffect, useMemo } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { Badge } from '@/components/ui/badge'
import { LineChart, BarChart, AreaChart } from '@tremor/react'
import { TrendingUp, TrendingDown, MapPin, Minus } from 'lucide-react'

interface GeneratedComponent {
  id: string
  agent_name: string
  component_code: string
  business_context: string
}

export default function GenerativeUIDashboard() {
  const [components, setComponents] = useState<GeneratedComponent[]>([])
  const [isLoading, setIsLoading] = useState(false)

  // Listen for components generated by ADK agents
  useEffect(() => {
    const eventSource = new EventSource('/api/adk-components')
    
    eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data)
      
      if (data.type === 'component_generated') {
        setComponents(prev => [...prev, data.component])
      }
      
      if (data.type === 'analysis_complete') {
        setIsLoading(false)
      }
    }
    
    return () => eventSource.close()
  }, [])

  const handleBusinessQuery = async (query: string) => {
    setIsLoading(true)
    setComponents([])
    
    // Send query to ADK agent
    await fetch('/api/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    })
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold mb-4">Generative UI Business Intelligence</h1>
          <BusinessQueryInput onSubmit={handleBusinessQuery} isLoading={isLoading} />
        </div>
        
        <div className="grid gap-6">
          {components.map((component) => (
            <GeneratedComponentWrapper 
              key={component.id}
              component={component}
            />
          ))}
        </div>
      </div>
    </div>
  )
}

// Dynamic component renderer with error boundaries
function GeneratedComponentWrapper({ component }: { component: GeneratedComponent }) {
  const RenderedComponent = useMemo(() => {
    try {
      // In a real implementation, you'd use a safe JSX compiler
      // For demo purposes, this shows the concept
      return () => <div dangerouslySetInnerHTML={{ __html: component.component_code }} />
    } catch (error) {
      return () => (
        <Card className="border-red-200">
          <CardContent className="p-4">
            <p className="text-red-600">Error rendering component from {component.agent_name}</p>
          </CardContent>
        </Card>
      )
    }
  }, [component.component_code])

  return (
    <div className="space-y-2">
      <div className="flex items-center gap-2 text-sm text-gray-600">
        <Badge variant="outline">{component.agent_name}</Badge>
        <span>{component.business_context}</span>
      </div>
      <RenderedComponent />
    </div>
  )
}
```

## Phase Implementation Plan

### Phase 1: Foundation - UI Tools Architecture (Week 1)

#### Implementation Plan for Claude Code
Claude Code will implement this phase with strict adherence to UI-components-as-tools architecture.

#### Task Checklist - Week 1
- [ ] **Day 1-2**: ADK Project Foundation
  - [ ] Initialize ADK project: `adk init generative-ui-bi`
  - [ ] Create root agent with delegation to 2 specialized agents
  - [ ] Implement chart generation agent with 3 basic UI tools
  - [ ] Test tool calling in ADK web interface

- [ ] **Day 3-4**: Basic UI Component Tools
  - [ ] Implement `create_trend_line_tool` returning JSX strings
  - [ ] Implement `create_metric_card_tool` with dynamic styling
  - [ ] Test tools individually - verify JSX output in ADK traces
  - [ ] Validate React component syntax and structure

- [ ] **Day 5-7**: Next.js Integration Bridge
  - [ ] Create Next.js project with Tremor Charts + ShadcnUI
  - [ ] Implement `/api/adk-components` streaming endpoint
  - [ ] Create dynamic component renderer with error boundaries
  - [ ] Test end-to-end: ADK agent tool → API → Dashboard rendering

#### Success Criteria Week 1
```typescript
// Test query: "Show me our sales trends for Q4"
// Expected flow:
// 1. Root agent → delegates to chart_generation_agent
// 2. Chart agent → calls create_trend_line_tool
// 3. Tool returns JSX string for LineChart component
// 4. Dashboard receives and renders component dynamically
```

#### Deliverables Week 1
- [ ] Functional ADK root agent with chart generation sub-agent
- [ ] 3 working UI component tools that return JSX
- [ ] Next.js dashboard that renders agent-generated components
- [ ] Sample business dataset and working end-to-end demo

### Phase 2: Specialized Agent Expansion (Week 2)

#### Task Checklist - Week 2
- [ ] **Day 1-2**: Geospatial Agent Development
  - [ ] Create geospatial agent with map component tools
  - [ ] Implement `create_regional_heatmap_tool`
  - [ ] Add location-based UI component generation
  - [ ] Test with geographic business data

- [ ] **Day 3-4**: Accessibility Agent Implementation  
  - [ ] Create accessibility agent with a11y-optimized tools
  - [ ] Implement `create_high_contrast_chart_tool`
  - [ ] Add screen reader compatible component variants
  - [ ] Test accessibility features and ARIA compliance

- [ ] **Day 5-7**: Multi-Agent Composition
  - [ ] Test root agent delegating to multiple specialized agents
  - [ ] Implement complex queries requiring multiple UI types
  - [ ] Debug agent coordination and tool composition
  - [ ] Polish dashboard layout for multiple component types

#### Success Criteria Week 2
```typescript
// Complex query: "Analyze our regional sales performance with accessibility features"
// Expected flow:
// 1. Root agent analyzes need for both geospatial AND accessibility
// 2. Delegates to geospatial_agent → creates map heatmap
// 3. Delegates to accessibility_agent → creates high-contrast chart
// 4. Dashboard renders both components with proper a11y features
```

### Phase 3: Advanced Tool Composition (Week 3-4)

#### Task Checklist - Week 3
- [ ] **Day 1-3**: Dashboard Layout Agent
  - [ ] Create dashboard layout agent for component composition
  - [ ] Implement tools that combine outputs from other agents
  - [ ] Add responsive grid layout generation
  - [ ] Test complex multi-component dashboards

- [ ] **Day 4-7**: Educational Interface Enhancement
  - [ ] Enhance ADK traces to show UI generation reasoning
  - [ ] Add component generation explanations
  - [ ] Create student exercises for extending UI tools
  - [ ] Document agentic UI generation patterns

#### Task Checklist - Week 4
- [ ] **Day 1-3**: Advanced UI Tool Patterns
  - [ ] Implement conditional component generation based on data
  - [ ] Add interactive component generation (buttons, forms)
  - [ ] Create component variant selection tools
  - [ ] Test sophisticated business intelligence scenarios

- [ ] **Day 4-7**: Integration Polish
  - [ ] Comprehensive testing with diverse business queries
  - [ ] Performance optimization for component generation
  - [ ] Error handling and fallback component strategies
  - [ ] Student-ready documentation and tutorial creation

## Educational Objectives & Assessment

### Core Learning Goals
1. **UI Components as Tools**: Students understand React components as callable ADK tools
2. **Agent Specialization**: Students design focused agents with specific UI generation capabilities
3. **Tool Composition**: Students compose complex UIs through multiple tool calls
4. **ADK Best Practices**: Students follow proper delegation and tool calling patterns

### Student Assessment Framework

#### Technical Skills (60%)
- **Tool Development (25%)**: Can create new UI component tools within ADK agents
- **Agent Architecture (20%)**: Understands specialized agent responsibilities and delegation
- **React Integration (15%)**: Implements dynamic component rendering in Next.js

#### Conceptual Understanding (40%)  
- **Generative UI Concepts (20%)**: Explains difference between configuration-driven vs. generative UI
- **Agentic Reasoning (20%)**: Traces multi-agent workflows in ADK evaluation interface

### Hands-On Exercises
1. **Week 1**: Create a new chart type tool for the chart generation agent
2. **Week 2**: Design a specialized agent for a new UI domain (e.g., forms, notifications)
3. **Week 3**: Build a complex dashboard requiring 3+ different agent types
4. **Week 4**: Extend the system with custom business intelligence workflows

## Model Configuration & Deployment

### Option A: Cloud-First (Recommended)
```python
# config/models.py
AGENT_CONFIG = {
    "model": "gemini-2.0-flash",
    "provider": "google-ai-studio", 
    "api_key": os.environ["GOOGLE_AI_STUDIO_KEY"],
    "advantages": ["Fast inference", "No local requirements", "Latest capabilities"]
}
```

### Option B: Local Development
```python
# config/models.py  
AGENT_CONFIG = {
    "model": "ollama/gemma3:9b",
    "provider": "litellm",
    "base_url": "http://localhost:11434",
    "advantages": ["Privacy", "No API costs", "Offline capability"]
}
```

## Success Metrics & Validation

### Technical Benchmarks
- [ ] Agents generate syntactically correct React JSX > 95% of the time
- [ ] Component rendering latency < 2 seconds per component
- [ ] ADK tool calling success rate > 98%
- [ ] Dashboard handles 10+ simultaneous component generations

### Educational Validation
- [ ] Students can create new UI component tools independently
- [ ] Students understand agent delegation patterns in ADK traces
- [ ] Students extend the system with novel UI generation capabilities
- [ ] Students explain generative UI vs. traditional component libraries

## Risk Mitigation & Scope Control

### Implementation Boundaries
**IN SCOPE:**
- UI components as ADK tools returning JSX strings
- Specialized agents for different UI generation domains
- Next.js dashboard for rendering generated components
- Educational framework with hands-on exercises

**OUT OF SCOPE:**
- Complex state management between generated components
- Real-time collaborative editing of generated UI
- Advanced animation or interaction generation
- Production-scale deployment optimization

### Critical Success Factors for Claude Code
1. **Focus on Tool Architecture**: Every UI capability must be implemented as an ADK tool
2. **Educational Clarity**: Prioritize learning outcomes over technical sophistication  
3. **ADK-Native Patterns**: Leverage built-in ADK capabilities rather than custom solutions
4. **Incremental Complexity**: Each phase builds on previous functionality without breaking changes

## Conclusion

This architecture demonstrates authentic generative UI by treating React components as callable tools within Google ADK's agent framework. Students learn cutting-edge UI generation concepts while mastering professional agent development practices.

The UI-components-as-tools approach provides a clean conceptual model that scales from simple chart generation to sophisticated multi-agent dashboard composition, making it ideal for educational environments while showcasing real-world generative UI capabilities.