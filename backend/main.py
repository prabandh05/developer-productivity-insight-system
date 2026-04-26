from fastapi import FastAPI
import pandas as pd
from metrics import (
    calculate_cycle_time,
    get_developer_data,
    get_developer_team,
    get_team_data
)
from insights import cycle_time_insight


app = FastAPI()



data = pd.read_excel("../data/input.xlsx", sheet_name=None)

# Finding Fact_Jira_Issues sheet
issues_df = None    

for name, df in data.items():
    if "issue" in name.lower():
        issues_df = df
        break
issues_df = issues_df.dropna()





@app.get("/")
def home():
    return {"message": "API is running"}


@app.get("/cycle-time")
def get_cycle(dev_id: str):
    if issues_df is None:
        return {"error": "Issues data not found"}

    # Developer data
    dev_data = get_developer_data(issues_df, dev_id)
    dev_cycle_time = calculate_cycle_time(dev_data)

    # Team data
    team = get_developer_team(issues_df, dev_id)

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