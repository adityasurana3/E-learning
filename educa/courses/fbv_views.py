from django.shortcuts import redirect, render, get_object_or_404
from .models import Course, Subject

def course_list(request):
    if request.user.is_authenticated:
        courses = Course.objects.filter(owner=request.user)
    else:
        courses = Course.objects.none()
    return render(request, 'courses/manage/course/list.html', {'courses': courses})


def course_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            slug = request.POST.get('slug')
            overview = request.POST.get('overview')
            subject_id = request.POST.get('subject_id')
            subject = get_object_or_404(Subject, pk=subject_id)
            Course.objects.create(
                owner=request.user,
                subject=subject,
                title=title,
                slug=slug,
                overview=overview
            )
            return redirect('manage_course_list')
        return render(request, 'courses/manage/course/form.html')
    else:
        return redirect('login')
    
def course_update(request, course_id):

    if request.user.is_authenticated:
        course = Course.objects.get(pk = course_id, owner = request.user)
        if request.method == 'POST':
            course.title = request.POST.get('title', course.title)
            course.slug = request.POST.get('title', course.slug)
            course.overview = request.POST.get('title', course.overview)
            subject_id = Subject.objects.get(pk=request.POST.get('subject_id', None))
            if subject_id:
                course.subject = get_object_or_404(Subject, pk=subject_id)
            course.save()
            return redirect('manage_course_list')
        else:
            return render(request, 'course_update.html', {'course': course})
    else:
        return redirect("login")
    
def course_delete(request, course_id):
    if request.user.is_authenticated:
        if request.method == 'DELETE':
            course = Course.objects.get(pk = course_id)
            course.delete()
            return redirect('manage_course_list')
    else:
        return redirect("login")
    


