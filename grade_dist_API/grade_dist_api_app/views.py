from django.shortcuts import render
from django.http import JsonResponse

from grade_dist_api_app.models import Section

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'display.html')


def get_profs(request, subject_code, course_code):
    professors = Section.objects.filter(subject_code=subject_code.upper(), course_code=course_code).values_list('professor_name', flat=True).distinct()

    professor_data = [{'professor': prof} for prof in professors]

    return JsonResponse(professor_data, safe=False)

def get_subject_codes(request):

    # Get all unique subject codes
    unique_subject_codes = Section.objects.values('subject_code').distinct()

    # Create a dictionary to store subject codes and associated course numbers
    subject_data = []

    for subject in unique_subject_codes:
        subject_code = subject['subject_code']

        # Query the database to get unique course codes for the current subject code
        course_numbers = Section.objects.filter(subject_code=subject_code).values_list('course_code', flat=True).distinct()
        course_numbers_list = list(course_numbers)

        # Create a dictionary for the current subject code and its course numbers
        subject_info = {
            'subject_code': subject_code,
            'course_numbers': course_numbers_list,
        }

        # Add the subject info to the subject_data list
        subject_data.append(subject_info)

    # Convert the subject_data list to JSON
    return JsonResponse(subject_data, safe=False)