# inpiration from https://old.reddit.com/r/PowerShell/comments/e4w6b2/get_last_working_day_of_current_monthwith
import datetime
import calendar
yy = 2019
mm = 1
timeoff = ['2019-12-30','2019-12-31']

for i in range (mm,13):
    month = str(calendar.month_name[i])
    ld = calendar.monthrange(yy,i)[-1]
    workdays = []
    for ii in range(ld,0,-1):
        ldcheck = datetime.date(yy,i,ii).strftime("%Y-%m-%d")
        workingday = ldcheck not in timeoff
        day = str(datetime.date(yy,i,ii).strftime('%A'))
        weekend = day in ['Saturday','Sunday']
        if (workingday == True and weekend == False):
            workday = str(yy) + '-' + str(i) + '-' + str(ii).rjust(2, '0')
            workdays.append(workday)
    workdays.sort(reverse=True)
    year, month, day = workdays[0].split('-')
    lastworkingday = str(datetime.date(int(year),int(month),int(day)).strftime('%A'))
    print('Last working day of ' + year + '-' + month.rjust(2, '0') + ', ' + lastworkingday + ' ' + day)
