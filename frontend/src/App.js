import React from 'react';
import {BrowserRouter as Router,Routes,Route}  from 'react-router-dom';
import { About } from './components/about';
import { Teachers } from './components/Teachers';

function App() {
  return (
    <Router>

    <div>
      <Routes>
        <Route path='/about' element = {< About />}/>
        <Route path='/' element = {<Teachers/>} />
      </Routes>
    </div>
    </Router>
  );
}

export default App;
