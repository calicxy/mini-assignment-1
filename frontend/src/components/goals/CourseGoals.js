import React from 'react';

import './CourseGoals.css';
import Card from '../UI/Card';

function CourseGoals(props) {
  const hasNoFiles = !props.goals || props.goals.length === 0;

  return (
    <section id='checksum_results'>
      <Card>
        {hasNoFiles && <h2>No files uploaded. Start uploading some!</h2>}
        <ul>
          {props.goals.map((file, i) => (
            <li key={i} >
              {file.name}
              {file.checksum}
            </li>
          ))}
        </ul>
      </Card>
    </section>
  );
}

export default CourseGoals;
