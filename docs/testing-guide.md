# Testing Guide for Authentic Google ADK Integration

This guide provides comprehensive testing instructions for the authentic Google ADK agent system with two interfaces: the React frontend client and the ADK web UI.

## Overview

The system now uses authentic Google ADK agents instead of keyword-based simulation:
- **FastAPI Server**: `http://localhost:8081` - Bridges ADK agents to frontend
- **ADK Web UI**: Available via `adk web` command - Direct agent interaction
- **React Frontend**: `http://localhost:3000` - Business intelligence dashboard

## Prerequisites

1. **Environment Setup**:
   ```bash
   # Ensure Google API key is configured
   export GOOGLE_API_KEY="your_api_key_here"
   
   # Or check .env file in agents/.env
   cat agents/.env
   ```

2. **Required Services Running**:
   ```bash
   # ADK Server (for frontend integration)
   python adk_server.py
   
   # React Frontend (optional, for frontend testing)
   npm run dev
   
   # ADK Web UI (for direct agent testing)
   adk web --app_name="generative_ui_system" --agents_dir="agents"
   ```

## Testing Method 1: Frontend Client Testing

### Starting the Frontend Test Environment

```bash
# Terminal 1: Start the ADK server
cd /path/to/google-ai-sprint
python adk_server.py

# Terminal 2: Start the React frontend
npm run dev
```

### Frontend Test Prompts

Test these prompts through the React dashboard at `http://localhost:3000`:

#### **Chart Generation Tests**
```
1. "show sales trends"
   Expected: Sales trend card with Q4 2024 data and +23% growth indicator

2. "display revenue metrics"
   Expected: Metric card showing $47.2K monthly revenue with change indicators

3. "create performance comparison"
   Expected: Bar chart comparing Product A, B, C, D with insights

4. "show quarterly trends with metrics"
   Expected: Multiple components - trend chart + metric cards

5. "sales performance dashboard"
   Expected: Comprehensive sales visualization components
```

#### **Geospatial Tests**
```
1. "show regional performance"
   Expected: US states heatmap with California leading at $45K

2. "display territory breakdown"
   Expected: Territory analysis with Western region performance

3. "regional sales analysis"
   Expected: Location metrics for major US regions

4. "geographic performance map"
   Expected: Interactive map with regional sales data

5. "show territory metrics for west coast"
   Expected: Location-specific metrics for California, Oregon, Washington
```

#### **Accessibility Tests**
```
1. "create accessible sales chart"
   Expected: High contrast chart with WCAG compliance features

2. "show screen reader compatible data"
   Expected: Data table with comprehensive ARIA labels

3. "accessible dashboard components"
   Expected: Keyboard navigable dashboard with focus indicators

4. "high contrast performance metrics"
   Expected: Accessibility-optimized metric displays

5. "wcag compliant regional data"
   Expected: Accessible geographic visualizations
```

#### **Multi-Agent Tests**
```
1. "accessible regional sales trends"
   Expected: Delegation to both accessibility and geospatial agents

2. "show accessible sales trends with regional breakdown"
   Expected: Multiple agent coordination - charts + geography + accessibility

3. "comprehensive business intelligence dashboard"
   Expected: Full multi-agent response with various component types
```

### Frontend Testing Validation

For each test, verify:

1. **API Response Structure**:
   ```json
   {
     "success": true,
     "query": "your_query",
     "components": [
       {
         "agent": "chart_generation_agent",
         "component_type": "sales_trend",
         "component_code": "<Card className=...>...</Card>",
         "business_context": "..."
       }
     ],
     "total_components": 1,
     "processing_time": "2.1s",
     "agent_trace": [...]
   }
   ```

2. **Component Rendering**: Check that JSX components render properly in the dashboard
3. **Data Accuracy**: Verify sample data matches expected business metrics
4. **Styling**: Confirm Tailwind CSS classes apply correctly

### Frontend Troubleshooting

If components don't render:
1. Check browser console for JSX parsing errors
2. Verify component imports (Card, CardHeader, etc.)
3. Test with simplified queries first
4. Check network tab for API response format

## Testing Method 2: ADK Web UI Testing

### Starting the ADK Web UI

```bash
# Start ADK Web UI (separate from frontend)
cd /path/to/google-ai-sprint
adk web --app_name="generative_ui_system" --agents_dir="agents"

# Access at: http://localhost:8080 (default ADK web port)
```

### ADK Web UI Test Prompts

Use these exact prompts in the ADK web interface:

#### **Direct Agent Testing**
```
1. "show sales trends"
   Agent: Should delegate to chart_generation_agent
   Expected: Tool call to create_sales_trend_card()

2. "regional performance data"
   Agent: Should delegate to geospatial_agent  
   Expected: Tool calls to geographic visualization tools

3. "accessible sales dashboard"
   Agent: Should delegate to accessibility_agent
   Expected: Tool calls to accessibility optimization tools

4. "quarterly sales comparison with regional breakdown"
   Agent: Should coordinate multiple sub-agents
   Expected: Multi-agent delegation and tool orchestration
```

#### **Agent Delegation Verification**
```
Test Sequence:
1. Start with: "show sales trends"
2. Monitor agent trace for delegation to chart_generation_agent
3. Verify tool calling: create_sales_trend_card() execution
4. Check response includes React JSX component code
5. Validate sample data inclusion (Q4 2024, +23% growth)
```

#### **Tool Execution Validation**
```
For each agent, test direct tool calling:

Chart Generation Agent:
- "create sales trend visualization"
- "generate revenue metric card" 
- "build comparison bar chart"

Geospatial Agent:
- "create regional heatmap"
- "show location metrics"
- "generate territory analysis"

Accessibility Agent:
- "create high contrast chart"
- "build screen reader table"
- "generate keyboard navigation dashboard"
```

### ADK Web UI Validation Checklist

1. **Agent Discovery**:
   - [ ] `generative_ui_orchestrator` appears as root agent
   - [ ] Sub-agents listed: `chart_generation_agent`, `geospatial_agent`, `accessibility_agent`
   - [ ] All agents show "Active" status

2. **Delegation Flow**:
   - [ ] Root agent receives query
   - [ ] LLM analyzes query type (sales/geographic/accessibility)
   - [ ] Appropriate sub-agent delegation occurs
   - [ ] Tool calls execute with parameters

3. **Tool Execution**:
   - [ ] Tools called with default parameters when not specified
   - [ ] JSX component code generated in response
   - [ ] Business context and sample data included
   - [ ] No "Could you please provide..." responses

4. **Response Quality**:
   - [ ] Complete React components with proper syntax
   - [ ] Tailwind CSS styling classes included
   - [ ] Realistic business sample data
   - [ ] Professional insights and context

### ADK Web UI Troubleshooting

**If agents don't appear**:
```bash
# Check agent discovery
adk web --agents_dir="agents" --debug

# Verify agent files
ls -la agents/
ls -la agents/generative_ui/
```

**If delegation fails**:
1. Check agent descriptions are clear and distinct
2. Verify sub_agents parameter in root_agent
3. Test individual agents directly
4. Review agent instruction clarity

**If tools don't execute**:
1. Verify tools parameter in LlmAgent constructor
2. Check function signatures match expected parameters
3. Test tool functions independently
4. Review tool docstrings for clarity

## Performance Testing

### Load Testing Queries
```bash
# Test multiple concurrent requests
for i in {1..5}; do
  curl -X POST "http://localhost:8081/api/analyze" \
    -H "Content-Type: application/json" \
    -d '{"query": "show sales trends"}' &
done
wait
```

### Response Time Benchmarks
- Simple queries (single agent): < 3 seconds
- Complex queries (multi-agent): < 5 seconds
- Geographic queries (with maps): < 4 seconds
- Accessibility queries: < 3 seconds

## Expected Behavior Summary

### ✅ Success Indicators
- Agents respond without asking for clarification
- JSX components generated with proper syntax
- Tool calls execute with reasonable defaults
- Multi-agent coordination works for complex queries
- Response includes business insights and sample data

### ❌ Failure Indicators
- "Could you please provide..." responses
- Empty or text-only responses
- Tool execution errors
- Session management failures
- API key authentication issues

## Advanced Testing Scenarios

### Edge Cases
```
1. "undefined business query"
   Expected: Default to chart generation with sample data

2. "show everything"
   Expected: Multi-agent response with diverse components

3. "invalid regional data request"
   Expected: Use default US states data

4. "accessibility requirements not specified"
   Expected: Apply WCAG standards automatically
```

### Integration Testing
```
1. Test all three agents in sequence
2. Verify session persistence across queries
3. Test rapid query succession
4. Validate memory usage with multiple sessions
5. Test graceful degradation with API limits
```

This comprehensive testing guide ensures the authentic ADK integration works correctly across both frontend and direct agent interfaces.