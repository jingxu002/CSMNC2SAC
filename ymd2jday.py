def ymd2jday(year, month, day):
    noleap = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334];
    leap = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335];
    if ((year%4==0 and year%100!=0) or (year%400==0)):
        return leap[month-1] + day;
    else:
        return noleap[month-1] + day;
