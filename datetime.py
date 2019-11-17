from datetime import datetime, date, time

dt_object = datetime.now()
print(dt_object)

n_format = dt_object.strftime('%d/%m/%Y %H:%M:%S')
print(n_format)

date_ = date.today()
print(date_)
print('%d/%d/%d' % (date_.day, date_.month, date_.year))

t1_i = date(year = 2018, month = 12, day = 12)
t2_f = date(year = 2018, month = 12, day = 23)
t3 = t2_f - t1_i
tn = t3.days
print(type(tn))
print(tn)

#print(dir(datetime))
#print(dir(date))
#print(dir(time))