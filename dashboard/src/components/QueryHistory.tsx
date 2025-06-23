'use client'

import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'

interface QueryHistoryItem {
  id: string
  query: string
  timestamp: Date
  componentCount: number
  isFavorite: boolean
}

interface QueryHistoryProps {
  onSelectQuery: (query: string) => void
  currentQuery?: string
}

export function QueryHistory({ onSelectQuery, currentQuery }: QueryHistoryProps) {
  const [history, setHistory] = useState<QueryHistoryItem[]>([])
  const [isOpen, setIsOpen] = useState(false)

  // Load history from localStorage on mount
  useEffect(() => {
    const savedHistory = localStorage.getItem('query-history')
    if (savedHistory) {
      try {
        const parsed = JSON.parse(savedHistory).map((item: any) => ({
          ...item,
          timestamp: new Date(item.timestamp)
        }))
        setHistory(parsed.slice(0, 10)) // Keep only last 10 queries
      } catch (error) {
        console.error('Failed to parse query history:', error)
      }
    }
  }, [])

  // Save to localStorage whenever history changes
  useEffect(() => {
    localStorage.setItem('query-history', JSON.stringify(history))
  }, [history])

  const addToHistory = (query: string, componentCount: number) => {
    const newItem: QueryHistoryItem = {
      id: Date.now().toString(),
      query: query.trim(),
      timestamp: new Date(),
      componentCount,
      isFavorite: false
    }

    setHistory(prev => {
      // Remove duplicates and add to front
      const filtered = prev.filter(item => item.query.toLowerCase() !== query.toLowerCase())
      return [newItem, ...filtered].slice(0, 10)
    })
  }

  const toggleFavorite = (id: string) => {
    setHistory(prev => prev.map(item => 
      item.id === id ? { ...item, isFavorite: !item.isFavorite } : item
    ))
  }

  const clearHistory = () => {
    setHistory([])
    localStorage.removeItem('query-history')
  }

  const favorites = history.filter(item => item.isFavorite)
  const recent = history.filter(item => !item.isFavorite).slice(0, 5)

  // Expose addToHistory for parent component
  useEffect(() => {
    ;(window as any).addQueryToHistory = addToHistory
  }, [])

  if (history.length === 0) {
    return null
  }

  return (
    <div className="mb-8">
      <motion.button
        whileHover={{ scale: 1.02 }}
        whileTap={{ scale: 0.98 }}
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center space-x-2 text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition-colors"
      >
        <span className="text-sm font-medium">Query History</span>
        <motion.div
          animate={{ rotate: isOpen ? 180 : 0 }}
          transition={{ duration: 0.2 }}
        >
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </motion.div>
        <Badge variant="secondary" className="text-xs">
          {history.length}
        </Badge>
      </motion.button>

      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.3 }}
            className="mt-4 overflow-hidden"
          >
            <Card className="bg-white/50 dark:bg-gray-800/50 backdrop-blur-sm border-gray-200 dark:border-gray-700">
              <CardContent className="p-4">
                <div className="flex justify-between items-center mb-4">
                  <h3 className="text-sm font-semibold text-gray-700 dark:text-gray-300">Recent & Favorites</h3>
                  <button
                    onClick={clearHistory}
                    className="text-xs text-red-500 hover:text-red-700 transition-colors"
                  >
                    Clear All
                  </button>
                </div>

                {/* Favorites Section */}
                {favorites.length > 0 && (
                  <div className="mb-4">
                    <h4 className="text-xs font-medium text-gray-500 dark:text-gray-400 mb-2 flex items-center">
                      <span className="mr-1">⭐</span> Favorites
                    </h4>
                    <div className="space-y-2">
                      {favorites.map((item) => (
                        <QueryHistoryItem
                          key={item.id}
                          item={item}
                          onSelect={onSelectQuery}
                          onToggleFavorite={toggleFavorite}
                          isCurrentQuery={item.query === currentQuery}
                        />
                      ))}
                    </div>
                  </div>
                )}

                {/* Recent Section */}
                <div>
                  <h4 className="text-xs font-medium text-gray-500 dark:text-gray-400 mb-2 flex items-center">
                    <span className="mr-1">🕒</span> Recent
                  </h4>
                  <div className="space-y-2">
                    {recent.map((item) => (
                      <QueryHistoryItem
                        key={item.id}
                        item={item}
                        onSelect={onSelectQuery}
                        onToggleFavorite={toggleFavorite}
                        isCurrentQuery={item.query === currentQuery}
                      />
                    ))}
                  </div>
                </div>
              </CardContent>
            </Card>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}

function QueryHistoryItem({ 
  item, 
  onSelect, 
  onToggleFavorite, 
  isCurrentQuery 
}: { 
  item: QueryHistoryItem
  onSelect: (query: string) => void
  onToggleFavorite: (id: string) => void
  isCurrentQuery: boolean
}) {
  const formatTimestamp = (date: Date) => {
    const now = new Date()
    const diffMs = now.getTime() - date.getTime()
    const diffHours = diffMs / (1000 * 60 * 60)
    
    if (diffHours < 1) {
      return 'Just now'
    } else if (diffHours < 24) {
      return `${Math.floor(diffHours)}h ago`
    } else {
      return date.toLocaleDateString()
    }
  }

  return (
    <motion.div
      whileHover={{ scale: 1.01 }}
      className={`p-3 rounded-lg border transition-all cursor-pointer ${
        isCurrentQuery 
          ? 'bg-blue-50 dark:bg-blue-900/20 border-blue-200 dark:border-blue-700' 
          : 'bg-gray-50 dark:bg-gray-700/50 border-gray-200 dark:border-gray-600 hover:bg-gray-100 dark:hover:bg-gray-700'
      }`}
      onClick={() => onSelect(item.query)}
    >
      <div className="flex items-start justify-between">
        <div className="flex-1 min-w-0">
          <p className="text-sm text-gray-900 dark:text-gray-100 truncate font-medium">
            {item.query}
          </p>
          <div className="flex items-center space-x-2 mt-1">
            <span className="text-xs text-gray-500 dark:text-gray-400">
              {formatTimestamp(item.timestamp)}
            </span>
            <Badge variant="outline" className="text-xs">
              {item.componentCount} components
            </Badge>
          </div>
        </div>
        <motion.button
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
          onClick={(e) => {
            e.stopPropagation()
            onToggleFavorite(item.id)
          }}
          className={`ml-2 p-1 rounded transition-colors ${
            item.isFavorite 
              ? 'text-yellow-500 hover:text-yellow-600' 
              : 'text-gray-400 hover:text-yellow-500'
          }`}
        >
          <svg className="w-4 h-4" fill={item.isFavorite ? 'currentColor' : 'none'} stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
          </svg>
        </motion.button>
      </div>
    </motion.div>
  )
}