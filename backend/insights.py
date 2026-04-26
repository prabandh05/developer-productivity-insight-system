import pandas as pd  



# Cycle Time Insights

def cycle_time_insight(dev_value, team_value):

    
    if dev_value is None or team_value is None or pd.isna(dev_value) or pd.isna(team_value):
        return {
            "insight": "Insufficient data to evaluate cycle time",
            "suggestion": "Ensure tasks have valid in-progress and completion dates"
        }

    if team_value == 0:
        return {
            "insight": "No team baseline available",
            "suggestion": "Insufficient team data for comparison"
        }

    if dev_value > team_value * 1.2:
        return {
            "insight": f"Cycle time is significantly higher than team average ({dev_value} vs {team_value} days)",  
            "suggestion": "Break tasks into smaller units and reduce delays during active development"
        }

    elif dev_value > team_value:
        return {
            "insight": f"Cycle time is slightly higher than team average ({dev_value} vs {team_value} days)", 
            "suggestion": "Review task complexity and identify minor execution bottlenecks"
        }

    elif dev_value < team_value * 0.8:
        return {
            "insight": f"Cycle time is lower than team average ({dev_value} vs {team_value} days)", 
            "suggestion": "Maintain current workflow and consistency"
        }

    else:
        return {
            "insight": "Cycle time is within the normal range",
            "suggestion": "Maintain current workflow and consistency"
        }



# PR Throughput Insights

def pr_throughput_insight(dev_value, team_value):

    
    if dev_value is None or team_value is None or pd.isna(dev_value) or pd.isna(team_value):
        return {
            "insight": "Insufficient data to evaluate PR throughput",
            "suggestion": "Ensure PR data is properly tracked"
        }

    if team_value == 0:
        return {
            "insight": "No team activity detected",
            "suggestion": "Check if PR data is missing or team is inactive"
        }

    if dev_value == 0:
        return {
            "insight": "No pull requests completed",
            "suggestion": "Check if work is blocked or not being submitted"
        }

    if dev_value < team_value * 0.8:
        return {
            "insight": f"PR throughput is lower than team average ({dev_value} vs {team_value})", 
            "suggestion": "Increase contribution frequency and reduce delays in submitting code"
        }

    elif dev_value > team_value * 1.2:
        return {
            "insight": f"PR throughput is higher than team average ({dev_value} vs {team_value})", 
            "suggestion": "Good contribution level, maintain consistency"
        }

    else:
        return {
            "insight": "PR throughput is within normal range",
            "suggestion": "Maintain current pace and consistency"
        }



# Lead Time Insights

def lead_time_insight(dev_value, team_value):

    # 🔥 CHANGED (safe handling)
    if dev_value is None or team_value is None or pd.isna(dev_value) or pd.isna(team_value):
        return {
            "insight": "Insufficient data to evaluate lead time",
            "suggestion": "Ensure PR and deployment data are properly linked"
        }

    if dev_value == 0 and team_value == 0:
        return {
            "insight": "No lead time data available",
            "suggestion": "Ensure deployment activity is recorded"
        }

    if team_value == 0:
        return {
            "insight": "No team baseline available",
            "suggestion": "Insufficient team deployment data"
        }

    if dev_value > team_value * 1.2:
        return {
            "insight": f"Lead time is higher than team average ({dev_value} vs {team_value} days)", 
            "suggestion": "Reduce delays between PR creation and deployment"
        }

    elif dev_value < team_value * 0.8:
        return {
            "insight": f"Lead time is lower than team average ({dev_value} vs {team_value} days)", 
            "suggestion": "Maintain efficient delivery practices"
        }

    else:
        return {
            "insight": "Lead time is within normal range",
            "suggestion": "Maintain current workflow and consistency"
        }



# Bug Rate Insights

def bug_rate_insight(dev_value, team_value):

    if dev_value is None or team_value is None or pd.isna(dev_value) or pd.isna(team_value):
        return {
            "insight": "Insufficient data to evaluate bug rate",
            "suggestion": "Ensure bug tracking data is available"
        }

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
            "insight": f"Bug rate is higher than team average ({dev_value} vs {team_value})", 
            "suggestion": "Improve testing practices and reduce production-level defects"
        }

    elif dev_value < team_value * 0.8:
        return {
            "insight": f"Bug rate is lower than team average ({dev_value} vs {team_value})", 
            "suggestion": "Maintain current development and testing practices"
        }

    else:
        return {
            "insight": "Bug rate is within normal range",
            "suggestion": "Maintain current workflow and quality practices"
        }



# Deployment Frequency Insights

def deployment_frequency_insight(dev_value, team_value):

    if dev_value is None or team_value is None or pd.isna(dev_value) or pd.isna(team_value):
        return {
            "insight": "Insufficient data to evaluate deployment frequency",
            "suggestion": "Ensure deployment tracking is available"
        }

    if dev_value == 0 and team_value == 0:
        return {
            "insight": "No deployment activity detected",
            "suggestion": "Ensure deployment data is properly tracked"
        }

    if team_value == 0:
        return {
            "insight": "No team baseline available",
            "suggestion": "Insufficient team deployment data"
        }

    if dev_value < team_value * 0.8:
        return {
            "insight": f"Deployment frequency is lower than team average ({dev_value} vs {team_value})",  
            "suggestion": "Increase deployment frequency to improve delivery speed"
        }

    elif dev_value > team_value * 1.2:
        return {
            "insight": f"Deployment frequency is higher than team average ({dev_value} vs {team_value})",  
            "suggestion": "Good release cadence, maintain consistency"
        }

    else:
        return {
            "insight": "Deployment frequency is within normal range",
            "suggestion": "Maintain current deployment practices"
        }