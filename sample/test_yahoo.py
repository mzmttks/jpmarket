import jpmarket
from datetime import datetime

start = datetime(2013, 1, 1)
end = datetime(2013, 1, 10)
print "7203"
print jpmarket.DataReader(7203, 'yahoojp', start, end)
print "9999 (error)"
print jpmarket.DataReader(9999, 'yahoo', start, end)


# inquiry 
start = datetime(2009, 3, 25)
end = datetime(2009, 4, 23)
print "1617"
print jpmarket.DataReader(1617, 'yahoojp', start, end)
print "1618"
print jpmarket.DataReader(1618, 'yahoojp', start, end)
