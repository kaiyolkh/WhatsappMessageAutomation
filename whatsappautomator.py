# You need both pywhatkit and flask installed for this to work
# Just do "pip install pywhatkit" and do the same thing for flask in the PyCharm terminal
import pywhatkit
print("Whatsapp message automator made by Kyle Lam on January 13, 2022, Welcome!\n")

phonenum = str(input("Please enter the phone number of the contact you want to send the message to: "))
msg = str(input("Please enter the message you want to send: "))
hr = int(input("Please enter the hour you want this message to send (Use 24 hour format): "))
minute = int(input("Please enter the minute you want this message to send: "))

# The if statements below basically just makes the output look better
# For example if you want a message to be delivered at 12am, the output would show 00:00 instead of 0:0
if 0 <= hr <= 9: 
    hr = "0"+str(hr)
if 0 <= minute <= 9:
    minute = "0"+str(minute)

print("\nThank you for using the Whatsapp message automator! The message will be delivered to " + phonenum + " at " + str(hr) + ":" + str(minute))

pywhatkit.sendwhatmsg(phonenum, msg, int(hr), int(minute))
# Syntax: pywhatkit.sendwhatmsg("area code and phone number", "message", time (hour), time (minute))
