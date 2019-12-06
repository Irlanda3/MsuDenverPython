'''cgi common gateway interface
beautiful soup es nada mas para html
* madisdata.py in jupiter
https://madis-data.ncep.noaa.gov/madisPublic1/cgi-bin/madisXmlPublicDir
cuando abras el jupyter en la mac  ponle https://mth290b.msudenver.edu
la b' antes de terminar es que esta en bytes
'''

import urllib.request
import urllib.parse

# todo antes del ?
url = "https://madis-data.ncep.noaa.gov/madisPublic1/cgi-bin/madisXmlPublicDir"
# lo q esta despues del question mark se necesita construir

# list of tuples
values = [
    ("rdr", " "),
    ("time", 0),
    ("minbck", -59),
    ("minfwd", 0),
    ("recwin", 3),
    ("dfltrsel", 2),
    ("state", "CO"),
    ("latll", 0.0),
    ("lonll", 0.0),
    ("latur", 90.0),
    ("lonur", 0.0),
    ("stanam", " "),
    ("stasel", 0),
    ("pvdrsel", 0),
    ("varsel", 1),
    ("qctype", 0),
    ("qcsel", 1),
    ("xml", 0),
    ("csvmiss", 0),
    ("nvars", "T"),
    ("nvars", "P"),
]

# create the url based on values
data = urllib.parse.urlencode(values)
data = data.encode("ascii")

# fetch the webssite using the cgi data
with urllib.request.urlopen(url, data)as response:
    page = response.readlines()

print(page)
