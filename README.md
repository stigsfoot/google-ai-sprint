# Generative UI Business Intelligence System

A multi-agent system using Google ADK that transforms business questions into interactive React UI components through specialized AI agents.

## 🏗️ Architecture

### Multi-Agent System
- **Root Orchestrator**: Coordinates and delegates queries to specialized agents
- **Chart Generation Agent**: Creates visualization components (trends, metrics, comparisons)
- **Geospatial Agent**: Generates map-based and location components  
- **Accessibility Agent**: Produces WCAG-compliant, high-contrast UI variants

### Core Innovation
- **UI Components as Tools**: React JSX components are generated as callable tools within ADK agents
- **Business Intelligence Focus**: Natural language queries become interactive dashboards
- **Educational Transparency**: Real-time agent tracing via ADK web interface

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Google AI API key

### Setup
```bash
# 1. Environment setup
cp .env.example agents/.env
# Edit agents/.env and replace 'your_google_ai_api_key_here' with your actual API key

# 2. Install Python dependencies
pip install google-adk python-dotenv
# Or install all: pip install -r requirements.txt
# Or modern approach: pip install -e .

# 3. Install frontend dependencies  
cd dashboard && npm install

# 4. Start development environment
python deployment/deploy.py dev
```

### Development Servers
```bash
# Terminal 1: ADK Web Interface (requires API key setup)
adk web agents --port 8000

# Terminal 2: Frontend Dashboard  
cd dashboard && npm run dev
```

### Access Points
- **ADK Web Interface**: http://localhost:8000/dev-ui/
- **Frontend Dashboard**: http://localhost:3000

## 🧪 Testing

```bash
# Run development server to test functionality
python deployment/deploy.py dev
```

## 📋 Project Structure

```
generative-ui-adk/
├── agents/                   # ADK Multi-Agent System
│   ├── generative_ui/       # Main orchestrator agent
│   │   ├── __init__.py
│   │   └── agent.py        # Root agent + Chart agent
│   ├── geospatial_agent.py # Map-based UI generation
│   ├── accessibility_agent.py # WCAG-compliant components
│   ├── dashboard_layout_agent.py # Layout composition
│   └── __init__.py         # Agent package entry
├── dashboard/              # Enhanced Frontend
│   ├── src/app/           # Next.js app with Vercel-inspired UI
│   ├── src/components/    # React components including SafeComponentRenderer
│   └── src/components/ui/ # Shadcn UI components
├── deployment/            # Deployment Utilities
│   └── deploy.py         # Local dev + production scripts
├── pyproject.toml        # Modern Python packaging
├── requirements.txt       # Python dependencies
└── README.md
```

## 🎯 Example Queries

### Single Agent
- `"Show me sales trends for Q4"` → Chart Agent
- `"Display regional performance"` → Geospatial Agent  
- `"Create accessible metrics"` → Accessibility Agent

### Multi-Agent Coordination
- `"Show regional sales with accessible high-contrast visualization"`
- `"Create a complete dashboard with charts, maps, and accessible design"`

## 🔧 Development

### Adding New Agents
1. Create agent file in `agents/`
2. Define specialized tools returning JSX
3. Add to root agent's `sub_agents` list
4. Update evaluation scenarios

### Frontend Integration
- Components rendered via `dangerouslySetInnerHTML`
- Real-time agent status indicators
- Syntax highlighting for generated code
- Responsive Vercel-inspired design

## 🚀 Deployment

### Local Development
```bash
python deployment/deploy.py dev
```

### Production (Google Cloud)
```bash
python deployment/deploy.py vertex
```

## 📚 Learn More

- [Google ADK Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder)
- [Project Architecture (CLAUDE.md)](./CLAUDE.md)
- [Agent Development Guide](./agents/README.md)

---

**Built with Google ADK** | **Enhanced UI with Next.js + Tailwind** | **Multi-Agent Coordination**