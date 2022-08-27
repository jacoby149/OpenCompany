import React from 'react';
import './App.css';
import { useGit } from './interfaces/gh'
import { useSearchParams } from 'react-router-dom';
import Login from './components/Login';
import Profile from './components/Profile';

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
    GI.readToken() ?
      <Profile profile={GI.readToken()} I={GI} />
      : <Login url={GI.loginURL} />

  )
}

export default App;
