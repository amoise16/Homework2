from django.db import models

class Student(models.Model):
  #primary key for student
  s_id = models.CharField(max_length = 13, primary_key = True)
  #student's first name
  first_name = models.CharField(max_length = 30)
  #student's last name
  last_name = models.CharField(max_length = 30)

class Instructor(models.Model):
  #primary key for instructor
  i_id = models.CharField(max_length = 13, primary_key = True)
  #instructors's first name
  first_name = models.CharField(max_length = 30)
  #instructors's last name
  last_name = models.CharField(max_length = 30)
    
class Course(models.Model):
  c_id = models.CharField(max_length = 13, primary_key = True)
  course_name = models.CharField(max_length = 30)
  i_id = models.ForeignKey(Instructor, on_delete = models.CASCADE)
  students = models.ManyToManyField(Student)
  
class QR_instructor(models.Model):
  qr_id = models.AutoField(primary_key = True)
  c_ID = models.ForeignKey(Course, on_delete = models.CASCADE)
  i_id = models.ForeignKey(Instructor, on_delete = models.CASCADE)
  qr_time = models.DateTimeField(auto_now = True)

class QR_student(models.Model):
  qr_id_u = models.ForeignKey(QR_instructor, on_delete = models.CASCADE)
  c_ID = models.ForeignKey(Course, on_delete = models.CASCADE)
  i_id = models.ForeignKey(Instructor, on_delete = models.CASCADE)
  qr_image = models.ImageField()
  qr_time_u = models.DateTimeField(auto_now = True)





