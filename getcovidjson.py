 # -*- coding: UTF-8 -*- #

from bs4 import BeautifulSoup
import requests
import json


"""Table Data To List.

    Args:
        table: bs4 element Tag.

    Returns:
        A list of key:value pairs in the form of a json array.

"""
def tableDataToList(table):       
    i = 0
    rows = []
    trs = tableBody.find_all('tr')
    for tr in trs[1:-1]:
        kvpair = {}
        for td in tr.find_all('td'):
            if i%2 == 0:
                kvpair['location'] = td.get_text(strip=True)
            else:
                kvpair['cases'] = int(td.get_text(strip=True).replace(",", ""))
            i+=1
        rows.append(kvpair)
    return rows

page = requests.get('https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert/coronavirus-covid-19-current-situation-and-case-numbers')
pageContent = BeautifulSoup(page.content, 'html.parser')    # Parse the page throuh
tableBody = pageContent.find('tbody')                       # Strip thr table body out

'''
Testing statements including some json testing
'''
list_table = tableDataToList(tableBody)
# print(list_table[:2])
# print(list_table)
print(json.dumps(list_table, indent=3))
#print(json.dumps(list_table[:1], indent=3))