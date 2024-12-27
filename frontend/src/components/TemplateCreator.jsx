import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const TemplateCreator = () => {
  const [templates, setTemplates] = useState([]);

  const addTemplate = () => {
    const newTemplate = {
      id: templates.length + 1,
      name: `Template ${templates.length + 1}`,
      description: "You can create a template and add the amount of workouts you want to add.",
    };
    setTemplates([...templates, newTemplate]);
  };

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-header">Create New Template</div>
        <div className="card-body">
          <h5 className="card-title">Name</h5>
          <p className="card-text">
            You can create a template and add the amount of workouts you want to add.
          </p>
          <button className="btn btn-primary" onClick={addTemplate}>
            Create Template
          </button>
        </div>
      </div>

      <div className="mt-4">
        {templates.map((template) => (
          <div className="card mb-3" key={template.id}>
            <div className="card-header">{template.name}</div>
            <div className="card-body">
              <p className="card-text">{template.description}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TemplateCreator;
