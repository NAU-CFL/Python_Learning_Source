#Develop and test a program that determines approximately how many breaths
#and how many heartbeats the 20 year old person has had in their life.
#The average respiration (breath) rate of people changes
#during different stages of development. Use the breath rates given
#below for use in your program:
#Breaths per Minute
#Infant 30–60 1–4 years 20–30 5–14 years 15–25
#adults 12–20 For heart rate, use an average of 67.5 beats per second

Author: Aliya Kassimova

a=(30+60)/2
b=(30+20)/2
c=(15+25)/2
tot=(12+c)/2
blue=a*60*24*365
pink=b*60*24*365*3
red=c*60*24*365*9
total=tot*60*24*365*4
breath=blue+pink+red+total
heart=67.5*60*60*24*365*20
print("The breath rate is ", breath, "The heart rate is ", heart)
