import logo from './web10.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to the <code>web10</code> network.
        </p>
        <a
          className="App-link"
          href="http://api.localhost/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Log in
        </a>
      </header>
    </div>
  );
}

export default App;
