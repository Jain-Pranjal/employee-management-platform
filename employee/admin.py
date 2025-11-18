from django.contrib import admin
from employee.models import Department, Role, Employee

admin.site.site_header = "Employee Management Admin"
admin.site.site_title = "Employee Management Admin Portal"
admin.site.index_title = "Welcome to Employee Management Portal"


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'location')
    search_fields = ('name',)
    list_filter = ('location',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','title','description')
    search_fields = ('title',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'position', 'department', 'role')
    search_fields = ('first_name', 'last_name', 'email', 'position')
    list_filter = ('department', 'role')