import datetime 
import calendar 
  
def dia_exato(data): 
    
    info = datetime.datetime.strptime(data, '%d %m %Y').weekday() 
    return (calendar.day_name[info]) 

data = '17 08 2022'
print(dia_exato(data)) 
