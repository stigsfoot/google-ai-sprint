'use client'

import React from 'react'
import { 
  LineChart, 
  Line, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer,
  BarChart,
  Bar
} from 'recharts'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { TrendingUp, BarChart3 } from 'lucide-react'

interface ChartData {
  [key: string]: string | number
}

interface SalesTrendProps {
  data?: ChartData[]
  title?: string
  period?: string
}

interface ComparisonChartProps {
  data?: ChartData[]
  title?: string
}

// Default data matching ADK agent output
const defaultSalesData = [
  { month: "Jan", value: 1200 },
  { month: "Feb", value: 1350 },
  { month: "Mar", value: 1580 },
  { month: "Apr", value: 1420 },
  { month: "May", value: 1650 },
  { month: "Jun", value: 1780 }
]

const defaultProductData = [
  { category: "Product A", value: 2400 },
  { category: "Product B", value: 1800 },
  { category: "Product C", value: 3200 },
  { category: "Product D", value: 1600 }
]

export function RechartsSalesTrend({ 
  data = defaultSalesData, 
  title = "Sales Trend", 
  period = "Q4" 
}: SalesTrendProps) {
  console.log('📈 RechartsSalesTrend rendering with data:', data)
  
  return (
    <Card className="p-6 bg-gradient-to-r from-green-50 to-blue-50 dark:from-green-900/20 dark:to-blue-900/20">
      <CardHeader className="pb-4">
        <div className="flex items-center space-x-2">
          <TrendingUp className="h-6 w-6 text-green-600 dark:text-green-400" />
          <CardTitle className="dark:text-white">{title} - {period}</CardTitle>
        </div>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#e0e7ff" />
            <XAxis 
              dataKey="month" 
              stroke="#6b7280"
              fontSize={12}
            />
            <YAxis 
              stroke="#6b7280"
              fontSize={12}
              tickFormatter={(value) => `$${value}`}
            />
            <Tooltip 
              formatter={(value) => [`$${value}`, 'Sales']}
              labelStyle={{ color: '#374151' }}
              contentStyle={{ 
                backgroundColor: 'white', 
                border: '1px solid #e5e7eb',
                borderRadius: '8px'
              }}
            />
            <Line 
              type="monotone" 
              dataKey="value" 
              stroke="#10b981" 
              strokeWidth={3}
              dot={{ fill: '#10b981', strokeWidth: 2, r: 4 }}
              activeDot={{ r: 6, fill: '#059669' }}
            />
          </LineChart>
        </ResponsiveContainer>
        
        <div className="mt-6 flex items-center justify-between">
          <Badge className="bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200">
            +23% Growth
          </Badge>
          <span className="text-sm text-gray-600 dark:text-gray-300">vs previous period</span>
        </div>
        
        <div className="mt-4 p-3 bg-green-50 dark:bg-green-900/20 rounded-lg">
          <p className="text-sm text-green-800 dark:text-green-300">
            Sales showing strong upward trend with 23% growth over the period
          </p>
        </div>
      </CardContent>
    </Card>
  )
}

export function RechartsComparison({ 
  data = defaultProductData, 
  title = "Product Performance Comparison" 
}: ComparisonChartProps) {
  console.log('📊 RechartsComparison rendering with data:', data)
  
  return (
    <Card className="p-6 bg-white dark:bg-gray-800">
      <CardHeader className="pb-4">
        <div className="flex items-center space-x-2">
          <BarChart3 className="h-6 w-6 text-blue-600 dark:text-blue-400" />
          <CardTitle className="dark:text-white">{title}</CardTitle>
        </div>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#e0e7ff" />
            <XAxis 
              dataKey="category" 
              stroke="#6b7280"
              fontSize={12}
            />
            <YAxis 
              stroke="#6b7280"
              fontSize={12}
              tickFormatter={(value) => `$${value}`}
            />
            <Tooltip 
              formatter={(value) => [`$${value}`, 'Sales']}
              labelStyle={{ color: '#374151' }}
              contentStyle={{ 
                backgroundColor: 'white', 
                border: '1px solid #e5e7eb',
                borderRadius: '8px'
              }}
            />
            <Bar 
              dataKey="value" 
              fill="#3b82f6"
              radius={[4, 4, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
        
        <div className="mt-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
          <p className="text-sm text-blue-800 dark:text-blue-300">
            Product C leads with highest performance at $3,200
          </p>
        </div>
      </CardContent>
    </Card>
  )
}

export function RechartsMetricCard({ 
  value = "$47.2K", 
  label = "Monthly Revenue", 
  change = "+12.3%", 
  context = "Compared to previous month" 
}) {
  const isPositive = change.startsWith('+')
  const isNegative = change.startsWith('-')
  
  return (
    <Card className="p-6 text-center max-w-xs bg-white dark:bg-gray-800">
      <CardContent className="space-y-4">
        <div className="text-4xl font-bold text-gray-900 dark:text-white">{value}</div>
        <div className="text-sm text-gray-600 dark:text-gray-300">{label}</div>
        <Badge className={`${
          isPositive ? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200' :
          isNegative ? 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200' :
          'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-200'
        }`}>
          {change}
        </Badge>
        <div className="text-xs text-gray-500 dark:text-gray-400">{context}</div>
      </CardContent>
    </Card>
  )
}