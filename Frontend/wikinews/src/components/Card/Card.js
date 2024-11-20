import React from "react";
import "./Card.css";

const Card = ({ title, children, className }) => {
  return (
    <div className={`card ${className}`}>
      {title && <h4 className="card-title">{title}</h4>}
      <div className="card-content">{children}</div>
    </div>
  );
};

export default Card;
