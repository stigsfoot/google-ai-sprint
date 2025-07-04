# Test Prompts for Generative UI System

This document provides comprehensive test prompts to validate the **multi-agent generative UI system** using curl commands, ADK Web UI, and frontend dashboard tests. Tests are organized from simple single-agent requests to complex multi-agent coordination scenarios.

## 📡 **API Testing with Curl Commands (Postman Compatible)**

### **Postman Collection Setup**

**Base Configuration**
- **Base URL**: `http://localhost:8081`
- **Content-Type**: `application/json`
- **Method**: `POST`
- **Endpoint**: `/api/analyze`

**Request Body Template**
```json
{
  "query": "{{test_query}}"
}
```

**Environment Variables for Postman**
```json
{
  "base_url": "http://localhost:8081",
  "api_endpoint": "/api/analyze",
  "content_type": "application/json"
}
```

### **Basic Single-Agent Tests**

**Chart Generation Agent**
```bash
# Simple sales trend
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "show sales trends"}'

# Revenue metrics
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "revenue metrics"}'

# Product comparison
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "compare product performance"}'
```

**Geospatial Agent**
```bash
# Regional analysis
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "regional performance data"}'

# California-specific map
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "california territory analysis"}'

# New York metrics
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "new york metrics"}'
```

**Accessibility Agent**
```bash
# High contrast charts
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "accessible sales dashboard"}'

# Screen reader table
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "screen reader compatible table"}'
```

**Dashboard Layout Agent**
```bash
# Comprehensive BI dashboard
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "comprehensive business intelligence dashboard"}'

# YTD metrics dashboard
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "YTD metrics dashboard"}'

# Ranking table
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "top performers ranking"}'
```

### **Multi-Agent Coordination Tests**

```bash
# Chart + Geospatial coordination
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "regional sales trends with geographic breakdown"}'

# All agents coordination
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "accessible comprehensive business intelligence dashboard"}'

# Complex BI request
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "business intelligence dashboard of the data we have"}'
```

### **Performance Testing Commands**

```bash
# Rapid fire testing (run these in succession)
curl -X POST "http://localhost:8081/api/analyze" -H "Content-Type: application/json" -d '{"query": "sales trends"}' &
curl -X POST "http://localhost:8081/api/analyze" -H "Content-Type: application/json" -d '{"query": "california map"}' &
curl -X POST "http://localhost:8081/api/analyze" -H "Content-Type: application/json" -d '{"query": "accessible dashboard"}' &
wait
```

## 🌐 **ADK Web UI Testing**

Start the ADK Web UI: `adk web agents --port 8080`

### **Simple Agent Tests**
```
show sales trends
revenue metrics
compare products
regional performance
california analysis
texas metrics
accessible charts
high contrast dashboard
business intelligence dashboard
YTD metrics
top performers
ranking table
```

### **Location Intelligence Tests**
```
california
texas sales map
new york territory
florida breakdown
seattle metrics
chicago performance
west coast analysis
southeast region
```

### **Multi-Agent Scenarios**
```
comprehensive business intelligence dashboard
accessible regional sales analysis
interactive dashboard with maps and charts
business intelligence dashboard of the data we have
multi-territory performance dashboard
accessible geographic sales visualization
```

### **Edge Case Tests**
```
show me data
business intelligence
help with visualization
create dashboard
xyz undefined query
```

## 💻 **Frontend Dashboard Testing**

Access the React dashboard at: `http://localhost:3001`

### **Progressive Complexity Tests**

**Level 1: Single Component Generation**
```
sales trends
revenue metrics
california map
accessible chart
```

**Level 2: Enhanced Components**
```
quarterly sales trends
regional performance analysis
high contrast sales dashboard
YTD performance metrics
```

**Level 3: Complex Dashboards**
```
business intelligence dashboard
comprehensive dashboard
business intelligence dashboard of the data we have
interactive sales and geographic dashboard
```

**Level 4: Multi-Agent Coordination**
```
accessible comprehensive business intelligence dashboard
regional sales analysis with interactive maps
business intelligence dashboard with accessibility features
comprehensive multi-territory performance dashboard
```

## 🎯 **Core Functionality Tests**

### **Chart Generation Agent**
Test prompts for sales trends, metrics, and comparison visualizations:

```
show sales trends
```
**Expected**: Line chart with Q4 sales trend data

```
revenue metrics
```
**Expected**: Metric card with $47.2K revenue and +12.3% growth

```
compare product performance
```
**Expected**: Bar chart comparing Product A-D performance

```
quarterly revenue trends
```
**Expected**: Sales trend chart with quarterly breakdown

```
display key performance indicators
```
**Expected**: Metric card with KPI data and change indicator

### **Geospatial Agent**
Test prompts for location-based visualizations and regional analysis:

```
regional performance data
```
**Expected**: US-wide heatmap with all states performance data

```
california territory analysis
```
**Expected**: California-focused map with zoom level 6, CA-specific data

```
texas sales map
```
**Expected**: Texas-centered map with territory analysis and markets

```
new york metrics
```
**Expected**: New York location metrics with mini-map

```
show florida territory breakdown
```
**Expected**: Florida territory analysis with regional markets

```
lets look at illinois
```
**Expected**: Illinois location metrics card

### **Accessibility Agent**
Test prompts for WCAG-compliant components:

```
accessible sales dashboard
```
**Expected**: High contrast chart with accessibility features

```
screen reader compatible table
```
**Expected**: ARIA-labeled data table with screen reader optimization

```
keyboard navigable interface
```
**Expected**: Dashboard with keyboard navigation instructions

```
high contrast data visualization
```
**Expected**: High contrast chart with enhanced visibility features

```
wcag compliant charts
```
**Expected**: Accessible chart component with ARIA labels

## 🔄 **Multi-Agent Coordination Tests**

### **Complex Delegation**
Test prompts that require multiple agent coordination:

```
show accessible regional sales trends
```
**Expected**: Geospatial + accessibility agent coordination

```
create accessible california sales dashboard
```
**Expected**: Geographic focus + accessibility features

```
regional sales comparison with high contrast
```
**Expected**: Chart + geospatial + accessibility coordination

```
comprehensive business intelligence dashboard
```
**Expected**: Multi-agent composition with various components

## 📊 **Specific Component Tests**

### **Sales & Performance**
```
1. "display revenue metrics"
2. "create performance comparison"  
3. "quarterly trends analysis"
4. "sales dashboard components"
5. "show profit margins"
6. "monthly sales breakdown"
7. "year over year growth"
8. "revenue vs target analysis"
```

### **Geographic & Regional**
```
1. "territory breakdown analysis"
2. "show location-based metrics"
3. "geographic sales distribution"
4. "regional market performance"
5. "west coast sales territory"
6. "southeast region analysis"
7. "midwest territory performance"
8. "pacific northwest markets"
```

### **Accessibility & Compliance**
```
1. "high contrast data visualization"
2. "screen reader compatible dashboard"
3. "keyboard navigable interface"
4. "wcag compliant charts"
5. "accessible performance metrics"
6. "voice navigation dashboard"
7. "large text visualization"
8. "color blind friendly charts"
```

## 🚀 **Edge Case & Robustness Tests**

### **Vague Queries**
Test how agents handle ambiguous requests:

```
show me data
```
**Expected**: Intelligent default (likely chart generation)

```
business intelligence
```
**Expected**: Agent reasoning and appropriate delegation

```
help with visualization
```
**Expected**: Default chart or metric component

### **Invalid/Unusual Queries**
Test error handling and fallbacks:

```
xyz undefined query
```
**Expected**: Graceful fallback with default component

```
show me purple elephants
```
**Expected**: Agent interprets as general visualization request

```
@#$%^&*()
```
**Expected**: Error handling with fallback response

### **Rate Limit Testing**
Test circuit breaker functionality:

```
regional performance data
```
**(Repeat 4+ times quickly)**
**Expected**: Circuit breaker activates, shows rate limit message

## 🎬 **Demo Scenarios**

### **Business Executive Demo**
Sequential prompts for comprehensive business overview:

```
1. "show quarterly sales trends"
2. "california territory performance"  
3. "accessible revenue dashboard"
4. "regional market comparison"
```

### **Technical Demo**
Showcase advanced agent coordination:

```
1. "comprehensive accessible regional sales analysis"
2. "multi-territory performance with high contrast visualization"
3. "keyboard navigable geographic dashboard"
```

### **Location-Specific Deep Dive**
Demonstrate geographic intelligence:

```
1. "texas"
2. "texas metrics"  
3. "texas territory analysis"
4. "texas sales map"
```
**Expected**: Progressive detail from basic to comprehensive Texas analysis

## 🔧 **Performance & Quality Validation**

### **Response Time Benchmarks**
| Query Type | Expected Time | Agent(s) |
|------------|---------------|----------|
| Simple Charts | < 3 seconds | chart_generation_agent |
| Geographic Data | < 4 seconds | geospatial_agent |
| Accessibility | < 3 seconds | accessibility_agent |
| Multi-Agent | < 5 seconds | Multiple agents |

### **Quality Checklist**
For each test, verify:
- [ ] Agent responds within expected timeframe
- [ ] No "Could you please provide..." responses
- [ ] JSX component code generated
- [ ] Contains Tailwind CSS classes
- [ ] Includes sample business data
- [ ] Professional business insights included
- [ ] Proper delegation occurs (ADK Web UI traces)

## 🌐 **Frontend vs ADK Web UI Testing**

### **Frontend Dashboard Tests**
Use these prompts in the React dashboard at `http://localhost:3000`:

```
regional sales performance
show accessible charts
california territory analysis
quarterly revenue trends
```

### **ADK Web UI Tests** 
Use these same prompts in ADK Web Interface at `http://localhost:8080`:

```
regional sales performance
show accessible charts  
california territory analysis
quarterly revenue trends
```

**Compare**:
- Agent delegation patterns
- Tool execution traces
- Response generation speed
- Component output quality

## 🎯 **Advanced Testing Scenarios**

### **Rapid Fire Testing**
Test system resilience with quick successive queries:

```
sales trends
california map
accessible dashboard
revenue metrics
texas analysis
```
**(Submit within 10 seconds)**

### **Location Intelligence Testing**
Test geographic detection accuracy:

```
"Show me New York" → NY-focused map
"California breakdown" → CA territory analysis  
"Texas metrics" → TX location metrics
"Florida performance" → FL territory data
```

### **Agent Specialization Testing**
Verify proper agent selection:

```
Charts/Metrics → chart_generation_agent
Maps/Regional → geospatial_agent
Accessibility → accessibility_agent
```

## 📝 **Documentation for Demos**

### **YouTube Teaching Points**
1. **Agent Reasoning**: Show how LLM analyzes query intent
2. **Tool Selection**: Demonstrate intelligent delegation
3. **Component Generation**: Real React.createElement output
4. **Error Handling**: Circuit breakers and rate limit protection
5. **Production Quality**: Professional UI components

### **Student Learning Outcomes**
- Understanding real ADK agent patterns vs simulations
- Seeing authentic LLM reasoning and delegation
- Learning tool calling and component generation
- Experiencing production-quality generative UI

## 🧪 **Validation & Success Criteria**

### **Expected Response Patterns**

**Single-Agent Responses (2-4 seconds)**
```json
{
  "success": true,
  "query": "show sales trends",
  "components": [
    {
      "agent": "chart_generation_agent",
      "component_type": "sales_trend",
      "component_code": "React.createElement(Card, {...})",
      "business_context": "Sales trend analysis with Q4 data"
    }
  ],
  "total_components": 1,
  "processing_time": "2.1s",
  "agent_trace": ["Root agent delegated to chart_generation_agent"]
}
```

**Multi-Agent Responses (3-6 seconds)**
```json
{
  "success": true,
  "query": "comprehensive business intelligence dashboard",
  "components": [
    {
      "agent": "dashboard_layout_agent",
      "component_type": "comprehensive_dashboard",
      "component_code": "React.createElement(\"div\", {...}) // 8000+ chars",
      "business_context": "Complete BI dashboard with tabs, map, metrics, rankings"
    }
  ],
  "total_components": 1,
  "processing_time": "3.2s",
  "agent_trace": ["Delegated to dashboard_layout_agent", "Comprehensive dashboard generated"]
}
```

### **Component Validation Checklist**

For each successful response, verify:
- [ ] **Success Flag**: `"success": true`
- [ ] **Component Code**: Contains `React.createElement` syntax
- [ ] **Agent Attribution**: Correct agent name in response
- [ ] **Business Context**: Meaningful business insight included
- [ ] **Processing Time**: Within expected ranges (2-6 seconds)
- [ ] **No Questions**: Agent never asks for clarification
- [ ] **Professional Styling**: Includes Tailwind CSS classes
- [ ] **Interactive Elements**: Hover states, transitions, click handlers

### **Multi-Agent Architecture Validation**

**Agent Delegation Patterns**
```
"sales trends" → chart_generation_agent
"california map" → geospatial_agent  
"accessible dashboard" → accessibility_agent
"business intelligence dashboard" → dashboard_layout_agent
"accessible regional analysis" → multi-agent coordination
```

**Component Integration**
- Dashboard components include multiple data types
- Interactive maps with clickable regions
- Tab navigation between different views
- YTD metrics with trend indicators
- Ranking tables with performance data

### **Performance Benchmarks**

| Test Type | Expected Time | Agent(s) | Component Size |
|-----------|---------------|----------|----------------|
| Simple Chart | 2-3s | chart_generation_agent | 1-2KB |
| Regional Map | 3-4s | geospatial_agent | 2-4KB |
| Accessibility | 2-3s | accessibility_agent | 1-3KB |
| BI Dashboard | 3-5s | dashboard_layout_agent | 8-12KB |
| Multi-Agent | 4-6s | Multiple | Variable |

### **Quality Assurance Steps**

1. **Start Services**
   ```bash
   # Terminal 1: ADK Server
   python adk_server.py
   
   # Terminal 2: Frontend
   cd dashboard && npm run dev
   
   # Terminal 3: ADK Web UI (optional)
   adk web agents --port 8080
   ```

2. **Run Basic Tests**
   ```bash
   curl -X POST "http://localhost:8081/api/analyze" \
     -H "Content-Type: application/json" \
     -d '{"query": "show sales trends"}'
   ```

3. **Verify Dashboard Generation**
   ```bash
   curl -X POST "http://localhost:8081/api/analyze" \
     -H "Content-Type: application/json" \
     -d '{"query": "comprehensive business intelligence dashboard"}'
   ```

4. **Test Frontend Integration**
   - Visit `http://localhost:3001`
   - Enter: "business intelligence dashboard"
   - Verify dashboard renders with tabs, map, metrics

### **Troubleshooting Common Issues**

**Server Not Starting**
```bash
# Check environment
echo $GOOGLE_API_KEY
# Check dependencies
pip install -r requirements.txt
```

**Agent Import Errors**
```bash
# Verify agent structure
python -c "from agents.generative_ui.agent import root_agent; print(root_agent.name)"
```

**Frontend Connection Issues**
```bash
# Check server health
curl http://localhost:8081/
# Verify CORS settings in adk_server.py
```

**Fixed Issues (v2.0)**
- ✅ **Default Parameter Error**: Removed all default values from function signatures (Google AI doesn't support them)
- ✅ **Function Loop Prevention**: Enhanced circuit breaker to prevent infinite tool calling
- ✅ **Multi-Agent Coordination**: Complex queries like "comprehensive accessible regional sales analysis" now work perfectly
- ✅ **Performance**: All queries complete in 2-6 seconds without timeouts

## 🎬 **Demo Sequence Recommendations**

### **Quick Demo (5 minutes)**
```bash
# 1. Simple chart
curl -X POST "http://localhost:8081/api/analyze" -H "Content-Type: application/json" -d '{"query": "sales trends"}'

# 2. Geographic focus  
curl -X POST "http://localhost:8081/api/analyze" -H "Content-Type: application/json" -d '{"query": "california territory analysis"}'

# 3. Comprehensive dashboard
curl -X POST "http://localhost:8081/api/analyze" -H "Content-Type: application/json" -d '{"query": "business intelligence dashboard"}'
```

### **Complete Demo (15 minutes)**
1. **Single Agents**: Show each agent individually
2. **Multi-Agent**: Demonstrate coordination
3. **Frontend**: Show React dashboard integration
4. **ADK Web UI**: Show agent traces and reasoning

### **System Status Verification**
```bash
# Health check
curl http://localhost:8081/

# Agent availability
curl -X POST "http://localhost:8081/api/analyze" -H "Content-Type: application/json" -d '{"query": "test"}' | jq '.success'
```

## 📊 **Expected Success Metrics**

- **API Response Rate**: 100% success for valid queries
- **Response Time**: 95% under 5 seconds
- **Component Generation**: All responses contain React.createElement code
- **Agent Delegation**: Correct agent selection for query types
- **Frontend Integration**: Seamless component rendering
- **Business Quality**: Professional insights and data visualization

This comprehensive test suite validates the entire system from basic functionality to advanced multi-agent coordination, ensuring both educational value and production-level reliability.

---

**🚀 Ready for Production Demonstration!** Use these tests to validate the complete multi-agent generative UI system across all interfaces and scenarios.