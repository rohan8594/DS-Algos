import urllib
import json


def getCountries(s, p):
    count = 0
    url = "https://jsonmock.hackerrank.com/api/countries/search?name=" + s
    res = urllib.request.urlopen(url)
    content = json.loads(res.read())
    pages = content['total_pages']

    for pageno in range(1, pages + 1):
        url = "https://jsonmock.hackerrank.com/api/countries/search?name=" + \
            s + "&page=" + str(pageno)
        content = json.loads(urllib.request.urlopen(url).read())

        for i in range(len(content['data'])):
            data = content['data'][i]
            popul = data['population']
            if popul > p:
                count += 1
    return count
