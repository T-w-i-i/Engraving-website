from django.db import models

# Create your models here.

class Font(models.Model):
	name = models.CharField(max_length = 100)
	file_path = models.FileField(upload_to=f'static/fonts/',null = True)

	def __str__(self):
		return self.name

class Booking(models.Model):
	name = models.CharField(max_length = 100)
	phone_number = models.CharField(max_length = 15)
	booking_time = models.DateTimeField()

class EngravingBookings(models.Model):
	Name = models.CharField(max_length = 100)
	Phone_number = models.CharField(max_length = 100)
	Engraved_text = models.CharField(max_length = 500,blank=True, null=True)
	font_name = models.CharField(max_length= 100)
	font_size = models.CharField(max_length = 100, blank=True, null=True)
	date = models.DateField()
	Time = models.TimeField()

	def __str__(self):
		return self.Name



class BookAppointment(models.Model):
	name = models.CharField(max_length = 100)
	phone_number = models.CharField(max_length = 15)
	Font_name = models.CharField(max_length = 100)
	Engraving_Text = models.CharField(max_length = 100)
	date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()

class EngraveBooking(models.Model):
	name = models.CharField(max_length = 100)
	phone_number = models.CharField(max_length = 15)
	Font_name = models.CharField(max_length = 100)
	Engraving_Text = models.CharField(max_length = 100)
	date = models.DateField()
	time = models.TimeField()

