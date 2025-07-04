"""
Deployment utilities for generative UI ADK agents
Supports local development and production deployment
"""
import os
import subprocess
import sys
from typing import Optional

def check_requirements():
    """Check that all required dependencies are installed"""
    try:
        import google.adk
        from dotenv import load_dotenv
        print("✅ Core dependencies available")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return False

def validate_environment():
    """Validate environment configuration"""
    from dotenv import load_dotenv
    
    # Load environment variables
    load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'agents', '.env'))
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ GOOGLE_API_KEY not found in environment")
        return False
    
    print("✅ Environment configuration valid")
    return True

def start_local_development():
    """Start local development environment"""
    print("🚀 Starting Local Development Environment")
    print("=" * 50)
    
    if not check_requirements():
        return False
    
    if not validate_environment():
        return False
    
    print("\n📋 Services to start:")
    print("1. ADK Web Interface: adk web agents --port 8080")
    print("2. Frontend Dashboard: cd dashboard && npm run dev")
    print("\n🔗 URLs:")
    print("- ADK Web: http://localhost:8080/dev-ui/")
    print("- Frontend: http://localhost:3000")
    
    return True

def run_tests():
    """Validate agent functionality"""
    print("🧪 Validating Agent System")
    print("=" * 30)
    
    # Basic functionality validation
    try:
        # Import and validate agents can be loaded
        from agents.generative_ui.agent import generative_ui_agent
        from agents.geospatial_agent import geospatial_agent
        from agents.accessibility_agent import accessibility_agent
        from agents.dashboard_layout_agent import dashboard_layout_agent
        
        print("✅ All agents imported successfully")
        print("✅ Agent validation passed")
        return True
    except Exception as e:
        print(f"❌ Agent validation failed: {e}")
        return False

def deploy_to_vertex():
    """Deploy to Google Cloud Vertex AI (placeholder)"""
    print("🚀 Deploying to Vertex AI")
    print("This would handle production deployment to Google Cloud")
    # Placeholder for Vertex AI deployment logic
    pass

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Deploy generative UI agents")
    parser.add_argument("command", choices=["dev", "test", "vertex"], 
                       help="Deployment command")
    
    args = parser.parse_args()
    
    if args.command == "dev":
        start_local_development()
    elif args.command == "test":
        run_tests()
    elif args.command == "vertex":
        deploy_to_vertex()