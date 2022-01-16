from django.http import HttpResponse
from .models import AllCourses, Details
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from App1.models import AllCourses


def Courses(request):
    ac = AllCourses.objects.all()
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        user.save()
        selected_courses = user.allcourses_set.all()
        if request.method == "POST":
            # user = request.user
            selected_courses = request.POST.getlist('course')
            for sc in selected_courses:
                course = AllCourses.objects.get(courseName=sc)
                user.allcourses_set.add(course)  # either works
                # course.user.add(user)#either works
        return render(request, "App1/Courses.html", {'ac': ac, 'sc': user.allcourses_set.all()})

    else:
        return render(request, "App1/Courses.html", {'ac': ac})


def removecourse(request):
    user = User.objects.get(username=request.user.username)
    courses_to_remove = request.POST.getlist('course')
    for ec in courses_to_remove:
        course = AllCourses.objects.get(courseName=ec)
        user.allcourses_set.remove(course)  # either works
    return redirect("/")
    # return render(request, "App1/Courses.html", {'ac': AllCourses.objects.all(), 'sc': user.allcourses_set.all()})


# return HttpResponse('<h1>CS LAB ROCKS! </h1>')
@login_required
def detail(request, course_id):
    course = get_object_or_404(AllCourses, pk=course_id)
    template = loader.get_template('App1/Detail.html')
    context = {
        'course': course,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'App1/Detail.html')


# return render (request, 'App1/Detail.html', {'course':course})
# return HttpResponse('<h2> These are the course details for course: ' + str(course_id) + '</h2>')

def yourchoice(request, course_id):
    course = get_object_or_404(AllCourses, pk=course_id)
    try:
        selected_ct = course.details_set.get(pk=request.POST['choice'])
    except(KeyError, AllCourses.DoesNotExist):
        template = loader.get_template('App1/Detail.html')
        context = {
            'course': course,
            'error_message': 'select a valid option'
        }
        return HttpResponse(template.render(context, request))
        # return render(request, 'App1/Detail.html', {
        #     'course': course,
        #     'error_message': 'select a valid option'
        # })
    else:
        selected_ct.your_choice = True
        selected_ct.save()
        template = loader.get_template('App1/Detail.html')
        context = {
            'course': course,
        }
        return HttpResponse(template.render(context, request))
