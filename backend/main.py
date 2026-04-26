from fastapi import FastAPI
import pandas as pd

from metrics import (
    calculate_cycle_time,
    get_developer_data,
    get_developer_team,
    get_team_data,
    calculate_pr_throughput,
    get_sheet_by_keywords,
    calculate_team_pr_average,
    get_team_developers,
    preprocess_issue_dates,
    calculate_lead_time,
    calculate_bug_rate,
    calculate_deployment_frequency,
    calculate_team_deployment_average
)

from insights import (
    cycle_time_insight,
    pr_throughput_insight,
    lead_time_insight,
    bug_rate_insight,
    deployment_frequency_insight
)

app = FastAPI()

# Load data
data = pd.read_excel("../data/input.xlsx", sheet_name=None)

# Load issues data
issues_df = get_sheet_by_keywords(data, ["jira"])
issues_df = preprocess_issue_dates(issues_df)

# Load PR data
prs_df = get_sheet_by_keywords(data, ["request", "pull"])
prs_df = prs_df.dropna(subset=["developer_id"])

# Load deployment data
deploy_df = get_sheet_by_keywords(data, ["deployment"])
deploy_df = deploy_df.dropna(subset=["completed_at", "pr_id"])

# Load bug data
bugs_df = get_sheet_by_keywords(data, ["bug"])
bugs_df = bugs_df.dropna(subset=["developer_id"])

@app.get("/")
def home():
    return {"message": "API is running"}


# Cycle Time API

@app.get("/cycle-time")
def get_cycle(dev_id: str):
    if issues_df is None:
        return {"error": "Issues data not found"}

    dev_data = get_developer_data(issues_df, dev_id, "developer_id")

    if dev_data.empty:
        return {"error": "No data found for developer"}

    dev_cycle_time = calculate_cycle_time(dev_data)

    team = get_developer_team(issues_df, dev_id, "developer_id", "team_name")

    if team is None:
        return {"error": "Team not found for developer"}

    team_data = get_team_data(issues_df, team)
    team_cycle_time = calculate_cycle_time(team_data)

    insight_result = cycle_time_insight(dev_cycle_time, team_cycle_time)

    return {
        "developer_id": dev_id,
        "team": team,
        "developer_cycle_time": dev_cycle_time,
        "team_cycle_time": team_cycle_time,
        "insight": insight_result["insight"],
        "suggestion": insight_result["suggestion"]
    }


# PR Throughput API

@app.get("/pr-throughput")
def get_pr_throughput(dev_id: str):
    if prs_df is None:
        return {"error": "PR data not found"}

    dev_prs = get_developer_data(prs_df, dev_id, "developer_id")

    if dev_prs.empty:
        return {"error": "No PR data found for developer"}

    dev_value = calculate_pr_throughput(dev_prs)

    team = get_developer_team(issues_df, dev_id, "developer_id", "team_name")

    if team is None:
        return {"error": "Team not found"}

    team_devs = get_team_developers(issues_df, team)

    team_prs = prs_df[prs_df["developer_id"].isin(team_devs)]

    team_value = calculate_team_pr_average(team_prs, "developer_id")

    insight = pr_throughput_insight(dev_value, team_value)

    return {
        "developer_id": dev_id,
        "team": team,
        "developer_pr_throughput": dev_value,
        "team_avg_pr_throughput": team_value,
        "insight": insight["insight"],
        "suggestion": insight["suggestion"]
    }


# Lead Time API

@app.get("/lead-time")
def get_lead_time(dev_id: str):

    if deploy_df is None or prs_df is None:
        return {"error": "Required data not found"}

    dev_prs = get_developer_data(prs_df, dev_id, "developer_id")        
    dev_deploys = get_developer_data(deploy_df, dev_id, "developer_id") 

    if dev_prs.empty or dev_deploys.empty:
        return {"error": "No sufficient data for developer"}

    dev_value = calculate_lead_time(dev_deploys)

    team = get_developer_team(issues_df, dev_id, "developer_id", "team_name")

    if team is None:
        return {"error": "Team not found"}

    team_devs = get_team_developers(issues_df, team)

    team_prs = prs_df[prs_df["developer_id"].isin(team_devs)]          
    team_deploys = deploy_df[deploy_df["developer_id"].isin(team_devs)]

    if team_prs.empty or team_deploys.empty:
        return {"error": "No sufficient data for team"}

    team_value = calculate_lead_time(team_deploys)

    insight = lead_time_insight(dev_value, team_value)

    return {
        "developer_id": dev_id,
        "team": team,
        "developer_lead_time": dev_value,
        "team_lead_time": team_value,
        "insight": insight["insight"],
        "suggestion": insight["suggestion"]
    }


# Bug Rate API

@app.get("/bug-rate")
def get_bug_rate(dev_id: str):

    if bugs_df is None or issues_df is None:
        return {"error": "Required data not found"}

    dev_bugs = get_developer_data(bugs_df, dev_id, "developer_id")
    dev_issues = get_developer_data(issues_df, dev_id, "developer_id")

    if dev_issues.empty:
        return {"error": "No issue data for developer"}

    dev_value = calculate_bug_rate(dev_bugs, dev_issues)   

    team = get_developer_team(issues_df, dev_id, "developer_id", "team_name")

    if team is None:
        return {"error": "Team not found"}

    team_devs = get_team_developers(issues_df, team)

    team_bugs = bugs_df[bugs_df["developer_id"].isin(team_devs)]
    team_issues = issues_df[issues_df["developer_id"].isin(team_devs)]

    team_value = calculate_bug_rate(team_bugs, team_issues)

    insight = bug_rate_insight(dev_value, team_value)

    return {
        "developer_id": dev_id,
        "team": team,
        "developer_bug_rate": dev_value,
        "team_bug_rate": team_value,
        "insight": insight["insight"],
        "suggestion": insight["suggestion"]
    }


# Deployment Frequency API

@app.get("/deployment-frequency")
def get_deployment_frequency(dev_id: str):

    if deploy_df is None:
        return {"error": "Deployment data not found"}

    dev_deploys = get_developer_data(deploy_df, dev_id, "developer_id")

    if dev_deploys.empty:
        return {"error": "No deployment data for developer"}

    dev_value = calculate_deployment_frequency(dev_deploys)   

    team = get_developer_team(issues_df, dev_id, "developer_id", "team_name")

    if team is None:
        return {"error": "Team not found"}

    team_devs = get_team_developers(issues_df, team)

    team_deploys = deploy_df[deploy_df["developer_id"].isin(team_devs)]

    team_value = calculate_team_deployment_average(team_deploys)

    insight = deployment_frequency_insight(dev_value, team_value)

    return {
        "developer_id": dev_id,
        "team": team,
        "developer_deployment_frequency": dev_value,
        "team_deployment_frequency": team_value,
        "insight": insight["insight"],
        "suggestion": insight["suggestion"]
    }