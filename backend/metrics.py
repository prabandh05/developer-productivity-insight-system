import pandas as pd

# Pre process to convert date columns to datetime format
def preprocess_issue_dates(df):
    df = df.copy()

    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    df["done_at"] = pd.to_datetime(df["done_at"], errors="coerce")

    df = df.dropna(subset=["created_at", "done_at"])

    return df

#Calculating cycle time in days for each developer
def calculate_cycle_time(df):
    df = preprocess_issue_dates(df)

    cycle_times = (df["done_at"] - df["created_at"]).dt.days

    return round(cycle_times.mean(), 2)

#Filtering data for a specific developer
def get_developer_data(df, dev_id):
    return df[df["developer_id"] == dev_id]


#Getting the team of a developer
def get_developer_team(df, dev_id, team_column="team_name"):
    team = df[df["developer_id"] == dev_id][team_column]

    if team.empty:
        return None

    return team.iloc[0]


#Filtering data for a specific team
def get_team_data(df, team, team_column="team_name"):
    return df[df[team_column] == team]