import React, { useState } from 'react';

import GoalInput from './components/goals/GoalInput';
import CourseGoals from './components/goals/CourseGoals';
import ErrorAlert from './components/UI/ErrorAlert';

function App() {
  const [loadedResponse, setResponse] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  async function addGoalHandler(data) {
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:5000/checksum-routetoapi', {
        method: 'POST',
        body: data,
        // headers: {
        //   // 'Content-Type': 'application/json'
        //   'Access-Control-Allow-Origin':'*'
        // }
      });

      const resData = await response.json();
      console.log(resData)

      if (!response.ok) {
        throw new Error(resData.message || 'Error calculating the checksum.');
      }
      else {
        setResponse(resData)
      }

      
      // setLoadedChecksums((prevGoals) => {
      //   const updatedGoals = [
      //     {
      //       id: resData.file.id,
      //       name: resData.file.name,
      //       checksum: resData.file.fileChecksum,
      //     },
      //     ...prevGoals,
      //   ];
      //   return updatedGoals;
      // });

    } catch (err) {
      setError(
        err.message ||
          'Adding a goal failed - the server responsed with an error.'
      );
    }
    setIsLoading(false);
  }

  return (
    <div>
      {error && <ErrorAlert errorText={error} />}
      <GoalInput onAddGoal={addGoalHandler} />
      {!isLoading && (
        <CourseGoals goals={loadedResponse}/>
      )}
    </div>
  );
}

export default App;
