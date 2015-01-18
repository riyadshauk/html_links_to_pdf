"""
This script should get the meaningful links from the site

Note: This code was originally written specifically to run on the following url:
	https://github.com/angrave/SystemProgramming/wiki
"""

from bs4 import BeautifulSoup as bs
import urllib.request as urlreq
import sys, os
sys.path.append(os.getcwd())
import user_defined_parameters as params

url = params.url
page = urlreq.urlopen(url)
pageHtml = page.read()
page.close()

url_dn_cnt = 0
dist_from_period = 0
for c in params.url:
	if dist_from_period > 0:
		if c is "/":
			break
	if c is ".":
		dist_from_period += 1
	url_dn_cnt += 1
# This prefixes the rest of the url (e.g.: "https://dn.com" before any slashes):
url_dn = params.url[:url_dn_cnt]

soup = bs(pageHtml)
pageLinks = soup.find_all(params.links_list)
for link in pageLinks:
	sys.stdout.write(url_dn + link.get("href") + "\n")