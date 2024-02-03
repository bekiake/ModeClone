from django.db import models

# Create your models here.

class Teacher(models.Model):
    
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    modme_id = models.IntegerField(unique=True)
    branch = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.modme_id
    
    

class Groups(models.Model):
    
    group_id = models.IntegerField()
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField()
    CHOISE_WEEK = (
        ('Odd days','Odd days'),
        ('Even days','Even days')
    )
    lesson_week_time = models.CharField(choices = CHOISE_WEEK,max_length=20)
    
    lesson_time = models.CharField(max_length=6)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.group_id
    


class Student(models.Model):
    
    name = models.CharField(max_length=255)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    status_payment = models.BooleanField(default=True)
    modme_id = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    activated_at = models.DateTimeField(auto_now=True)
    coins = models.IntegerField(default=0)
    note = models.TextField()
    password = models.CharField(max_length=255)
    
    
    def __str__(self) -> str:
        return self.modme_id



class Parents(models.Model):
    
    name = models.CharField(max_length=255)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name
    
    
    
    