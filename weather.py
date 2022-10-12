import json
import calendar


def read_data(filename):
    try:
        with open(filename, 'r') as f:  # read only
            return json.load(f)
    except FileNotFoundError:
        return {}


def write_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def max_temperature(data, date):  # data is dict
    x = 0  # temp in celsius
    for key in data:  # key: date, value: temp
        if date == key[0:8]:
            if data[key]['t'] > x:
                x = data[key]['t']
    return x


def min_temperature(data, date):
    x = 9999
    for key in data:
        if date == key[0:8]:
            if data[key]['t'] < x:
                x = data[key]['t']
    return x


def max_humidity(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if data[key]['h'] > x:
                x = data[key]['h']
    return x


def min_humidity(data, date):
    x = 9999
    for key in data:
        if date == key[0:8]:
            if data[key]['h'] < x:
                x = data[key]['h']
    return x


def tot_rain(data, date):
    sum = 0
    for key in data:
        if date == key[0:8]:
            sum = sum + data[key]['r']
    return sum


def report_daily(data, date):
    display = "========================= DAILY REPORT ========================\n"
    display = display + "Date                      Time  Temperature  Humidity  Rainfall\n"
    display = display + "====================  ========  ===========  ========  ========\n"
    for key in data:
        if date == key[0:8]:
            m = calendar.month_name[int(
                date[4:6])] + " " + str(int(date[6:8])) + ", " + str(int(date[0:4]))
            tm = key[8:10] + ":" + key[10:12] + ":" + key[12:14]  # time
            t = data[key]['t']
            h = data[key]['h']
            r = data[key]['r']
            display += f'{m:22}{tm:8}{t:13}{h:10}{r:10}\n'  # potential bug
    return display


def report_historical(data):
    display = "============================== HISTORICAL REPORT ===========================\n"
    display += "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    display += "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    display += "====================  ===========  ===========  ========  ========  ========\n"
    h = ''
    for key in data:
        if h == key[0:8]:
            continue
        else:
            h = key[0:8]
            # calendar.month_name returns a month string
            m = calendar.month_name[int(h[4:6])] + " " + \
                str(int(h[6:8])) + ", " + str(int(h[0:4]))
            min_temp = min_temperature(data, key[0:8])
            max_temp = max_temperature(data, key[0:8])
            min_hum = min_humidity(data, key[0:8])
            max_hum = max_humidity(data, key[0:8])
            rain = tot_rain(data, key[0:8])
            # r = {rain:10.2f}
            display += f'{m:20}{min_temp:13}{max_temp:13}{min_hum:10}{max_hum:10}{rain:10.2f}' + "\n"
    return display
