__author__ = 'jouke-bouwe'

from  MiniprojectProgrammerenWeek3 import FilmsOphalen

FilmsOphalen.getJaartal()

if jaar <= 1969:
    aanbieder = "Kevin"
elif jaar >= 1970 <= 1989:
    aanbieder = "Frank"
elif jaar >= 1990 <= 1999:
    aanbieder = "Bram"
elif jaar >= 2000 <= 2009:
    aanbieder = "Jouke-Bouwe"
elif jaar >= 2010:
    aanbieder = "Ricardo"