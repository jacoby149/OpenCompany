import React from 'react';
import logo from '../web10.png';

function Login({url}) {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Welcome to the <code>web10</code> network.
                </p>
                <a
                    className="App-link"
                    href={url}
                >
                    Log in
                </a>
            </header>
        </div>
    );
}

export default Login;