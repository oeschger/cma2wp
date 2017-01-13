import xml.etree.ElementTree as ET
import os.path
import urllib, json
import requests

# access_key   = 'dXJiYW5jb2RlOmpsZHNhZmphMzI0NzA5ZCUoeCMwNGsxazIxM2NramRmbGtqMzkzMjA4MzA0ago='
# access_url   = 'https://www.ibm.com/developerworks/dwwi/jsp/getaccesstoken.jsp'
# access_resp  = requests.post(access_url,
#                             headers={'Authorization': 'Basic ' + access_key})
# access_token = access_resp.json()['access_token']

access_token = 'b489d9b9ebb56b7f045cb5b72fb25f98a82377ec81725b9de49c937a1a82a27e5a1f70eb36c8dfa29376b003eb430c0309e9d559f3381d2fe895a4a9befd5359e71929154c77f504fa03b7582f139bd139002f228e618b3edc8d5767b5e155314cedca28777d6888dc80cf333bbd30d6a88d288427850afce1b49db31bc2e09256935310eb8db5db78f82d7da7885f2fb4a6167c191a855135008992eece46e521bd6b65347e9e07'

# post_url     = 'https://developer.ibm.com/dw/wp-json/posts?token='+access_token
post_url     = 'https://nextstage.torolab.ibm.com/dw/wp-json/posts?token='+access_token

print "creating post at " + post_url + " ..."

post_body = {
    "title":"Hello CMA content!",
    "content_raw":"Can put XML content here",
    "excerpt_raw":"CMA article goodness"
    }

post_resp = requests.post(post_url,
                          data=json.dumps(post_body),
                          headers={'Accept':'application/json','Content-Type': 'application/json'})

print post_resp.status_code


# article = 'C:\Users\IBM_ADMIN\Downloads\IoT-Articles\iot-blockchain-sharing-economy\index.xml'





# tree = ET.parse(article)
# root = tree.getroot()
# docb = root.findall('dw-article')[0].findall('docbody')[0]

# remove the docbody surrounding and then
# print ET.tostring(docb)
