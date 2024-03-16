from django.shortcuts import render,redirect


# Create your views here.
def button_action(request): 
    # return redirect('http://localhost:8000/home/')
    return render(request,'home.html')
