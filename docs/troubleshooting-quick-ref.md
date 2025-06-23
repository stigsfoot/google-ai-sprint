# Troubleshooting Quick Reference

## 🚨 Common Issues & Quick Fixes

### 1. "No root_agent found for 'agents'"
```bash
# Check agent discovery
ls -la agents/
python -c "from agents import root_agent; print('✅ Agents loaded')"

# Restart ADK Web UI
adk web --app_name="generative_ui_system" --agents_dir="agents"
```

### 2. "Session not found" Errors
```bash
# Check API key
echo $GOOGLE_API_KEY
cat agents/.env

# Restart ADK server
pkill -f "adk_server.py"
python adk_server.py
```

### 3. "Agent execution failed: 503 UNAVAILABLE"
```bash
# Google API overloaded - wait and retry
sleep 30
curl -X POST "http://localhost:8081/api/analyze" -d '{"query": "test"}'
```

### 4. Agents Ask for Clarification
**Issue**: Agent responds with "Could you please provide..."
**Fix**: Agent instructions need strengthening

### 5. Empty/Text-Only Responses  
**Issue**: No JSX components generated
**Fix**: Check tool integration and agent delegation

### 6. Port Already in Use
```bash
# Kill existing processes
lsof -ti:8081 | xargs kill
lsof -ti:8080 | xargs kill

# Restart services
python adk_server.py &
adk web --agents_dir="agents" &
```

## ⚡ Quick Test Commands

### Health Checks
```bash
# ADK Server Health
curl http://localhost:8081/

# Agent Status
curl http://localhost:8081/api/agents | jq .

# Simple Test Query
curl -X POST "http://localhost:8081/api/analyze" \
  -H "Content-Type: application/json" \
  -d '{"query": "show sales trends"}' | jq .success
```

### ADK Web UI Tests
```bash
# Start ADK Web UI
adk web --app_name="generative_ui_system" --agents_dir="agents"

# Test in browser at http://localhost:8080
# Try: "show sales trends"
```

### React Frontend Tests
```bash
# Start frontend
npm run dev

# Access at http://localhost:3000
# Test with: "regional performance data"
```

## 🔍 Debug Mode

### Verbose Logging
```bash
# ADK Server with debug
python adk_server.py --log-level debug

# ADK Web UI with debug
adk web --agents_dir="agents" --debug

# Check Python imports
python -c "
from agents.generative_ui.agent import root_agent
print(f'Root: {root_agent.name}')
print(f'Sub-agents: {[a.name for a in root_agent.sub_agents]}')
"
```

## 📊 Expected Behavior

### ✅ Working System
- Health check returns `"agents_loaded": true`
- Queries complete in 2-5 seconds
- Responses contain JSX components
- No "Could you please" messages
- Agent delegation visible in traces

### ❌ Problem Indicators
- 503 errors (API overload - retry later)
- Session errors (check API key)
- Import errors (check file structure)
- Empty responses (check agent instructions)
- Timeout errors (check network/API limits)

## 🛠️ Recovery Procedures

### Full System Restart
```bash
# 1. Kill all processes
pkill -f "adk_server.py"
pkill -f "adk web"
pkill -f "npm run dev"

# 2. Check environment
echo $GOOGLE_API_KEY

# 3. Restart services
python adk_server.py &
adk web --agents_dir="agents" &
npm run dev &
```

### Agent Reload
```bash
# If agents aren't working
python -c "
import importlib
import sys
sys.path.append('agents')
import agents.generative_ui.agent
importlib.reload(agents.generative_ui.agent)
print('✅ Agents reloaded')
"
```

### Clean Environment
```bash
# Reset Python environment
pip install --force-reinstall google-adk

# Clear any cached imports
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +
```

## 📞 Support Checklist

Before seeking help, check:
- [ ] Google API key configured and valid
- [ ] All required ports available (8080, 8081, 3000)
- [ ] Agent files present and importable
- [ ] No syntax errors in agent files
- [ ] Environment variables loaded
- [ ] Network connectivity to Google APIs

## 🚀 Performance Optimization

### If responses are slow:
1. Check internet connection to Google APIs
2. Monitor API rate limits
3. Use simpler queries for testing
4. Check system resources (memory/CPU)

### If components don't render:
1. Validate JSX syntax in responses
2. Check React component imports
3. Verify Tailwind CSS classes
4. Test with minimal queries first

Keep this reference handy for quick issue resolution!