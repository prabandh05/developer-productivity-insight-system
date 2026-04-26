import pandas as pd


# Finding sheet with multiple keywords
def get_sheet_by_keywords(data, keywords):
    for name, df in data.items():
        name_lower = name.lower()

        if all(keyword in name_lower for keyword in keywords):
            return df

    return None


# Preprocess issue dates 
def preprocess_issue_dates(df):
    df = df.copy()

    df["in_progress_at"] = pd.to_datetime(df["in_progress_at"], errors="coerce") 
    df["done_at"] = pd.to_datetime(df["done_at"], errors="coerce")

    df = df.dropna(subset=["in_progress_at", "done_at"])  

    return df


# Calculating cycle time 
def calculate_cycle_time(df):
    if df.empty:
        return 0

    if "cycle_time_days" not in df.columns:
        return 0

    result = df["cycle_time_days"].mean()

    if pd.isna(result):
        return 0

    return round(result, 2)


# Filtering data for a specific developer
def get_developer_data(df, dev_id, dev_column):
    return df[df[dev_column] == dev_id]


# Getting team of developer 
def get_developer_team(df, dev_id, dev_column="developer_id", team_column="team_name"):
    result = df[df[dev_column] == dev_id]

    if result.empty:
        return None

    return result[team_column].iloc[0]


# Filtering data for a specific team
def get_team_data(df, team, team_column="team_name"):
    return df[df[team_column] == team]


# Calculating PR throughput 
def calculate_pr_throughput(df):
    if df.empty:
        return 0

    return len(df[df["status"].fillna("").str.lower() == "merged"])  


# Average PR per developer in team 
def calculate_team_pr_average(df, dev_column="developer_id"):
    if df.empty:
        return 0

    total_prs = len(df)
    unique_devs = df[dev_column].nunique()

    if unique_devs == 0:
        return 0

    return round(total_prs / unique_devs, 2)


# Unique developers in team
def get_team_developers(df, team, team_column="team_name", dev_column="developer_id"):
    return df[df[team_column] == team][dev_column].unique()


def calculate_lead_time(df):
    if df.empty:
        return 0

    if "lead_time_days" not in df.columns:
        return 0

    result = df["lead_time_days"].mean()

    if pd.isna(result):
        return 0

    return round(result, 2)

# Dev PRs (optional helper)
def get_developer_prs(df, dev_id, dev_column="developer_id"):
    return df[df[dev_column] == dev_id]


#  Bug rate FIXED (escaped_to_prod)
def calculate_bug_rate(bugs_df, issues_df):
    if issues_df.empty:
        return 0

    bugs_df = bugs_df[
    bugs_df["escaped_to_prod"]
    .astype(str)
    .str.lower()
    .isin(["true", "yes", "1"])
]

    total_bugs = len(bugs_df)
    total_issues = len(issues_df)

    if total_issues == 0:
        return 0

    return round(total_bugs / total_issues, 3)


#  Deployment Frequency FIXED
def calculate_deployment_frequency(df):
    if df.empty:
        return 0

    df = df[df["status"].fillna("").str.lower() == "success"]

    return len(df)

# Deployment Frequency for Team (Calculating Average deployment per team member)
def calculate_team_deployment_average(df, dev_column="developer_id"):
    if df.empty:
        return 0

    df = df[df["status"].fillna("").str.lower() == "success"]

    total_deploys = len(df)
    unique_devs = df[dev_column].nunique()

    if unique_devs == 0:
        return 0

    return round(total_deploys / unique_devs, 2)