Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5
>>> 10 / 3
3
>>> 10 // 3
3
>>> print('Mijn naam is Aidan')
Mijn naam is Aidan
>>> naam = 'Aidan'
>>> print(naam)
Aidan
>>> print(naam.upper())
AIDAN
>>> print(naam[0:2])
Ai
>>> print(naam[::-1])
nadiA
>>> leeftijd = 16
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Aidan ben je al 16 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
17
>>> leeftijd-=1
>>> leeftijd
16
>>>if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
Over 2 jaar wordt je 18
>>>else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')
Je bent precies 16 jaar
>>> from random import randint
>>> randint(0,1000)
825
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
885
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 885
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-09 11:57:21.984000
>>> datum.strftime('%A %d %B %Y')
'Wednesday 09 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    locale.setlocale(locale.LC_TIME, 'nl_NL')
  File "C:\Python27\lib\locale.py", line 581, in setlocale
    return _setlocale(category, locale)
Error: unsupported locale setting
>>> datum.strftime('%A %d %B %Y')
'Wednesday 09 September 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    locale.setlocale(locale.LC_TIME, 'it_IT')
  File "C:\Python27\lib\locale.py", line 581, in setlocale
    return _setlocale(category, locale)
Error: unsupported locale setting
>>> datum.strftime('%A %d %B %Y')
'Wednesday 09 September 2020'
>>>
