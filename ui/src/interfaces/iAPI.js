import React from 'react';
import { useSearchParams } from 'react-router-dom';

function useAPI() {
    const AI = {};
    [AI.searchParams, AI.setSearchParams] = useSearchParams();
    [AI.loginURL, AI.setLoginURL] = React.useState(null);
    [AI.ranks, AI.setRanks] = React.useState(null);
    [AI.token, AI.setToken] = React.useState(null);
    [AI.message, AI.setMessage] = React.useState("");
    [AI.contributors, AI.setContributors] = React.useState({});

    React.useEffect(() => {
        fetch("http://api.localhost/login_url")
            .then((r) => r.json().then(AI.setLoginURL)
            );
        fetch("http://api.localhost/ranks")
            .then((r) => r.json().then(AI.setRanks)
            );
        fetch("http://api.localhost/contributors")
            .then((r) => r.json().then(AI.setContributors)
            );
    }, []);

    AI.tryLogin = function () {
        const code = AI.searchParams.get("code")
        if (code) {
            AI.setMessage("logging in ...")
            fetch(`http://api.localhost/login?code=${code}`)
                .then((r) => {
                    r.json().then((t) => {
                        AI.setToken(t);
                        AI.setMessage("")
                        AI.searchParams.delete("code")
                        AI.setSearchParams(AI.searchParams)
                    });
                })
        }
    }

    AI.logOut = function () {
        AI.setToken(null);
    }

    AI.readToken = function () {
        if (!AI.token) return AI.token;
        return JSON.parse(atob(AI.token.split(".")[1]));
    }

    AI.neededCommits = function () {
        return AI.ranks[AI.readToken()["rank"] + 1]["min_commits"];
    }

    AI.mergedCommits = function (email){
        return email in AI.contributors ? AI.contributors[email] : 0;
    }

    AI.promoteable = function(email){
        return AI.mergedCommits(email) >= AI.neededCommits()
    }

    return AI;
}

export { useAPI };