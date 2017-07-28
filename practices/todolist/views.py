from django.shortcuts import get_object_or_404,render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from .models import tobedone
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib import auth  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html', {'username': request.user.username})
	
def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('todolist:login'))
    return render(request, 'register.html', {'form': form})



@login_required
def index(request):
	#latest_task = tobedone.objects.order_by('-pub_date')[:5]
	latest_task=tobedone.objects.filter(user=request.user.username)
	context = {'latest_task': latest_task}
	return render(request,'index.html', context)
	
@login_required
def detail(request, tobedone_id):
    t = get_object_or_404(tobedone, pk=tobedone_id)
    return render(request, 'detail.html', {'tobedone': t})
	
@login_required
def add(request):
    return render(request,'add.html',{'currenttime':timezone.now()})

@login_required
def add_submit(request):
    tobedone.objects.create(user=request.POST.get('user',''),title=request.POST.get('title',''),detail=request.POST.get('detail',''),deadline=request.POST.get('deadline',''),finish=request.POST.get('finish','') ,pub_date=timezone.now())
    return HttpResponseRedirect(reverse('todolist:index'))
	
@login_required	
def update_submit(request):
	u=tobedone.objects.filter(id=request.POST.get('id',''))
	u.update(title=request.POST.get('title',''),detail=request.POST.get('detail',''),deadline=request.POST.get('deadline',''),finish=request.POST.get('finish',''))
	return HttpResponseRedirect(reverse('todolist:index'))

@login_required	
def delete_submit(request):
	t=tobedone.objects.get(pk=request.POST.get('id',''))
	t.delete()
	return HttpResponseRedirect(reverse('todolist:index'))

@login_required
def complete(request):
	completed_task=tobedone.objects.filter(finish=True).filter(user=request.user.username)
	return render(request,'complete.html',{'completed_task': completed_task})
	
@login_required
def expired(request):
	#ex=tobedone.objects.get(tobedone=True)
	ex=tobedone.objects.filter(deadline__lte=timezone.now())
	#ex=tobedone.objects.all()
	return render(request,'expired.html',{'expired_task': ex})

@login_required
def tobedoned(request):
	tobedoned_task=tobedone.objects.filter(finish=False)
	return render(request,'tobedone.html',{'tobedoned_task': tobedoned_task})

@login_required	
def logout(request):
    auth.logout(request)
    return render(request,'home.html')

@login_required	
def profile(request):
    return render(request,'profile.html')

@login_required	
def profile_submit(request):
	user=User.objects.get(username=request.POST.get('user',''))
	user.set_password(request.POST.get('password',''))
	user.save()
	user=User.objects.filter(username=request.POST.get('user',''))
	user.update(first_name=request.POST.get('first_name',''),last_name=request.POST.get('last_name',''),email=request.POST.get('email',''))
	return HttpResponseRedirect(reverse('todolist:index'))
	








