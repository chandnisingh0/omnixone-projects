from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
import json
from .models import Controller
from .models import EmbeddedLinux
from .models import PcbDesigning
from .models import WebApp
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

 
# portfolio password section
from django.http import FileResponse
from django.http import Http404

CURRENT_PASSWORD = "123"


def blur_image_view(request, image_id):
    print("blur_image_view")
    try:
        obj = Controller.objects.get(id=image_id)
        img = open(obj.blurController.path, "rb")
        return FileResponse(img)
    except Controller.DoesNotExist:
        raise Http404("image dies not exits")



def image_view(request, password, image_id):
    print("image_view")
    if password == CURRENT_PASSWORD:
        obj = Controller.objects.get(id=image_id)
        img = open(obj.originalController.path, "rb")
        response = FileResponse(img)
        return response
    else:
        raise Http404()

def check_password_image(request, password):
    if password == CURRENT_PASSWORD:
        return HttpResponse()
    else:
        raise Http404()
# ---------------------------------
def blur_image_view_01(request, image_id):
    try:
        obj = EmbeddedLinux.objects.get(id=image_id)
        img = open(obj.blurEmbeddedLinux.path, "rb")
        return FileResponse(img)
    except Controller.DoesNotExist:
        raise Http404("image dies not exits")

def image_view_01(request, password, image_id):
    if password == CURRENT_PASSWORD:
        obj = EmbeddedLinux.objects.get(id=image_id)
        img = open(obj.originalEmbeddedLinux.path, "rb")
        response = FileResponse(img)
        return response
    else:
        raise Http404()
# ---------------------------------
def blur_image_view_02(request, image_id):
    try:
        obj = PcbDesigning.objects.get(id=image_id)
        img = open(obj.blurPcbDesigning.path, "rb")
        return FileResponse(img)
    except Controller.DoesNotExist:
        raise Http404("image dies not exits")

def image_view_02(request, password, image_id):
    if password == CURRENT_PASSWORD:
        obj = PcbDesigning.objects.get(id=image_id)
        img = open(obj.originalPcbDesigning.path, "rb")
        response = FileResponse(img)
        return response
    else:
        raise Http404()
# ---------------------------------
def blur_image_view_03(request, image_id):
    try:
        obj = WebApp.objects.get(id=image_id)
        img = open(obj.blurWebApp.path, "rb")
        return FileResponse(img)
    except Controller.DoesNotExist:
        raise Http404("image dies not exits")

def image_view_03(request, password, image_id):
    if password == CURRENT_PASSWORD:
        obj = WebApp.objects.get(id=image_id)
        img = open(obj.originalWebApp.path, "rb")
        response = FileResponse(img)
        return response
    else:
        raise Http404()



def projects(request, password=False) :
    controllervar = Controller.objects.all()
    EmbeddedLinuxvar = EmbeddedLinux.objects.all()
    PcbDesigningvar = PcbDesigning.objects.all()
    WebAppvar = WebApp.objects.all()

    original_image = False
    if password == CURRENT_PASSWORD:
        original_image = True

    original_image_01 = False
    if password == CURRENT_PASSWORD:
        original_image_01 = True

    original_image_02 = False
    if password == CURRENT_PASSWORD:
        original_image_02 = True

    original_image_03 = False
    if password == CURRENT_PASSWORD:
        original_image_03 = True
        

    return render(
        request,
        "trail.html",
        {
            "controllervar": controllervar,
            "EmbeddedLinuxvar": EmbeddedLinuxvar,
            "PcbDesigningvar": PcbDesigningvar,
            "WebAppvar": WebAppvar,
            "original_image": original_image,
            "original_image_01": original_image_01,
            "original_image_02": original_image_02,
            "original_image_03": original_image_03,
            "password": password,
        },
    )
    # return render(request,'trail.html' , {'titles':'trail'})

@api_view(['GET'])
def getApiprojectDetails(request, data, idx):
    if data == 'controllerr':
        s = Controller.objects.filter(id=idx).values('title', 'blurController', 'originalController', 'description', 'html_code')
        return Response(s)
    elif data=='embeddedlinux':
        s = EmbeddedLinux.objects.filter(id=idx).values('title', 'blurEmbeddedLinux', 'originalEmbeddedLinux', 'description', 'html_code')
        return Response(s)
    elif data == 'pcb':
        s = PcbDesigning.objects.filter(id=idx).values('title', 'blurPcbDesigning', 'originalPcbDesigning', 'description', 'html_code')
        return Response(s)
    elif data == 'web':
        s = WebApp.objects.filter(id=idx).values('title', 'blurWebApp', 'originalWebApp', 'description', 'html_code')
        return Response(s)
    
        

# def portfolio1(request) :
#     if request.method == 'POST':
#         port_username = request.POST.get('port_username')
#         port_email = request.POST.get('port_email')
#         port_subject = request.POST.get('port_subject')
#         port_message = request.POST.get('port_message')

#         info = 'Username :' + str(port_username) +'\n'+ 'Email : ' + str(port_email) + '\n'+ 'Subject:' +str(port_subject) + '\n' + 'Message : ' + str(port_message) + '\n\n\n'
#         file = open('/home/omnixone/omnix_one/contact/portfolio_contact.txt', 'a')
#         file.write(info)
#         messages.success(request, 'Message Sent !!! We will answer as soon as possible...')

#     controllerr = Controller.objects.all()
#     embeddedlinuxx = EmbeddedLinux.objects.all()
#     pcbdesigningg = PcbDesigning.objects.all()
#     webappp = WebApp.objects.all()
#     return render(request,'simple_portfolio1.html',{'controllerr': controllerr ,'embeddedlinuxx': embeddedlinuxx,'pcbdesigningg': pcbdesigningg,'webappp': webappp})
#     # return render(request,'simple_portfolio.html' , {'titles':'simple portolio'})

def home(request) :
    # controllerr = Controller.objects.all()
    # embeddedlinuxx = EmbeddedLinux.objects.all()
    # pcbdesigningg = PcbDesigning.objects.all()
    # webappp = WebApp.objects.all()
    # return render(request,'home.html',{'controllerr': controllerr ,'embeddedlinuxx': embeddedlinuxx,'pcbdesigningg': pcbdesigningg,'webappp': webappp})
    return render(request,'home.html' , {'titles':'home'})
