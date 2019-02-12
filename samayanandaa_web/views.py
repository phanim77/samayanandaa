from django.shortcuts import render
from samayanandaa_web.forms import NatalHoroscopeForm
from samayanandaa_web.forms import PaymentForm
from . models import NatalHoroscope
from django.views.generic import View
# Create your views here.
def index(request):
    print ("index from views.py")
    form_class = NatalHoroscopeForm
    if request.method == 'POST':
        print ("request method is post")
        form = form_class(data=request.POST)
        print (form.data['first_name'])
        print (form.data['middle_name'])
        print (form.data['last_name'])
        print (form.data['date_of_birth'])
        print (form.data['time_of_birth'])
        print (form.data['place_of_birth'])  
        print (form.data['current_location'])
        print (form.data['message'])                
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            print (first_name)
            middle_name = form.cleaned_data['middle_name']
            print (middle_name)
            last_name = form.cleaned_data['last_name']
            print (last_name)
            date_of_birth = form.cleaned_data['date_of_birth']
            print (date_of_birth)   
            time_of_birth = form.cleaned_data['time_of_birth']
            print (time_of_birth)
            place_of_birth = form.cleaned_data['place_of_birth']
            print (place_of_birth)    
            current_location = form.cleaned_data['current_location']
            print (current_location)  
            message = form.cleaned_data['message']
            print (message)             
    return render(request, 'index.html', {
    'form': form_class, 
})

def payment(request):
    print ("payment from views.py")
    form_class = PaymentForm
    if request.method == 'POST':
        print ("request method is post")
        form = form_class(data=request.POST)
        print (form.data['cc_num'])
        print (form.data['expiry_date'])
        print (form.data['cvv'])
        if form.is_valid():
            cc_num = form.cleaned_data['cc_num']
            print (cc_num)
            expiry_date = form.cleaned_data['expiry_date']
            print (expiry_date)
            cvv = form.cleaned_data['cvv']
            print (cvv)
    return render(request, 'index.html', {
    'form': form_class,
})