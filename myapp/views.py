from django.shortcuts import render, redirect
from .models import News
from .models import Work, File
from django.contrib.auth.decorators import login_required
from .functions import handle_uploaded_file 
from .forms import FileForm, SearchForm
from django.db.models import Q  #

# Create your views here.
def show_page(request):
    #get all recipes from recipes table
    news = News.objects.all()
    works= Work.objects.all()
    context = {
        "news": news,
        "works":works,
    }
    return render(request,"pages/Philhub_index.html",context )

def redirect_to_page(request):
    return redirect("show_page")

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
    
    context = {
        "uploads":uploads,
    }
    return render(request,"pages/uploads.html",context )

def redirect_to_page(request):
    return redirect("show_page")

def search_results(request):
    posts= File.objects.all()
    search_post = request.GET.get('search')
    if search_post:
        posts = File.objects.filter (name__icontains=search_post)
        print(posts)
    else:
        posts=SearchForm()
    

    return render(request, "pages/Published_works.html", {"posts":posts})   
