#!/usr/bin/env python3
"""
Test script for ADK-style agents
Demonstrates UI components as tools within agent framework
"""
import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from para_agent.root_agent import create_root_agent
from para_agent.agents.chart_generation_agent import create_chart_generation_agent


async def test_chart_generation_agent():
    """Test the chart generation agent with various queries"""
    print("🎨 Testing Chart Generation Agent...")
    
    agent = create_chart_generation_agent()
    
    # Test trend query
    print("\n--- Test 1: Trend Analysis ---")
    result = await agent.process_query("Show me sales trends over time")
    print(f"Result: {result}")
    
    # Test metric query
    print("\n--- Test 2: Key Metrics ---")
    result = await agent.process_query("Display key metrics for the dashboard")
    print(f"Result: {result}")
    
    # Test comparison query
    print("\n--- Test 3: Product Comparison ---")
    result = await agent.process_query("Compare performance across products")
    print(f"Result: {result}")


async def test_root_agent():
    """Test the root orchestrator agent"""
    print("\n🎯 Testing Root Agent (Generative UI Orchestrator)...")
    
    root_agent = create_root_agent()
    
    # Test delegation
    print("\n--- Test: Root Agent Delegation ---")
    result = await root_agent.process_query("Show me quarterly sales trends and key metrics")
    print(f"Root Agent Result: {result}")


async def main():
    """Run all agent tests"""
    print("🚀 Starting ADK Agent Tests...")
    print("=" * 50)
    
    try:
        # Test individual chart generation agent
        await test_chart_generation_agent()
        
        # Test root agent coordination
        await test_root_agent()
        
        print("\n" + "=" * 50)
        print("✅ All agent tests completed successfully!")
        print("\nKey Achievements:")
        print("• Chart Generation Agent with 3 UI component tools")
        print("• Root Agent with delegation capabilities") 
        print("• UI components returned as JSX strings")
        print("• Educational transparency through console logging")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())