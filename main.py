import weather


#file = "weather.dat"
weather1 = {}
mychoice = 0
while (True):
    print("      *** TUFFY TITAN WEATHER LOGGER MAIN MENU")  # roughly 6 spaces
    print()
    print("1. Set data filename\n")
    print("2. Add weather data\n")
    print("3. Print daily report\n")
    print("4. Print historical report\n")
    print("9. Exit the program\n")

    mychoice = input("Enter menu choice: ")
    print()
    if mychoice == '1':
        myfile = input("Enter data filename:")
        weather1 = weather.read_data(myfile)
    elif mychoice == '2':
        dt = input("Enter date (YYYYMMDD):")
        tm = input("Enter time (hhmmss):")
        t = int(input("Enter temperature:"))
        h = int(input("Enter humidity:"))
        r = float(input("Enter rainfall:"))
        weather1[dt+tm] = {'t': t, 'h': h, 'r': r}
        weather.write_data(weather1, myfile)
    elif mychoice == '3':
        d = input("Enter date (YYYYMMDD):")
        display = weather.report_daily(weather1, d)
        print(display)
    elif mychoice == '4':
        display = weather.report_historical(weather1)
        print(display)
    elif mychoice == '9':
        break
