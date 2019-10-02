import os
from os import system
from django.shortcuts import render
from .models import images
from .forms import *
from django.core.files.storage import FileSystemStorage


def Home(request):
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)

        if form.is_valid():

            # this code save in 'media/'
            file_one = request.FILES['content_image']
            file_two = request.FILES['style_image']

            fs = FileSystemStorage()
            ext1 = file_one.name[-4:]
            ext2 = file_two.name[-4:]

            file_two_ext = file_two.name[-4]
            fs.save('content_image'+ext1, file_one)
            fs.save('style_image'+ext2, file_two)

            context = {'Final_image':'True'}
            system('python Demo\\turtle.py')
        return render(request, 'final.html', context)

    else:

        form = imageForm()
        context = {'form':form}
        return render(request, 'Home.html',context)





















# def Home(request):
#      if request.method == 'POST':
#         form = imageForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             data = images(Title = form.cleaned_data['Title'],
#             content_image = form.cleaned_data['content_image'],
#             style_image = form.cleaned_data['style_image']
#             )
#             # data.title = form.cleaned_data['Title']
#             # data.image1 = form.cleaned_data['content_image']
#             # data.image2 = form.cleaned_data['style_image']
#             data.save()
#         return HttpResponse('successfuly uploaded')
#
#      else:
#
#         form = imageForm()
#
#      return render(request,"Home.html",{'form':form})

#
# def Uploads(request):
#      if request.method == 'POST':
#         form = images(request.POST)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     context = {}
#
#     return render(request,"Home.html",context)































        # this code save in 'media/'
        # file_one = request.FILES['content_image']
        # file_two = request.FILES['style_image']
        #
        # fs = FileSystemStorage()
        #
        # name_one = fs.save(file_one.name, file_one)
        # name_two = fs.save(file_two.name, file_two)
