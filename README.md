# Developer Productivity Insight System (MVP)

## Overview

This project is a lightweight full-stack MVP designed to help developers and managers understand engineering productivity metrics and take actionable decisions.

In many engineering environments, metrics such as cycle time, lead time, bug rate, and deployment frequency are available. However, these numbers alone do not explain what is happening or what actions should be taken.

This system addresses that gap by converting raw metrics into meaningful insights and actionable suggestions.

---

## Problem Statement

Engineering teams commonly track metrics such as:

- Cycle Time
- Lead Time
- Bug Rate
- Deployment Frequency
- PR Throughput

However, these metrics:

- Lack context
- Are difficult to interpret
- Do not provide guidance for improvement

The core problem is not the absence of data, but the absence of interpretation and decision support.

---

## Solution

This project builds a Developer Productivity Insight System that:

1. Processes structured engineering data from Excel
2. Calculates key productivity metrics
3. Interprets those metrics using rule-based logic
4. Provides actionable suggestions for improvement

---

## Key Features

- Developer-level productivity analysis (Individual Contributor view)
- Team vs individual comparison
- Rule-based insight generation
- Actionable recommendations
- API-driven backend for fast computation

---

## Tech Stack

### Backend
- Python
- FastAPI
- Pandas

### Frontend
- React.js

---

## System Architecture

Excel Data → FastAPI Backend → Metric Calculation → Insight Engine → React UI

---

## Input Data

The system consumes structured Excel data containing:

- Issue data (tasks with start and end time)
- Pull request data (creation and merge details)
- Deployment logs
- Bug reports

---

## Metrics Implemented

| Metric                  | Description                                      |
|------------------------|--------------------------------------------------|
| Cycle Time             | Time taken to complete a task                    |
| Lead Time              | Time from PR creation to deployment              |
| Bug Rate               | Number of bugs relative to completed tasks       |
| Deployment Frequency   | Number of deployments in a given time period     |
| PR Throughput          | Number of merged pull requests                   |

---

## Insight Engine

The system uses a rule-based approach to interpret metrics:

- Each developer's metrics are compared with team averages
- Insights are generated based on deviations
- Suggestions are provided for improvement

Example:

Cycle Time: 6 days  
Team Average: 4 days  

Insight:  
Cycle time is higher than team average, indicating potential delays.

Suggestion:  
Break tasks into smaller units and reduce review bottlenecks.

---

## User Flow

1. Load or upload dataset
2. Select a developer
3. View:
   - Metrics
   - Insights
   - Suggestions
4. Take action based on recommendations

---

## Project Structure

backend/
  main.py
  metrics.py
  insights.py

frontend/
  src/
  components/

data/
  input.xlsx

---

## How to Run

### Backend

pip install -r requirements.txt  
uvicorn main:app --reload  

### Frontend

npm install  
npm start  

---

## Design Decisions

- FastAPI was chosen for efficient data processing and API handling
- Pandas is used for data manipulation and metric computation
- A rule-based insight engine was used for clarity and explainability
- Focused on individual contributor view to keep the MVP simple
- No database was used to reduce complexity and development time

---

## Future Improvements

- Add manager-level dashboard
- Improve insight intelligence
- Add real-time data integration
- Enhance user interface and experience

---

## Execution Approach

This project was built using a structured, phase-wise approach.

Refer to CHECKLIST.md for detailed execution steps and progress tracking.

---

## Demo

Demo video link: (to be added)

---

## Final Note

The goal of this project is not just to display metrics, but to help developers understand their work patterns and make better decisions.

This system focuses on clarity, simplicity, and actionable insights.