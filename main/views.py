import os
import mimetypes
from django.views import generic 
from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import Education, Experience, About, Project
from django.http.response import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


def index(request): 
    about = About.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    project = Project.objects.all()     
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = request.POST['email']
        message_body = f'\n {message} \n send by {from_email}' 
        if subject and message and from_email:
            try:
                send_mail(subject, message_body, from_email, ['sarvinoz20161111@gmail.com'])
                messages.add_message(request, messages.WARNING, 'Your message has been sent')
            except BadHeaderError:
                messages.add_message(request, messages.WARNING, 'Invalid header found.')
        else:
            messages.add_message(request, messages.WARNING, 'Make sure all fields are entered and valid.')
      

    return render(request, 'index.html', 
        {
            'project': project,
            'about': about,
            'education': education,
            'experience': experience
        })

def download_file(request, filename):
    if filename != '':
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/downloadFile/' + filename
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    else:
        return render(request, 'index.html')
    