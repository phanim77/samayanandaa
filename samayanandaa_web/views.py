from django.shortcuts import render

from . models import NatalHoroscope
# Create your views here.
def index(request, pagename):
    pagename='/'+pagename	
    print (request.POST.get('first_name'))
    print (request.POST.get('middle_name'))
    print (request.POST.get('last_name'))
    print (request.POST.get('date_of_birth'))
    print (request.POST.get('time_of_birth'))
    try:
        natalHoroscope = NatalHoroscope.objects.get(permalink=pagename)
        context = {
            'first_name': natalHoroscope.first_name,
            'middle_name': natalHoroscope.middle_name,
            'last_name': natalHoroscope.last_name,
        }
    except NatalHoroscope.DoesNotExist:
        natalHoroscope = None
        context = {
            'first_name': "Bob",
            'middle_name': "X",
            'last_name': "Thornton",
        }
    return render(request, 'natal_horoscope.html', context)

def natal_horoscope(request, pagename):
    print ("natal_horoscope from views.py")
    submitted = False
    print (request.POST.get('first_name'))
    print (request.POST.get('middle_name'))
    print (request.POST.get('last_name'))
    print (request.POST.get('date_of_birth'))
    print (request.POST.get('time_of_birth'))
    context = {
        'first_name': request.POST.get('first_name'),
        'middle_name': request.POST.get('middle_name'),
        'last_name': request.POST.get('last_name'),
    }
    return render(request, 'natal_horoscope.html', context)