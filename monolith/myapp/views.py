from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .models import Work, File, Notes
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .functions import handle_uploaded_file 
from .forms import FileForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import textForm
from django.http import JsonResponse
import json
from .encoder import Show_pageListEncoder, Show_pageDetailsDetailEncoder, WorksListEncoder, Show_WorksDetailEncoder

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
        ret = []
        for n in range(len(posts)):
            ret.append({
                "filepath":posts[n].filepath.__str__(),
                "user":posts[n].author.__str__(),
                "name":posts[n].name
            })

        return JsonResponse(
            ret,
            encoder=WorksListEncoder,
            safe=False
        )
    else:
        content = json.loads(request.body)
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
                "user":posts.author.__str__(),
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
# def search_results(request):
#     posts= File.objects.all()

#     notes=Notes.objects.all()
#     if request.method=="POST":
#         form= textForm(request.POST)
#         if form.is_valid():
#             note=form.save(False)
#             note.author=request.user
#             note.save()
#             return redirect("make_notes")
#     else:
#         form = textForm()
#     search_post = request.GET.get('search')
#     if search_post:
#         posts = File.objects.filter (name__icontains=search_post)
#         print(posts)
#     else:
#         posts = File.objects.all()
#     context={
#          "posts":posts,
#          "notes":notes,
#          "form":form,
#     }
#     return render(request, "pages/Published_works.html", context)   


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

def make_notes(request):
    notes= Notes.objects.all()
    if request.method=="POST":
        form= textForm(request.POST)
        if form.is_valid():
            note=form.save(False)
            note.author=request.user
            note.save()
    else:
        form = textForm()
        
    context= {
        "form":form,
        "notes": notes
    }
    return render(request, "pages/notes.html", context)

def edit_post(request, id):
    post=get_object_or_404(Notes, id=id)
    # Get the object that we want to edit
    if request.method == "POST":
        form= textForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        redirect('make_notes')
    else:
        form=textForm(instance=post)
    context={
         "post_object":post,
         "post_form":form,
    }
    return render(request, "pages/edit.html",context)

@login_required
def favorites_add(request, id):
    file=get_object_or_404(File,id=id)
    # if file.favorites.filter(id=request.user.id).exists():
    #     file.favorites.remove(request.user)
    # else:
    file.favorites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def favorites_list(request, id):
    notes=Notes.objects.all()
    favorites= File.objects.filter(favorites=request.user)
    context = {
        "favorites": favorites,
        "notes": notes
    }
    return render(request,"pages/toread.html",context )

def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            first= form.cleaned_data["first_name"]
            from_email = form.cleaned_data["email_address"]
            message = form.cleaned_data['message']
            try:
                send_mail(first, message, from_email, ["gabbyburgard@the-gabby.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("show_page")
    return render(request, "pages/contact.html", {"form": form})



