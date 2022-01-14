import pywhatkit
print("Whatsapp message automator made by Kyle Lam on January 13, 2022, Welcome!\n")

phonenum = str(input("Please enter the phone number of the contact you want to send the message to: "))
msg = str(input("Please enter the message you want to send: "))
hr = int(input("Please enter the hour you want this message to send (Use 24 hour format): "))
min = int(input("Please enter the minute you want this message to send: "))

if 0 <= hr <= 9:
    hr = "0"+str(hr)
if 0 <= min <= 9:
    min = "0"+str(min)

print("\nThank you for using the Whatsapp message automator! The message will be delivered to " + phonenum + " at " + str(hr) + ":" + str(min))

pywhatkit.sendwhatmsg(phonenum, msg, int(hr), int(min))
# syntax: pywhatkit.sendwhatmsg("area code and phone number", "message", time in hours, time in minutes)


