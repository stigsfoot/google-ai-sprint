# GenUI-ADK Learning Exercises

## Phase 1: Foundation Exercises

### Exercise 1: Create Your First UI Tool
**Objective**: Build a basic metric card tool for the chart generation agent

**Task**: 
```python
# Complete this tool function (NO @Tool decorator!)
def create_revenue_card_tool(revenue_amount, period, growth_rate, target):
    """Create a revenue metric card with growth indicators"""
    # TODO: Implement the tool logic
    # Hints:
    # - Use green for positive growth, red for negative
    # - Include progress toward target
    # - Return JSX string with Card, Badge, and progress elements
    pass
Success Criteria:

Function returns valid JSX string
Styling changes based on growth_rate (positive/negative)
Includes progress indicator toward target
Uses appropriate Tremor/ShadcnUI components

Exercise 2: Agent Tool Integration
Objective: Add your tool to a chart generation agent
Task:
python# Add your revenue card tool to this agent
def create_my_chart_agent():
    return LlmAgent(
        name="my_chart_agent",
        instruction="Generate financial metric cards and charts",
        tools=[
            # TODO: Add your create_revenue_card_tool here
            # TODO: Add at least 2 more tools for different chart types
        ]
    )
Phase 2: Specialization Exercises
Exercise 3: Design a New Specialized Agent
Objective: Create an agent for a specific domain (e.g., HR analytics, inventory management)
Requirements:

Choose a business domain not covered by existing agents
Design 3-4 tools specific to that domain
Write clear agent instruction prompt
Include appropriate tool selection logic

Example Domains:

HR Analytics Agent (employee metrics, retention charts, performance dashboards)
Inventory Agent (stock levels, demand forecasting, supply chain visualization)
Customer Experience Agent (satisfaction scores, journey maps, feedback analysis)

Exercise 4: Multi-Agent Coordination
Objective: Build a query that requires multiple agents working together
Scenario: "Analyze our Q4 performance across regions with accessibility features"
Expected Agent Flow:

Root agent analyzes the query
Delegates to geospatial_agent for regional analysis
Delegates to chart_generation_agent for performance metrics
Delegates to accessibility_agent for a11y-compliant versions
Dashboard renders all generated components

Phase 3: Advanced Composition
Exercise 5: Complex Tool Composition
Objective: Create tools that coordinate outputs from multiple agents
pythondef create_executive_summary_tool(chart_outputs, map_outputs, key_metrics):
    """Compose multiple agent outputs into executive summary"""
    # TODO: Combine chart data, geographic insights, and metrics
    # TODO: Generate executive-level dashboard layout
    # TODO: Include actionable recommendations
    pass
Exercise 6: Context-Aware UI Generation
Objective: Tools that adapt based on data characteristics
Challenge: Create a tool that automatically selects chart type based on:

Data size (small datasets → simple charts, large → aggregated views)
Data type (temporal → line charts, categorical → bar charts)
Business context (executive → summary cards, analyst → detailed charts)
User accessibility needs (high contrast, screen reader compatible)

Assessment Rubric
Technical Implementation (40%)

Tool Syntax: Correct ADK tool implementation (no decorators)
JSX Quality: Valid React component syntax and structure
Agent Integration: Proper tool registration and agent configuration
Error Handling: Graceful handling of edge cases and invalid data

Conceptual Understanding (35%)

Architecture Comprehension: Understands specialized agent roles
Tool Composition: Can explain how tools work together
UI Generation Logic: Grasps dynamic component creation concepts
ADK Best Practices: Follows proper delegation and evaluation patterns

Creativity & Extension (25%)

Novel Applications: Creative use cases beyond provided examples
Domain Adaptation: Successful application to new business domains
User Experience: Consideration of accessibility and usability
Code Quality: Clean, maintainable, and well-documented implementations

Common Mistakes to Avoid

Using @Tool decorators - ADK tools are regular Python functions
Static component thinking - Remember these are dynamic, AI-generated UIs
Ignoring accessibility - Always consider inclusive design principles
Overcomplicating tools - Start simple, add complexity gradually
Forgetting business context - Tools should solve real business problems

Extension Challenges
For Advanced Students

Real-time Integration: Connect to live data sources
Interactive Components: Generate UIs with user interaction capabilities
Multi-platform Generation: Adapt tools for mobile/desktop differences
Performance Optimization: Efficient component generation for large datasets
Custom Design Systems: Integrate with brand guidelines and design tokens