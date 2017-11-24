from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from mentorapp.forms import StudentForm, MentorForm
from mentorapp.models import Student, Mentor, TestModel


def index(request):
    context_dict = {'boldmessage' : "I am a bold message"}
    return render(request,'mentorapp/index.html',context_dict)


def about(request) :
    return HttpResponse("This is the about page <br/> <a href='/mentor/'>Home</a>")


def registerStudent(request) :
    # A HTTP POST?
    if request.method == 'POST':
        form = StudentForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = StudentForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'mentorapp/index.html', {'form': form, 'valid' : False})




def registerMentor(request) :
    # A HTTP POST?
    if request.method == 'POST':
        form = MentorForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print (form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = MentorForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).

    return render(request, 'mentorapp/index.html', {'form': form, 'valid' : False})

def welcome(request):
    context_list=Mentor.objects.all()
    username = request.POST.get('user')
    password = request.POST.get('pass')
    for i in context_list :
        print('username is ' + i.username)
        print('password is ' +i.password)
    user = myauthenticate(username=username, password=password)
    print(user)

    if user is not None:
        #auth.login(request,user)
        user.isAuthenticated = True
        context_list = {'user' : user}
        return render(request,"mentorapp/home.html",context_list)
    else:
        return HttpResponseRedirect('/mentor/failed')


def failed_login(request):
    context_list={}
    return render(request,"mentorapp/failed.html",context_list)

def mysession(request):
    context_list={}
    return render(request,"mentorapp/mysession.html",context_list)

def apply(request):
    context_list={}
    return render(request,"mentorapp/application.html",context_list)

def course(request):
    context_list={}
    return render(request,"mentorapp/course.html",context_list)

def myauthenticate(username,password):
    context_list=Mentor.objects.all()
    flag=False
    flag2 = False
    for i in context_list :
        #   print(i.username)
        if(i.username==username):

             flag = True
             user = i
             break

    if not flag:
        print('Username not found')
        return None

    elif user.password == password :
        flag2 = True


    if flag == True and flag2 == True:
        return user

def home(request):
    context_list={}
    return render(request,"mentorapp/home.html",context_list)

def search(request):
    context_list={}
    return render(request,"mentorapp/search.html",context_list)

def profile(request):
    context_list={}
    return render(request,"mentorapp/profile.html",context_list)



#
# def apply(request):
#     context_list={}
#     return render(request,"mentorapp/apply.html",context_list)

# def search(request):
#     context_list={}
#
#     key = request.POST.get('key')
#
#     mentor_list = Mentor.objects.all()
#
#     li = []
#     for ob in mentor_list :
#         if(ob.tag==key) :
#             li.append(ob)
#
#     context_list = {'results' : li}
#
#     return render(request,"mentorapp/search.html",context_list)

def logout(request) :
    # for i in Mentor.objects.all() :
    #     i.isAuthenticated=False
    #
    # for i  in Student.objects.all() :
    #     i.isAuthenticated = False

    context_list = {}

    return render(request,"mentorapp/index.html",context_list)
