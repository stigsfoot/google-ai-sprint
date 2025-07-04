# Test Prompts for Generative UI System

This document provides comprehensive test prompts to validate both the **ADK Web UI** and **Frontend Dashboard** functionality.

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

This comprehensive test suite validates the entire system from basic functionality to advanced multi-agent coordination, ensuring both educational value and production-level reliability.