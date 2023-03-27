from django import forms
from django.forms import ModelForm
from .models import Font, EngraveBooking, BookAppointment, EngravingBookings

from datetime import datetime, time
class ChoiceTimeField(forms.ChoiceField):
    def __init__(self, choices=(), **kwargs):
        super().__init__(choices=choices, **kwargs)
        self.widget = forms.Select(choices=self.choices, attrs=self.widget.attrs)

    def to_python(self, value):
        if value in self.empty_values:
            return None
        return datetime.strptime(value, '%H:%M:%S').time()

TIME_CHOICES = (
    ('08:00:00', '8:00 AM'),
    ('08:05:00', '8:05 AM'),
    ('08:10:00', '8:10 AM'),
    ('08:15:00', '8:15 AM'),
    ('08:20:00', '8:20 AM'),
    ('08:25:00', '8:25 AM'),
    ('08:30:00', '8:30 AM'),
    ('08:35:00', '8:35 AM'),
    ('08:40:00', '8:40 AM'),
    ('08:45:00', '8:45 AM'),
    ('08:50:00', '8:50 AM'),
    ('08:55:00', '8:55 AM'),
    ('09:00:00', '9:00 AM'),
    ('09:05:00', '9:05 AM'),
    ('09:10:00', '9:10 AM'),
    ('09:15:00', '9:15 AM'),
    ('09:20:00', '9:20 AM'),
    ('09:25:00', '9:25 AM'),
    ('09:30:00', '9:30 AM'),
    ('09:35:00', '9:35 AM'),
    ('09:40:00', '9:40 AM'),
    ('09:45:00', '9:45 AM'),
    ('09:50:00', '9:50 AM'),
    ('09:55:00', '9:55 AM'),
    ('10:00:00', '10:00 AM'),
    ('10:05:00', '10:05 AM'),
    ('10:10:00', '10:10 AM'),
    ('10:15:00', '10:15 AM'),
    ('10:20:00', '10:20 AM'),
    ('10:25:00', '10:25 AM'),
    ('10:30:00', '10:30 AM'),
    ('10:35:00', '10:35 AM'),
    ('10:40:00', '10:40 AM'),
    ('10:45:00', '10:45 AM'),
    ('10:50:00', '10:50 AM'),
    ('10:55:00', '10:55 AM'),
    ('11:00:00', '11:00 AM'),
    ('11:05:00', '11:05 AM'),
    ('11:10:00', '11:10 AM'),
    ('11:15:00', '11:15 AM'),
    ('11:20:00', '11:20 AM'),
    ('11:25:00', '11:25 AM'),
    ('11:30:00', '11:30 AM'),

    ('11:35:00', '11:35 AM'),
    ('11:40:00', '11:40 AM'),
    ('11:45:00', '11:45 AM'),
    ('11:50:00', '11:50 AM'),
    ('11:55:00', '11:55 AM'),
    ('12:00:00', '12:00 PM'),
    ('12:05:00', '12:05 PM'),
    ('12:10:00', '12:10 PM'),
    ('12:15:00', '12:15 PM'),
    ('12:20:00', '12:20 PM'),
    ('12:25:00', '12:25 PM'),
    ('12:30:00', '12:30 PM'),
    ('12:35:00', '12:35 PM'),
    ('12:40:00', '12:40 PM'),
    ('12:45:00', '12:45 PM'),
    ('12:50:00', '12:50 PM'),
    ('12:55:00', '12:55 PM'),
    ('12:55:00', '12:55 PM'),
    ('13:00:00', '1:00 PM'),
    ('13:05:00', '1:05 PM'),
    ('13:10:00', '1:10 PM'),
    ('13:15:00', '1:15 PM'),
    ('13:20:00', '1:20 PM'),
    ('13:25:00', '1:25 PM'),
    ('13:30:00', '1:30 PM'),
    ('13:35:00', '1:35 PM'),
    ('13:40:00', '1:40 PM'),
    ('13:45:00', '1:45 PM'),
    ('13:50:00', '1:50 PM'),
    ('13:55:00', '1:55 PM'),
    ('14:00:00', '2:00 PM'),
    ('14:05:00', '2:05 PM'),
    ('14:10:00', '2:10 PM'),
    ('14:15:00', '2:15 PM'),
    ('14:20:00', '2:20 PM'),
    ('14:25:00', '2:25 PM'),
    ('14:30:00', '2:30 PM'),
    ('14:35:00', '2:35 PM'),
    ('14:40:00', '2:40 PM'),
    ('14:45:00', '2:45 PM'),

    ('14:50:00', '2:50 PM'),
    ('14:55:00', '2:55 PM'),
    ('15:00:00', '3:00 PM'),
    ('15:05:00', '3:05 PM'),
    ('15:10:00', '3:10 PM'),
    ('15:15:00', '3:15 PM'),
    ('15:20:00', '3:20 PM'),
    ('15:25:00', '3:25 PM'),
    ('15:30:00', '3:30 PM'),
    ('15:35:00', '3:35 PM'),

    ('15:40:00', '3:40 PM'),
    ('15:45:00', '3:45 PM'),
    ('15:50:00', '3:50 PM'),
    ('15:55:00', '3:55 PM'),
    ('16:00:00', '4:00 PM'),
    ('16:05:00', '4:05 PM'),
    ('16:10:00', '4:10 PM'),
    ('16:15:00', '4:15 PM'),
    ('16:20:00', '4:20 PM'),
    ('16:25:00', '4:25 PM'),
    ('16:30:00', '4:30 PM'),
    ('16:35:00', '4:35 PM'),
    ('16:40:00', '4:40 PM'),
    ('16:45:00', '4:45 PM'),
    ('16:50:00', '4:50 PM'),
    ('16:55:00', '4:55 PM'),
    ('17:00:00', '5:00 PM'),
    ('17:05:00', '5:05 PM'),
    ('17:10:00', '5:10 PM'),
    ('17:15:00', '5:15 PM'),
    ('17:20:00', '5:20 PM'),
    ('17:25:00', '5:25 PM'),
    ('17:30:00', '5:30 PM'),
    ('17:35:00', '5:35 PM'),
    ('17:40:00', '5:40 PM'),
    ('17:45:00', '5:45 PM'),
    ('17:50:00', '5:50 PM'),

    
    # Add more time intervals as needed
    ('17:55:00', '5:55 PM'),
    ('18:00:00', '6:00 PM'),
)

class TextGraphicsForm(forms.Form):
	text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input Text to be Engraved', 'style': 'width: 300px;', 'class': 'form-control'}))
	font = forms.ModelChoiceField(queryset=Font.objects.all())
	color = forms.CharField(max_length=7, widget=forms.TextInput(attrs={'type': 'color', 'style': 'width: 300px;', 'class': 'form-control'}))
	size = forms.IntegerField(min_value=1, max_value=100)






class AppointmentForm(forms.ModelForm):
    class Meta:
        model = BookAppointment
        fields = ('name', 'phone_number', 'Font_name','Engraving_Text','date', 'start_time')
        widgets = {
        	'date': forms.DateInput(attrs={'type': 'date'}),
        }

    start_time = forms.TimeField(widget=forms.HiddenInput())





class BookingForm(forms.Form):
    Name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'What is your name?', 'style': 'width: 300px;', 'class': 'form-control'}))
    Phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'What is your phone_number?', 'style': 'width: 300px;', 'class': 'form-control'}))
    
    font_name = forms.ModelChoiceField(queryset=Font.objects.all())
    
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Time = forms.ChoiceField(choices=[(time(hour=hour, minute=minute), f'{hour:02d}:{minute:02d}') for hour in range(8, 18) for minute in range(0, 60, 5)], widget=forms.Select(attrs={'class': 'form-control'}))

   


