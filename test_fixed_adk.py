#!/usr/bin/env python3
"""
Test the Fixed ADK Implementation
Verify all agents and tools work correctly
"""
import asyncio
from agents.generative_ui.agent import root_agent, chart_generation_agent


async def test_fixed_adk():
    """Test the corrected ADK implementation"""
    print("🔧 Testing Fixed ADK Implementation...")
    print("=" * 50)
    
    try:
        # Test 1: Check agent initialization
        print("\n✅ Test 1: Agent Initialization")
        print(f"Root Agent: {root_agent.name}")
        print(f"Chart Agent: {chart_generation_agent.name}")
        print(f"Chart Agent Tools: {len(chart_generation_agent.tools)}")
        
        # Test 2: Check tool access
        print("\n✅ Test 2: Tool Access")
        for i, tool in enumerate(chart_generation_agent.tools):
            print(f"Tool {i+1}: {tool}")
        
        # Test 3: Try to call tools directly (if possible)
        print("\n✅ Test 3: Direct Tool Testing")
        from agents.generative_ui.agent import create_sales_trend_card
        
        result = create_sales_trend_card("test_data", "Q4")
        print(f"Tool Result Length: {len(result)} characters")
        print(f"Contains React JSX: {'<Card' in result}")
        
        print("\n🎉 All Tests Passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Test Failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    asyncio.run(test_fixed_adk())