from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm,PostForm,NeighbourhoodForm,BusinessForm
from .models import User,Profile,Post,Neighborhood,Business

# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    neighbors =Neighborhood.objects.all()
    # profile = Profile.objects.filter(user=current_user).first()
    return render(request,'all-neighbours/index.html',{'neighbor':neighbors})
 
    # posts= Post.objects.all().order_by("posted_date")
    # return render(request, 'all-neighbours/index.html',{"posts":posts})


@login_required(login_url='/accounts/login/')
def neighborhood(request,neighborhood_id):
    
    current_user = request.user
    neighbors = Neighborhood.objects.get(id=neighborhood_id)
    business = Business.objects.filter(neighborhood = neighbors.id).all()
    posts = Post.objects.filter(neighborhood = neighbors.id).all()
    profile = Profile.objects.filter(id=current_user.id).first()
    
    return render(request,'all-neighbours/hood.html',{'business':business,'neighbors':neighbors,'post':posts,'neighborhood_id':neighborhood_id})
 
@login_required(login_url='/accounts/login/')
def new_business(request):

    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business_post = form.save(commit=False)
            business_post.user = current_user
            business_post.save()
            return redirect('index')
    else:
        form = BusinessForm()
        return render(request,'all-neighbours/new_business.html',{"form": form})

# @login_required(login_url='/accounts/login/')
# def view_business(request,neighborhood_id):
#     current_user = request.user
#     neighbors = Neighborhood.objects.get(id=neighborhood_id)
#     business = Business.objects.filter(neighborhood = neighbors.id).all()
#     return render(request,'all-neighbours/business.html',{'business':business,'neighbor':neighbors})

@login_required(login_url='/accounts/login/')
def new_post(request):

    current_user = request.user
    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request,'all-neighbours/post_form.html',{"form":form})

def profile(request,user_id ):

    current_user = request.user.username
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('index')

    else:
        form = UpdateProfileForm()

    user=User.objects.all()

    post = Post.objects.filter(user__username=current_user)


    profile = Profile.objects.filter(user__username = current_user)

    return render(request,"all-neighbours/profile.html",{"user":user,"profile":profile,"post":post})

# @login_required(login_url='/accounts/login/')
# def update_profile(request):

#     current_user=request.user
#     if request.method =='POST':
#         if Profile.objects.filter(user_id=current_user).exists():
#             form = UpdateProfileForm(request.POST,request.FILES,instance=Profile.objects.get(user_id = current_user))
#         else:
#             form=UpdateProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#           profile=form.save(commit=False)
#           profile.user=current_user
#           profile.save()
#           return redirect('profile',current_user.id)
#     else:

#         if Profile.objects.filter(user_id = current_user).exists():
#            form=UpdateProfileForm(instance =Profile.objects.get(user_id=current_user))
#         else:
#             form=UpdateProfileForm()

#     return render(request,'all-neighbours/update_profile.html',{"form":form}) 




#