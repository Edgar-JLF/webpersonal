from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm(data = request.POST)
    if contact_form.is_valid():
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        content = request.POST.get('content','')

        #Enviamos el correo y redireccionamos
        email = EmailMessage(
            "Mi web personal: Nuevo mensaje de contancto",
            f"De {name} <{email}>\n\nEscribio:\n\n{content}",
            email,
            ["edgarlopezf43@gmail.com"],
            reply_to=[email]
        )

        try:
            email.send()
            #Todo ha ido bien redireccionamos a ok
            return redirect(reverse('contact')+'?ok')
        
        except:
            #Algo no ha ido bien, redireccionamos a FAIL
            return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', {'form':contact_form})
