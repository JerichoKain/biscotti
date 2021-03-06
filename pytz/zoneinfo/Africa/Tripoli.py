'''tzinfo timezone information for Africa/Tripoli.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Tripoli(DstTzInfo):
    '''Africa/Tripoli timezone definition. See datetime.tzinfo for details'''

    zone = 'Africa/Tripoli'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1919,12,31,23,7,16),
d(1951,10,14,1,0,0),
d(1951,12,31,22,0,0),
d(1953,10,9,1,0,0),
d(1953,12,31,22,0,0),
d(1955,9,29,23,0,0),
d(1955,12,31,22,0,0),
d(1958,12,31,23,0,0),
d(1981,12,31,22,0,0),
d(1982,3,31,23,0,0),
d(1982,9,30,22,0,0),
d(1983,3,31,23,0,0),
d(1983,9,30,22,0,0),
d(1984,3,31,23,0,0),
d(1984,9,30,22,0,0),
d(1985,4,5,23,0,0),
d(1985,9,30,22,0,0),
d(1986,4,3,23,0,0),
d(1986,10,2,22,0,0),
d(1987,3,31,23,0,0),
d(1987,9,30,22,0,0),
d(1988,3,31,23,0,0),
d(1988,9,30,22,0,0),
d(1989,3,31,23,0,0),
d(1989,9,30,22,0,0),
d(1990,5,3,23,0,0),
d(1996,9,29,22,0,0),
d(1997,4,3,23,0,0),
d(1997,10,3,22,0,0),
        ]

    _transition_info = [
i(3180,0,'LMT'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,0,'EET'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(3600,0,'CET'),
i(7200,0,'EET'),
i(3600,0,'CET'),
i(7200,3600,'CEST'),
i(7200,0,'EET'),
        ]

Tripoli = Tripoli()

