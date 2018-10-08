from django.contrib import admin

# Register your models here.
from .models import Employee, Student, Course, Trainer, Product, Institute

class AEmployee(admin.ModelAdmin):
	list_display=['ename','esal','eloc','date_of_join']
class AStudent(admin.ModelAdmin):
	list_display=['sname','sage','sfname','scollege']
class ACourse(admin.ModelAdmin):
	list_display=['cname','cfee','cduration']
class ATrainer(admin.ModelAdmin):
	list_diaplay=['tname','tqual','tmarritalstatus']
class AProduct(admin.ModelAdmin):
	list_diaplay=['pname','pcost','pexpdate']
class AInstitute(admin.ModelAdmin):
	list_display=['iname','iloc','ihead']

admin.site.register(Employee,AEmployee)
admin.site.register(Student,AStudent)
admin.site.register(Course,ACourse)
admin.site.register(Trainer,ATrainer)
admin.site.register(Product,AProduct)
admin.site.register(Institute,AInstitute)