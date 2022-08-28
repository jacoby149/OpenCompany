import React from 'react';
import logo from '../web10.png';
import discord from '../discord.png';

function Profile({ profile, I }) {
    const [mode, setMode] = React.useState("user");
    return (
        <div>
            <a
                className="App-link"

                style={{ top: "5px", right: "5px", position: "absolute" }}
                href={""}
                onClick={I.logOut}
            >
                <code className="App-link"><u>Log Out</u></code>
            </a>
            {
                mode === "user" ?
                    <UserInfo profile={profile} I={I} setMode={setMode} /> :
                    <PromoInfo profile={profile} I={I} setMode={setMode} />}
        </div>);
}

function UserInfo({ profile, I, setMode }) {
    return (
        <div className="App">
            <header className="App-header">
                <a href={"https://github.com/jacoby149/web10"}>
                    <img src={logo} className="App-logo" alt="logo" />
                </a>
                <p>
                    Welcome <code>{profile["login"]}</code>
                    <br></br>
                    Rank : <code>{"assistant"}</code>
                </p>
                <img style={{ margin: "20px" }} src={profile["avatar_url"]} width={"64px"}></img>
                <p>
                    Merged Commits : 12
                    <br></br>
                    Commits Necessary : 10</p>
                <a
                    className="App-link"
                    onClick={() => setMode("promotion")}
                >
                    Eligible for Promotion!
                </a>
                <a
                    href={"https://discord.gg/Dbd4VEDznU"}
                    style={{ margin: "20px" }}
                    className="App-link"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    <img width={"160px"} src={discord}></img>
                </a>

            </header>
        </div >
    )
}

function PromoInfo({ profile, I, setMode }) {
    return (
        <div className="App">
            <header className="App-header">
                <a href={"https://github.com/jacoby149/web10"}>
                    <img src={logo} className="App-logo" alt="logo" />
                </a>
                <p>
                    Current Rank : <code>{"assistant"}</code>
                    <br></br>
                    Rank After Promotion : <code>{"intern"}</code>
                    <br></br><br></br>
                    Enter the GH of your mentor :<br></br>
                    <input className="input" type="text" style={{ margin: "5px", backgroundColor: "black", color: "orange" }}></input>
                    <p class="help is-success">This is a valid mentor above your rank : @jacoby149 <img src={profile["avatar_url"]} width={"12px"}></img></p>
                    <button className="button is-light" style={{ marginTop: "10px", marginBottom: "5px" }}>Get Promoted</button>
                </p>
                <a style={{ margin: "10px" }}
                    className="App-link"
                    onClick={() => setMode("user")}
                >
                    Go Back
                </a>

            </header>
        </div >

    )
}


export default Profile;