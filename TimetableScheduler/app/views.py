from django.shortcuts import render

# Create your views here.

def dashboard(request):
    """
    Renders the dashboard page.
    """
    # In a real application, you would pass context data here.
    # context = {'total_classes': 150, 'active_faculties': 25, ...}
    return render(request, 'dashboard.html')

def faculties(request):
    """
    Renders the faculties management page.
    """
    return render(request, 'faculties.html')

def subjects(request):
    """
    Renders the subjects management page.
    """
    return render(request,  'subjects.html')

def classrooms(request):
    """
    Renders the classrooms management page.
    """
    return render(request, 'classrooms.html')

def batches(request):
    """
    Renders the batches management page.
    """
    return render(request, 'batches.html')

def constraints(request):
    """
    Renders the constraints management page.
    This corresponds to the file currently in the Canvas.
    """
    return render(request, 'constraints.html')

def timetable(request):
    """
    Renders the timetable management page.
    """
    return render(request, 'timetable.html')
