from django.db import models

# Create your models here.
class Employee(models.Model):
	ename=models.CharField(max_length=30)
	esal=models.IntegerField()
	eloc=models.CharField(max_length=20)
	date_of_join=models.DateField()

	def __str__(self):
		return self.ename

class Student(models.Model):
	sname=models.CharField(max_length=30)
	sage=models.IntegerField()
	sfname=models.CharField(max_length=30)
	scollege=models.CharField(max_length=30)

	def __str__(self):
		return self.sname

class Trainer(models.Model):
	tname=models.CharField(max_length=30)
	tqual=models.CharField(max_length=20)
	tmarritalstatus=models.CharField(max_length=20)

	def __str__(self):
		return self.tname

class Course(models.Model):
	trainer=models.ManyToManyField(Trainer)
	employee=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,blank=True)
	student=models.ForeignKey(Student,on_delete=models.SET_NULL,null=True,blank=True)
	cname=models.CharField(max_length=20)
	cfee=models.IntegerField()
	cduration=models.IntegerField()

	def __str__(self):
		return self.cname

class Product(models.Model):
	employee=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,blank=True)
	pname=models.CharField(max_length=30)
	pcost=models.IntegerField()
	pexpdate=models.DateField()

	def __str__(self):
		return self.pname

class Institute(models.Model):
	trainer=models.ForeignKey(Trainer,on_delete=models.SET_NULL,null=True,blank=True)
	iname=models.CharField(max_length=20)
	iloc=models.CharField(max_length=30)
	ihead=models.CharField(max_length=30)

	def __str__(self):
		return self.iname