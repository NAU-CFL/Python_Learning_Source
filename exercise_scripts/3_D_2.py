# Life Signs

"""
Develop and test a program that prompts the user for their age and determines
approximately how many breaths and how many heartbeats the person has had in
their life. The average respiration (breath) rate of people changes during
different stages of development. Use the breath rates given below for use in your
program:
                     Breaths per Minute
Infant               30–60
1–4 years            20–30
5–14 years           15–25
adults               12–20
For heart rate, use an average of 67.5 beats per second.
"""

age = 20
total_breaths = 45*60*24*365
age -= 1
total_breaths += 25*60*24*365*3
age -= 3
total_breaths += 20*60*24*365*9
age -= 9
total_breaths += 16*60*24*365*7

heart_beats = 67.5*60*60*24*365*20

print("20 years old person had breath approximately: ", total_breaths , " times")
print("20 years old person had heartbeats approximately: ", heart_beats , " times")
