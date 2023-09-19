from collections import Counter
from pprint import pprint

import readrides

rows = readrides.read_rides_as_dictionaries('Data/ctabus.csv')

print('Number of bus routes in Chicago:', len({r['route'] for r in rows}))

rides = Counter()

for r in rows:
	rides[(r['route'], r['date'])] = r['rides']

print('Number of people who rode the 22 bus on 2nd Feb 2011:', rides['22', '02/02/2011'])
print('Number of people who rode the 4 bus on 1st Feb 2011:', rides['4', '02/01/2011'])


routes = Counter()
for r in rows:
	routes[r['route']] += r['rides']
print('Total of bus rides for each route:')
pprint(routes)

routes_2001 = Counter()
routes_2011 = Counter()
for r in rows:
    year = r['date'][-4:]
    if year == '2001':
        routes_2001[r['route']] += r['rides']
    elif year == '2011':
  	    routes_2011[r['route']] += r['rides']
print('Five bus routes which had the most ten-year increase in ridership from 2001 to 2011:')
pprint((routes_2011 - routes_2001).most_common(5))