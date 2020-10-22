import React from 'react';
import './App.css';

import Navbar from './Navbar'
import Main from './Main';
import requests from './Requests';

function App() {
  


  return (
    <div className="app">
      <Navbar />
      <Main fetchUrl={requests.fetchClassroom} />
    </div>
  );
}

export default App;
