from rauth import OAuth2Service

yahoo = OAuth2Service(
    client_id = 'dj0yJmk9aVdFSzBVRW9aSlNPJmQ9WVdrOWRuUmhRVm8xTXpRbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1iNQ--',
    client_secret ='9438c2f7462ee9481869668faaeec29ea749cf8e'
    name = 'yahoo'
    authorize_url = 'https://api.login.yahoo.com/oauth2/request_auth'
    access_token_url = 'https://api.login.yahoo.com/oauth2/get_token'
    base_url= 'https://fantasysports.yahooapis.com/')
