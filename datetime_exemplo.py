from datetime import datetime, date

dt_object = datetime.now()
print(f'Data e hora atual: {dt_object}')

n_format = dt_object.strftime('%d/%m/%Y %H:%M:%S')
print(f'Data e hora atual(formatada): {n_format}')

date_ = date.today()
print(f'Outra forma de obter a data atual: {date_}')
print(f'Data atual(formatada):{date_.day}/{date_.month}/{date_.year}')


def calc_dias():
    t1_i = date(year=2018, month=12, day=12)
    t2_f = date(year=2018, month=12, day=23)
    t3 = t2_f - t1_i
    return t3.days


def calc_dias2():
    t1_i = date(year=date_.year, month=date_.month, day=date_.day)
    t2_1 = date(year=2020, month=6, day=23)
    t3 = t2_1 - t1_i
    return t3.days


print(f'calc_dias(): {calc_dias()}')
print(f'calc_dias2(): {calc_dias2()}')
