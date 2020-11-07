import requests


url = 'http://httpbin.org/'
data={"mm":"123","gg":"sjndsf"}
ff={"yet":"1", "another":45}

response=requests.get(url, data= data, params=ff, auth=requests.auth.HTTPProxyAuth("mm","ll"), headers={"Authorization": "Basic dkdskfjd"},verify=False)

print (response.request.headers)

print (response.request.body)
