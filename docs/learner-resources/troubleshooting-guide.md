# GenUI-ADK Troubleshooting Guide

## Common Issues and Solutions

### 1. Tool Not Found Errors
**Problem**: Agent can't find or call your tool
**Symptoms**: "Tool X not found" or "No tool available for task Y"

**Solutions**:
- Verify tool is added to agent's tools list
- Check function name matches exactly
- Ensure function is properly defined (no syntax errors)
- Confirm no @Tool decorators are used (ADK doesn't use them)

```python
# ❌ Incorrect - Don't use decorators
@Tool
def my_tool(data):
    return "..."

# ✅ Correct - Plain function
def my_tool(data):
    return "..."

# ✅ Correct - Add to agent
agent = LlmAgent(
    name="my_agent",
    tools=[my_tool]  # Function reference, not string
)
2. Invalid JSX Output
Problem: Generated components don't render properly
Symptoms: Dashboard shows errors or blank components
Solutions:

Validate JSX syntax (closing tags, proper nesting)
Check for unescaped quotes in dynamic content
Ensure all variables are properly interpolated
Test JSX in isolation before integrating

python# ❌ Invalid JSX - Missing quotes, improper nesting
def bad_tool(title, data):
    return f'''
    <Card className=p-6>  <!-- Missing quotes -->
        <CardTitle>{title}
        <LineChart data={data} />  <!-- Missing closing tag -->
    </Card>
    '''

# ✅ Valid JSX
def good_tool(title, data):
    return f'''
    <Card className="p-6">
        <CardTitle>{title}</CardTitle>
        <LineChart data={{{json.dumps(data)}}} />
    </Card>
    '''
3. Agent Delegation Issues
Problem: Root agent not properly delegating to sub-agents
Symptoms: All responses from root agent, no delegation visible in traces
Solutions:

Review agent instruction prompts for clarity
Ensure sub-agents are properly registered
Check delegation conditions in root agent logic
Verify sub-agent capabilities are clearly described

4. Styling and Layout Problems
Problem: Components render but look broken or unstyled
Symptoms: Missing styles, poor layout, accessibility issues
Solutions:

Use complete Tailwind class names (e.g., "text-blue-600" not "blue")
Include proper container and spacing classes
Test responsive behavior across screen sizes
Validate accessibility attributes (aria-labels, etc.)

5. Data Serialization Errors
Problem: Complex data structures cause rendering failures
Symptoms: JSON serialization errors, data display issues
Solutions:

Use json.dumps() for complex data structures
Handle None/null values appropriately
Escape special characters in text content
Validate data types before processing

Debugging Strategies
1. ADK Web Interface Debugging

Use ADK web UI to trace agent interactions
Check tool call parameters and return values
Monitor delegation flow between agents
Review error messages in trace logs

2. Component Testing
python# Test tools in isolation
def test_my_tool():
    sample_data = [{"x": 1, "y": 10}, {"x": 2, "y": 20}]
    result = my_tool(sample_data, "Test Chart", "up", "Growth trend")
    print(result)  # Check JSX output
    # Copy JSX to test in React playground

test_my_tool()
3. Progressive Development

Start with simple static JSX
Add dynamic data interpolation
Include conditional styling
Test edge cases and error conditions
Integrate with agent system

4. Common Debugging Commands
python# Check agent configuration
print(f"Agent tools: {[tool.__name__ for tool in agent.tools]}")

# Validate tool output
result = my_tool(test_data)
print(f"Tool output length: {len(result)}")
print(f"Contains JSX: {'<Card' in result}")

# Test JSON serialization
import json
test_data = {"values": [1, 2, 3]}
print(json.dumps(test_data))  # Ensure no serialization errors
Performance Optimization
1. Efficient Tool Design

Minimize tool execution time
Cache expensive computations
Use appropriate data structures
Avoid unnecessary DOM complexity

2. Component Optimization

Limit nesting depth in generated JSX
Use efficient chart rendering libraries
Minimize inline styles (prefer CSS classes)
Optimize for mobile rendering

3. Agent Coordination

Design clear agent responsibilities
Minimize cross-agent dependencies
Use efficient delegation patterns
Cache common tool results

Getting Help
1. Self-Diagnosis Checklist

 Tool functions defined without decorators
 Tools added to agent's tools list
 JSX syntax validated
 Data properly serialized
 Agent instructions clear and specific

2. Community Resources

ADK documentation and examples
Student discussion forums
Code review sessions
Office hours and Q&A sessions

3. Advanced Support

Share ADK trace logs for complex issues
Provide minimal reproducible examples
Document expected vs actual behavior
Include relevant error messages and stack traces

