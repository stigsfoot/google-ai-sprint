"""
ADK Agent for Generative UI Business Intelligence
Simplified structure for demo without full ADK package
"""
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))


def create_sales_trend_card(sales_data: str = '[]', period: str = 'Q4') -> str:
    """Tool that generates a sales trend React component with clean JSX."""
    # Generate sample data for visualization
    sample_data = [
        {"month": "Jan", "value": 1200},
        {"month": "Feb", "value": 1350}, 
        {"month": "Mar", "value": 1580},
        {"month": "Apr", "value": 1420},
        {"month": "May", "value": 1650},
        {"month": "Jun", "value": 1780}
    ]
    
    return f'''<Card className="p-6 bg-gradient-to-r from-green-50 to-blue-50 dark:from-green-900/20 dark:to-blue-900/20">
  <CardHeader>
    <div className="flex items-center space-x-2">
      <TrendingUp className="h-6 w-6 text-green-600" />
      <CardTitle className="text-lg">Sales Trend - {period}</CardTitle>
    </div>
  </CardHeader>
  <CardContent>
    <div className="mt-4">
      <LineChart 
        data={{{json.dumps(sample_data)}}}
        className="h-64"
        stroke="#10b981"
        strokeWidth={{3}}
      />
    </div>
    <div className="mt-4 flex items-center justify-between">
      <Badge variant="default" className="bg-green-100 text-green-800">+23% Growth</Badge>
      <span className="text-sm text-gray-600 dark:text-gray-300">vs previous period</span>
    </div>
    <div className="mt-4 p-3 bg-green-50 dark:bg-green-900/20 rounded-lg">
      <p className="text-sm text-green-800 dark:text-green-300">Sales showing strong upward trend with 23% growth over the period</p>
    </div>
  </CardContent>
</Card>'''


def create_metric_card(value: str = '$47.2K', label: str = 'Monthly Revenue', change: str = '+12.3%', context: str = 'Compared to previous month') -> str:
    """Generate a key metric card with change indicator using clean JSX."""
    change_color = "green" if change.startswith("+") else "red" if change.startswith("-") else "gray"
    
    return f'''<Card className="p-6 text-center max-w-xs">
  <CardContent className="pt-6">
    <div className="text-4xl font-bold text-gray-900 dark:text-white">{value}</div>
    <p className="text-sm text-gray-600 dark:text-gray-300 mt-1">{label}</p>
    <Badge variant="default" className="mt-2 bg-{change_color}-100 text-{change_color}-800">{change}</Badge>
    <p className="text-xs text-gray-500 dark:text-gray-400 mt-2">{context}</p>
  </CardContent>
</Card>'''


def create_comparison_bar_chart(title: str = 'Product Performance Comparison', insight: str = 'Product C leads with 3.2K units') -> str:
    """Generate a comparison bar chart component using clean JSX."""
    sample_data = [
        {"category": "Product A", "value": 2400}, 
        {"category": "Product B", "value": 1800}, 
        {"category": "Product C", "value": 3200}, 
        {"category": "Product D", "value": 1600}
    ]
    
    return f'''<Card className="p-6">
  <CardHeader>
    <div className="flex items-center space-x-2">
      <BarChart3 className="h-6 w-6 text-blue-600" />
      <CardTitle className="text-lg">{title}</CardTitle>
    </div>
  </CardHeader>
  <CardContent>
    <div className="mt-4">
      <BarChart 
        data={{{json.dumps(sample_data)}}}
        className="h-64"
        fill="#3b82f6"
      />
    </div>
    <div className="mt-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
      <p className="text-sm text-blue-800 dark:text-blue-300">{insight}</p>
    </div>
  </CardContent>
</Card>'''


# For demo purposes - these would be ADK tools in full implementation
# Tool functions are available for direct calling without full ADK framework