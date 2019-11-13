from datetime import date
def changeDate(birthDate):
    today=date.today()
    age=today.year-birthDate.year-((today.month,today.day)<(birthDate.month,birthDate.day))
    return age
datee=input("Enter your birth date")
num=datee.split("-")
print(changeDate(date(int(num[2]),int(num[1]),int(num[0]))),"years")
