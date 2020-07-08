from django.db import models

class Staffregistration(models.Model):
    name = models.CharField(max_length=255)
    staffid = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    emailid = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    mobileno = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    def __str__(self):
        return (str(self.name)+ "- [" + str(self.faculty) +"]")

class Studentregistration(models.Model):
    name = models.CharField(max_length=255)
    studentid = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)
    emailid = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    mobileno = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    def __str__(self):
        return (str(self.name) + "- [" + str(self.faculty) + "]")


class Query(models.Model):
    token = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    staffregistration = models.ForeignKey(Staffregistration, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.name) + "- [" + str(self.email) + "]")


class Query2(models.Model):
    token = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    studentregistration = models.ForeignKey(Studentregistration, on_delete=models.CASCADE)
    def __str__(self):
        return (str(self.name) + "- [" + str(self.email) + "]")
