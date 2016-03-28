#!/usr/bin/python

import mysql.connector
import json

cnx = mysql.connector.connect(user='root', password='admin', database='d3')
cursor = cnx.cursor()
query = ("select * from country_name_code_lat_long_diabetespercentage_incomegroup where diabetes_percentage is not null;")
cursor.execute(query)

entries = []

fill_dict = {
    "Low income" : 'L',
    "Lower middle income" : "LM",
    "Upper middle income" : "UM",
    "High income: nonOECD" : "HIN",
    "High income: OECD" : "HIO"
}

for (country_name, country_code, latitude, longitude, dp, ig) in cursor:
    entry = {}
    entry['name'] = country_name + " diabetes " + str(dp) + "%"
    entry['latitude'] = float(latitude)
    entry['longitude'] = float(longitude)
    entry['radius'] = (float(dp) / 40) * 50
    entry['fillKey'] = ig
    entries.append(entry)

print "imported_data = ", json.dumps(entries, sort_keys=True, indent=4, separators=(',', ': ')), ";"

