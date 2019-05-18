from django.shortcuts import render

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
