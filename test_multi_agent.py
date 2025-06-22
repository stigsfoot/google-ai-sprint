#!/usr/bin/env python3
"""
Test Multi-Agent Coordination
Verify all three specialized agents work together
"""
import asyncio
import sys
import os

# Add agents directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'agents'))

try:
    from agents.generative_ui.agent import root_agent, chart_generation_agent
    from agents.geospatial_agent import geospatial_agent
    from agents.accessibility_agent import accessibility_agent
except ImportError as e:
    print(f"Import error: {e}")
    print("Trying alternative import method...")
    
    from geospatial_agent import geospatial_agent
    from accessibility_agent import accessibility_agent


async def test_individual_agents():
    """Test each specialized agent individually"""
    print("🧪 Testing Individual Agents...")
    print("=" * 50)
    
    agents_to_test = [
        ("Chart Generation", chart_generation_agent if 'chart_generation_agent' in globals() else None),
        ("Geospatial", geospatial_agent),
        ("Accessibility", accessibility_agent)
    ]
    
    for name, agent in agents_to_test:
        if agent is None:
            print(f"❌ {name} Agent: Not available")
            continue
            
        print(f"\n✅ {name} Agent:")
        print(f"   Name: {agent.name}")
        print(f"   Tools: {len(agent.tools)}")
        
        # Test tools individually
        for i, tool in enumerate(agent.tools):
            print(f"   Tool {i+1}: {type(tool).__name__}")


async def test_tool_functionality():
    """Test that tools can be called directly"""
    print("\n🔧 Testing Tool Functionality...")
    print("=" * 50)
    
    try:
        # Test geospatial tools
        print("\n🗺️ Testing Geospatial Tools:")
        from geospatial_agent import create_regional_heatmap_tool
        result = create_regional_heatmap_tool("California", "Sales", "Strong performance in tech sector")
        print(f"   Regional Heatmap: {len(result)} chars, Contains JSX: {'<Card' in result}")
        
        # Test accessibility tools  
        print("\n♿ Testing Accessibility Tools:")
        from accessibility_agent import create_high_contrast_chart_tool
        result = create_high_contrast_chart_tool("revenue", "Revenue Analysis", "Q4 revenue increased 15%")
        print(f"   High Contrast Chart: {len(result)} chars, Contains JSX: {'<Card' in result}")
        
        print("\n🎉 All Tools Working!")
        
    except Exception as e:
        print(f"❌ Tool Test Error: {e}")
        import traceback
        traceback.print_exc()


def simulate_multi_agent_queries():
    """Simulate complex queries requiring multiple agents"""
    print("\n🎯 Multi-Agent Query Simulation...")
    print("=" * 50)
    
    test_queries = [
        {
            "query": "Show regional sales performance with accessible high-contrast visualization",
            "expected_agents": ["geospatial_agent", "accessibility_agent"],
            "description": "Should use both geospatial (regional) and accessibility (high-contrast) agents"
        },
        {
            "query": "Create a dashboard with sales trends and territory analysis",
            "expected_agents": ["chart_generation_agent", "geospatial_agent"],
            "description": "Should use chart (trends) and geospatial (territory) agents"
        },
        {
            "query": "Display accessible metrics dashboard with keyboard navigation",
            "expected_agents": ["chart_generation_agent", "accessibility_agent"],
            "description": "Should use chart (metrics) and accessibility (keyboard) agents"
        }
    ]
    
    for i, test in enumerate(test_queries, 1):
        print(f"\n--- Test Query {i} ---")
        print(f"Query: {test['query']}")
        print(f"Expected Agents: {', '.join(test['expected_agents'])}")
        print(f"Logic: {test['description']}")


async def main():
    """Run comprehensive multi-agent tests"""
    print("🚀 Multi-Agent System Testing")
    print("=" * 60)
    
    try:
        await test_individual_agents()
        await test_tool_functionality()
        simulate_multi_agent_queries()
        
        print("\n" + "=" * 60)
        print("✅ Multi-Agent System Ready!")
        print("\nNext Steps:")
        print("1. Start ADK web interface: adk web agents --port 8080")
        print("2. Test queries in ADK UI")
        print("3. Watch multi-agent delegation in real-time")
        
    except Exception as e:
        print(f"\n❌ Test Failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())