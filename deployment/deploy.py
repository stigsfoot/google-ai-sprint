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
    
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    if not api_key:
        print("❌ GOOGLE_AI_API_KEY not found in environment")
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
    """Run the test suite"""
    print("🧪 Running Test Suite")
    print("=" * 30)
    
    # Run pytest if available
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/", "-v"
        ], cwd=os.path.dirname(os.path.dirname(__file__)))
        return result.returncode == 0
    except FileNotFoundError:
        print("pytest not found, running basic tests")
        # Fallback to basic test
        try:
            from tests.test_agent_integration import test_agent_imports
            import asyncio
            asyncio.run(test_agent_imports())
            print("✅ Basic tests passed")
            return True
        except Exception as e:
            print(f"❌ Tests failed: {e}")
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