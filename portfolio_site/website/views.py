from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def projects(request):
    return render(request, 'website/projects.html')

def skills(request):
    return render(request, 'website/skills.html')

def contact(request):
    return render(request, 'website/contact.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        full_message = f"From: {name} <{email}>\n\n{message}"
        send_mail('New Contact Message', full_message, email, ['ktmongali@gmail.com'])
        
        messages.success(request, "Your message has been sent.")
        return redirect('contact')
    return render(request, 'website/contact.html')