import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";

const data = [
  { date: "10/25/2024", views: 5500 },
  { date: "10/26/2024", views: 5300 },
  { date: "10/27/2024", views: 6000 },
  { date: "10/28/2024", views: 6500 },
  { date: "10/29/2024", views: 6700 },
  { date: "10/30/2024", views: 6600 },
  { date: "11/01/2024", views: 5500 },
  { date: "11/03/2024", views: 6000 },
  { date: "11/05/2024", views: 7000 },
  { date: "11/07/2024", views: 5800 },
  { date: "11/09/2024", views: 5600 },
  { date: "11/11/2024", views: 5900 },
  { date: "11/13/2024", views: 6100 },
  { date: "11/14/2024", views: 6000 },
];

const PageViewTrend = () => {
  return (
    <div style={{ width: "100%", padding: "20px", background: "#fff", borderRadius: "8px" }}>
      <div style={{ marginBottom: "10px" }}>
        <input
          type="text"
          placeholder="Enter page name"
          style={{
            padding: "5px",
            borderRadius: "4px",
            border: "1px solid #ccc",
            marginRight: "10px",
          }}
        />
        <button style={{ padding: "5px 10px", borderRadius: "4px", background: "#007bff", color: "#fff" }}>
          Chart type
        </button>
        <button style={{ padding: "5px 10px", borderRadius: "4px", background: "#007bff", color: "#fff", marginLeft: "10px" }}>
          Permalink
        </button>
        <button style={{ padding: "5px 10px", borderRadius: "4px", background: "#007bff", color: "#fff", marginLeft: "10px" }}>
          Download
        </button>
      </div>

      <LineChart
        width={800}
        height={400}
        data={data}
        margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="views" stroke="#8884d8" activeDot={{ r: 8 }} />
      </LineChart>
    </div>
  );
};

export default PageViewTrend;
