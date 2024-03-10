# views.py

import stripe
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin, Register
from .models import Hotel
from .forms import FeedbackForm

# Initialize Stripe with your API key
stripe.api_key = settings.STRIPE_SECRET_KEY

# Rest of your views...


def HMhome(request):
    return render(request,"HMhome.html")

def checkadminlogin(request):
    if request.method == "POST":
        adminuname = request.POST["uname"]
        adminpwd = request.POST["pwd"]
        flag = Admin.objects.filter(username=adminuname, password=adminpwd).values()

        if flag:
            return render(request,"HMhome.html")
        else:
            return HttpResponse("Login Fail")
def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request,"username existing...")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request,"email existing....")
                return render(request,"register.html")
            else:
                user=Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd)
                user.save()
                messages.info(request,"user created...")
                return render(request,"login.html")
        else:
            messages.info(request,"password is not matching...")
            return render(request,"register.html")

def checkChangePassword(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag=Register.objects.filter(username=uname,password=opwd).values()
        if flag:
           Register.objects.filter(username=uname, password=opwd).update(password=npwd)
           messages.info(request, "Password Updated")
           return render(request, "index.html")
        else:
            messages.info(request, "TRY AGAIN")
            return render(request, "index.html")
    else:
        return render(request,"changepassword.html")
def logout(request):
    messages.info(request,"logout")
    return render(request,"login.html")

def search_hotel(request):
    if request.method == "GET":
        city = request.GET.get('city')  # Assuming 'city' is the name of the parameter from the form
        hotels = Hotel.objects.filter(city=city)  # Query hotels based on the selected city
        return render(request, "hotel.html", {'hotels': hotels})
    else:
        return HttpResponse("Invalid request method")

def book_hotel(request):
    # Add your view logic here
    return render(request, 'book_hotel.html')


def medical_health_view(request):
    if request.method == 'POST':
        # Process the form data here
        medical_history = request.POST.get('medical_history')
        current_health_status = request.POST.get('current_health_status')
        medical_services_required = request.POST.get('medical_services_required')

        # Perform any necessary operations with the data
        return render(request,'payment_form.html')

    else:
        return render(request, 'feedback.html')

def process_payment(request):
    if request.method == 'POST':
        # Retrieve the token submitted by the form
        token = request.POST['stripeToken']
        amount = 1000  # Amount in cents, change to suit your needs

        try:
            # Create a charge: this will charge the user's card
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description='Hotel booking payment',
                source=token,
            )

            # If the charge is successful, display a success message
            if charge.status == 'succeeded':
                messages.success(request, 'Payment processed successfully!')
                return redirect('success_url')  # Redirect to a success page
            else:
                messages.error(request, 'Payment processing failed. Please try again later.')
                return redirect('failure_url')  # Redirect to a failure page

        except stripe.error.CardError as e:
            # Display error message to user
            messages.error(request, f'Card Error: {e.error.message}')
            return redirect('failure_url')  # Redirect to a failure page

    else:
        # Render a payment form if the request method is not POST
        return render(request, 'payment_form.html')

def checkout(request):
    # Handle checkout process
    # Generate payment request or redirect user to payment gateway URL

    # Example: Redirect user to payment gateway URL
    payment_url = 'https://example.com/payment'
    return redirect(payment_url)

def payment_callback(request):
    # Handle payment callback from payment gateway
    # This endpoint will receive the payment confirmation from the payment gateway

    # Example: Get payment status from request parameters
    payment_status = request.GET.get('status')

    if payment_status == 'success':
        # Payment successful, update order status and complete checkout process
        # You may want to save the payment details in your database
        return HttpResponse('Payment successful!')
    else:
        # Payment failed or cancelled, handle accordingly
        return HttpResponse('Payment failed or cancelled.')

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Booking Successfull")
            return render(request, "home.html")
            # Redirect to a success page
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})