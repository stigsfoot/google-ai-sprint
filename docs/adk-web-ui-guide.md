# ADK Web UI Testing Quick Reference

## Quick Start Commands

```bash
# 1. Start ADK Web UI
cd /path/to/google-ai-sprint
adk web --app_name="generative_ui_system" --agents_dir="agents"

# 2. Access Web Interface
# Open browser to: http://localhost:8080

# 3. Verify Agent Discovery
# Should see: generative_ui_orchestrator with 3 sub-agents
```

## Test Prompts for ADK Web UI

### 🎯 **Core Functionality Tests**

Copy these exact prompts into the ADK web interface:

#### Chart Generation
```
show sales trends
```
**Expected**: Delegation to `chart_generation_agent` → Tool call: `create_sales_trend_card()`

#### Geographic Analysis  
```
regional performance data
```
**Expected**: Delegation to `geospatial_agent` → Tool call: `create_regional_heatmap_tool()`

#### Accessibility
```
accessible sales dashboard
```
**Expected**: Delegation to `accessibility_agent` → Tool call: `create_high_contrast_chart_tool()`

### 🔄 **Multi-Agent Coordination**

```
show accessible regional sales trends
```
**Expected**: Multiple agent delegation + tool orchestration

### 📊 **Detailed Component Tests**

#### Sales & Performance
```
1. "display revenue metrics"
2. "create performance comparison"  
3. "quarterly trends analysis"
4. "sales dashboard components"
```

#### Geographic & Regional
```
1. "territory breakdown analysis"
2. "show location-based metrics"
3. "geographic sales distribution"
4. "regional market performance"
```

#### Accessibility & Compliance
```
1. "high contrast data visualization"
2. "screen reader compatible dashboard"
3. "keyboard navigable interface"
4. "wcag compliant charts"
```

## ✅ Success Validation Checklist

### Agent Discovery
- [ ] Root agent: `generative_ui_orchestrator` visible
- [ ] Sub-agents: 3 agents listed (`chart_generation_agent`, `geospatial_agent`, `accessibility_agent`)
- [ ] All agents show active/available status

### Query Processing
- [ ] Agent responds within 5 seconds
- [ ] No "Could you please provide..." responses
- [ ] Delegation to appropriate sub-agent occurs
- [ ] Tool execution visible in trace

### Response Quality
- [ ] JSX component code generated
- [ ] Contains Tailwind CSS classes
- [ ] Includes sample business data
- [ ] Professional business insights included

## 🔧 Troubleshooting Guide

### Issue: "No root_agent found"
```bash
# Check agent file structure
ls -la agents/
ls -la agents/generative_ui/

# Verify imports
python -c "from agents import root_agent; print(root_agent.name)"

# Restart with debug
adk web --agents_dir="agents" --debug
```

### Issue: Agents don't delegate
**Check agent instructions contain `transfer_to_agent()` guidance**

### Issue: Tools don't execute  
**Verify `tools=[]` parameter in LlmAgent constructors**

### Issue: Session errors
**Check Google API key in environment:**
```bash
echo $GOOGLE_API_KEY
# or check agents/.env file
```

## 📝 ADK Web UI Features to Explore

### Conversation View
- **Message History**: See full conversation thread
- **Agent Traces**: Detailed execution flow
- **Tool Calls**: Inspect function calls and parameters

### Agent Inspection
- **Agent Details**: View agent configurations
- **Tool Lists**: See available tools per agent
- **Sub-Agent Relationships**: Explore delegation hierarchy

### Debug Features
- **Session Management**: Monitor session state
- **Performance Metrics**: Response times and token usage
- **Error Logs**: Detailed error information

## 🎯 Best Test Practices

### 1. Progressive Testing
```
Start Simple → Add Complexity → Test Edge Cases

1. "show sales trends" (single agent)
2. "regional sales trends" (multi-agent)  
3. "accessible regional sales dashboard" (full coordination)
```

### 2. Validation Pattern
```
For each test:
1. Send prompt
2. Check delegation occurs  
3. Verify tool execution
4. Validate response quality
5. Test response time
```

### 3. Edge Case Testing
```
Test with:
- Vague queries: "show me data"
- Complex requests: "comprehensive business intelligence"
- Invalid inputs: "xyz undefined query"
```

## 📊 Performance Expectations

| Query Type | Expected Response Time | Agent Involved |
|------------|----------------------|----------------|
| Simple Charts | < 3 seconds | chart_generation_agent |
| Geographic Data | < 4 seconds | geospatial_agent |
| Accessibility | < 3 seconds | accessibility_agent |
| Multi-Agent | < 5 seconds | Multiple agents |

## 🚀 Advanced ADK Features

### Custom Queries for Testing
```bash
# Test agent coordination
"Create an accessible dashboard showing regional sales trends with comparison charts"

# Test fallback behavior  
"Generate business intelligence components"

# Test default behavior
"Help me with data visualization"
```

### Monitoring Agent Performance
- Watch for delegation patterns in traces
- Monitor tool execution success rates
- Track response quality and component generation
- Validate multi-agent coordination efficiency

This quick reference should help you efficiently test the authentic ADK integration through the web interface!