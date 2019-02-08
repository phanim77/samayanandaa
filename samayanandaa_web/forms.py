from django import forms

class NatalHoroscopeForm(forms.Form):
	first_name = forms.CharField(label='First name', max_length=30)
	middle_name = forms.CharField(label='Middle name', max_length=30)
	last_name = forms.CharField(label='Last name', max_length=30)
	date_of_birth = forms.DateField(label='Date of Birth')
	time_of_birth = forms.DateField(label='Time of Birth')
	place_of_birth = forms.CharField(label='Place of Birth', max_length=80)
	current_location = forms.CharField(label='current_location', max_length=80)
	message = forms.CharField(widget=forms.Textarea)
class PaymentForm(forms.Form):
	cc_num = forms.CharField()
	expiry_date = forms.CharField()
	cvv = forms.CharField()	