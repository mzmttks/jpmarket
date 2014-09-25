import jpmarket
from tests import CODES

def test_get():
    print jpmarket.DataReader(CODES[0], 'yahoojp')
