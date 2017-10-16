# find the greatest number of total and its week
import datetime

index = 0
tal_ = 0
wek_ = ''

d3 = [
      {
        "days": [
          0,
          0,
          0,
          1,
          2,
          0,
          0
        ],
        "total": 3,
        "week": 1476576000
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          3,
          0,
          0
        ],
        "total": 3,
        "week": 1477180800
      },
      {
        "days": [
          0,
          0,
          0,
          1,
          0,
          2,
          0
        ],
        "total": 3,
        "week": 1477785600
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1478390400
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1478995200
      },
      {
        "days": [
          0,
          1,
          2,
          0,
          0,
          0,
          0
        ],
        "total": 3,
        "week": 1479600000
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1480204800
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1480809600
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1481414400
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1482019200
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1482624000
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          2,
          0
        ],
        "total": 2,
        "week": 1483228800
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1483833600
      },
      {
        "days": [
          0,
          0,
          0,
          2,
          0,
          4,
          0
        ],
        "total": 6,
        "week": 1484438400
      },
      {
        "days": [
          0,
          2,
          0,
          0,
          4,
          0,
          2
        ],
        "total": 8,
        "week": 1485043200
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1485648000
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1486252800
      },
      {
        "days": [
          0,
          0,
          0,
          1,
          0,
          0,
          2
        ],
        "total": 3,
        "week": 1486857600
      },
      {
        "days": [
          4,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 4,
        "week": 1487462400
      },
      {
        "days": [
          0,
          0,
          2,
          0,
          2,
          0,
          0
        ],
        "total": 4,
        "week": 1488067200
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          2,
          0
        ],
        "total": 2,
        "week": 1488672000
      },
      {
        "days": [
          0,
          2,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 2,
        "week": 1489276800
      },
      {
        "days": [
          0,
          0,
          0,
          1,
          0,
          2,
          0
        ],
        "total": 3,
        "week": 1489881600
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1490486400
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1491091200
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          2,
          0
        ],
        "total": 2,
        "week": 1491696000
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1492300800
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1492905600
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1493510400
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1494115200
      },
      {
        "days": [
          0,
          2,
          2,
          0,
          0,
          0,
          0
        ],
        "total": 4,
        "week": 1494720000
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1495324800
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1495929600
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1496534400
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1497139200
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1497744000
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1498348800
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          2,
          1
        ],
        "total": 3,
        "week": 1498953600
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          2,
          0
        ],
        "total": 2,
        "week": 1499558400
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1500163200
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1500768000
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1501372800
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1501977600
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1502582400
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1503187200
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          3
        ],
        "total": 3,
        "week": 1503792000
      },
      {
        "days": [
          2,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 2,
        "week": 1504396800
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1505001600
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1505606400
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1506211200
      },
      {
        "days": [
          0,
          0,
          2,
          0,
          0,
          0,
          0
        ],
        "total": 2,
        "week": 1506816000
      },
      {
        "days": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": 0,
        "week": 1507420800
      }
    ]

for i in range(0, len(d3)):
    if d3[i]['total'] > tal_:
        tal_ = d3[i]['total']
        wek_ = d3[i]['week']
        index = i

print(f"Time start: {datetime.datetime.fromtimestamp(int(d3[0]['week'])).strftime('%Y-%m-%d %H:%M:%S')} to",'\n')
print(f"Time end: {datetime.datetime.fromtimestamp(int(d3[51]['week'])).strftime('%Y-%m-%d %H:%M:%S')}",'\n')
print(f"The greatest number of total is: {tal_}",'\n')
print(f"It was week {datetime.datetime.fromtimestamp(int(wek_)).strftime('%Y-%m-%d %H:%M:%S')}. The {index + 1}th week.",'\n')

print("Details: ")
print("Commits: ",d3[int(index)]['days'])
print("Total: ",d3[int(index)]['total'])
print("Week: ",d3[int(index)]['week'])
