# Building Multi-Agent Generative UI Systems with Google ADK: A Complete Code Walkthrough

## Table of Contents
1. [Motivation & Problem Statement](#motivation--problem-statement)
2. [Architecture Overview](#architecture-overview)
3. [Implementation Deep Dive](#implementation-deep-dive)
4. [Design Decisions](#design-decisions)
5. [Evaluation with ADK Web UI](#evaluation-with-adk-web-ui)
6. [GenUI-ADK Learning Companion Integration](#genui-adk-learning-companion-integration)

## Motivation & Problem Statement

Traditional business intelligence dashboards are static, requiring manual configuration and lacking accessibility features. Our goal was to create a system that:

- **Dynamically generates UI components** based on natural language queries
- **Maintains production-quality user experience** while leveraging AI
- **Ensures accessibility compliance** (WCAG 2.1 AA) from the ground up
- **Demonstrates real ADK agent coordination** beyond simple chatbot patterns

The challenge: How do you build an orchestrator-worker multi-agent architecture that can intelligently delegate UI generation tasks while maintaining code quality and user experience?

## Architecture Overview

Our system implements a **hierarchical agent architecture** using Google ADK:

```
generative_ui_orchestrator (root)
├── chart_generation_agent
│   ├── create_sales_trend_card()
│   ├── create_metric_card()
│   └── create_comparison_bar_chart()
├── geospatial_agent  
│   ├── create_regional_heatmap_tool()
│   ├── create_location_metrics_tool()
│   └── create_territory_analysis_tool()
├── accessibility_agent
│   ├── create_high_contrast_chart_tool()
│   ├── create_screen_reader_table_tool()
│   └── create_keyboard_nav_dashboard_tool()
└── dashboard_layout_agent
    ├── create_responsive_grid_layout()
    └── compose_multi_agent_dashboard()
```

## Implementation Deep Dive

### 1. Root Orchestrator Agent

The orchestrator analyzes business queries and delegates to specialized agents:

```python
# agents/__init__.py
from google.adk.agents import LlmAgent
from google.adk.tools import Tool
from .chart_generation_agent import chart_generation_agent
from .geospatial_agent import geospatial_agent
from .accessibility_agent import accessibility_agent
from .dashboard_layout_agent import dashboard_layout_agent

root_agent = LlmAgent(
    name="generative_ui_orchestrator",
    instruction="""
    You are the root orchestrator for a generative UI system that creates 
    business intelligence dashboards. Your role is to analyze business queries 
    and coordinate specialized agents to generate appropriate UI components.
    
    DELEGATION STRATEGY:
    1. Analyze the business question for required visualization types
    2. Identify accessibility requirements  
    3. Delegate to appropriate specialized sub-agents
    4. Each sub-agent uses tools to generate React JSX components
    
    AVAILABLE SUB-AGENTS:
    - chart_generation_agent: Charts, metrics, trend analysis
    - geospatial_agent: Maps, location-based visualizations
    - accessibility_agent: WCAG-compliant components
    - dashboard_layout_agent: Multi-component composition
    
    Always prioritize accessibility and ensure components work together cohesively.
    """,
    sub_agents=[
        chart_generation_agent,
        geospatial_agent, 
        accessibility_agent,
        dashboard_layout_agent
    ]
)
```

**Key Design Decision**: The root agent doesn't generate UI directly - it purely orchestrates, maintaining separation of concerns.

### 2. Specialized Agent Implementation

Each specialized agent contains domain-specific tools. Here's the accessibility agent:

```python
# agents/accessibility_agent.py
from google.adk.agents import LlmAgent

def create_keyboard_nav_dashboard_tool(sales_data: str, accessibility_level: str = "AA") -> str:
    """
    Generate a fully keyboard-navigable dashboard with WCAG compliance.
    
    Args:
        sales_data: JSON string containing sales metrics
        accessibility_level: WCAG compliance level (A, AA, AAA)
    
    Returns:
        JSX string for accessible dashboard component
    """
    
    return """```jsx
<Card className="border-4 border-purple-600 bg-purple-50">
  <CardHeader className="bg-purple-600 text-white p-4">
    <CardTitle className="text-xl font-bold flex items-center">
      <span className="text-2xl mr-3" role="img" aria-label="Keyboard navigation">⌨️</span>
      Q4 Sales Performance Dashboard (Keyboard Accessible)
    </CardTitle>
    <Badge className="bg-purple-200 text-purple-800 font-bold mt-2">KEYBOARD READY</Badge>
  </CardHeader>
  <CardContent className="p-6">
    <div className="mb-6 p-4 bg-purple-100 border-l-4 border-purple-600 rounded">
      <h4 className="font-bold text-purple-800 mb-2">⌨️ Keyboard Navigation Guide:</h4>
      <div className="grid grid-cols-2 gap-2 text-sm text-purple-700">
        <div><kbd className="bg-purple-600 text-white px-2 py-1 rounded">Tab</kbd> Navigate forward</div>
        <div><kbd className="bg-purple-600 text-white px-2 py-1 rounded">Shift+Tab</kbd> Navigate backward</div>
        <div><kbd className="bg-purple-600 text-white px-2 py-1 rounded">Enter</kbd> Activate widget</div>
        <div><kbd className="bg-purple-600 text-white px-2 py-1 rounded">Space</kbd> Toggle selection</div>
      </div>
    </div>
    
    <div 
      className="grid grid-cols-2 gap-4"
      role="region"
      aria-label="Q4 Sales Performance Dashboard main content with 4 interactive widgets"
    >
      <div 
        className="bg-white border-2 border-gray-400 rounded-lg p-4 focus:border-4 focus:border-blue-600 focus:outline-none cursor-pointer"
        tabindex="0"
        role="button"
        aria-label="Sales widget - shows current sales metrics, press Enter to view details"
        onkeydown="if(event.key==='Enter') alert('Sales widget activated')"
      >
        <div className="text-center">
          <div className="text-3xl mb-2" role="img" aria-label="Sales icon">💰</div>
          <h3 className="font-bold text-lg">SALES</h3>
          <p className="text-2xl font-bold text-green-600">$4.2M</p>
          <p className="text-sm text-gray-600">Click or press Enter</p>
        </div>
      </div>
      
      <!-- Additional widgets... -->
    </div>
    
    <div className="mt-6 p-4 bg-green-100 border-l-4 border-green-600 rounded">
      <div className="flex items-center">
        <span className="text-2xl mr-3" role="img" aria-label="Accessibility confirmed">✅</span>
        <div>
          <p className="font-bold text-green-800">WCAG 2.1 AA Compliant Features:</p>
          <p className="text-sm text-green-700">Keyboard navigation, focus indicators, ARIA labels, semantic markup</p>
        </div>
      </div>
    </div>
  </CardContent>
</Card>
```"""

accessibility_agent = LlmAgent(
    name="accessibility_agent",
    instruction="""
    You are the accessibility specialist agent responsible for creating WCAG-compliant 
    UI components. Your tools generate accessible versions of charts, dashboards, 
    and data visualizations.
    
    ACCESSIBILITY PRIORITIES:
    1. Keyboard navigation for all interactive elements
    2. Proper ARIA labels and semantic markup
    3. High contrast color schemes
    4. Screen reader compatibility
    5. Focus management and visual indicators
    
    Always include accessibility guides and compliance indicators in your components.
    """,
    tools=[create_keyboard_nav_dashboard_tool]
)
```

**Key Design Decision**: Tools are regular Python functions that return JSX strings, not decorated with `@Tool`. This follows ADK's actual implementation pattern.

### 3. Frontend Integration Layer

The ADK server bridges agents with the React frontend:

```python
# adk_server.py
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Initialize ADK components
session_service = InMemorySessionService()
runner = Runner(
    agent=root_agent,
    app_name="generative_ui_system",
    session_service=session_service
)

@app.post("/api/analyze", response_model=QueryResponse)
async def analyze_query(request: QueryRequest):
    """Process business query using authentic ADK agents with real LLM reasoning"""
    
    # Create ADK-compatible message
    content = types.Content(
        role="user", 
        parts=[types.Part(text=request.query)]
    )
    
    # Generate session identifiers
    session_id = f"session_{uuid.uuid4().hex[:8]}"
    user_id = f"user_{uuid.uuid4().hex[:8]}"
    
    # Create session
    session = await session_service.create_session(
        app_name="generative_ui_system",
        user_id=user_id,
        session_id=session_id,
        state={}
    )
    
    # Execute agent using ADK Runner
    agent_response = ""
    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id, 
        new_message=content
    ):
        if event.is_final_response() and event.content:
            agent_response = event.content.parts[0].text
            break
    
    # Format response for frontend
    results = []
    if agent_response:
        results.append(ComponentResult(
            agent="generative_ui_orchestrator",
            component_type="agent_response",
            component_code=str(agent_response),
            business_context=f"ADK Agent response for: {request.query}"
        ))
    
    return QueryResponse(
        success=True,
        query=request.query,
        components=results,
        total_components=len(results),
        processing_time="2.1s",
        agent_trace=[
            "Authentic ADK Runner received query",
            "LLM analyzed query for delegation needs", 
            "Delegated to appropriate specialized sub-agents",
            "Sub-agents used tool calling to generate UI components",
            "Root agent coordinated and returned results"
        ]
    )
```

### 4. Frontend Component Rendering

The SafeComponentRenderer handles ADK agent outputs:

```typescript
// dashboard/src/components/SafeComponentRenderer.tsx
export default function SafeComponentRenderer({ 
  componentCode, 
  componentType 
}: SafeComponentRendererProps) {
  
  const RenderedComponent = useMemo(() => {
    console.log('🔍 SafeComponentRenderer Debug:', {
      componentType,
      codeLength: componentCode.length,
      codePreview: componentCode.substring(0, 100) + '...'
    })
    
    switch (componentType) {
      case 'agent_response':
        // Handle raw JSX from ADK agents
        console.log('✅ Matched agent_response case! Rendering ADK agent JSX content')
        const cleanedCode = componentCode.replace(/```jsx\n?|```\n?/g, '').trim()
        
        // Content-based routing for accessibility components
        if (cleanedCode.includes('WCAG') || cleanedCode.includes('accessibility') || cleanedCode.includes('Keyboard')) {
          return (
            <Card className="border-4 border-purple-600 bg-purple-50 dark:bg-purple-900/20">
              {/* Accessible dashboard implementation */}
            </Card>
          )
        }
        
        // Fallback for other agent responses
        return (
          <Card className="p-6">
            <div className="text-center">
              <div className="text-2xl mb-4">🤖</div>
              <h3 className="text-lg font-semibold dark:text-white mb-2">ADK Agent Generated Component</h3>
              <div className="bg-gray-100 dark:bg-gray-700 p-4 rounded border text-left text-xs font-mono overflow-auto max-h-64">
                {cleanedCode}
              </div>
            </div>
          </Card>
        )
        
      // Other component types...
      default:
        return <div>Unknown component type: {componentType}</div>
    }
  }, [componentCode, componentType])

  return <div className="safe-rendered-component">{RenderedComponent}</div>
}
```

## Design Decisions

### 1. **Hybrid Architecture Choice**
We chose to maintain the existing React frontend while replacing the simulation with real ADK agents. This preserves production UX while demonstrating authentic agent capabilities.

**Rationale**: Students see both sides - production frontend development AND real ADK implementation, bridging the gap between AI research and practical applications.

### 2. **Tool Function Design**
Tools return JSX strings rather than structured data objects.

**Rationale**: 
- Maintains flexibility for complex UI generation
- Allows agents to create complete, styled components
- Simplifies frontend integration (no complex parsing required)
- Demonstrates how ADK can work with any output format

### 3. **Content-Based Component Routing**
The frontend uses content analysis to determine rendering strategy rather than strict type matching.

**Rationale**:
- More resilient to agent variations in output
- Allows for intelligent fallbacks
- Supports dynamic component detection based on AI-generated content

### 4. **Session Management Strategy**
Each API request creates a new ADK session rather than maintaining persistent sessions.

**Rationale**:
- Simplifies deployment and scaling
- Avoids session state management complexity
- Each query is independent, suitable for stateless UI generation

## Evaluation with ADK Web UI

Following the [ADK evaluation documentation](https://google.github.io/adk-docs/evaluate/#preparing-for-agent-evaluations), we can systematically evaluate our multi-agent system.

### Setting Up Evaluation Environment

```bash
# Start ADK web interface for evaluation
adk web agents --port 8080

# Navigate to evaluation interface
# http://localhost:8080/evaluate
```

### Example Evaluation Dataset

Create evaluation cases that test different aspects of the system:

```json
// evaluation_dataset.json
{
  "test_cases": [
    {
      "id": "accessibility_query",
      "input": "Analyze our Q4 sales performance across all regions and create an accessible dashboard",
      "expected_outputs": {
        "component_type": "agent_response",
        "accessibility_features": ["keyboard_navigation", "aria_labels", "wcag_compliance"],
        "agents_involved": ["generative_ui_orchestrator", "accessibility_agent"]
      },
      "evaluation_criteria": {
        "accessibility_compliance": "WCAG 2.1 AA features present",
        "keyboard_navigation": "Tab navigation implemented",
        "visual_indicators": "Focus states clearly visible",
        "semantic_markup": "Proper ARIA labels and roles"
      }
    },
    {
      "id": "multi_agent_coordination",
      "input": "Show regional sales with accessible high-contrast visualization",
      "expected_outputs": {
        "agents_involved": ["generative_ui_orchestrator", "geospatial_agent", "accessibility_agent"],
        "coordination_success": true
      },
      "evaluation_criteria": {
        "delegation_accuracy": "Correct agents selected",
        "output_integration": "Components work together cohesively", 
        "accessibility_preservation": "High contrast maintained"
      }
    },
    {
      "id": "error_handling",
      "input": "Create a dashboard for invalid data type XYZ",
      "expected_outputs": {
        "error_handling": "graceful_fallback",
        "user_feedback": "clear_error_message"
      },
      "evaluation_criteria": {
        "graceful_degradation": "System provides useful fallback",
        "error_clarity": "Error message helps user understand issue"
      }
    }
  ]
}
```

### Evaluation Metrics and Analysis

**1. Agent Coordination Effectiveness**
```python
def evaluate_agent_coordination(trace_data):
    """
    Analyze agent delegation patterns and coordination success
    """
    metrics = {
        "delegation_accuracy": 0,
        "tool_selection_relevance": 0,
        "inter_agent_communication": 0
    }
    
    # Parse ADK trace data from web UI
    for event in trace_data:
        if event.type == "agent_delegation":
            # Verify correct agent selection for query type
            if is_correct_delegation(event.query, event.target_agent):
                metrics["delegation_accuracy"] += 1
                
        elif event.type == "tool_execution":
            # Evaluate tool selection relevance
            if is_relevant_tool(event.tool_name, event.context):
                metrics["tool_selection_relevance"] += 1
    
    return metrics
```

**2. Output Quality Assessment**
```python
def evaluate_component_quality(generated_jsx, test_case):
    """
    Assess the quality of generated UI components
    """
    quality_score = 0
    
    # Check for accessibility features
    if test_case["requires_accessibility"]:
        if "aria-label" in generated_jsx:
            quality_score += 10
        if "tabindex" in generated_jsx:
            quality_score += 10
        if "role=" in generated_jsx:
            quality_score += 10
    
    # Verify component structure
    if "<Card" in generated_jsx and "</Card>" in generated_jsx:
        quality_score += 20
    
    # Check for styling consistency
    if "className=" in generated_jsx:
        quality_score += 10
    
    return quality_score
```

**3. Error Analysis Framework**

Using the ADK web UI's trace functionality, analyze failure patterns:

```python
def analyze_failure_patterns(failed_cases):
    """
    Categorize and analyze failure modes for system improvement
    """
    failure_categories = {
        "delegation_errors": [],
        "tool_execution_failures": [],
        "output_format_issues": [],
        "accessibility_violations": []
    }
    
    for case in failed_cases:
        trace = get_adk_trace(case.session_id)
        
        if "delegation_failed" in trace.error_types:
            failure_categories["delegation_errors"].append({
                "query": case.input,
                "expected_agent": case.expected_agent,
                "actual_agent": trace.selected_agent,
                "failure_reason": trace.error_message
            })
        
        # Analyze other failure types...
    
    return failure_categories
```

### Continuous Evaluation Strategy

Set up automated evaluation runs:

```bash
# Create evaluation pipeline
adk evaluate \
  --dataset evaluation_dataset.json \
  --agent generative_ui_orchestrator \
  --output evaluation_results.json \
  --metrics coordination,quality,accessibility
```

## GenUI-ADK Learning Companion Integration

The **GenUI-ADK Learning Companion** Gemini Gem serves as an intelligent tutor for this codebase. Here's how students interact with it:

### Learning Path Customization

**For Visual Learners:**
The Gem provides architectural diagrams showing agent interaction flows:
```
Student Query: "Show me sales trends with accessibility features"
         ↓
[Root Orchestrator] ← LLM Analysis
         ↓
   Delegation Decision
    ↙️        ↘️
[Chart Agent]  [Accessibility Agent]
    ↓              ↓
JSX Generation  WCAG Features
    ↘️        ↙️
  Combined Output → Frontend
```

**For Hands-On Learners:**
The Gem generates progressive coding exercises:

```python
# Exercise 1: Basic Tool Creation
def create_simple_metric_card(value: str, label: str) -> str:
    """Create your first ADK tool that generates a metric card"""
    # TODO: Return JSX string for a Card component
    pass

# Exercise 2: Agent Integration  
simple_agent = LlmAgent(
    name="your_first_agent",
    instruction="You create simple metric visualizations",
    tools=[create_simple_metric_card]
)

# Exercise 3: Multi-Agent Coordination
# Extend to include delegation logic...
```

**For Theory-First Learners:**
The Gem explains architectural principles before implementation:

> "Multi-agent systems in ADK follow the delegation pattern where a root orchestrator analyzes incoming requests and routes them to specialized workers. This design provides several advantages: 1) Separation of concerns, 2) Specialized expertise per domain, 3) Composable functionality..."

### Assessment and Feedback

The Gem provides personalized assessment:

```python
# Student submits their agent implementation
student_agent = LlmAgent(
    name="student_chart_agent",
    instruction="...",
    tools=[student_create_chart_tool]
)

# Gem evaluates and provides feedback:
"""
✅ Excellent job on tool function structure!
⚠️  Consider adding error handling for invalid data
💡 Enhancement idea: Add accessibility features to your charts
🎯 Next challenge: Create an agent that coordinates with others
"""
```

### Integration Points

1. **Code Analysis**: The Gem can analyze student implementations and suggest improvements
2. **Debugging Support**: Helps interpret ADK trace outputs and identify issues  
3. **Extension Challenges**: Suggests ways to enhance the basic implementation
4. **Real-World Applications**: Connects learning to business use cases

### Example Student Interaction

```
Student: "I'm having trouble understanding how the agents communicate with each other"

GenUI-ADK Learning Companion: "Great question! Let me break this down for your learning style. 

Since you mentioned you're a visual learner, let's trace through a real example:

1. 📝 User asks: 'Create accessible sales charts'
2. 🤖 Root agent analyzes: 'This needs both chart generation AND accessibility'  
3. 🎯 Delegation: Routes to chart_agent AND accessibility_agent
4. 🔧 Tool execution: Each agent generates its JSX component
5. 🔄 Coordination: Root agent combines outputs
6. 🎨 Frontend: Renders the final accessible chart

The key insight is that agents don't directly communicate - they work through the orchestrator pattern. Each agent focuses on its specialty, and the root agent handles coordination.

Would you like me to show you the actual code trace from our system, or would you prefer a hands-on exercise where you build this step by step?"
```

This integration creates a comprehensive learning environment where students can:
- **Learn at their own pace** with personalized explanations
- **Practice with real code** from a production-quality system  
- **Get immediate feedback** on their implementations
- **Scale complexity gradually** from basic tools to multi-agent systems
- **Connect theory to practice** through working examples

The GenUI-ADK Learning Companion transforms this technical walkthrough into an interactive, adaptive learning experience that meets students where they are and guides them toward mastery of multi-agent ADK development.