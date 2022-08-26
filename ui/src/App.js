import React from 'react';
import logo from './web10.png';
import './App.css';
import { useGit } from './interfaces/gh'
import {useSearchParams} from 'react-router-dom';

function App() {
  const [searchParams, setSearchParams] = useSearchParams();
  const GI = useGit();
  window.GI = GI;
  React.useEffect(() => {
    if (!GI.token) GI.tryLogin();
    searchParams.delete("code")
    setSearchParams(searchParams)

  },
    [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to the <code>web10</code> network.
        </p>
        <a
          className="App-link"
          href={GI.loginURL}
        >
          Log in
        </a>
      </header>
    </div>
  );
}

export default App;
