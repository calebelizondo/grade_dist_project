from django.shortcuts import render
from django.http import JsonResponse

from grade_dist_api_app.models import Section_grades

# Create your views here.
from django.http import HttpResponse

grading_system = {'a': 4.0, 'b': 3.0, 'c': 2.0, 'd': 1.0, 'f': 0.0}

def home(request):
    return render(request, 'display.html')


def calculate_gpa(grade_counts):
    # Define your grading system here (e.g., A=4.0, B=3.0, etc.)

    total_points = 0
    total_students = 0

    for grade, count in grade_counts.items():
        total_points += grading_system.get(grade, 0) * count
        total_students += count

    if total_students == 0:
        return 0.0

    return total_points / total_students

def get_profs(request, subject_code, course_code):
    subject_code = subject_code.upper()
    course_code = course_code.upper()

    section_grades = Section_grades.objects.filter(subject_code=subject_code, course_code=course_code)

    professor_data = []

    # Group section grades by professor name
    professors = set(section_grade.professor_name for section_grade in section_grades)

    for professor in professors:
        professor_grades = section_grades.filter(professor_name=professor)
        print(professor_grades)

        # Calculate the grade distribution for the professor
        grade_distribution = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'f': 0}
        for section_grade in professor_grades:
            for grade in grading_system.keys():
                grade_distribution[grade] += getattr(section_grade, "{}_count".format(grade.lower()), 0)

        # Calculate the average GPA for the professor
        average_gpa = calculate_gpa(grade_distribution)

        professor_info = {
            'professor': professor,
            'average_gpa': average_gpa,
            'grade_distribution': grade_distribution
        }

        professor_data.append(professor_info)

    return JsonResponse(professor_data, safe=False)


def get_subject_codes(request):

    # Get all unique subject codes
    unique_subject_codes = Section_grades.objects.values('subject_code').distinct()

    # Create a dictionary to store subject codes and associated course numbers
    subject_data = []

    for subject in unique_subject_codes:
        subject_code = subject['subject_code']

        # Query the database to get unique course codes for the current subject code
        course_numbers = Section_grades.objects.filter(subject_code=subject_code).values_list('course_code', flat=True).distinct()
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

def get_eval_data(request, professor_name, subject_code, course_code):
    sections = Section_grades.objects.filter(subject_code=subject_code, course_code=course_code, professor_name=professor_name)

    answers_1 = [0, 0, 0]
    answers_2 = [0, 0, 0, 0]
    answers_3 = [0, 0, 0, 0]
    answers_4 = [0, 0, 0, 0]
    answers_5 = [0, 0, 0, 0, 0, 0]
    answers_6 = [0, 0, 0, 0, 0, 0,]

    for section in sections:
        answers_1[0] += section.answers_1_1
        answers_1[1] += section.answers_1_1
        answers_1[2] += section.answers_1_1
        answers_2[0] += section.answers_2_1
        answers_2[1] += section.answers_2_2
        answers_2[2] += section.answers_2_3
        answers_2[3] += section.answers_2_4
        answers_3[0] += section.answers_3_1
        answers_3[1] += section.answers_3_2
        answers_3[2] += section.answers_3_3
        answers_3[3] += section.answers_3_4
        answers_4[0] += section.answers_4_1
        answers_4[1] += section.answers_4_2
        answers_4[2] += section.answers_4_3
        answers_4[3] += section.answers_4_4
        answers_5[0] += section.answers_5_0
        answers_5[1] += section.answers_5_1
        answers_5[2] += section.answers_5_2
        answers_5[3] += section.answers_5_3
        answers_5[4] += section.answers_5_4
        answers_5[5] += section.answers_5_5
        answers_6[0] += section.answers_6_1
        answers_6[1] += section.answers_6_2
        answers_6[2] += section.answers_6_3
        answers_6[3] += section.answers_6_4
        answers_6[4] += section.answers_6_5
        answers_6[5] += section.answers_6_6

    return JsonResponse({
        'professor': professor_name,
        'answers': {answers_1, answers_2, answers_3, answers_4, answers_5, answers_6}
    })

