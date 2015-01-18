"""
This script should get the meaningful content from a given url and outputs it to 
stdout as html

Note: This code was originally written specifically to run on the following url:
	https://github.com/angrave/SystemProgramming/wiki
"""

from bs4 import BeautifulSoup
import urllib.request as urlreq
import sys, os
sys.path.append(os.getcwd())
import user_defined_parameters as params

# I was unsure how to parse a parameter list, so posted to Stack Overflow,
# and got this answer, which I packaged into a function called function_parser:
# http://stackoverflow.com/questions/27914657/
#  parameter-list-with-variable-types-python-3
def function_parser(param_list):
	kwargs = {}
	args = []
	for i in param_list:
		parts = i.split('=')
		if len(parts) > 1:
			kwargs[parts[0].strip()] = parts[1].strip()
		else:
			args.append(parts[0].strip())
	return (args, kwargs) # returns a tuple of type as such: ([], {})

url = params.url
page = urlreq.urlopen(url)
pageHtml = page.read()
page.close()

soup = BeautifulSoup(pageHtml)

ret_params = function_parser(params.header_list)
header = soup.find(*ret_params[0], **ret_params[1])

ret_params = function_parser(params.content_list)
content = soup.find_all(*ret_params[0], **ret_params[1])

print(header) # important for Table of Contents functionality

# If there are style sheets, import them:
for css in soup.find_all("link"):
	href = css["href"]
	if href[len(href)-4:] == ".css":
		print(css)

# The following outputs all the html in "content", the content that fits the
# parameters of what the user wants to find useful on the page.
for tags in content:
	print(tags.prettify())