import re


def findEmailDomain(address):
   result = re.search(r'(\w+(-|\.)?\w+\.\w+|\w+)$', address)
   return result.group(0)


address = "example-indeed@strange-example.com"
# address = "<>[]:,;@"!  \# $%&*+-/=?^_{}| ~.a"@example.org"
print(findEmailDomain(address)) 
# = "example.org"
