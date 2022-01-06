from django.http import HttpResponse
from .models import AllCourses, Details
from django.template import loader
from django.shortcuts import render, get_object_or_404


def Courses(request):
    ac = AllCourses.objects.all()
    template = loader.get_template('App1/Courses.html')
    context = {
        'ac': ac,
    }
    return HttpResponse(template.render(context, request))


# return HttpResponse('<h1>CS LAB ROCKS! </h1>')

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
            'error_message':'select a valid option'
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
