import requests
names = []
values = []

getLocal = requests.get("http://api.open-notify.org/iss-now")
getNumber = requests.get("http://api.open-notify.org/astros")

dataN = getNumber.json()
dataP = dataN['people']
for bio in dataP:
    names.append(bio['name'])
    

dataLocal =getLocal.json()
data_pos = dataLocal['iss_position']
for datas in data_pos:
    values.append(data_pos[datas])

print("The longitude of the ISS is now: "+values[0]+" while the latitude is: "+values[1])
print("They are currently "+ str(len(names))+" in the ISS")
print(names)
