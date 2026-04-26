

def cycle_time_insight(dev_value, team_value):
    

    # Safety check
    if dev_value is None or team_value is None:
        return {
            "insight": "Insufficient data to evaluate cycle time",
            "suggestion": "Ensure tasks have valid start and end dates"
        }

    # Difference ratio 
    diff = dev_value - team_value
 
    if dev_value > team_value * 1.2:
        return {
            "insight": "Cycle time is significantly higher than team average",
            "suggestion": "Break tasks into smaller units and reduce delays in execution or review"
        }

    elif dev_value > team_value:
        return {
            "insight": "Cycle time is slightly higher than team average",
            "suggestion": "Review task complexity and identify minor bottlenecks"
        }

    elif dev_value < team_value * 0.8:
        return {
            "insight": "Cycle time is lower than team average",
            "suggestion": "Good execution speed, maintain consistency"
        }

    else:
        return {
            "insight": "Cycle time is within the normal range",
            "suggestion": "Maintain current workflow"
        }