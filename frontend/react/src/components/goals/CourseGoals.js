import React from 'react';

import './CourseGoals.css';
import Card from '../UI/Card';

function CourseGoals(props) {
  const hasNoFiles = !props.response;
  return (
    <section id='checksum_results'>
      <Card>
        {hasNoFiles && <h2>No files uploaded. Start uploading some!</h2>}
        <ul>
          {Object.entries(props.goals).map((pair, i) => (
            <li key={i} >
              {pair[0]} : {pair[1].toString()}
            </li>
          ))}
        </ul>
      </Card>
    </section>
  );
}

export default CourseGoals;
