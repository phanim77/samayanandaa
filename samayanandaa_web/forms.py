from django import forms

class NatalHoroscopeForm(forms.Form):
	first_name = forms.CharField(label='First name', max_length=30)
	middle_name = forms.CharField(label='Middle name', max_length=30)
	last_name = forms.CharField(label='Last name', max_length=30)
	date_of_birth = forms.DateField(label='Date of Birth')
	time_of_birth = forms.DateField(label='Time of Birth')
	place_of_birth = forms.CharField(label='Place of Birth', max_length=80)
	current_location = forms.CharField(label='Current Location', max_length=80)
	message = forms.CharField(widget=forms.Textarea)
class PaymentForm(forms.Form):
	cc_num = forms.CharField(label='Credit Card Number', max_length=19)
	expiry_date = forms.CharField(label='Expiry Date', max_length=5)
	cvv = forms.CharField(label='CVV Code', max_length=4)