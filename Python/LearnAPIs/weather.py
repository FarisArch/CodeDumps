import requests

key = 'b45f1d386764484b8a0b0c3673786ee7'

def weather(postalCode,*countrycode):
    if len(countrycode) == 1:
        for code in countrycode:
            country = code
        
        web = requests.get('https://api.weatherbit.io/v2.0/current?&postal_code='+str(postalCode)+'&country='+country+'&key='+key)
        try:
            datas = web.json()
            stats = datas['data']

            for stat in stats:
                city_name = stat['city_name']
                temperature = stat['app_temp']
                pod = stat['pod']
                rh = stat['rh']
                timeObsv = stat['ob_time']

            secondaryData = stat['weather']
            descrip = secondaryData['description']

            if pod == "n":
                pod = "night time"
            else:
                pod = "day time"

            result = (f" In the city of {city_name}\n Temperature is {temperature}\n It is currently {descrip}\n It is {pod} \n The humidity is {rh}\n Observed at {timeObsv} ")
            return result
        except:
            raise ValueError ("Not a valid country!")

    else:
        return None
print(weather(62050,"MY"))