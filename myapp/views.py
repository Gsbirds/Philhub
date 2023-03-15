from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .models import Work, File, Notes
from django.contrib.auth.decorators import login_required
from .functions import handle_uploaded_file 
from .forms import FileForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import textForm
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

def search_results(request):
    posts= File.objects.all()
    notes=Notes.objects.all()
    if request.method=="POST":
        form= textForm(request.POST)
        if form.is_valid():
            note=form.save(False)
            note.author=request.user
            note.save()
            return redirect("make_notes")
    else:
        form = textForm()
    search_post = request.GET.get('search')
    if search_post:
        posts = File.objects.filter (name__icontains=search_post)
        print(posts)
    else:
        posts = File.objects.all()
    context={
         "posts":posts,
         "notes":notes,
         "form":form,
    }
    return render(request, "pages/Published_works.html", context)   

# def see_notes(request):
#     notes= Notes.objects.all()
#     context = {
#         "notes": notes
#     }
#     return render(request,"pages/notes.html",context )
def make_notes(request):
    notes= Notes.objects.all()
    if request.method=="POST":
        form= textForm(request.POST)
        if form.is_valid():
            note=form.save(False)
            note.author=request.user
            note.save()
            return redirect("make_notes")
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
    if file.favorites.filter(id=request.user.id).exists():
        file.favorites.remove(request.user)
    else:
         file.favorites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def favorites_list(request, id):
    favorites= File.objects.filter(favorites=request.user)
    context = {
        "favorites": favorites
    }
    return render(request,"pages/toread.html",context )

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'gabbyburgard@yahoo.com', ['gabbyburgard@yahoo.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("show_page")
      
	form = ContactForm()
	return render(request, "pages/contact.html", {'form':form})

