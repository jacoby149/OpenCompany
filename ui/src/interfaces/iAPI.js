import React from 'react';
import {useSearchParams} from 'react-router-dom';

function useAPI(){
    const AI = {};
    [AI.searchParams, AI.setSearchParams] = useSearchParams();
    [AI.loginURL, AI.setLoginURL] = React.useState(null);
    [AI.token, AI.setToken] = React.useState(null);
    [AI.message,AI.setMessage] = React.useState("")

    React.useEffect(() => {
      fetch("http://api.localhost/login_url")
        .then((r) => r.json().then(AI.setLoginURL)
        )
    }, []);

    AI.tryLogin = function(){
        const code = AI.searchParams.get("code")
        if (code) {
            AI.setMessage("logging in ...")
            fetch(`http://api.localhost/login?code=${code}`)
            .then((r) => {
                r.json().then((t)=>{
                    AI.setToken(t);
                    AI.setMessage("")
                    AI.searchParams.delete("code")
                    AI.setSearchParams(AI.searchParams)
                });
            })    
        }
    }

    AI.logOut = function(){
        AI.setToken(null);
    }

    AI.readToken = function(){
        if (!AI.token) return AI.token;
        return JSON.parse(atob(AI.token.split(".")[1]));
    }

    return AI;
}

export {useAPI};