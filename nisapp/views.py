from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .forms import UpdateProfileForm,PostForm,NeighbourhoodForm,BusinessForm,NewProfileForm,UserUpdate
from .models import User,Profile,Post,Neighborhood,Business,Product,Join

# Create your views here.

def signUp(request):
    currentUser=request.user
    if request.method=='POST':
        form=UserUpdate(request.POST)
        
        if form.is_valid():
            user=form.save()
            
          
            #neighbour
          

            username=form.cleaned_data.get('username')
          
            
            return redirect('logIn')
    else:
        form=UserUpdate()
       

       
    return render(request,'registration/registration_form.html',{
            'form':form ,
          
        })


def logIn(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            print(user.id)
            #query join()
            # neighbors=Neighborhood.objects.filter(admin_id=user).first()
    
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                # return redirect('neighborhood',neighborhood_id=neighbors)
                return redirect('welcome')
    else:
        form=AuthenticationForm()
    return render(request,'registration/login.html',{'form':form})
def logOut(request):
    if request.method=='POST':
        logout(request)
        return redirect('logIn')
    return redirect('logIn')



# @login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    neighbors =Neighborhood.objects.all()
    profile = Profile.objects.filter(user=current_user).first()
    return render(request,'all-neighbours/welcome.html')


@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    join = Join.objects.filter(user=current_user).first()
    if (join):
        return redirect('neighborhood',neighborhood_id=join.neighborhood.id)
    neighbors =Neighborhood.objects.all()
    profile = Profile.objects.filter(user=current_user).first()
    return render(request,'all-neighbours/index.html',{'neighbor':neighbors})

@login_required(login_url='/accounts/login/')
def joinFunc(request,neighborhood_id):
    current_user = request.user
    Neighbr = Neighborhood.objects.get(id=neighborhood_id) 
    join=Join(neighborhood=Neighbr, user=current_user)
    join.save()
    # profile = Profile.objects.filter(user=current_user).first()
    return redirect('neighborhood',neighborhood_id=neighborhood_id)


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
            return redirect('viewProduct')
    else:
        form = BusinessForm()
        return render(request,'all-neighbours/new_business.html',{"form": form})

# 
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
################
@login_required(login_url='/accounts/login/')
def profile(request,user_id  ):

    current_user = request.user.username
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('welcome')

    else:
        form = UpdateProfileForm()

    user=User.objects.all()



    profile = Profile.objects.filter(user__username = current_user)

    return render(request,"all-neighbours/profile.html",{"user":user,"profile":profile})


# @login_required(login_url='/accounts/login/')
@login_required(login_url='/accounts/login/')
def update_profile(request):

    current_user=request.user
    if request.method =='POST':
        if Profile.objects.filter(user_id=current_user).exists():
            form = UpdateProfileForm(request.POST,request.FILES,instance=Profile.objects.get(user_id = current_user))
        else:
            form=UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
          profile=form.save(commit=False)
          profile.user=current_user
          profile.save()
          return redirect('profile',current_user.id)
    else:

        if Profile.objects.filter(user_id = current_user).exists():
           form=UpdateProfileForm(instance =Profile.objects.get(user_id=current_user))
        else:
            form=UpdateProfileForm()

    return render(request,'all-neighbours/update_profile.html',{"form":form}) 



# def project(request):
#     name = request.POST.get('your_name')
#     email = request.POST.get('email')

#     recipient = NewsLetterRecipients(name=name, email=email)
#     recipient.save()
#     send_welcome_email(name, email)
#     data = {'success': 'You have been successfully added to mailing list'}
#     return JsonResponse(data)
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



@login_required(login_url='/accounts/login/')
def search_product(request):
    if 'product' in request.GET and request.GET["product"]:
        search_term = request.GET.get("product")
        products = Product.search_by_prodName(search_term)
        # products = Business.search_by_businessName(search_term)
        message = f"{search_term}"
        return render(request, 'all-neighbours/search.html',{"message":message,"product":products})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-neighbours/search.html',{"message":message})

@login_required(login_url='/accounts/login/')        
def search_location(request):
    location= request.GET.get("your location")
    recipient=Neighborhood(location=location)
    recipient.save()
    search_location(location)
    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        location = Neighborhood.search_location(search_term)
        message = f"{search_term}"
        return render(request, 'all-neighbours/searchloc.html',{"message":message,"product":product})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-neighbours/searchloc.html',{"message":message})

@login_required(login_url='/accounts/login/')
def viewProduct(request):
    products = Product.get_all_products()
    
    return render(request,'all-neighbours/product.html',{"product":products})

def filter_by_business(request,business_id):
  product = Product.filter_by_business(id=business_id )
  return render (request,"all_photos/location.html", {"product":product})


@login_required(login_url='/accounts/login/')
def viewBusiness(request):
    businesses = Business.objects.all()
    
    return render(request,'all-neighbours/product.html',{"business":businesses})

@login_required(login_url='/accounts/login/')
def viewBusinessDetails(request,business_pk):
    businesses = Business.objects.get(id=business_pk)
    products = Product.objects.filter(business_id=businesses)
    return render(request,'all-neighbours/productdet.html',{"product":products,"business":businesses})


# def default_map(request):
     # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    # mapbox_access_token = 'pk.eyJ1IjoiaG9ub3JpbmUxIiwiYSI6ImNrMzdmd2QzbDBhMjgzbW11MGtscTI2OG8ifQ.ykYCnlagcATteL2taY6NfA'
    # return render(request, 'default.html', 
    #               { 'mapbox_access_token': mapbox_access_token })


