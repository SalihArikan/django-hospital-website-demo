from django.shortcuts import render, redirect
from .forms import AppointmentForm


def book(request):
    if request.method == 'POST':
        # the user sent the form
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        # the user just opened the page
        form = AppointmentForm()

    return render(request, 'appointments/book.html', {'form': form})


def success(request):
    return render(request, 'appointments/success.html')
