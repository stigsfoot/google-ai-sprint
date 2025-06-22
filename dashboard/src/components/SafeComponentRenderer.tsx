'use client'

import React, { useMemo, useState, useEffect } from 'react'
import { 
  Card, 
  LineChart, 
  BarChart, 
  Metric, 
  Text, 
  Badge, 
  Flex,
  Title,
  Subtitle
} from '@tremor/react'
import { TrendingUp, BarChart3, MapPin } from 'lucide-react'
import dynamic from 'next/dynamic'

// Dynamically import Leaflet components to avoid SSR issues
const MapContainer = dynamic(() => import('react-leaflet').then(mod => mod.MapContainer), { ssr: false })
const TileLayer = dynamic(() => import('react-leaflet').then(mod => mod.TileLayer), { ssr: false })
const CircleMarker = dynamic(() => import('react-leaflet').then(mod => mod.CircleMarker), { ssr: false })
const Popup = dynamic(() => import('react-leaflet').then(mod => mod.Popup), { ssr: false })

interface SafeComponentRendererProps {
  componentCode: string
  componentType: string
}

/**
 * Safe Component Renderer
 * Handles React.createElement syntax for maximum safety and compatibility
 */
export default function SafeComponentRenderer({ 
  componentCode, 
  componentType 
}: SafeComponentRendererProps) {
  const [isClient, setIsClient] = useState(false)
  
  useEffect(() => {
    setIsClient(true)
  }, [])
  
  const RenderedComponent = useMemo(() => {
    console.log('🔍 SafeComponentRenderer Debug:', {
      componentType,
      codeLength: componentCode.length,
      codePreview: componentCode.substring(0, 100) + '...'
    })
    
    try {
      // Check if this is React.createElement syntax
      if (componentCode.includes('React.createElement')) {
        console.log('✅ Processing React.createElement format')
        
        // The component code might be JSON-encoded, so we need to decode it properly
        let cleanCode = componentCode
        
        // If the code looks like it's JSON-encoded (starts and ends with quotes), clean it
        if (cleanCode.startsWith('"') && cleanCode.endsWith('"')) {
          try {
            cleanCode = JSON.parse(cleanCode)
          } catch (parseError) {
            console.warn('Failed to JSON parse component code, using as-is', parseError)
          }
        }
        
        console.log('📦 Clean component code preview:', cleanCode.substring(0, 200) + '...')
        
        // Validate the component code before execution
        try {
          // Test if the code can be parsed as a function
          new Function(`return (${cleanCode})`)
        } catch (parseError) {
          console.error('❌ Component code parse error:', parseError)
          console.error('❌ Invalid component code:', cleanCode.substring(0, 500))
          throw new Error(`Invalid React.createElement syntax: ${parseError instanceof Error ? parseError.message : 'Parse error'}`)
        }
        
        // Create execution context with all necessary components
        const componentFunction = new Function(
          'React',
          'Card', 
          'LineChart',
          'BarChart', 
          'Metric',
          'Text',
          'Badge',
          'Flex',
          'Title',
          'Subtitle',
          'TrendingUp',
          'BarChart3',
          'MapPin',
          'MapContainer',
          'TileLayer',
          'CircleMarker',
          'Popup',
          `
          console.log('🚀 Executing React.createElement component');
          return ${cleanCode};
          `
        )
        
        console.log('🎨 Executing component function...')
        
        // Create placeholder components for SSR
        const MapContainerPlaceholder = isClient ? MapContainer : () => 
          React.createElement('div', { className: 'h-64 bg-gray-200 rounded-lg flex items-center justify-center' }, 'Loading Map...')
        const TileLayerPlaceholder = isClient ? TileLayer : () => null
        const CircleMarkerPlaceholder = isClient ? CircleMarker : () => null  
        const PopupPlaceholder = isClient ? Popup : () => null
        
        const result = componentFunction(
          React,
          Card,
          LineChart,
          BarChart,
          Metric,
          Text,
          Badge,
          Flex,
          Title,
          Subtitle,
          TrendingUp,
          BarChart3,
          MapPin,
          MapContainerPlaceholder,
          TileLayerPlaceholder,
          CircleMarkerPlaceholder,
          PopupPlaceholder
        )
        
        console.log('✅ React.createElement component executed successfully:', result)
        return result
      }
      
      // Fall back to IIFE format
      const iifeMatch = componentCode.match(/\(\(\)\s*=>\s*{([\s\S]*?)}\)\(\)/)
      
      if (iifeMatch) {
        console.log('✅ Processing IIFE format component')
        
        const componentBody = iifeMatch[1]
        
        const componentFunction = new Function(
          'React',
          'Card', 
          'LineChart',
          'BarChart', 
          'Metric',
          'Text',
          'Badge',
          'Flex',
          'Title',
          'Subtitle',
          'TrendingUp',
          'BarChart3',
          'MapPin',
          'MapContainer',
          'TileLayer',
          'CircleMarker',
          'Popup',
          `
          console.log('🚀 Executing IIFE component');
          const { useState, useEffect } = React;
          ${componentBody}
          `
        )
        
        // Create placeholder components for SSR
        const MapContainerPlaceholder = isClient ? MapContainer : () => 
          React.createElement('div', { className: 'h-64 bg-gray-200 rounded-lg flex items-center justify-center' }, 'Loading Map...')
        const TileLayerPlaceholder = isClient ? TileLayer : () => null
        const CircleMarkerPlaceholder = isClient ? CircleMarker : () => null  
        const PopupPlaceholder = isClient ? Popup : () => null
        
        const result = componentFunction(
          React,
          Card,
          LineChart,
          BarChart,
          Metric,
          Text,
          Badge,
          Flex,
          Title,
          Subtitle,
          TrendingUp,
          BarChart3,
          MapPin,
          MapContainerPlaceholder,
          TileLayerPlaceholder,
          CircleMarkerPlaceholder,
          PopupPlaceholder
        )
        
        console.log('✅ IIFE component executed successfully:', result)
        return result
      }
      
      // If neither format matches, show debug info
      console.warn('⚠️ Unrecognized component format')
      console.warn('Component preview:', componentCode.substring(0, 300))
      
      return (
        <Card className="p-6 border-orange-200 bg-orange-50">
          <div className="text-center">
            <div className="text-orange-600 mb-2">⚠️ Unrecognized Component Format</div>
            <div className="text-sm text-orange-700 mb-4">
              Expected React.createElement or IIFE format
            </div>
            <div className="bg-white p-4 rounded border text-left">
              <div className="text-lg font-semibold mb-2">
                {componentType === 'sales_trend' ? '📈 Sales Trend Analysis' : 
                 componentType === 'metric_card' ? '💰 Key Metrics' :
                 componentType === 'comparison_chart' ? '📊 Performance Comparison' : 
                 '📋 Business Component'}
              </div>
              <div className="text-sm text-gray-600 mb-2">
                Debug information:
              </div>
              <div className="text-xs text-gray-400 font-mono bg-gray-100 p-2 rounded">
                Format: {componentCode.includes('React.createElement') ? 'React.createElement' : 
                         componentCode.includes('(() => {') ? 'IIFE' : 'Unknown'}
                <br />
                Length: {componentCode.length}
                <br />
                Preview: {componentCode.substring(0, 100)}...
              </div>
            </div>
          </div>
        </Card>
      )
      
    } catch (error) {
      console.error('❌ Error rendering component:', error)
      console.error('Component code that caused error:', componentCode)
      
      return (
        <Card className="p-6 border-red-200 bg-red-50">
          <div className="text-center">
            <div className="text-red-600 mb-2">❌ Component Execution Error</div>
            <div className="text-sm text-red-700 mb-4">
              {error instanceof Error ? error.message : 'Unknown error'}
            </div>
            <details className="text-left">
              <summary className="cursor-pointer text-sm text-red-600">Show Details</summary>
              <div className="text-xs text-red-500 mt-2 font-mono bg-red-100 p-2 rounded">
                {componentCode}
              </div>
            </details>
          </div>
        </Card>
      )
    }
  }, [componentCode, componentType, isClient])

  return <div className="safe-rendered-component">{RenderedComponent}</div>
}