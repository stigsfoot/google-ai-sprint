'use client'

import React from 'react'
import { 
  Card, 
  LineChart, 
  BarChart, 
  Metric, 
  Text, 
  Badge, 
  Flex 
} from '@tremor/react'
import { TrendingUp, BarChart3 } from 'lucide-react'

interface ChartData {
  [key: string]: string | number
}

interface TremorChartProps {
  data?: ChartData[]
  title?: string
  subtitle?: string
  chartType: 'line' | 'bar' | 'metric'
  period?: string
  value?: string
  label?: string
  change?: string
  context?: string
}

// Sample data for charts
const defaultSalesData = [
  { month: "Jan", Sales: 1200, Revenue: 2400 },
  { month: "Feb", Sales: 1350, Revenue: 2100 },
  { month: "Mar", Sales: 1580, Revenue: 2800 },
  { month: "Apr", Sales: 1420, Revenue: 2300 },
  { month: "May", Sales: 1650, Revenue: 3100 },
  { month: "Jun", Sales: 1780, Revenue: 3400 }
]

const defaultProductData = [
  { product: "Product A", Sales: 2400, Units: 240 },
  { product: "Product B", Sales: 1800, Units: 180 },
  { product: "Product C", Sales: 3200, Units: 320 },
  { product: "Product D", Sales: 1600, Units: 160 }
]

export function TremorSalesTrend({ 
  data = defaultSalesData, 
  title = "Sales Trend", 
  period = "Q4" 
}: Partial<TremorChartProps>) {
  console.log('🔍 TremorSalesTrend input data:', data)
  
  // Transform data if it has 'value' key instead of 'Sales'
  const transformedData = data ? data.map(item => {
    if ('value' in item && !('Sales' in item)) {
      return { ...item, Sales: item.value }
    }
    return item
  }) : defaultSalesData
  
  console.log('📈 TremorSalesTrend final data for LineChart:', transformedData)
  console.log('📊 Data structure check:', {
    isArray: Array.isArray(transformedData),
    length: transformedData.length,
    firstItem: transformedData[0],
    hasMonthKey: transformedData[0] && 'month' in transformedData[0],
    hasSalesKey: transformedData[0] && 'Sales' in transformedData[0]
  })
  
  return (
    <Card className="p-6 bg-gradient-to-r from-green-50 to-blue-50 dark:from-green-900/20 dark:to-blue-900/20">
      <div className="flex items-center space-x-2 mb-6">
        <TrendingUp className="h-6 w-6 text-green-600 dark:text-green-400" />
        <Text className="text-lg font-semibold dark:text-white">{title} - {period}</Text>
      </div>
      
      <LineChart
        className="h-80"
        data={transformedData}
        index="month"
        categories={["Sales"]}
        colors={["green"]}
        valueFormatter={(number: number) => `$${Intl.NumberFormat("us").format(number).toString()}`}
      />
      
      <div className="mt-6 flex items-center justify-between">
        <Badge color="green" size="lg">+23% Growth</Badge>
        <Text className="text-sm text-gray-600 dark:text-gray-300">vs previous period</Text>
      </div>
      
      <div className="mt-4 p-3 bg-green-50 dark:bg-green-900/20 rounded-lg">
        <Text className="text-sm text-green-800 dark:text-green-300">
          Sales showing strong upward trend with 23% growth over the period
        </Text>
      </div>
    </Card>
  )
}

export function TremorMetricCard({ 
  value = "$47.2K", 
  label = "Monthly Revenue", 
  change = "+12.3%", 
  context = "Compared to previous month" 
}: Partial<TremorChartProps>) {
  const isPositive = change.startsWith('+')
  const isNegative = change.startsWith('-')
  const changeColor = isPositive ? "emerald" : isNegative ? "red" : "gray"
  
  return (
    <Card className="p-6 text-center max-w-xs bg-white dark:bg-gray-800">
      <Flex flexDirection="col" alignItems="center" className="space-y-4">
        <Metric className="text-4xl font-bold text-gray-900 dark:text-white">{value}</Metric>
        <Text className="text-sm text-gray-600 dark:text-gray-300">{label}</Text>
        <Badge color={changeColor} size="lg">{change}</Badge>
        <Text className="text-xs text-gray-500 dark:text-gray-400">{context}</Text>
      </Flex>
    </Card>
  )
}

export function TremorComparisonChart({ 
  data = defaultProductData, 
  title = "Product Performance Comparison" 
}: Partial<TremorChartProps>) {
  // Transform data if it has different key structure
  const transformedData = data ? data.map(item => {
    if ('category' in item && 'value' in item) {
      return { product: item.category, Sales: item.value }
    } else if ('value' in item && !('Sales' in item)) {
      return { ...item, Sales: item.value }
    }
    return item
  }) : defaultProductData
  
  console.log('📊 TremorComparisonChart rendering with data:', transformedData)
  
  return (
    <Card className="p-6 bg-white dark:bg-gray-800">
      <div className="flex items-center space-x-2 mb-6">
        <BarChart3 className="h-6 w-6 text-blue-600 dark:text-blue-400" />
        <Text className="text-lg font-semibold dark:text-white">{title}</Text>
      </div>
      
      <BarChart
        className="h-80"
        data={transformedData}
        index="product"
        categories={["Sales"]}
        colors={["blue"]}
        valueFormatter={(number: number) => `$${Intl.NumberFormat("us").format(number).toString()}`}
      />
      
      <div className="mt-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
        <Text className="text-sm text-blue-800 dark:text-blue-300">
          Leading product shows strong performance in comparison analysis
        </Text>
      </div>
    </Card>
  )
}

export function TremorRevenueTrend({ 
  data = defaultSalesData, 
  title = "Revenue Analysis", 
  period = "6 Months" 
}: Partial<TremorChartProps>) {
  return (
    <Card className="p-6 bg-gradient-to-r from-purple-50 to-pink-50 dark:from-purple-900/20 dark:to-pink-900/20">
      <div className="flex items-center space-x-2 mb-6">
        <TrendingUp className="h-6 w-6 text-purple-600 dark:text-purple-400" />
        <Text className="text-lg font-semibold dark:text-white">{title} - {period}</Text>
      </div>
      
      <LineChart
        className="h-80"
        data={data}
        index="month"
        categories={["Revenue", "Sales"]}
        colors={["purple", "pink"]}
        valueFormatter={(number: number) => `$${Intl.NumberFormat("us").format(number).toString()}`}
      />
      
      <div className="mt-6 flex items-center justify-between">
        <Badge color="purple" size="lg">+35% Revenue Growth</Badge>
        <Text className="text-sm text-gray-600 dark:text-gray-300">Outpacing sales by 12%</Text>
      </div>
      
      <div className="mt-4 p-3 bg-purple-50 dark:bg-purple-900/20 rounded-lg">
        <Text className="text-sm text-purple-800 dark:text-purple-300">
          Revenue growth accelerating with improved margins and pricing strategy
        </Text>
      </div>
    </Card>
  )
}