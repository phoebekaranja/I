from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def welcome(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = current_user
            profile.save()
        return redirect('news-Profile')
    else:
        form = NewProfileForm()
    return render(request,'welcome.html',{'form':form})
def today(request):
    current_user = request.user
    news = Image.get_all()
    # profile = Profile.objects.get(user = current_user) 
    profile = Profile.objects.all()
    comments= Comment.objects.all()
    form = NewCommentForm()
    return render(request,'all-news/index.html',{'news':news, 'profile':profile,'profile':profile,'form':form , 'comments':comments})
