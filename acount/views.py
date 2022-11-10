from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile

# Create your views here.
def acount(request):
    username = ''
    password = ''
    email = ''
    full_name = ''
    erorrs_check = False
    if request.method =='POST':
        if 'signup' in request.POST:
            if request.POST['username'] and request.POST['email'] and request.POST['password'] and request.POST['name'] :
                    username = request.POST['username'] 
                    if len(username) < 5:
                        messages.warning(request, 'username is short at less 5 letters')
                        erorrs_check = True
                    if User.objects.filter(username = username):
                          messages.warning(request, 'username is exsit')
                          erorrs_check = True    
                    full_name = request.POST['name'] 
                    if len(full_name) <10:
                        messages.warning(request, 'name is short at less 10 letters')
                        erorrs_check = True
                    email = request.POST['email'] 
                    if User.objects.filter(email = email):
                          messages.warning(request, 'eamil is exsit')
                          erorrs_check = True
                    password = request.POST['password']
                    if len(full_name) <5:
                        messages.warning(request, 'password is short at less 5 cahrercter')
                        erorrs_check = True

                    if erorrs_check:
                         context = {
                         'password':password,
                         'email':email,
                         'username':username,
                         }

                         return render(request,'pages/acount.html',context)
                    else:
                      user = User.objects.create_user(username = username,password = password,email = email)
                      user.save()
                      userprofile = UserProfile(user=user,full_name=full_name)
                      userprofile.save()
                    
                    # request.session.set_expire(0) when get off browser session clock
                      auth.login(request, user)
                      return redirect('home')

            else:
              messages.warning(request, 'the fields is deleted or empty ')
              return render(request,'pages/acount.html')
      
        # login
        else:
            if request.POST['username']  and request.POST['password'] :
            
                username = request.POST['username'] 
                password = request.POST['password']

                user = auth.authenticate(username=username,password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('home')
                else:
                  messages.warning(request, 'the information is wrong try agian ')  
                  return render(request,'pages/acount.html')
            else:
              messages.warning(request, 'the fields is deleted or empty ')  
              return render(request,'pages/acount.html')
        
   
    else:

      return render(request,'pages/acount.html')
def loguot(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('home')
    else:
       return redirect('acount')
def profile(request):
    if request.user.is_authenticated:
        request.user.set_password('123123')
        request.user.save()
        auth.login(request, request.user)
        # danger pass need to auth,log(request.user)  agian it change every time
        return  render(request,'pages/index.html')
    else:
         return redirect('acount')
