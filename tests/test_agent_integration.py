"""
Integration tests for multi-agent generative UI system
"""
import pytest
import asyncio
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.mark.asyncio
async def test_agent_imports():
    """Test that all agents can be imported successfully"""
    try:
        from agents.generative_ui.agent import root_agent, chart_generation_agent
        from agents.geospatial_agent import geospatial_agent
        from agents.accessibility_agent import accessibility_agent
        
        assert root_agent is not None
        assert chart_generation_agent is not None
        assert geospatial_agent is not None
        assert accessibility_agent is not None
        
        print("✅ All agents imported successfully")
        
    except ImportError as e:
        pytest.fail(f"Agent import failed: {e}")

@pytest.mark.asyncio
async def test_agent_structure():
    """Test agent structure and configuration"""
    from agents.generative_ui.agent import root_agent
    
    # Test root agent has sub-agents
    assert hasattr(root_agent, 'sub_agents')
    assert len(root_agent.sub_agents) >= 3  # Chart, Geospatial, Accessibility
    
    # Test agent names
    assert root_agent.name == "generative_ui_orchestrator"
    
    print("✅ Agent structure validated")

@pytest.mark.asyncio
async def test_tool_functionality():
    """Test that individual tools can be called"""
    try:
        # Test chart generation tools
        from agents.generative_ui.agent import create_sales_trend_card
        result = create_sales_trend_card("sample_data", "Q4")
        assert "<Card" in result
        assert "JSX" in result or "className" in result
        
        # Test geospatial tools
        from agents.geospatial_agent import create_regional_heatmap_tool
        result = create_regional_heatmap_tool("California", "Sales", "Strong performance")
        assert "<Card" in result
        
        # Test accessibility tools
        from agents.accessibility_agent import create_high_contrast_chart_tool
        result = create_high_contrast_chart_tool("revenue", "Revenue Analysis", "Growth trend")
        assert "<Card" in result
        
        print("✅ All tools functional")
        
    except Exception as e:
        pytest.fail(f"Tool test failed: {e}")

@pytest.mark.asyncio
async def test_environment_config():
    """Test environment configuration loading"""
    import os
    from dotenv import load_dotenv
    
    # Load environment
    load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'agents', '.env'))
    
    # Check API key is loaded
    api_key = os.getenv('GOOGLE_API_KEY')
    assert api_key is not None, "GOOGLE_API_KEY not found in environment"
    assert len(api_key) > 20, "API key appears to be invalid"
    
    print("✅ Environment configuration valid")

if __name__ == "__main__":
    # Run tests directly
    pytest.main([__file__, "-v"])