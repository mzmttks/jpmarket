jpmarket
===============

Pandas DataReader extension for Japanese market data.

Pandas の DataReader で日本の市場データを読めるようにした拡張。


* Supported sources
  * yahoo ファイナンス
  * [Not Yet] Ullet 企業情報

Sample code
===========
import jpmarket
from datetime import datetime

start = datetime(2013, 1, 1)
end = datetime(2013, 1, 10)

print jpmarket.DataReader(7203, 'yahoojp', start, end)

* Dependent packages
  * jsm
  * lxml


Changelog
---------
2014.9.25 Create a repository


Author
------
@mzmttks
