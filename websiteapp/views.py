from django.shortcuts import render,redirect
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
from django.core.mail import send_mail
from django.conf import settings
from io import BytesIO
import base64
from .forms import TextGraphicsForm,AppointmentForm,BookingForm
from .models import Font, EngravingBookings
from django.utils import timezone
from datetime import datetime, timedelta, time, date
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
	return render(request, 'home.html', {})


from django.db.models import Q


@csrf_exempt
def bookingpage(request):
    image_data = None
    if request.method == 'POST':
        graphicform = TextGraphicsForm(request.POST)
        bookingform = BookingForm(request.POST)

        if graphicform.is_valid():
            text = graphicform.cleaned_data['text']
            font = graphicform.cleaned_data['font'].file_path.path
            color = graphicform.cleaned_data['color']
            size = graphicform.cleaned_data['size']
            font_obj = ImageFont.truetype(font, size)
            width, height = font_obj.getsize(text)
            print(f"width={width}, height={height}")
            image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
            draw = ImageDraw.Draw(image)
            draw.text((0, 0), text, font=font_obj, fill=color)
            buffer = BytesIO()
            image.save(buffer, 'PNG')
            image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
            print(f"image_data={image_data}")
            img_tag = f'<img src="data:image/png;base64,{image_data}" alt="Generated Image">'
            return HttpResponse(img_tag)



             

        if bookingform.is_valid():
            # Check if the selected date and time have already been booked
            date = bookingform.cleaned_data['date']
            time = bookingform.cleaned_data['Time']
            bookings = EngravingBookings.objects.filter(
                Q(date=date, Time=time) | Q(date=date, Time__startswith=time + ':')
            )
            if bookings.exists():
                messages.error(request, 'Sorry, that date and time has already been booked.')
                # Remove the selected option from the dropdown list
                bookingform.fields['Time'].choices = [
                    (choice_value, choice_label) for choice_value, choice_label in bookingform.fields['Time'].choices
                    if choice_value != time
                ]
                context = {'bookingform': bookingform,'fonts': Font.objects.all(),'graphicform': graphicform, 'image_data': image_data, 'error': 'Sorry, that date and time have already been booked.'}
                return render(request, 'bookingpage.html', context)

            # Create a new booking
            booking = EngravingBookings(
                Name=bookingform.cleaned_data['Name'],
                Phone_number=bookingform.cleaned_data['Phone_number'],
                font_name=bookingform.cleaned_data['font_name'],
                date=date,
                Time=time
            )
            booking.save()
            send_mail(
                'New Booking',
                f'You have received a new Booking!! Check out the Details below:\nName: {booking.Name}\nMobile number: {booking.Phone_number}\nDate: {booking.date}\nTime: {booking.Time}\nFont: {booking.font_name}',
                settings.EMAIL_HOST_USER,
                ['mutwiri333@gmail.com'],
                fail_silently=False
            )
            return redirect('bookingconfirmation')

    else:
        graphicform = TextGraphicsForm()
        bookingform = BookingForm()

    context = {'bookingform': bookingform, 'fonts': Font.objects.all(), 'graphicform': graphicform, 'image_data': image_data}
    return render(request, 'bookingpage.html', context)


'''
def bookingpage(request):
    image_data = None
    if request.method == 'POST':
        graphicform = TextGraphicsForm(request.POST)
        bookingform = BookingForm(request.POST)

        if graphicform.is_valid():
            text = graphicform.cleaned_data['text']
            font = graphicform.cleaned_data['font'].file_path.path
            color = graphicform.cleaned_data['color']
            size = graphicform.cleaned_data['size']
            font_obj = ImageFont.truetype(font, size)
            width, height = font_obj.getsize(text)
            print(f"width={width}, height={height}")
            image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
            draw = ImageDraw.Draw(image)
            draw.text((0, 0), text, font=font_obj, fill=color)
            buffer = BytesIO()
            image.save(buffer, 'PNG')
            image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
            print(f"image_data={image_data}") 
            pass

        if bookingform.is_valid():
            booking = EngravingBookings(
                Name=bookingform.cleaned_data['Name'],
                Phone_number=bookingform.cleaned_data['Phone_number'],
                Engraved_text=bookingform.cleaned_data['Engraved_text'],
                font_name=bookingform.cleaned_data['font_name'],
                font_size=bookingform.cleaned_data['font_size'],
                date=bookingform.cleaned_data['date'],
                Time=bookingform.cleaned_data['Time']

                )
            booking.save()
            send_mail(
                'New Booking',
                f'You have received a new Booking!! Check out the Details below:\nName: {booking.Name}\nMobile number: {booking.Phone_number}\nDate: {booking.date}\nTime: {booking.Time}\nEngravedMessage: {booking.Engraved_text}\nFont: {booking.font_name}',
                settings.EMAIL_HOST_USER,
                ['mutwiri333@gmail.com'],
                fail_silently = False,


                )
            return redirect('bookingconfirmation')
            pass
    


    else:
        graphicform = TextGraphicsForm()
        bookingform = BookingForm()

    context = {}



    return render(request, 'bookingpage.html', {'bookingform': bookingform,'fonts': Font.objects.all(),'graphicform': graphicform, 'image_data': image_data})

'''


def generate_text_graphics(request):
	if request.method == 'POST':
		form = TextGraphicsForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['text']
			font = form.cleaned_data['font'].file_path.path
			color = form.cleaned_data['color']
			size = form.cleaned_data['size']
			font_obj = ImageFont.truetype(font, size)
			width, height = font_obj.getsize(text)
			print(f"width={width}, height={height}")
			image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
			draw = ImageDraw.Draw(image)
			draw.text((0, 0), text, font=font_obj, fill=color)
			buffer = BytesIO()
			image.save(buffer, 'PNG')
			image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
			print(f"image_data={image_data}") 
			return render(request, 'booking.html', {'form': form, 'image_data': image_data, 'fonts': Font.objects.all()})
	


	else:
		form = TextGraphicsForm()


	return render(request, 'booking.html', {'form': form,'fonts': Font.objects.all()})


def bookingdate(request):
	return render(request, 'booking_schedule.html', {})


def booking_view(request):
    if request.method == 'POST':
        # Handle form submission
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the booking to the database
            booking = form.save()
            return redirect('booking_success')
    else:
        # Display the booking form and the available time slots
        form = BookingForm()
        date = datetime.now().date()
        time_slots = []
        start_time = time(hour=8)
        end_time = time(hour=18)
        delta = timedelta(minutes=5)
        while start_time < end_time:
            end_slot = (datetime.combine(date, start_time) + delta).time()
            bookings = EngraveBooking.objects.filter(date=date, time__gte=start_time, time__lt=end_slot)
            if bookings:
                time_slots.append({'time': start_time.strftime('%I:%M %p'), 'available': False})
            else:
                time_slots.append({'time': start_time.strftime('%I:%M %p'), 'available': True})
            start_time = end_slot
        return render(request, 'booking_schedule.html', {'form': form, 'time_slots': time_slots})


def bookingAppointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')
    else:
        form = AppointmentForm()

    # Get all existing appointments for the selected date
    appointments = BookAppointment.objects.filter(date=form.data.get('date'))

    # Create a list of all available time slots (5-minute intervals)
    available_times = []
    time = datetime(1900, 1, 1, 8, 0)
    while time <= datetime(1900, 1, 1, 18, 0):
        if not appointments.filter(start_time=time.time()).exists():
            available_times.append(time.time())
        time += timedelta(minutes=5)

    return render(request, 'bookingtwo.html', {'form': form, 'available_times': available_times})



def available_times(request, date):
    # Get the list of existing bookings for the selected date
    bookings = EngraveBooking.objects.filter(date=date)

    # Create a list of all possible appointment times for the day
    start_time = time(8, 0)
    end_time = time(18, 0)
    interval = timedelta(minutes=5)
    available_times = []
    current_time = datetime.combine(date, start_time)
    while current_time <= datetime.combine(date, end_time):
        if not bookings.filter(time=current_time.time()).exists():
            available_times.append(current_time.time())
        current_time += interval

    # Render the template with the available times
    return render(request, 'booking_schedule.html', {'available_times': available_times})




def Engravebooking(request):
    if request.method == 'POST':
        # Handle form submission
        date = request.POST.get('date')
        time = request.POST.get('time')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        Font_name = request.POST.get('Font_name')
        Engraving_Text = request.POST.get('Engraving_Text')
        appointment = EngraveBooking.objects.create(
            date=date,
            time=time,
            name=name,
            phone_number=phone_number,
            Font_name = Font_name,
            Engraving_Text = Engraving_Text
        )
        appointment.save()
        # Redirect to success page
        return redirect('booking_success')
    else:
        # Generate list of available appointment times
        date = datetime.strptime(request.GET.get('date'), '%Y-%m-%d')
        appointment_times = []
        start_time = datetime.combine(date, datetime.min.time()) + timedelta(hours=8)
        end_time = datetime.combine(date, datetime.min.time()) + timedelta(hours=18)
        time_slot = timedelta(minutes=5)
        while start_time <= end_time:
            appointment_times.append(start_time.time())
            start_time += time_slot
        # Pass appointment times to template
        context = {'date': date, 'appointment_times': appointment_times}
        return render(request, 'booking_schedule.html', context)
'''       
def bookingview(request):
    print('helo')
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = EngravingBookings(
                Name=form.cleaned_data['Name'],
                Phone_number=form.cleaned_data['Phone_number'],
                Engraved_text=form.cleaned_data['Engraved_text'],
                font_name=form.cleaned_data['font_name'],
                font_size=form.cleaned_data['font_size'],
                date=form.cleaned_data['date'],
                Time=form.cleaned_data['Time']
            )
            booking.save()
            send_mail(
                'New Booking',
                f'You have received a new Booking!! Check out the Details below:\nName: {booking.Name}\nMobile number: {booking.Phone_number}\nDate: {booking.date}\nTime: {booking.Time}\nEngravedMessage: {booking.Engraved_text}\nFont: {booking.font_name}',
                settings.EMAIL_HOST_USER,
                ['mutwiri333@gmail.com'],
                fail_silently=False,
            )
            return redirect('bookingconfirmation')
    else:
        form = BookingForm(available_times=get_available_times())
    return render(request, 'bookengraving.html', {'form': form})

'''



def bookingview(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = EngravingBookings(
				Name=form.cleaned_data['Name'],
				Phone_number=form.cleaned_data['Phone_number'],
				Engraved_text=form.cleaned_data['Engraved_text'],
				font_name=form.cleaned_data['font_name'],
				font_size=form.cleaned_data['font_size'],
				date=form.cleaned_data['date'],
				Time=form.cleaned_data['Time']

				)
            booking.save()
            send_mail(
				'New Booking',
				f'You have received a new Booking!! Check out the Details below:\nName: {booking.Name}\nMobile number: {booking.Phone_number}\nDate: {booking.date}\nTime: {booking.Time}\nEngravedMessage: {booking.Engraved_text}\nFont: {booking.font_name}',
				settings.EMAIL_HOST_USER,
				['mutwiri333@gmail.com'],
				fail_silently = False,


				)
            return redirect('bookingconfirmation')
    else:
        form = BookingForm()



    return render(request, 'bookengraving.html', {'form':form})


def get_available_times():
    start_time = time(8, 0) # 8:00 AM
    end_time = time(18, 0) # 6:00 PM
    interval = timedelta(minutes=5)
    available_times = []
    current_time = datetime.combine(datetime.today(), start_time)
    while current_time.time() <= end_time:
        available_times.append((current_time.time().strftime('%H:%M:%S'), current_time.time().strftime('%I:%M %p')))
        current_time += interval

    return available_times

def bookingconfirmation(request):
	return render(request, 'bookingconfirmation.html', {})