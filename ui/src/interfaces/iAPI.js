import React from 'react';
import { useSearchParams } from 'react-router-dom';
import axios from 'axios'

function useAPI(APIURL) {
    const AI = {};
    [AI.searchParams, AI.setSearchParams] = useSearchParams();
    [AI.loginURL, AI.setLoginURL] = React.useState(null);
    [AI.ranks, AI.setRanks] = React.useState(null);
    [AI.token, AI.setToken] = React.useState(null);
    [AI.message, AI.setMessage] = React.useState({text:"",color:"success"});
    [AI.contributors, AI.setContributors] = React.useState({});
    [AI.mentor, AI.setMentor] = React.useState({});

    React.useEffect(() => {
        axios.get(`${APIURL}/login_url`)
            .then((r) => {AI.setLoginURL(r.data)}
            );
        axios.get(`${APIURL}/ranks`)
            .then((r) => AI.setRanks(r.data)
            );
        axios.get(`${APIURL}/contributors`)
            .then((r) => AI.setContributors(r.data)
            );
    }, [AI.token]);

    AI.tryLogin = function () {
        const code = AI.searchParams.get("code")
        if (code) {
            AI.setMessage({text:"logging in ...",color:"success"})
            axios.get(`${APIURL}/login?code=${code}`)
                .then((r) => {
                        AI.setToken(r.data);
                        AI.setMessage("")
                        AI.searchParams.delete("code")
                        AI.setSearchParams(AI.searchParams)
                }).catch((r)=>{
                    console.log(r)
                    AI.setMessage(
                        {
                            text:"In order to log in, you must star",
                            color:"danger",
                            star:r.response.data.detail})
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

    AI.mergedCommits = function (email) {
        return email in AI.contributors ? AI.contributors[email] : 0;
    }

    AI.isPromoteable = function (email) {
        return AI.mergedCommits(email) >= AI.neededCommits()
    }

    AI.promote = function (username) {
        const data = {
            "mentor_node_id": AI.mentor["node_id"],
            "my_node_id": AI.readToken()["node_id"]
        }
        axios.post(`${APIURL}/promote`, data).then((r) => window.open("/"))
    }

    AI.getMentor = function (username) {
        const data = {
            "mentor_username": username,
            "gh_tok": AI.readToken()["token"],
            "my_node_id": AI.readToken()["node_id"]
        }
        console.log(data)
        axios.post(`${APIURL}/mentor`, data).then((r) => AI.setMentor(r.data))
    }

    //TODO pull it out of AI.ranks
    AI.maxRank = function () {
        return AI.readToken()["rank"] >= 5
    }

    return AI;
}

export { useAPI };