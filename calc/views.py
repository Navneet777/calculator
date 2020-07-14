from django.shortcuts import render
from calc.findlcm import findLCM
from calc.findgcd import findGCD
from calc.findprimefactor import primes
from calc.frequncycount import CountFrequency
# Create your views here.
def index(request):
    return render(request,'index.html')
def lcm(request):

    if request.method == "POST":
        x = int(request.POST['field1'])
        y = int(request.POST['field2'])
        lcm = findLCM(x,y)
        gcd = findGCD(x,y)
        mul = x*y
        primex = primes(x)
        primey = primes(y)
        primex_frequency = CountFrequency(primex)
        primey_frequency = CountFrequency(primey)

        return render(request,'result.html',{'lcm':lcm ,'gcd':gcd, 'x':x, 'y':y,'mul':mul,'primex':primex , 'primey':primey , 'primex_frequency':primex_frequency , 'primey_frequency':primey_frequency})
    return render(request,'lcm.html')

def gcd(request):
    x=0
    y=0
    if request.method == "POST":
        x = int(request.POST['field1'])
        y = int(request.POST['field2'])
        gcd = findGCD(x,y)
        primex = primes(x)
        primey = primes(y)
        primex_frequency = CountFrequency(primex)
        primey_frequency = CountFrequency(primey)
        return render(request,'gcdresult.html',{'gcd':gcd , 'x':x, 'y':y ,'primex':primex , 'primey':primey , 'primex_frequency':primex_frequency , 'primey_frequency':primey_frequency })
    return render(request,'gcd.html')
