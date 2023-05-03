from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .models import Work, File, Notes, Author, Topic
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .functions import handle_uploaded_file 
from .forms import FileForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import textForm
from django.http import JsonResponse
import json
from .encoder import Show_NotesDetailEncoder, Show_pageListEncoder, Show_pageDetailsDetailEncoder, WorksListEncoder, Show_ContactEncoder, Show_WorksDetailEncoder, Show_NotesListEncoder

@require_http_methods(["GET", "POST"])
def show_page(request):
    if request.method=="GET":
        news = News.objects.all()   
        return JsonResponse(
            {"news": news},
            encoder=Show_pageListEncoder,
            )
    else:
        content = json.loads(request.body)

        news = News.objects.create(**content)
        return JsonResponse(
            news,
            encoder=Show_pageListEncoder,
            safe=False,
        )
    
@require_http_methods(["GET", "DELETE", "PUT"])
def show_page_details(request, id):
    if request.method == "GET":
        news = News.objects.get(id=id)
        return JsonResponse(
            news, encoder=Show_pageDetailsDetailEncoder, safe=False
        )
    elif request.method == "DELETE":
        count, _ = News.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        News.objects.filter(id=id).update(**content)
        news = News.objects.get(id=id)
        
        return JsonResponse(
            news,
            encoder=Show_pageDetailsDetailEncoder,
            safe=False,
        )
 
def redirect_to_page(request):
    return redirect("show_page")

@require_http_methods(["GET", "POST"])
def api_list_works(request):
    if request.method == "GET":
        posts = File.objects.all()
        return JsonResponse(
            {"posts":posts},
            encoder=WorksListEncoder
        )
    else:
        content = json.loads(request.body)
        try:
            author=content["author"]
            author = Author.objects.get(first_name=author)
            content["author"] = author
        except Author.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Author"},
                status=404,
                )
        try:
            topic=content["topic"]
            topic = Topic.objects.get(name=topic)
            content["topic"] = topic
        except Topic.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid Author"},
                status=404,
                )
        
        posts = File.objects.create(**content)
        return JsonResponse(
            posts,
            encoder=WorksListEncoder,
            safe=False,
        )

@require_http_methods(["GET", "PUT", "DELETE"])
def api_show_works(request, id):
    if request.method == "GET":
        posts = File.objects.get(id=id)
        return JsonResponse(
            {"filepath":posts.filepath.__str__(),
                "name":posts.name}, encoder=Show_pageDetailsDetailEncoder, safe=False
        )
    elif request.method == "DELETE":
        count, _ = File.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        File.objects.filter(id=id).update(**content)
        posts = File.objects.get(id=id)
        
        return JsonResponse(
            posts,
            encoder=Show_WorksDetailEncoder,
            safe=False,
        )

@login_required
def showfile(request):
    form= FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        uploads=form.save(False)
        uploads.author=request.user
        uploads.save()
        return redirect("your_uploads")
    context= { 
              'form': form
              }
      
    return render(request, 'pages/files.html', context)

@login_required
def showuploads(request):
    uploads= File.objects.filter(author=request.user)
    if request.method=="POST":
        form= textForm(request.POST)
        if form.is_valid():
            note=form.save(False)
            note.author=request.user
            note.save()
            return redirect("make_notes")
    else:
        form = textForm()
    context = {
        "uploads":uploads,
        "form":form,
    }
    return render(request,"pages/uploads.html",context )

def redirect_to_page(request):
    return redirect("show_page")

@require_http_methods(["GET", "POST"])
def api_list_notes(request):
    if request.method == "GET":
        notes = Notes.objects.all()
        return JsonResponse(
            {"notes": notes},
            encoder=Show_NotesListEncoder,
        )

    else:
        content = json.loads(request.body)
        notes = Notes.objects.create(**content)
        return JsonResponse(
            notes,
            encoder=Show_NotesListEncoder,
            safe=False,
        )
    
@require_http_methods(["GET", "PUT", "DELETE"])
def api_notes_detail(request, id):
    if request.method == "GET":
        posts = File.objects.get(id=id)
        return JsonResponse(
            posts, encoder=Show_NotesDetailEncoder, safe=False
        )
    elif request.method == "DELETE":
        count, _ = Notes.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        Notes.objects.filter(id=id).update(**content)
        posts = Notes.objects.get(id=id)
        
        return JsonResponse(
            posts,
            encoder=Show_NotesDetailEncoder,
            safe=False,
        )
# @require_http_methods(["POST"])
# def contact(request):       
#     # if request.method == "GET":
#     #     form = ContactForm()
#     # else:
#     form = ContactForm(request.POST)
#     if form.is_valid():
#         first= form.cleaned_data["first_name"]
#         email = form.cleaned_data["email_address"]
#         message = form.cleaned_data['message']
#         try:
#             send_mail(first, message, email, ["gabbyburgard@the-gabby.com"])
#             content = json.loads(request.body)
#             contact = ContactForm.objects.create(**content)
#             return JsonResponse(
#                 contact,
#                 encoder=Show_NotesDetailEncoder,
#                 safe=False,
#                 )

#         except BadHeaderError:
#             return HttpResponse("Invalid header found.")
        
@require_http_methods(["POST"])
def contact(request):
    if request.method == "POST":
        # serializer = Show_ContactEncoder()
        # if serializer.is_valid():
        #     first_name = request.POST['first_name']
        #     email = request.POST['email_address']
        #     message = request.POST['message']
        form = ContactForm(request.POST)

        if form.is_valid():
            first_name= form.cleaned_data["first_name"]
            email = form.cleaned_data["email_address"]
            message = form.cleaned_data['message']

        # if request.method=="POST":
        #     form= ContactForm(request.POST)
        #     if form.is_valid():
        #         note=form.save(False)
        #         note.save()

            # send mail
            send_mail(
                'Contact Form mail from ' + first_name,
                message,
                email,
                ["gabbyburgard@the-gabby.com"],
            )
            form.save()
            return JsonResponse(
                form,
                encoder=Show_ContactEncoder,
                safe=False,
                status=200
            )
        # else:
        #     return JsonResponse(
        #         status=400
        #     )
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            # content = json.loads(request.body)
            # Notes.objects.filter(id=id).update(**content)
            # posts = ContactForm.objects.get(id=id)
        
            # return JsonResponse(
            #     posts,
            #     encoder=Show_NotesDetailEncoder,
            #     safe=False,
            # )


        # content = json.loads(request.body)
        # Notes.objects.filter(id=id).update(**content)
        # posts = ContactForm.objects.get(id=id)
        
        # return JsonResponse(
        #     posts,
        #     encoder=Show_NotesDetailEncoder,
        #     safe=False,
        # )