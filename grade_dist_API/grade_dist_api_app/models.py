from django.contrib.postgres.fields import ArrayField
from django.db import models

class Section_grades(models.Model):
    SEMESTER_CHOICES = [
        ('SPRING', 'Spring'),
        ('SUMMER', 'Summer'),
        ('FALL', 'Fall'),
        ('WINTER', 'Winter'),
    ]

    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    year = models.PositiveIntegerField()
    subject_code = models.CharField(max_length=4)
    course_code = models.CharField(max_length=4)
    section_code = models.CharField(max_length=4)
    professor_name = models.CharField(max_length=100)
    a_count = models.PositiveIntegerField()
    b_count = models.PositiveIntegerField()
    c_count = models.PositiveIntegerField()
    d_count = models.PositiveIntegerField()
    f_count = models.PositiveIntegerField()
    q_count = models.PositiveIntegerField()
    i_count = models.PositiveIntegerField()
    s_count = models.PositiveIntegerField()
    u_count = models.PositiveIntegerField()
    x_count = models.PositiveIntegerField()
    
    answers_1_1 = models.PositiveIntegerField()
    answers_1_2 = models.PositiveIntegerField()
    answers_1_3 = models.PositiveIntegerField()

    answers_2_1 = models.PositiveIntegerField()
    answers_2_2 = models.PositiveIntegerField()
    answers_2_3 = models.PositiveIntegerField()
    answers_2_4 = models.PositiveIntegerField()

    answers_3_1 = models.PositiveIntegerField()
    answers_3_2 = models.PositiveIntegerField()
    answers_3_3 = models.PositiveIntegerField()
    answers_3_4 = models.PositiveIntegerField()

    answers_4_1 = models.PositiveIntegerField()
    answers_4_2 = models.PositiveIntegerField()
    answers_4_3 = models.PositiveIntegerField()
    answers_4_4 = models.PositiveIntegerField()

    answers_5_0 = models.PositiveIntegerField()
    answers_5_1 = models.PositiveIntegerField()
    answers_5_2 = models.PositiveIntegerField()
    answers_5_3 = models.PositiveIntegerField()
    answers_5_4 = models.PositiveIntegerField()
    answers_5_5 = models.PositiveIntegerField()

    answers_6_1 = models.PositiveIntegerField()
    answers_6_2 = models.PositiveIntegerField()
    answers_6_3 = models.PositiveIntegerField()
    answers_6_4 = models.PositiveIntegerField()
    answers_6_5 = models.PositiveIntegerField()
    answers_6_6 = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.year} {self.semester} - {self.course_code} ({self.section_code})"
