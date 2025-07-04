'use client'

import React, { useState, useEffect, useRef } from 'react'
import { Card } from '@/components/ui/card'
import dynamic from 'next/dynamic'

// Dynamically import Leaflet components with proper typing
import type { Map } from 'leaflet'
const MapContainer = dynamic(() => import('react-leaflet').then(mod => mod.MapContainer), { ssr: false })
const TileLayer = dynamic(() => import('react-leaflet').then(mod => mod.TileLayer), { ssr: false })
const CircleMarker = dynamic(() => import('react-leaflet').then(mod => mod.CircleMarker), { ssr: false })
const Popup = dynamic(() => import('react-leaflet').then(mod => mod.Popup), { ssr: false })

// Type definitions for interactive map data
interface PerformanceCategory {
  label: string
  color: string
  regions: string[]
  threshold: { min: number; max?: number }
  zoom_bounds: { center: [number, number]; zoom: number }
}

interface MarkerData {
  center: [number, number]
  label: string
  color: string
  radius: number
}

interface MapConfig {
  center: [number, number]
  zoom: number
  markers: MarkerData[]
}

interface InteractiveMapData {
  type: string
  title: string
  map_config: MapConfig
  performance_categories: Record<string, PerformanceCategory>
  current_category?: string
  interactions: {
    legend_click_behavior: string
    marker_click_behavior: string
    keyboard_navigation: boolean
  }
  insight: string
  data: string
}

interface InteractiveMapDisplayProps {
  mapData: InteractiveMapData
}

export default function InteractiveMapDisplay({ mapData }: InteractiveMapDisplayProps) {
  const [isClient, setIsClient] = useState(false)
  const [currentCenter, setCurrentCenter] = useState<[number, number]>(mapData.map_config.center)
  const [currentZoom, setCurrentZoom] = useState(mapData.map_config.zoom)
  const [selectedCategory, setSelectedCategory] = useState<string | null>(mapData.current_category || null)
  const [filteredMarkers, setFilteredMarkers] = useState<MarkerData[]>(mapData.map_config.markers)
  const [statusMessage, setStatusMessage] = useState<string>('')
  const mapRef = useRef<Map | null>(null)

  // Debug logging
  console.log('🗺️ InteractiveMapDisplay received data:', {
    title: mapData.title,
    center: mapData.map_config.center,
    zoom: mapData.map_config.zoom,
    markersCount: mapData.map_config.markers.length,
    categoriesCount: Object.keys(mapData.performance_categories).length,
    categories: Object.keys(mapData.performance_categories)
  })

  useEffect(() => {
    setIsClient(true)
  }, [])

  // Handle performance category selection
  const handleCategoryClick = (categoryId: string) => {
    const category = mapData.performance_categories[categoryId]
    if (!category) return

    console.log(`🎯 Category clicked: ${categoryId}`, category)

    // Update selected category
    const isDeselecting = selectedCategory === categoryId
    setSelectedCategory(isDeselecting ? null : categoryId)

    // Update map view to zoom to category bounds
    setCurrentCenter(category.zoom_bounds.center)
    setCurrentZoom(category.zoom_bounds.zoom)

    // Update status message for screen readers
    if (isDeselecting) {
      setStatusMessage('Map view reset to show all regions')
    } else {
      setStatusMessage(`Zoomed to ${category.label} regions: ${category.regions.join(', ')}`)
    }

    // Filter markers based on category
    if (selectedCategory === categoryId) {
      // Deselect - show all markers
      setFilteredMarkers(mapData.map_config.markers)
      setCurrentCenter(mapData.map_config.center)
      setCurrentZoom(mapData.map_config.zoom)
    } else {
      // Filter markers for selected category
      const categoryMarkers = mapData.map_config.markers.filter(marker => {
        // Extract region name from marker label
        const regionName = marker.label.split(':')[0].trim()
        return category.regions.includes(regionName)
      })
      setFilteredMarkers(categoryMarkers)
    }

    // Update map view with smooth transition
    setTimeout(() => {
      if (mapRef.current) {
        try {
          const map = mapRef.current
          if (map && map.flyTo) {
            map.flyTo(category.zoom_bounds.center, category.zoom_bounds.zoom, {
              duration: 1.0 // Smooth 1-second transition
            })
          }
        } catch (error) {
          console.warn('Map flyTo failed, using setView instead:', error)
          if (mapRef.current && mapRef.current.setView) {
            mapRef.current.setView(category.zoom_bounds.center, category.zoom_bounds.zoom)
          }
        }
      }
    }, 100) // Small delay to ensure map is ready
  }

  // Handle keyboard navigation for accessibility
  const handleCategoryKeyDown = (event: React.KeyboardEvent, categoryId: string) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault()
      handleCategoryClick(categoryId)
    }
  }

  if (!isClient) {
    return (
      <Card className="p-6">
        <div className="h-64 bg-gray-200 dark:bg-gray-700 rounded-lg flex items-center justify-center">
          <span className="text-gray-500 dark:text-gray-400">Loading Interactive Map...</span>
        </div>
      </Card>
    )
  }

  return (
    <Card className="p-6 border-l-4 border-l-blue-500">
      {/* Screen reader status announcements */}
      <div 
        aria-live="polite" 
        aria-atomic="true" 
        className="sr-only"
        role="status"
      >
        {statusMessage}
      </div>
      
      <div className="flex items-center space-x-2 mb-4">
        <span className="text-2xl">🗺️</span>
        <div>
          <h3 className="text-lg font-semibold dark:text-white">{mapData.title}</h3>
          <p className="text-sm text-gray-600 dark:text-gray-300">
            Interactive geographic data visualization - Click categories to explore
          </p>
        </div>
      </div>
      
      <div className="relative bg-gradient-to-br from-blue-50 to-green-50 dark:from-blue-900/20 dark:to-green-900/20 rounded-lg p-6">
        <MapContainer
          ref={mapRef}
          center={currentCenter}
          zoom={currentZoom}
          style={{ height: "300px", width: "100%" }}
          className="rounded-lg z-0"
          scrollWheelZoom={true}
        >
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution="© OpenStreetMap contributors"
            maxZoom={19}
          />
          {filteredMarkers.map((marker, index) => (
            <CircleMarker
              key={index}
              center={marker.center}
              radius={marker.radius}
              pathOptions={{
                fillColor: marker.color,
                color: marker.color,
                weight: 2,
                opacity: 1,
                fillOpacity: 0.7
              }}
            >
              <Popup>{marker.label}</Popup>
            </CircleMarker>
          ))}
        </MapContainer>
      </div>
      
      {/* Interactive Performance Legend */}
      <div className="mt-4 grid grid-cols-4 gap-2 text-xs" role="group" aria-label="Performance categories">
        {Object.entries(mapData.performance_categories).map(([categoryId, category]) => (
          <button
            key={categoryId}
            onClick={() => handleCategoryClick(categoryId)}
            onKeyDown={(e) => handleCategoryKeyDown(e, categoryId)}
            className={`p-2 rounded text-center font-medium transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-1 ${
              selectedCategory === categoryId
                ? `bg-white text-gray-900 border-2 border-gray-900 shadow-lg transform scale-105`
                : `text-white hover:shadow-md hover:transform hover:scale-102 active:scale-95`
            }`}
            style={{ 
              backgroundColor: selectedCategory === categoryId ? 'white' : category.color,
              color: selectedCategory === categoryId ? category.color : 'white'
            }}
            aria-pressed={selectedCategory === categoryId}
            aria-label={`${category.label} - ${category.regions.join(', ')} - Click to zoom to region`}
            tabIndex={0}
          >
            {category.label}
            {selectedCategory === categoryId && (
              <div className="text-xs mt-1 opacity-75">
                ✓ Selected
              </div>
            )}
          </button>
        ))}
      </div>
      
      <div className="mt-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
        <p className="text-sm text-blue-800 dark:text-blue-300">
          📍 {mapData.insight}
          {selectedCategory && (
            <span className="ml-2 font-medium">
              (Viewing: {mapData.performance_categories[selectedCategory]?.label})
            </span>
          )}
        </p>
        <p className="text-xs text-blue-600 dark:text-blue-400 mt-1">
          Interactive: Click performance categories above to zoom to regions • Showing {filteredMarkers.length} data points
        </p>
      </div>
    </Card>
  )
}