# Frontend Client Testing Guide

## Overview

This guide covers testing the authentic Google ADK agents through the FastAPI bridge server that connects to the React dashboard frontend.

## Quick Start

```bash
# Terminal 1: Start ADK Server
cd /path/to/google-ai-sprint
python adk_server.py
# Server available at: http://localhost:8081

# Terminal 2: Test with curl (optional)
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "show sales trends"}'

# Terminal 3: Start React Frontend (optional)
npm run dev
# Frontend available at: http://localhost:3000
```

## 🔧 API Testing with curl

### Basic Health Check
```bash
curl http://localhost:8081/
```
**Expected Response**:
```json
{
  "status": "healthy",
  "service": "ADK Agent Bridge", 
  "agents_loaded": true,
  "environment": "loaded"
}
```

### Agent Status Check
```bash
curl http://localhost:8081/api/agents
```
**Expected Response**:
```json
{
  "root_agent": "generative_ui_orchestrator",
  "sub_agents": ["chart_generation_agent", "geospatial_agent", "accessibility_agent"],
  "status": "loaded",
  "api_configured": true
}
```

## 📊 Chart Generation Tests

### Sales Trend Analysis
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "show sales trends"}' | jq .
```

### Revenue Metrics
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "display revenue metrics for Q4"}' | jq .
```

### Performance Comparison
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "create product performance comparison"}' | jq .
```

### Combined Dashboard
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "sales dashboard with trends and metrics"}' | jq .
```

## 🗺️ Geographic Analysis Tests

### Regional Performance
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "show regional performance"}' | jq .
```

### Territory Breakdown
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "territory sales breakdown"}' | jq .
```

### Location Metrics
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "location-based sales metrics"}' | jq .
```

### Geographic Dashboard
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "comprehensive regional analysis"}' | jq .
```

## ♿ Accessibility Tests

### High Contrast Charts
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "accessible sales charts"}' | jq .
```

### Screen Reader Compatible
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "screen reader compatible dashboard"}' | jq .
```

### Keyboard Navigation
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "keyboard navigable interface"}' | jq .
```

### WCAG Compliant
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "wcag compliant business dashboard"}' | jq .
```

## 🔄 Multi-Agent Coordination Tests

### Accessible Regional Analysis
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "accessible regional sales analysis"}' | jq .
```

### Comprehensive BI Dashboard
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "comprehensive business intelligence dashboard"}' | jq .
```

### Complex Multi-Component
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "accessible geographic sales trends with performance metrics"}' | jq .
```

## ✅ Response Validation

### Expected Response Structure
```json
{
  "success": true,
  "query": "your_query_here",
  "components": [
    {
      "agent": "chart_generation_agent",
      "component_type": "sales_trend",
      "component_code": "<Card className=\"p-6 bg-gradient-to-r...\">...</Card>",
      "business_context": "ADK Agent response for: your_query_here"
    }
  ],
  "total_components": 1,
  "processing_time": "2.1s",
  "agent_trace": [
    "Authentic ADK Runner received query",
    "LLM analyzed query for delegation needs",
    "Delegated to appropriate specialized sub-agents",
    "Sub-agents used tool calling to generate UI components",
    "Root agent coordinated and returned results"
  ]
}
```

### Component Code Validation
The `component_code` should contain:
- **Valid JSX**: React component syntax
- **Tailwind CSS**: Professional styling classes
- **Sample Data**: Realistic business metrics
- **Complete Structure**: Self-contained renderable component

### Example Valid Component
```jsx
<Card className="p-6 bg-gradient-to-r from-green-50 to-blue-50">
  <CardHeader>
    <div className="flex items-center space-x-2">
      <TrendingUp className="h-6 w-6 text-green-600" />
      <CardTitle className="text-lg">Sales Trend - Q4 2024</CardTitle>
    </div>
  </CardHeader>
  <CardContent>
    <div className="mt-4">
      <LineChart 
        data={[{"month": "Jan", "value": 1200}, {"month": "Feb", "value": 1350}]}
        className="h-64"
        stroke="#10b981"
        strokeWidth={3}
      />
    </div>
    <div className="mt-4 p-3 bg-green-50 rounded-lg">
      <p className="text-sm text-green-800">Sales showing strong upward trend with 23% growth</p>
    </div>
  </CardContent>
</Card>
```

## 🚀 React Frontend Integration

### Testing in React Dashboard

1. **Start the frontend**:
   ```bash
   npm run dev
   # Access at http://localhost:3000
   ```

2. **Test these queries in the dashboard**:
   - "show sales trends"
   - "regional performance analysis"
   - "accessible dashboard components"

3. **Verify component rendering**:
   - Components appear in dashboard grid
   - Styling applies correctly
   - Data displays properly
   - Interactive elements work

### Frontend Integration Checklist

- [ ] **API Connection**: Frontend successfully calls `/api/analyze`
- [ ] **Response Parsing**: JSX components extracted from API response
- [ ] **Component Rendering**: Components render without errors
- [ ] **Styling**: Tailwind CSS classes apply correctly
- [ ] **Data Display**: Sample business data appears properly
- [ ] **Error Handling**: Failed requests handled gracefully

## 🔧 Troubleshooting

### Issue: Server Connection Failed
```bash
# Check server status
curl http://localhost:8081/

# Restart server
pkill -f "python adk_server.py"
python adk_server.py
```

### Issue: Agents Not Available
```bash
# Check agent loading
curl http://localhost:8081/api/agents

# Verify environment
echo $GOOGLE_API_KEY
```

### Issue: Invalid JSX in Response
**Common causes**:
- Missing quotes in component attributes
- Improper JSON escaping
- Malformed Tailwind classes

**Debug with**:
```bash
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "simple sales chart"}' | jq '.components[0].component_code'
```

### Issue: Empty or Text Responses
**Indicates**: Agent not calling tools properly
**Check**: Agent instructions and tool integration

### Issue: Slow Response Times
**Normal**: 2-5 seconds for ADK agent processing
**Slow**: >10 seconds may indicate API rate limiting

## 📈 Performance Testing

### Load Testing
```bash
# Test multiple concurrent requests
for i in {1..5}; do
  curl -X POST "http://localhost:8081/api/analyze" \
    -H "Content-Type: application/json" \
    -d '{"query": "show sales trends"}' \
    --silent --output /dev/null &
done
wait
echo "Load test complete"
```

### Response Time Benchmarking
```bash
# Time a single request
time curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "show sales trends"}' \
  --silent --output /dev/null
```

## 🎯 Best Practices

### Testing Workflow
1. **Start Simple**: Test basic queries first
2. **Validate Structure**: Check response format
3. **Test Components**: Verify JSX syntax
4. **Test Integration**: Use React frontend
5. **Load Test**: Check performance under load

### Query Optimization
- **Be Specific**: "sales trends Q4" vs "show data"
- **Use Keywords**: Include "regional", "accessible", "trends"
- **Test Variations**: Try different phrasings

### Error Handling
- Always check `success: true` in response
- Handle `components: []` empty arrays
- Validate JSX before rendering
- Implement retry logic for API failures

This comprehensive frontend testing guide ensures robust integration between the authentic ADK agents and your React dashboard!