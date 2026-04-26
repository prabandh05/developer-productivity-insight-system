import { useState, useEffect } from "react";
import API from "./api";
import "./App.css";

function App() {
  const [developers, setDevelopers] = useState<any[]>([]);
  const [devId, setDevId] = useState<string>("");
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    const fetchDevelopers = async () => {
      try {
        const res = await API.get("/developers");
        setDevelopers(res.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchDevelopers();
  }, []);

  const fetchData = async (id: string) => {
    try {
      const [cycle, lead, pr, bug, deploy] = await Promise.all([
        API.get(`/cycle-time?dev_id=${id}`),
        API.get(`/lead-time?dev_id=${id}`),
        API.get(`/pr-throughput?dev_id=${id}`),
        API.get(`/bug-rate?dev_id=${id}`),
        API.get(`/deployment-frequency?dev_id=${id}`)
      ]);

      setData({
        cycle: cycle.data,
        lead: lead.data,
        pr: pr.data,
        bug: bug.data,
        deploy: deploy.data
      });

    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="container">

      {/* LEFT */}
      <div className="sidebar">
        <h2>Developers</h2>

        {developers.map((dev) => (
          <button
            key={dev.developer_id}
            className="dev-button"
            onClick={() => {
              setDevId(dev.developer_id);
              fetchData(dev.developer_id);
            }}
          >
            {dev.developer_name}
          </button>
        ))}
      </div>

      {/* RIGHT */}
      <div className="main">

        {/* TOP RIGHT BUTTON */}
        <div className="topbar">
          <button className="upload-btn">Upload Excel</button>
        </div>

        {/* HEADER */}
        <div className="header">
          <h1>Developer Dashboard</h1>

          {devId && (
            <>
              <p><b>ID:</b> {devId}</p>
              <p><b>Team:</b> {data?.cycle?.team}</p>
            </>
          )}
        </div>

        {!data && <p>Select a developer to view metrics</p>}

        {data && (
          <div className="dashboard">

            <Metric
              title="Cycle Time"
              dev={data.cycle.developer_cycle_time}
              team={data.cycle.team_cycle_time}
              insight={data.cycle.insight}
              suggestion={data.cycle.suggestion}
            />

            <Metric
              title="Lead Time"
              dev={data.lead.developer_lead_time}
              team={data.lead.team_lead_time}
              insight={data.lead.insight}
              suggestion={data.lead.suggestion}
            />

            <Metric
              title="PR Throughput"
              dev={data.pr.developer_pr_throughput}
              team={data.pr.team_avg_pr_throughput}
              insight={data.pr.insight}
              suggestion={data.pr.suggestion}
            />

            <Metric
              title="Bug Rate"
              dev={data.bug.developer_bug_rate}
              team={data.bug.team_bug_rate}
              insight={data.bug.insight}
              suggestion={data.bug.suggestion}
            />

            <Metric
              title="Deployment Frequency"
              dev={data.deploy.developer_deployment_frequency}
              team={data.deploy.team_deployment_frequency}
              insight={data.deploy.insight}
              suggestion={data.deploy.suggestion}
            />

          </div>
        )}
      </div>
    </div>
  );
}

function Metric({ title, dev, team, insight, suggestion }: any) {
  return (
    <div className="card">
      <h3>{title}</h3>
      <p className="value"><b>Developer:</b> {dev}</p>
      <p className="value"><b>Team Avg:</b> {team}</p>
      <p><b>Insight:</b> {insight}</p>
      <p><b>Suggestion:</b> {suggestion}</p>
    </div>
  );
}

export default App;