import requests

TARGET_URL = 'https://login.etadirect.com/'

PAYLOAD = {
    'organization': 'metronet',
    'username': 'mcarpenter',
    'password': 'Peril1981'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    r = s.post(TARGET_URL, data=PAYLOAD)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print r.text

print ""
print "Status Code: " + str(r.status_code)
print "Content Type: " + r.headers['content-type']
print "Encoding: " + r.encoding

"""
print ""
print "Source: \n" + r.text
print ""
"""
