from django.shortcuts import render
from calc.findlcm import findLCM
from calc.findgcd import findGCD
# Create your views here.
def index(request):
    return render(request,'index.html')
def lcm(request):
    
    if request.method == "POST":
        x = int(request.POST['field1'])
        y = int(request.POST['field2'])
        lcm = findLCM(x,y)
        return render(request,'result.html',{'lcm':lcm , 'x':x, 'y':y})
    return render(request,'lcm.html')

def gcd(request):
    x=0
    y=0
    if request.method == "POST":
        x = int(request.POST['field1'])
        y = int(request.POST['field2'])
        gcd = findGCD(x,y)
        return render(request,'gcdresult.html',{'gcd':gcd , 'x':x, 'y':y })
    return render(request,'gcd.html')
