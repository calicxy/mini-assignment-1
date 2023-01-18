import React, { useState } from 'react';

import './GoalInput.css';
import Card from '../UI/Card';

function GoalInput(props) {
  const [fileList, setFileList] = useState(null);

  const handleFileChange = (e) => {
    setFileList(e.target.files);
  };

  const fileSubmitHandler = (event) => {
    if (!fileList) {
      return;
    }
    
    const data = new FormData();
    files.forEach((file, i) => {
      data.append(`file${i+1}`, file, file.name);
    });

    props.onAddGoal(data)

  };

  const files = fileList ? [...fileList] : [];

  return (
    <section id='goal-input'>
      <Card>
        <input
          type='file'
          onChange={handleFileChange}
          multiple
        />
        <ul>
          {files.map((file, i) => (
            <li key={i}>
              {file.name} - {file.type}
            </li>
          ))}
        </ul>
        <button onClick={fileSubmitHandler}>Upload</button>
      </Card>
    </section>
  );
}

export default GoalInput;
