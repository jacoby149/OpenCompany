import React from 'react';
import logo from '../web10.png';
import discord from '../discord.png';

function Profile({ profile, I }) {
    const [mode, setMode] = React.useState("user");
    return (

        mode === "user" ?
            <UserInfo profile={profile} I={I} setMode={setMode} /> :
            <PromoInfo profile={profile} I={I} setMode={setMode} />
    );
}

function UserInfo({ profile, I, setMode }) {
    return (
        <div className="App">
            <header className="App-header">
                <a
                    className="App-link"

                    style={{ top: "5px", right: "5px", position: "absolute" }}
                    href={""}
                    onClick={I.logOut}
                >
                    Log Out
                </a>                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Welcome <code>{profile["login"]}</code>.
                    <br></br>
                    Rank : <code>{"assistant"}</code>
                </p>
                <img src={profile["avatar_url"]} width={"64px"}></img>
                <p>
                    Merged Commits : 12
                    <br></br>
                    Commits Until Promotion : 10</p>
                <a
                    className="App-link"
                    onClick={() => setMode("promotion")}
                >
                    Eligible for Promotion!
                </a>
                <a href={""} style={{ margin: "20px" }} className="App-link">
                    <img height={"16px"} src={discord}></img>
                </a>

            </header>
        </div >
    )
}

function PromoInfo({ profile, I, setMode }) {
    return (
        <div className="App">
            <header className="App-header">
                <a
                    className="App-link"

                    style={{ top: "5px", right: "5px", position: "absolute" }}
                    href={""}
                    onClick={I.logOut}
                >
                    Log Out
                </a>                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Current Rank : <code>{"assistant"}</code>
                    <br></br>
                    Rank After Promotion : <code>{"intern"}</code>.
                    <br></br><br></br>
                    github handle of your mentor :<br></br>
                    <input style={{ backgroundColor: "black", color: "orange" }}></input>
                    <br></br><br></br>
                    <button style={{marginTop:"10px",marginBottom:"5px"}}>Get Promoted By</button><br></br> @jacoby149 <img src={profile["avatar_url"]} width={"16px"}></img>
                </p>
                <a
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