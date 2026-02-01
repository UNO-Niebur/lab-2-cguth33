#FutureTime.py
#Name:Carter Guthrie
#Date:2/1/2025
#Assignment:Lab 2- Future Time
#Purpose: Calculate future time using modular arithmetic
# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  #Ask user for minutes
  extraHours = int(input("Enter hours to add: "))
  extraMinutes = int(input("Enter minutes to add: "))
  #Calculate the time after the user-supplied time has passed.
  totalMinutes = currentMinute + extraMinutes
  futureMinute = totalMinutes % 60
  #Do not use any if statements in calculating the time.
  carryOverHours = totalMinutes // 60
  futureHour = (currentHour + extraHours + carryOverHours) % 24
  #Output the future time in standard format "HH:MM"
  print(f"Future time is: {futureHour:02d}:{futureMinute:02d}")

if __name__ == '__main__':
  main()
