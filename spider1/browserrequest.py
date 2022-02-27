# Use the Request library
import requests

# Set the target website
url = 'http://192.168.1.223/varsity/'
r = requests.get(url)
# This will get the full page
print(r.text)
# This will get the status code
print("Status code:")
print('\t*', r.status_code)

# This will just get the headers
h = requests.head(url)
print("Header:")
print("********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
    print("*********")
# This will modify the headers user-agent
headers = {
    'User-Agent' : 'mobile'
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)