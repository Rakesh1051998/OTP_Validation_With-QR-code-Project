from django.shortcuts import render
import random
import qrcode as qr


def index(request):
    return render(request,'index.html')

otpno=0
def loginPage(request):
    uname=request.POST['t1']
    pwd=request.POST['t2']
    if uname == "root" and pwd == "root":
        rn=random.randint(111111,999999)
        global otpno
        otpno=rn
        x=qr.make("OTP :"+str(rn))
        x.save(r'App\static\images\qrimg1.png')
        return render(request,'qrcode.html',{"rnum":rn})
    else:
        return render(request,'index.html',{"error" : "Invalid Details"})


def qrCode(request):
    otp=request.POST['t1']
    if  otp == str(otpno):
        return render(request, "welcome.html")
    else:
        return render(request,'qrcode.html',{"error":"Invalid OTP"})
