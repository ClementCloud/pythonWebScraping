import urllib.request
import re
import sys

web_page = 'https://www.randomlists.com/email-addresses'

with urllib.request.urlopen(web_page) as response:
    page_bytes = response.read()
the_page = str(page_bytes.decode('utf-8'))

email_pattern = re.compile("[-a-zA-z0-9._]+@[-a-zA-z0-9._]+.[-a-zA-z0-9._]")

emails =re.findall(email_pattern, the_page)

with open('readme.txt', 'w') as f:
    f.write(the_page)
print(emails)

