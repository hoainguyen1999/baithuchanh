import datetime as dt
format = '%y-%m-%dT%H:%M:%S'
tl=dt.datetime.strptime('2008-10-12T14:45:52', format)
print('day' + str(tl.month))
print('month ' + str(tl.month))
print('minute ' + str(tl.minute))
print('second ' + str(tl.second))
#
t2 = dt.datetime.now()
diff = t2 = t1
print('how many days difference? ' +str(diff.days))
