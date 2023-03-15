from django.shortcuts import render

# Create your views here.


def fibonachi(request):
    number = request.POST.get('number')
    n1 = 0
    n2 = 1
    if int(number) == 0:
        res = n1
    elif int(number) > 0:
        count = 0
        r = []
        while n1 != int(number):
            count += 1
            r.append(str(count))
            n1, n2 = n2, n1 + n2
            if n1 > int(number):
                res = 'no fib'
        res = ' '.join([i for i in r])
    
        
    else:
        res = 'no fib'
    return render(request, 'main/fibonachi.html', context={'res':res})
