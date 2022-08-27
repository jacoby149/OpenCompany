import React from 'react';
import logo from '../web10.png';

function Profile({profile}) {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Welcome {profile["login"]} to the <code>web10</code> network.
                </p>
                <img src={profile["avatar_url"]} width={"100px"}></img>
                <p>Rank : web10 {"Assistant"}<br></br>Merged Commits : 5</p>
                <a
                    className="App-link"
                    href={"promote"}
                >
                    Eligible for Promotion!
                </a>
            </header>
        </div>
    );
}

export default Profile;