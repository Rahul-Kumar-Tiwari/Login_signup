import way2sms

sms = way2sms.Sms("8804649322","8750153215")
print(sms.jsid)
print(sms.logged_in)
status = sms.send("8607618732","hi mandeep")
print(status)
print(sms.q)
sms.logout()