import * as React from "react"
import { cn } from "@/lib/utils"

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement> {
  variant?: "default" | "secondary" | "destructive" | "outline" | "success" | "green" | "red" | "gray"
}

function badgeVariants(variant: BadgeProps["variant"]) {
  const variants = {
    default:
      "border-transparent bg-primary text-primary-foreground hover:bg-primary/80",
    secondary:
      "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
    destructive:
      "border-transparent bg-destructive text-destructive-foreground hover:bg-destructive/80",
    outline: "text-foreground",
    success: "border-transparent bg-green-500 text-white hover:bg-green-600",
    green: "border-transparent bg-green-500 text-white hover:bg-green-600",
    red: "border-transparent bg-red-500 text-white hover:bg-red-600",
    gray: "border-transparent bg-gray-500 text-white hover:bg-gray-600",
  }

  return variants[variant || "default"]
}

const Badge = React.forwardRef<HTMLDivElement, BadgeProps>(
  ({ className, variant, ...props }, ref) => {
    return (
      <div
        ref={ref}
        className={cn(
          "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
          badgeVariants(variant),
          className
        )}
        {...props}
      />
    )
  }
)
Badge.displayName = "Badge"

export { Badge }