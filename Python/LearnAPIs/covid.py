import requests

def covid(yourcountry):
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":yourcountry}

    headers = {
        'x-rapidapi-key': "26f03295acmsh53d5b432fb58d5dp1e935fjsn926de1a3a282",
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    log = response.json()
    datas = log['data']
    stats = datas['covid19Stats']

    deaths = 0
    confirmed = 0
    recovered = 0

    for stat in stats:
        deaths += stat['deaths']
    for stat in stats:
        confirmed += stat['confirmed']

    for stat in stats:
        try:
            recovered += stat['recovered']
        except TypeError:
             continue

    country = yourcountry
    confirmedCases = confirmed
    deathCases = deaths
    recoveredCases = recovered

    return(print(f"Country : {country}\nConfirmed Cases : {confirmedCases}\nDeath : {deathCases}\nRecovered : {recoveredCases}"))
covid("Nigeria")