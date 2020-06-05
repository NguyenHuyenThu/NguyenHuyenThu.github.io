from operator import itemgetter
from itertools import groupby

rows = [ 
    {'address': '5412 N CLARK', 'date': '04/02/2012'},
    {'address': '5412 N CLARK', 'date': '07/07/2043'},
    {'address': '5412 N CLARK', 'date': '05/04/2086'},
    {'address': '5412 N CLARK', 'date': '01/05/2012'},
    {'address': '5412 N CLARK', 'date': '12/02/2015'}
    ]

rows.sort(key = itemgetter('date'))

data = groupby(rows, key = itemgetter('date'))

for date, items in data:
    print(date)
    for i in items:
        print(i)


# ------------------------- using defaultdict

from colections import defaultdict

row_by_date = defaultdict(list)

for row in rows:
    row_by_date[row['date']].append(row)

