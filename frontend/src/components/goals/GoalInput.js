import React, { useState } from 'react';

import './GoalInput.css';
import Card from '../UI/Card';

const IP = 'https://localhost:3000'

function GoalInput(props) {
  const [fileList, setFileList] = useState<FileList | null>(null);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    setFileList(e.target.files);
  };


  function fileSubmitHandler(event) {
    if (!fileList) {
      return;
    }
    
    const data = new FormData();
    files.forEach((file, i) => {
      data.append(`file-${i}`, file, file.name);
    });

    fetch(`${IP}/checksum-routetoapi`, {
      method: 'POST',
      body: data,
    })
      .then((res) => res.json())
      .then((data) => console.log(data))
      .catch((err) => console.error(err));
  };

  const files = fileList ? [...fileList] : [];

  return (
    <section id='goal-input'>
      <input
        type='file'
        id='file'
        onChange={updateGoalTextHandler}
        multiple
      />
    </section>
  );
}

export default GoalInput;
