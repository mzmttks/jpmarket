import jpmarket
from datetime import datetime

start = datetime(2013, 1, 1)
end = datetime(2013, 1, 10)

print jpmarket.DataReader(7203, 'yahoojp', start, end)
print jpmarket.DataReader(9999, 'yahoo', start, end)
