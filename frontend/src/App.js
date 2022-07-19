import Home from './containers/Home/Home';
import Results from './containers/Results/Results';

// import About from './containers/About/About';
// import Bookmarks from './containers/Bookmarks/Bookmarks';

import './App.css';
import {
  BrowserRouter as Router,
  Route,
  Routes,
} from "react-router-dom";
import { useState } from 'react';

function App() {

  const [search_results, setSearchResults]= useState([]);
  return (
    <Router>
      <div className='App'>
        <Routes>
          <Route exact path='/' element={<Home setSearchResults= {setSearchResults} />}/>
          <Route path='/results' element={<Results setSearchResults= {setSearchResults} search_results= {search_results} />} />

          {/* <Route path='/about'>
            <About />
          </Route>
          <Route path='/bookmarks'>
            <Bookmarks />
          </Route>
          <Route path='/results'>
            <Results />
          </Route> */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
