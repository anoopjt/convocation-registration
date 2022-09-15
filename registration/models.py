from django.db import models

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

def validate_photo(photo):
    width, height = get_image_dimensions(photo)
    if width < 99 or height < 128:
        raise ValidationError("Dimensions of the applicant photo must be at least 99x128 pixels (width x height)")
    if width > 495 or height > 640:
        raise ValidationError("Dimensions of the applicant photo cannot be at greater than 495x640 pixels (width x height)")

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    salutation = models.CharField(max_length=4,choices=[('Mr.', 'Mr.'),
                                                         ('Ms.', 'Ms.'),
                                                        ('Mrs.','Mrs.')],
                                  default='',)
    full_name = models.CharField('Full Name', max_length=200)
    registration_number = models.CharField('Registration Number', max_length=9)
    programme = models.CharField('Programme', max_length=3, choices=[('CSE','Computer Science & Engineering'), ('ECE', 'Electronics & Communication Engineering')], default='')
    personal_email = models.EmailField('Email address (Personal)', max_length=200, default='')
    institute_email = models.EmailField('Email address (Institute)', max_length=200, default='')
    mobile_number = models.CharField('Phone number', max_length=20, default='')
    address = models.TextField('Address for communication', max_length=500, default='')
    city = models.CharField('City', max_length=100, default='')
    state = models.CharField('State', max_length=50, default='')
    postal_code = models.PositiveIntegerField('Postal Code', default=0)
    country = models.CharField('Country', max_length=100, default='')
    photo = models.ImageField('Photo of Candidate', upload_to='photos', default='', validators=[validate_photo])
    mode_of_attendance = models.CharField('I will attend the convocation in person', max_length=12,choices=[('Yes', 'Yes'),
                                                         ('No', 'No')],
                                  default='Yes')
    pursuing = models.CharField('I am pursuing', max_length=20,choices=[('Higher Studies', 'Higher Studies'),
                                                                        ('Job', 'Job'),
                                                                        ('Others', 'Others')],
                                default='')
    details_of_pursuing = models.TextField('Details of Higher Studies/Job/Others', max_length=500, default='')
    transaction_number = models.CharField('Payment transaction number', max_length=30, default='')
    transaction_date = models.DateField('Date on which transaction was done', default='2022-09-01')
    amount = models.PositiveSmallIntegerField('Fees paid (amount)', default=0)
    declaration = models.BooleanField('I agree to all the instructions given here', default=False)
