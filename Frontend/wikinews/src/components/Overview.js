import React from 'react';
import Card from './Card/Card'
import "./Overview.css";

const Overview = () => {
  return (
    <div className="dashboard">
      {/* Total Page Views Card */}
      <Card title="Reading" className="metric-card">
        <h2>24B</h2>
        <p>
          October <span className="positive-trend">↑ 2.57% month over month</span>
        </p>
        <div className="chart">
          {/* Placeholder for a chart */}
          <div className="chart-bar"></div>
        </div>
        <p>
          299B <span className="negative-trend">↓ -8.40% year over year</span>
        </p>
      </Card>
    </div>
  );
};

export default Overview;
