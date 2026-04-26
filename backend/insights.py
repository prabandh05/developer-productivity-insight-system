import math
#cycle time insights
def cycle_time_insight(dev_value, team_value):

    if dev_value is None or team_value is None or math.isnan(dev_value) or math.isnan(team_value):
        return {
            "insight": "Insufficient data to evaluate cycle time",
            "suggestion": "Ensure tasks have valid start and end dates"
        }

    if team_value == 0:
        return {
            "insight": "No team baseline available",
            "suggestion": "Insufficient team data for comparison"
        }

    if dev_value > team_value * 1.2:
        return {
            "insight": "Cycle time is significantly higher than team average, indicating delays",
            "suggestion": "Break tasks into smaller units and reduce delays in execution or review"
        }

    elif dev_value > team_value:
        return {
            "insight": "Cycle time is slightly higher than team average",
            "suggestion": "Review task complexity and identify minor bottlenecks"
        }

    elif dev_value < team_value * 0.8:
        return {
            "insight": "Cycle time is lower than team average, indicating faster execution",
            "suggestion": "Maintain current workflow and consistency"
        }

    else:
        return {
            "insight": "Cycle time is within the normal range",
            "suggestion": "Maintain current workflow"
        }

#PR throughput insights
def pr_throughput_insight(dev_value, team_value):

    if team_value == 0:
        return {
            "insight": "No team activity detected",
            "suggestion": "Check if PR data is missing or team is inactive"
        }

    if dev_value == 0:
        return {
            "insight": "No pull requests completed",
            "suggestion": "Check if tasks are blocked or work is not being submitted"
        }

    if dev_value < team_value * 0.8:
        return {
            "insight": "PR throughput is lower than team average per developer",
            "suggestion": "Increase contribution frequency and reduce delays in submitting code"
        }

    elif dev_value > team_value * 1.2:
        return {
            "insight": "PR throughput is higher than team average",
            "suggestion": "Good contribution level, maintain consistency"
        }

    else:
        return {
            "insight": "PR throughput is within normal range",
            "suggestion": "Maintain current pace"
        }

#Lead time insights
def lead_time_insight(dev_value, team_value):

    if dev_value == 0 and team_value == 0:
        return {
            "insight": "No lead time data available",
            "suggestion": "Ensure deployment data is present"
        }

    if team_value == 0:
        return {
            "insight": "No team baseline available",
            "suggestion": "Insufficient team data"
        }

    if dev_value > team_value * 1.2:
        return {
            "insight": "Lead time is higher than team average, indicating delays between code completion and deployment",
            "suggestion": "Reduce delays between code completion and deployment"
        }

    elif dev_value < team_value * 0.8:
        return {
            "insight": "Lead time is lower than team average, indicating faster delivery",
            "suggestion": "Maintain efficient deployment practices"
        }

    else:
        return {
            "insight": "Lead time is within normal range",
            "suggestion": "Maintain current workflow"
        }

#bug rate insights
def bug_rate_insight(dev_value, team_value):

    if dev_value == 0 and team_value == 0:
        return {
            "insight": "No bug data available",
            "suggestion": "Ensure bug reports are properly tracked"
        }

    if team_value == 0:
        return {
            "insight": "No team baseline available",
            "suggestion": "Insufficient issue data"
        }

    if dev_value > team_value * 1.2:
        return {
            "insight": "Bug rate is higher than team average, indicating quality issues",
            "suggestion": "Improve testing practices and code review quality"
        }

    elif dev_value < team_value * 0.8:
        return {
            "insight": "Bug rate is lower than team average, indicating better code quality",
            "suggestion": "Maintain current development and testing practices"
        }

    else:
        return {
            "insight": "Bug rate is within normal range",
            "suggestion": "Maintain current workflow"
        }