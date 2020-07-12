from django.shortcuts import render
import numpy as np
# Create your views here.
def index(request):
    lcm = np.lcm(12, 4000)
    return render(request,'index.html',{'lcm':lcm})
def lcm(request):
    x=0
    y=0
    if request.method == "POST":
        x = int(request.POST['field1'])
        y = int(request.POST['field2'])
        lcm = np.lcm(x,y)
        return render(request,'result.html',{'lcm': lcm , 'x':x, 'y':y })
    return render(request,'lcm.html')

def gcd(request):
    x=0
    y=0
    if request.method == "POST":
        x = int(request.POST['field1'])
        y = int(request.POST['field2'])
        gcd = np.gcd(x,y)
        return render(request,'gcdresult.html',{'gcd':gcd , 'x':x, 'y':y })
    return render(request,'gcd.html')
