from django.http import HttpResponse
from django.shortcuts import render
from mentorapp.forms import StudentForm, MentorForm

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
    return render(request, 'mentorapp/registerStudent.html', {'form': form})




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
    return render(request, 'mentorapp/registerMentor.html', {'form': form})
