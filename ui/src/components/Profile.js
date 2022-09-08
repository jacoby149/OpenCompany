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
                <a
                    href={"https://github.com/jacoby149/web10"}
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    <img src={logo} className="App-logo" alt="logo" />
                </a>
                <p>
                    Welcome <code>{profile["login"]}</code>
                    <br></br>
                    Rank : <code>{I.ranks[profile["rank"]]["name"]}</code>
                </p>
                <img style={{ margin: "20px" }} src={profile["avatar_url"]} width={"64px"}></img>
                <p>
                    Merged Commits : {I.mergedCommits(profile["email"])}
                    <br></br>
                    Commits Necessary : {I.neededCommits()}</p>
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
    const [inputValue, setInputValue] = React.useState('')
    const [timer, setTimer] = React.useState(null)
    const inputChanged = e => {
        setInputValue(e.target.value)
        clearTimeout(timer)
        const Api = () => I.getMentor(e.target.value);
        const newTimer = setTimeout(() => {
            Api()
        }, 500)

        setTimer(newTimer)
    }
    const validMentor = I.readToken()["rank"] < I.mentor["rank"];
    return (
        <div className="App">
            <header className="App-header">
                <a
                    href={"https://github.com/jacoby149/web10"}
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    <img src={logo} className="App-logo" alt="logo" />
                </a>
                <div>
                    Current Rank :<code>{I.ranks[profile["rank"]]["name"]}</code>
                    <br></br>
                    Promotion Rank :<code>{I.ranks[profile["rank"] + 1]["name"]}</code>
                    <br></br><br></br>
                    Enter the GH of your mentor :<br></br>
                    <input
                        className="input"
                        value={inputValue}
                        type="text"
                        onChange={inputChanged}
                        style={{ margin: "5px", backgroundColor: "black", color: "orange" }}
                    >
                    </input>
                    <p className={validMentor?"help is-success":"help is-danger"}>
                        This is {validMentor?"":"NOT"} a valid mentor above your rank : @{I.mentor["login"]} <img src={I.mentor["avatar_url"]} width={"12px"}></img>
                    </p>
                    <button
                        className="button is-light"
                        style={{ marginTop: "10px", marginBottom: "5px" }}
                        disabled={!validMentor}>
                        Get Promoted
                    </button>
                </div>
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