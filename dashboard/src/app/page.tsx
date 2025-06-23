'use client'

import { useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import { TooltipProvider } from '@/components/ui/tooltip'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism'
import SafeComponentRenderer from '@/components/SafeComponentRenderer'
import { ThemeToggle } from '@/components/ui/theme-toggle'
import { QueryHistory } from '@/components/QueryHistory'
import { EnhancedLoadingState } from '@/components/EnhancedLoadingState'

interface GeneratedComponent {
  id: string
  agent_name: string
  component_code: string
  business_context: string
  component_type: string
}

interface AgentStatus {
  name: string
  status: 'idle' | 'thinking' | 'generating' | 'complete'
  icon: string
  color: string
}

export default function GenerativeUIDashboard() {
  const [components, setComponents] = useState<GeneratedComponent[]>([])
  const [isLoading, setIsLoading] = useState(false)
  const [query, setQuery] = useState('')
  const [performanceMetrics, setPerformanceMetrics] = useState<{
    processingTime: string
    componentCount: number
    agentTrace: string[]
  } | null>(null)
  const [agentStatuses, setAgentStatuses] = useState<AgentStatus[]>([
    { name: 'Chart Agent', status: 'idle', icon: '📊', color: 'blue' },
    { name: 'Geospatial Agent', status: 'idle', icon: '🗺️', color: 'green' },
    { name: 'Accessibility Agent', status: 'idle', icon: '♿', color: 'purple' }
  ])

  const handleBusinessQuery = async (inputQuery: string) => {
    setIsLoading(true)
    setComponents([])
    setPerformanceMetrics(null)
    
    const startTime = Date.now()
    
    // Simulate agent activation with delays
    const activateAgents = () => {
      setTimeout(() => {
        setAgentStatuses(prev => prev.map(agent => 
          ({ ...agent, status: 'thinking' as const })
        ))
      }, 300)
      
      setTimeout(() => {
        setAgentStatuses(prev => prev.map(agent => 
          ({ ...agent, status: 'generating' as const })
        ))
      }, 800)
    }
    
    activateAgents()
    
    try {
      // Send query to ADK agent
      const response = await fetch('/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: inputQuery })
      })
      
      const result = await response.json()
      
      if (result.components) {
        setComponents(result.components.map((comp: { agent: string; component_code: string; business_context: string; component_type: string }, index: number) => ({
          id: `comp-${index}`,
          agent_name: comp.agent,
          component_code: comp.component_code,
          business_context: comp.business_context,
          component_type: comp.component_type
        })))
        
        setAgentStatuses(prev => prev.map(agent => 
          ({ ...agent, status: 'complete' as const })
        ))

        // Set performance metrics
        const endTime = Date.now()
        setPerformanceMetrics({
          processingTime: `${((endTime - startTime) / 1000).toFixed(1)}s`,
          componentCount: result.components.length,
          agentTrace: result.agent_trace || []
        })

        // Add to query history
        if ((window as any).addQueryToHistory) {
          (window as any).addQueryToHistory(inputQuery, result.components.length)
        }
      }
    } catch (error) {
      console.error('Error querying agents:', error)
      setComponents([{
        id: 'error',
        agent_name: 'system',
        component_code: '<div class="text-red-600">Error processing query</div>',
        business_context: 'System error',
        component_type: 'error'
      }])
    }
    
    setIsLoading(false)
    
    // Reset agent statuses after delay
    setTimeout(() => {
      setAgentStatuses(prev => prev.map(agent => 
        ({ ...agent, status: 'idle' as const })
      ))
    }, 3000)
  }

  return (
    <TooltipProvider>
      <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-slate-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900 transition-colors">
        {/* Header */}
        <motion.div 
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="border-b bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm sticky top-0 z-50 transition-colors"
        >
          <div className="container mx-auto px-6 py-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-4">
                <motion.div
                  whileHover={{ scale: 1.05 }}
                  className="flex items-center space-x-3"
                >
                  <div className="w-8 h-8 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
                    <span className="text-white font-bold text-sm">AI</span>
                  </div>
                  <div>
                    <h1 className="text-xl font-semibold bg-gradient-to-r from-gray-900 to-gray-600 bg-clip-text text-transparent">
                      Generative UI Studio
                    </h1>
                    <p className="text-xs text-gray-500">Multi-Agent Business Intelligence</p>
                  </div>
                </motion.div>
              </div>
              
              <div className="flex items-center space-x-3">
                <AgentStatusBar agents={agentStatuses} />
                <ThemeToggle />
              </div>
            </div>
          </div>
        </motion.div>

        <div className="container mx-auto px-6 py-8">
          {/* Hero Section */}
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="text-center mb-12"
          >
            <h2 className="text-4xl md:text-5xl font-bold mb-4 bg-gradient-to-r from-gray-900 via-blue-800 to-purple-800 dark:from-gray-100 dark:via-blue-300 dark:to-purple-300 bg-clip-text text-transparent">
              Ask. Generate. Visualize.
            </h2>
            <p className="text-lg text-gray-600 dark:text-gray-300 mb-8 max-w-2xl mx-auto transition-colors">
              Transform business questions into interactive UI components using our specialized AI agents
            </p>
            
            <BusinessQueryInput 
              onSubmit={handleBusinessQuery} 
              isLoading={isLoading}
              value={query}
              onChange={setQuery}
            />
          </motion.div>

          {/* Query History */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
          >
            <QueryHistory 
              onSelectQuery={(selectedQuery) => {
                setQuery(selectedQuery)
                handleBusinessQuery(selectedQuery)
              }}
              currentQuery={query}
            />
          </motion.div>

          {/* Enhanced Loading State */}
          <AnimatePresence>
            {isLoading && (
              <EnhancedLoadingState isLoading={isLoading} query={query} />
            )}
          </AnimatePresence>

          {/* Performance Metrics */}
          <AnimatePresence>
            {performanceMetrics && (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="mb-8"
              >
                <Card className="bg-gradient-to-r from-green-50 to-blue-50 dark:from-green-900/20 dark:to-blue-900/20 border-green-200 dark:border-green-800">
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between">
                      <div className="flex items-center space-x-4">
                        <div className="text-2xl">⚡</div>
                        <div>
                          <h3 className="text-sm font-semibold text-green-800 dark:text-green-300">Generation Complete</h3>
                          <p className="text-xs text-green-600 dark:text-green-400">Components ready for use</p>
                        </div>
                      </div>
                      <div className="flex items-center space-x-6 text-sm">
                        <div className="text-center">
                          <div className="font-bold text-green-800 dark:text-green-300">{performanceMetrics.processingTime}</div>
                          <div className="text-xs text-green-600 dark:text-green-400">Processing Time</div>
                        </div>
                        <div className="text-center">
                          <div className="font-bold text-green-800 dark:text-green-300">{performanceMetrics.componentCount}</div>
                          <div className="text-xs text-green-600 dark:text-green-400">Components</div>
                        </div>
                        <div className="text-center">
                          <div className="font-bold text-green-800 dark:text-green-300">{performanceMetrics.agentTrace.length}</div>
                          <div className="text-xs text-green-600 dark:text-green-400">Agent Steps</div>
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </motion.div>
            )}
          </AnimatePresence>

          {/* Components Grid */}
          <AnimatePresence>
            {components.length > 0 && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="space-y-8"
              >
                {components.map((component, index) => (
                  <motion.div
                    key={component.id}
                    initial={{ opacity: 0, y: 50 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: index * 0.2 }}
                  >
                    <EnhancedComponentWrapper component={component} />
                  </motion.div>
                ))}
              </motion.div>
            )}
          </AnimatePresence>

          {/* Empty State */}
          {components.length === 0 && !isLoading && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 }}
              className="text-center py-16"
            >
              <EmptyState onQuery={handleBusinessQuery} />
            </motion.div>
          )}
        </div>
      </div>
    </TooltipProvider>
  )
}

function AgentStatusBar({ agents }: { agents: AgentStatus[] }) {
  const getStatusClasses = (agent: AgentStatus) => {
    if (agent.status === 'idle') {
      return 'bg-gray-100 text-gray-600 dark:bg-gray-700 dark:text-gray-300'
    }
    
    const colorMap = {
      blue: {
        thinking: 'bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300',
        generating: 'bg-blue-200 text-blue-800 dark:bg-blue-800 dark:text-blue-200'
      },
      green: {
        thinking: 'bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300',
        generating: 'bg-green-200 text-green-800 dark:bg-green-800 dark:text-green-200'
      },
      purple: {
        thinking: 'bg-purple-100 text-purple-700 dark:bg-purple-900 dark:text-purple-300',
        generating: 'bg-purple-200 text-purple-800 dark:bg-purple-800 dark:text-purple-200'
      }
    }
    
    if (agent.status === 'complete') {
      return 'bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300'
    }
    
    return colorMap[agent.color as keyof typeof colorMap]?.[agent.status as 'thinking' | 'generating'] || 'bg-gray-100 text-gray-600 dark:bg-gray-700 dark:text-gray-300'
  }
  
  const getDotClasses = (agent: AgentStatus) => {
    if (agent.status === 'complete') {
      return 'bg-green-500'
    }
    
    const dotColorMap = {
      blue: {
        thinking: 'bg-blue-400',
        generating: 'bg-blue-500'
      },
      green: {
        thinking: 'bg-green-400',
        generating: 'bg-green-500'
      },
      purple: {
        thinking: 'bg-purple-400',
        generating: 'bg-purple-500'
      }
    }
    
    return dotColorMap[agent.color as keyof typeof dotColorMap]?.[agent.status as 'thinking' | 'generating'] || 'bg-gray-400'
  }

  return (
    <div className="flex items-center space-x-2">
      {agents.map((agent) => (
        <motion.div
          key={agent.name}
          whileHover={{ scale: 1.05 }}
          className={`flex items-center space-x-2 px-3 py-1.5 rounded-full text-xs font-medium transition-colors ${getStatusClasses(agent)}`}
        >
          <span>{agent.icon}</span>
          <span className="hidden sm:inline">{agent.name}</span>
          {agent.status !== 'idle' && (
            <motion.div
              animate={{ scale: [1, 1.2, 1] }}
              transition={{ duration: 1, repeat: Infinity }}
              className={`w-2 h-2 rounded-full ${getDotClasses(agent)}`}
            />
          )}
        </motion.div>
      ))}
    </div>
  )
}

function BusinessQueryInput({ 
  onSubmit, 
  isLoading, 
  value, 
  onChange 
}: { 
  onSubmit: (query: string) => void
  isLoading: boolean
  value: string
  onChange: (value: string) => void
}) {
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (value.trim()) {
      onSubmit(value.trim())
    }
  }

  return (
    <motion.div
      whileHover={{ scale: 1.01 }}
      className="max-w-4xl mx-auto"
    >
      <Card className="border-0 shadow-xl bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm transition-colors">
        <CardContent className="p-6">
          <form onSubmit={handleSubmit}>
            <div className="flex gap-4">
              <div className="flex-1 relative">
                <input
                  type="text"
                  value={value}
                  onChange={(e) => onChange(e.target.value)}
                  placeholder="Ask about trends, regions, accessibility... (e.g., 'Show regional sales with high contrast charts')"
                  className="w-full px-6 py-4 text-lg border-2 border-gray-200 dark:border-gray-600 dark:bg-gray-700 dark:text-white rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all placeholder:text-gray-400 dark:placeholder:text-gray-500"
                  disabled={isLoading}
                />
                <div className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-400 dark:text-gray-500">
                  <span className="text-sm">⌘ + Enter</span>
                </div>
              </div>
              <motion.button
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                type="submit"
                disabled={isLoading || !value.trim()}
                className="px-8 py-4 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold rounded-xl hover:from-blue-700 hover:to-purple-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-lg"
              >
                {isLoading ? (
                  <span className="flex items-center space-x-2">
                    <motion.div
                      animate={{ rotate: 360 }}
                      transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
                      className="w-4 h-4 border-2 border-white border-t-transparent rounded-full"
                    />
                    <span>Generating...</span>
                  </span>
                ) : (
                  <span className="flex items-center space-x-2">
                    <span>🚀</span>
                    <span>Generate UI</span>
                  </span>
                )}
              </motion.button>
            </div>
          </form>
        </CardContent>
      </Card>
    </motion.div>
  )
}

function EnhancedComponentWrapper({ component }: { component: GeneratedComponent }) {
  return (
    <motion.div
      whileHover={{ scale: 1.01 }}
      className="max-w-6xl mx-auto"
    >
      <Card className="border-0 shadow-xl bg-white dark:bg-gray-800 overflow-hidden transition-colors">
        <CardHeader className="bg-gradient-to-r from-slate-50 to-gray-50 dark:from-gray-700 dark:to-gray-600 border-b border-gray-200 dark:border-gray-600 transition-colors">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <motion.div
                whileHover={{ rotate: 360 }}
                transition={{ duration: 0.5 }}
                className="text-2xl"
              >
                {component.agent_name.includes('chart') ? '📊' :
                 component.agent_name.includes('geospatial') ? '🗺️' :
                 component.agent_name.includes('accessibility') ? '♿' : '🤖'}
              </motion.div>
              <div>
                <CardTitle className="text-lg dark:text-white">Generated Component</CardTitle>
                <p className="text-sm text-gray-600 dark:text-gray-300">{component.business_context}</p>
              </div>
            </div>
            <div className="flex items-center space-x-2">
              <Badge variant="outline" className="font-mono text-xs">
                {component.agent_name}
              </Badge>
              <Badge variant="secondary" className="text-xs">
                {component.component_type}
              </Badge>
            </div>
          </div>
        </CardHeader>
        
        <CardContent className="p-0">
          <Tabs defaultValue="preview" className="w-full">
            <TabsList className="grid w-full grid-cols-2 rounded-none">
              <TabsTrigger value="preview" className="flex items-center space-x-2">
                <span>👀</span>
                <span>Preview</span>
              </TabsTrigger>
              <TabsTrigger value="code" className="flex items-center space-x-2">
                <span>💻</span>
                <span>Code</span>
              </TabsTrigger>
            </TabsList>
            
            <TabsContent value="preview" className="p-6 m-0">
              <div className="bg-gradient-to-br from-slate-50 to-white dark:from-gray-700 dark:to-gray-600 p-6 rounded-lg border-2 border-dashed border-gray-200 dark:border-gray-500 transition-colors">
                <SafeComponentRenderer 
                  componentCode={component.component_code}
                  componentType={component.component_type}
                />
              </div>
            </TabsContent>
            
            <TabsContent value="code" className="p-0 m-0">
              <div className="relative">
                <SyntaxHighlighter
                  language="jsx"
                  style={vscDarkPlus}
                  customStyle={{
                    margin: 0,
                    borderRadius: 0,
                    fontSize: '14px',
                    lineHeight: '1.5'
                  }}
                  showLineNumbers
                >
                  {component.component_code}
                </SyntaxHighlighter>
                <motion.button
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  onClick={() => navigator.clipboard.writeText(component.component_code)}
                  className="absolute top-4 right-4 px-3 py-1.5 bg-gray-700 hover:bg-gray-600 text-white text-xs rounded-md transition-colors"
                >
                  📋 Copy
                </motion.button>
              </div>
            </TabsContent>
          </Tabs>
        </CardContent>
      </Card>
    </motion.div>
  )
}

function EmptyState({ onQuery }: { onQuery: (query: string) => void }) {
  const exampleQueries = [
    {
      icon: '📈',
      title: 'Sales Trends',
      query: 'Show me sales trends for Q4',
      description: 'Chart generation agent creates trend visualizations',
      color: 'blue'
    },
    {
      icon: '🗺️',
      title: 'Regional Analysis',
      query: 'Display regional performance with territory breakdown',
      description: 'Geospatial agent generates map-based components',
      color: 'green'
    },
    {
      icon: '♿',
      title: 'Accessible Dashboard',
      query: 'Create accessible metrics with high contrast',
      description: 'Accessibility agent builds WCAG-compliant components',
      color: 'purple'
    },
    {
      icon: '🔄',
      title: 'Multi-Agent Query',
      query: 'Show regional sales with accessible high-contrast visualization',
      description: 'Multiple agents collaborate for complex requirements',
      color: 'orange'
    }
  ]

  return (
    <div className="max-w-4xl mx-auto">
      <motion.div
        animate={{ y: [0, -10, 0] }}
        transition={{ duration: 3, repeat: Infinity }}
        className="text-8xl mb-8"
      >
        🚀
      </motion.div>
      <h3 className="text-3xl font-bold mb-4 text-gray-900 dark:text-gray-100 transition-colors">
        Ready to Generate UI Components
      </h3>
      <p className="text-gray-600 dark:text-gray-300 mb-12 text-lg transition-colors">
        Choose an example below or ask your own business intelligence question
      </p>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {exampleQueries.map((example, index) => (
          <motion.div
            key={example.title}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
            whileHover={{ scale: 1.02, y: -5 }}
            whileTap={{ scale: 0.98 }}
            onClick={() => onQuery(example.query)}
            className={`p-6 border-2 rounded-xl cursor-pointer transition-all bg-white dark:bg-gray-800 hover:shadow-lg dark:hover:shadow-gray-900/25 ${
              example.color === 'blue' ? 'border-blue-200 hover:border-blue-300 dark:border-blue-700 dark:hover:border-blue-600' :
              example.color === 'green' ? 'border-green-200 hover:border-green-300 dark:border-green-700 dark:hover:border-green-600' :
              example.color === 'purple' ? 'border-purple-200 hover:border-purple-300 dark:border-purple-700 dark:hover:border-purple-600' :
              'border-orange-200 hover:border-orange-300 dark:border-orange-700 dark:hover:border-orange-600'
            }`}
          >
            <div className="text-3xl mb-3">{example.icon}</div>
            <h4 className="font-semibold text-lg mb-2 dark:text-white">{example.title}</h4>
            <p className="text-gray-600 dark:text-gray-300 text-sm mb-3">{example.description}</p>
            <p className="text-xs text-gray-500 dark:text-gray-400 italic">&ldquo;{example.query}&rdquo;</p>
          </motion.div>
        ))}
      </div>
    </div>
  )
}
