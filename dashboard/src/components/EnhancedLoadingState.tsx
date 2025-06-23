'use client'

import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Card, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'

interface LoadingStep {
  id: string
  label: string
  status: 'pending' | 'active' | 'complete'
  duration?: number
}

interface EnhancedLoadingStateProps {
  isLoading: boolean
  query: string
}

export function EnhancedLoadingState({ isLoading, query }: EnhancedLoadingStateProps) {
  const [currentStep, setCurrentStep] = useState(0)
  const [steps, setSteps] = useState<LoadingStep[]>([])

  useEffect(() => {
    if (!isLoading) {
      setCurrentStep(0)
      return
    }

    // Generate steps based on query content
    const generateSteps = (query: string): LoadingStep[] => {
      const baseSteps = [
        { id: 'analysis', label: 'Analyzing query intent', status: 'pending' as const, duration: 800 },
        { id: 'routing', label: 'Routing to specialized agents', status: 'pending' as const, duration: 600 }
      ]

      const agentSteps: LoadingStep[] = []

      if (query.toLowerCase().includes('trend') || query.toLowerCase().includes('sales') || query.toLowerCase().includes('metric')) {
        agentSteps.push({ id: 'chart', label: 'Chart agent generating visualizations', status: 'pending' as const, duration: 1200 })
      }

      if (query.toLowerCase().includes('regional') || query.toLowerCase().includes('territory') || query.toLowerCase().includes('map') || query.toLowerCase().includes('location')) {
        agentSteps.push({ id: 'geo', label: 'Geospatial agent creating maps', status: 'pending' as const, duration: 1400 })
      }

      if (query.toLowerCase().includes('accessible') || query.toLowerCase().includes('contrast') || query.toLowerCase().includes('a11y')) {
        agentSteps.push({ id: 'a11y', label: 'Accessibility agent optimizing components', status: 'pending' as const, duration: 1000 })
      }

      if (agentSteps.length === 0) {
        agentSteps.push({ id: 'chart', label: 'Chart agent generating visualizations', status: 'pending' as const, duration: 1200 })
      }

      const finalSteps = [
        { id: 'rendering', label: 'Compiling React components', status: 'pending' as const, duration: 500 },
        { id: 'complete', label: 'Ready to display', status: 'pending' as const, duration: 300 }
      ]

      return [...baseSteps, ...agentSteps, ...finalSteps]
    }

    const newSteps = generateSteps(query)
    setSteps(newSteps)
    setCurrentStep(0)

    // Progressive step activation
    let totalDelay = 0
    newSteps.forEach((step, index) => {
      setTimeout(() => {
        setSteps(prev => prev.map((s, i) => 
          i === index ? { ...s, status: 'active' } : s
        ))
        setCurrentStep(index + 1)

        // Mark as complete after duration
        setTimeout(() => {
          setSteps(prev => prev.map((s, i) => 
            i === index ? { ...s, status: 'complete' } : s
          ))
        }, step.duration || 800)

      }, totalDelay)
      totalDelay += (step.duration || 800)
    })

  }, [isLoading, query])

  if (!isLoading || steps.length === 0) {
    return null
  }

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.9 }}
      className="flex items-center justify-center py-16"
    >
      <Card className="max-w-md w-full mx-4 bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm border-0 shadow-xl">
        <CardContent className="p-6">
          <div className="text-center mb-6">
            <motion.div
              animate={{ rotate: 360 }}
              transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
              className="w-12 h-12 border-4 border-blue-200 dark:border-blue-700 border-t-blue-600 dark:border-t-blue-400 rounded-full mx-auto mb-4"
            />
            <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-2">
              Generating UI Components
            </h3>
            <p className="text-sm text-gray-600 dark:text-gray-300">
              &ldquo;{query.length > 50 ? `${query.substring(0, 50)}...` : query}&rdquo;
            </p>
          </div>

          <div className="space-y-3">
            {steps.map((step, index) => (
              <motion.div
                key={step.id}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.1 }}
                className="flex items-center space-x-3"
              >
                <div className="flex-shrink-0">
                  {step.status === 'complete' ? (
                    <motion.div
                      initial={{ scale: 0 }}
                      animate={{ scale: 1 }}
                      className="w-5 h-5 bg-green-500 rounded-full flex items-center justify-center"
                    >
                      <svg className="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                      </svg>
                    </motion.div>
                  ) : step.status === 'active' ? (
                    <motion.div
                      animate={{ scale: [1, 1.2, 1] }}
                      transition={{ duration: 1, repeat: Infinity }}
                      className="w-5 h-5 bg-blue-500 rounded-full"
                    />
                  ) : (
                    <div className="w-5 h-5 bg-gray-300 dark:bg-gray-600 rounded-full" />
                  )}
                </div>
                
                <div className="flex-1 min-w-0">
                  <p className={`text-sm font-medium transition-colors ${
                    step.status === 'complete' 
                      ? 'text-green-700 dark:text-green-400' 
                      : step.status === 'active'
                      ? 'text-blue-700 dark:text-blue-400'
                      : 'text-gray-500 dark:text-gray-400'
                  }`}>
                    {step.label}
                  </p>
                </div>

                {step.status === 'active' && (
                  <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    className="flex-shrink-0"
                  >
                    <Badge variant="secondary" className="text-xs">
                      Working...
                    </Badge>
                  </motion.div>
                )}
              </motion.div>
            ))}
          </div>

          <div className="mt-6 pt-4 border-t border-gray-200 dark:border-gray-600">
            <div className="flex items-center justify-between text-xs text-gray-500 dark:text-gray-400">
              <span>Progress: {Math.round((currentStep / steps.length) * 100)}%</span>
              <span>Step {Math.min(currentStep, steps.length)} of {steps.length}</span>
            </div>
            <div className="mt-2 bg-gray-200 dark:bg-gray-700 rounded-full h-2">
              <motion.div
                className="bg-blue-500 h-2 rounded-full"
                initial={{ width: 0 }}
                animate={{ width: `${(currentStep / steps.length) * 100}%` }}
                transition={{ duration: 0.5 }}
              />
            </div>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}