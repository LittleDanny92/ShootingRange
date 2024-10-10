from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime,timedelta
from reservation_form.models import BookedDate
from reservation_form.forms import ReservationForm

def visit_booking(request):
    free_dates = get_free_time()
    if request.method == "POST":
        
        form = ReservationForm(request.POST, free_dates=free_dates)

        selected_date = request.POST.get('date_dropdown')
        if selected_date in free_dates:
            available_times = free_dates[selected_date]
            form.fields['time_dropdown'].choices = [(time, time) for time in available_times]
        else:
            form.fields['time_dropdown'].choices = []

        if form.is_valid():
            print("validni")
            date = form.cleaned_data["date_dropdown"]
            time = form.cleaned_data["time_dropdown"]
            instructor = form.cleaned_data["instructor"]
            weapon = form.cleaned_data["weapon"]
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            
            booked_date = BookedDate(
                datetime_field = datetime.strptime(f"{date} {time}", "%d.%m.%Y %H:%M"),
                instructor_field = instructor,
                selected_weapon = weapon,
                name_field = name,
                email_field = email)

            booked_date.save()

            EmailMessage(
                "Shooting range - booking",
                f"Thank You for booking the visit of our shooting range! We look forward to seeing You {date} at {time}",
                "HlavackaDanielml@seznam.cz",
                [email],
                [],
            ).send()

            messages.success(request, "Thank You for booking the visit.")

            return redirect("visit_booking")
        else:
            print("neco se posralo")
            print(f"{form.errors}")
    else:
        form = ReservationForm(free_dates=free_dates)
    return render(request, "reservation_form/reservation_form.html", {"form":form, "messages": messages.get_messages(request)})

def get_free_time():

        working_days = [(datetime.now() + timedelta(days=i)).strftime("%d.%m.%Y") for i in range(10)]
        working_hours = [f"{hour:02d}:00" for hour in range(10,22)]

        all_working_hours = {}
        free_dates = {}

        booked_dates = BookedDate.objects.values_list("datetime_field", flat=True)
        booked_dates_formatted = [datetime.strftime(date, "%d.%m.%Y %H:%M") for date in booked_dates]

        for working_day in working_days:
            all_working_hours[working_day] = working_hours

        for working_day, working_hours in all_working_hours.items():
            free_hours = []
            for working_hour in working_hours:
                if f"{working_day} {working_hour}" not in booked_dates_formatted:
                    free_hours.append(working_hour)
            if free_hours:
                free_dates[working_day] = free_hours
        return free_dates

def get_available_times(request):
    selected_date = request.GET.get("date")
    free_dates = get_free_time()
    available_times = free_dates.get(selected_date, [])
    return JsonResponse({"available_times": available_times})