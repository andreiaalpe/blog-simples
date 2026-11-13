from django.shortcuts import render

def home(request):
    context = {
        'name': 'Joca da Silva',
        'age': 24,
        'tel': '(21) 998877665',
        'fruits' : ['banana', 'laranja', 'morango', 'uva']
    }
    return render(request, 'home.html', context)