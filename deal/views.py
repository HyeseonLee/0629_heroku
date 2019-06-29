from django.shortcuts import render
from .models import Money
from django.utils.timezone import now
# Create your views here.

def all_money(request):    
    return render(request, 'money.html')

def home(request):
    return render(request, 'home.html')

def create(request):
    money = Money()
    money.name = request.GET['name']
    money.deposit = request.GET['deposit']
    money.withdraw = request.GET['withdraw']
    money.input_date = request.GET['input_date']
    money.save()
    
    #moneys = Money.objects.all()

    return render(request, 'submit.html')

def sums(request):
    moneys = Money.objects.all()
    total = []
    please = 0
    for k in moneys:
        temp = k.deposit - k.withdraw
        please = please + temp
        total.append(please)

    return render(request, 'sum.html', {'moneys' : moneys, 'total' : total })
        

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password) #실제로 저장된 회원이 맞는지 확인하는 함수
        if user is not None:
            auth.login(request, user)
            return redirect('home') #로그인 성공시 홈으로 이동
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
