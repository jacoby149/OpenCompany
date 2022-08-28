import React from 'react';
import './bulma/css/bulma.min.css';
import './App.css';
import { useAPI } from './interfaces/iAPI'
import { useSearchParams } from 'react-router-dom';
import Login from './components/Login';
import Profile from './components/Profile';

function App() {
  const [searchParams, setSearchParams] = useSearchParams();
  const AI = useAPI();
  window.AI = AI;
  React.useEffect(() => {
    if (!AI.token) AI.tryLogin();
    searchParams.delete("code")
    setSearchParams(searchParams)
  },
    [])
  return (
    AI.readToken() ?
      <Profile profile={AI.readToken()} I={AI} />
      : <Login I={AI} />

  )
}

export default App;
