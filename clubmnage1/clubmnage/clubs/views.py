from django.shortcuts import render
from .models import *

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    event = Events.objects.all()
    ind = Index_content.objects.all()
    context ={'events':event,'ind':ind}
    return render(request, "club/index.html", context=context)

def gallery(request):
    clb = Club.objects.all()
   
    return render(request, 'club/gallery.html',{'clb': clb })

def photos(request, alb_name):
    if(Club.objects.filter(club_name = alb_name)):

        pts = Gallery.objects.filter(clbs__club_name = alb_name)
    return render(request,'club/imagess.html', {'pts': pts})


def club_page(request):
    club = Club.objects.all()
    context ={"club":club}
    return render(request,'club/club.html', context=context) 


def members(request,club_name):
    if(Club.objects.filter(club_name=club_name)):
        mem=Club_members.objects.filter(club__club_name=club_name)
        name = Club.objects.filter(club_name=club_name).values_list('club_name',flat=True)
        images = get_object_or_404(Club, club_name=club_name)
        context = {'mem':mem,'name':name,'im':images}
        return render(request,'club/members.html',context=context)
    else:
        return redirect('clubpage')
    


    

def about(request):

    return render(request, 'club/about.html')    
