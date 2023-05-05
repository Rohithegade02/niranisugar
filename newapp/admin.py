from django.contrib import admin

from .models import employee, department, account, attendance, leave_application, leavetype, employee_shift, shift

admin.site.register(employee)
admin.site.register(department)
admin.site.register(attendance)
admin.site.register(leave_application)
admin.site.register(leavetype)
admin.site.register(account)
admin.site.register(shift)
admin.site.register(employee_shift)



