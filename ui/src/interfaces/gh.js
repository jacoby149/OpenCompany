import React from 'react';
import {useSearchParams} from 'react-router-dom';

function useGit(){
    const GI = {};
    [GI.searchParams, GI.setSearchParams] = useSearchParams();
    [GI.loginURL, GI.setLoginURL] = React.useState(null);
    [GI.token, GI.setToken] = React.useState(null);

    React.useEffect(() => {
      fetch("http://api.localhost/login_url")
        .then((r) => r.json().then(GI.setLoginURL)
        )
    }, []);

    GI.tryLogin = function(){
        const code = GI.searchParams.get("code")
        if (code) {
            fetch(`http://api.localhost/get_token?code=${code}`)
            .then((r) => {
                r.json().then((t)=>{
                    GI.setToken(t);
                    GI.searchParams.delete("code")
                    GI.setSearchParams(GI.searchParams)
                });
            })    
        }
    }

    return GI;
}

export {useGit};