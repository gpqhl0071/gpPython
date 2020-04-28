import requests
import json
import nexusUtil

r = nexusUtil.requestNexus('dx-web')
j = json.loads(r.text)
print(j)