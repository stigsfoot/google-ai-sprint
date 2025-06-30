#!/usr/bin/env python3
"""
Test script for ADK agent functionality
Systematic test cases to verify all components work correctly
"""
import asyncio
import json
import os
import sys
from typing import List, Dict

# Add agents to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'agents'))

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from dotenv import load_dotenv

# Load environment variables
load_dotenv('agents/.env')

async def test_adk_agents():
    """Comprehensive test suite for ADK agents"""
    
    print("🧪 Starting ADK Agent Test Suite")
    print("=" * 50)
    
    # Import agents
    try:
        from agents import root_agent
        print(f"✅ Root agent loaded: {root_agent.name}")
        
        # Check sub-agents
        if hasattr(root_agent, 'sub_agents') and root_agent.sub_agents:
            print(f"✅ Sub-agents: {[agent.name for agent in root_agent.sub_agents]}")
        
        # Check tools (root should have none - only delegates)
        if hasattr(root_agent, 'tools'):
            if root_agent.tools:
                print(f"⚠️  Root agent has tools: {[tool.__name__ for tool in root_agent.tools]} (should delegate instead)")
            else:
                print("✅ Root agent has no tools - properly delegates to sub-agents")
        
        # Check sub-agent tools
        for sub_agent in root_agent.sub_agents:
            if hasattr(sub_agent, 'tools') and sub_agent.tools:
                print(f"✅ {sub_agent.name} tools: {[tool.__name__ for tool in sub_agent.tools]}")
        
    except ImportError as e:
        print(f"❌ Failed to import agents: {e}")
        return False
    
    # Initialize runner
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name="test_suite",
        session_service=session_service
    )
    
    # Test cases
    test_cases = [
        {
            "name": "Simple Sales Trend",
            "query": "show me sales trends for Q4",
            "expected_elements": ["<Card", "LineChart", "Sales", "Q4"],
            "expected_type": "trend_line"
        },
        {
            "name": "Metric Card Generation",
            "query": "create a metric card for monthly revenue",
            "expected_elements": ["<Card", "Badge", "revenue", "metric"],
            "expected_type": "metric_card"
        },
        {
            "name": "Product Comparison",
            "query": "compare product performance",
            "expected_elements": ["<Card", "BarChart", "Product", "comparison"],
            "expected_type": "comparison_bar"
        },
        {
            "name": "Regional Sales",
            "query": "Display regional performance with territory breakdown",
            "expected_elements": ["regional", "territory", "performance"],
            "expected_type": "regional_heatmap"
        },
        {
            "name": "Accessible Dashboard",
            "query": "Show regional sales with accessible high-contrast visualization",
            "expected_elements": ["accessible", "high-contrast", "aria-label"],
            "expected_type": "accessible_dashboard"
        }
    ]
    
    results = []
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🧪 Test {i}: {test_case['name']}")
        print(f"Query: {test_case['query']}")
        
        try:
            # Create session
            session_id = f"test_session_{i}"
            user_id = f"test_user_{i}"
            
            # Create the session first
            session = await session_service.create_session(
                app_name="test_suite",
                user_id=user_id,
                session_id=session_id,
                state={}
            )
            
            # Create message
            content = types.Content(
                role="user",
                parts=[types.Part(text=test_case['query'])]
            )
            
            # Execute agent
            agent_response = ""
            async for event in runner.run_async(
                user_id=user_id,
                session_id=session_id,
                new_message=content
            ):
                if event.is_final_response() and event.content:
                    agent_response = event.content.parts[0].text
                    break
            
            # Analyze response for multi-agent delegation
            contains_delegation = "transfer_to_agent" in agent_response.lower() or any(agent_name in agent_response.lower() for agent_name in ["chart_generation", "geospatial", "accessibility"])
            
            response_analysis = {
                "test_name": test_case['name'],
                "query": test_case['query'],
                "response_length": len(agent_response),
                "contains_jsx": "<Card" in agent_response,
                "contains_delegation": contains_delegation,
                "expected_elements_found": sum(1 for elem in test_case['expected_elements'] if elem in agent_response),
                "total_expected": len(test_case['expected_elements']),
                "raw_response": agent_response[:200] + "..." if len(agent_response) > 200 else agent_response,
                "success": len(agent_response) > 0 and ("<Card" in agent_response or contains_delegation)
            }
            
            results.append(response_analysis)
            
            # Print results
            status = "PASS" if response_analysis['success'] else "FAIL"
            print(f"Status: {status}")
            print(f"Response Length: {response_analysis['response_length']} chars")
            print(f"Contains JSX: {response_analysis['contains_jsx']}")
            print(f"Contains Delegation: {response_analysis['contains_delegation']}")
            print(f"Expected Elements: {response_analysis['expected_elements_found']}/{response_analysis['total_expected']}")
            print(f"Response Preview: {response_analysis['raw_response']}")
            
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            results.append({
                "test_name": test_case['name'],
                "query": test_case['query'],
                "error": str(e),
                "success": False
            })
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUITE SUMMARY")
    print("=" * 50)
    
    passed_tests = [r for r in results if r.get('success', False)]
    failed_tests = [r for r in results if not r.get('success', False)]
    
    print(f"Total Tests: {len(results)}")
    print(f"Passed: {len(passed_tests)}")
    print(f"Failed: {len(failed_tests)}")
    print(f"Success Rate: {len(passed_tests)/len(results)*100:.1f}%")
    
    if failed_tests:
        print("\nFailed Tests:")
        for test in failed_tests:
            print(f"- {test['test_name']}: {test.get('error', 'No JSX generated')}")
    
    # Save detailed results
    with open('test_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n📋 Detailed results saved to test_results.json")
    
    return len(passed_tests) == len(results)

if __name__ == "__main__":
    if not os.getenv('GOOGLE_API_KEY'):
        print("❌ GOOGLE_API_KEY not configured")
        print("Please set your API key in agents/.env")
        sys.exit(1)
    
    # Run tests
    success = asyncio.run(test_adk_agents())
    
    if success:
        print("\n✅ All tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed. Check the output above.")
        sys.exit(1)