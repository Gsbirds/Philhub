from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile, Friend, Collab
from django.http import JsonResponse
import json
from .encoder import Show_profileEncoder
from django.views.decorators.http import require_http_methods
# Create your views here.
# @login_required
@require_http_methods(["GET", "DELETE", "PUT"])
def show_profile(request):
    if request.method == "GET":
        profile = Profile.objects.get(name="gabby")
        return JsonResponse(
            {"profile":profile,
             "paper":profile.paper.filepath.__str__(),
             "picture":profile.picture
                }, encoder=Show_profileEncoder, safe=False
        )
    elif request.method == "DELETE":
        count, _ = Profile.objects.filter(name=request.user).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)
        Profile.objects.filter(id=id).update(**content)
        posts = Profile.objects.get(id=id)
        
        return JsonResponse(
            posts,
            encoder=Show_profileEncoder,
            safe=False,
        )



        # profile= Profile.objects.get(name=request.user)
        # friends= Friend.objects.all()
        # collabs=Collab.objects.all()
        # context = {
        #     "profile": profile,
        #     "friends": friends,
        #     "collabs":collabs,
        # }
        # return render(request,"pages/profile.html", context)
    
# def show_friends(request):
#     if request.method == "GET":
#         friends= Friend.objects.all()
#         context = {
#             "friends": friends,
#         }
#         return render(request,"pages/profile.html", context)
    
    