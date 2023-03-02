from django.shortcuts import render, redirect
from .models import News
from .models import Work
from .forms import WorksForm
from django.contrib.auth.decorators import login_required
from .functions import handle_uploaded_file 

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

def show_works_page(request):
    works= Work.objects.all()
    context = {
        "works":works,
    }
    return render(request,"pages/Published_works.html",context )

def redirect_to_page(request):
    return redirect("show_page")

@login_required
def works_form(request):
    if request.method=="POST":
        form= WorksForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect("show_page")
    else:
        form=WorksForm()
    context={
        "form":form,
    }
    return render(request, "pages/create.html", context)
