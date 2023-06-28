import  datetime
def check(day,month,year):
    isvalid=True
    try:
        datetime.datetime(int(year),int(month),int(day))
    except:
        isvalid=False
    if(isvalid):
        print("Yes")
    else:
        print("No")
check(1,12,2000)
