import React from 'react';
import logo from '../web10.png';

function Login({ I }) {
    return (
        <div className="App">
            <header className="App-header">
                <a href={"https://github.com/jacoby149/web10"}>
                    <img src={logo} className="App-logo" alt="logo" />
                </a>
                <p>
                    Welcome to the <code>web10</code> network.
                </p>
                <a
                    className="App-link"
                    href={I.loginURL}
                >
                    Log in
                </a>
                <p className="help is-success">{I.message}</p>

            </header>
        </div>
    );
}

export default Login;