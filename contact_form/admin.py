from django.contrib import admin
from contact_form.models import Person,Emails_only


from import_export import resources
# ----------------------------------------------------------
# from django.contrib.auth import get_user_model
# from django.http import HttpResponse
# import csv, datetime


# User = get_user_model()

# def export_to_csv(modeladmin, request, queryset):
#     opts = modeladmin.model._meta
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment;' 'filename={}.csv'.format(opts.verbose_name)
#     writer = csv.writer(response)
#     fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
#     # Write a first row with header information
#     writer.writerow([field.verbose_name for field in fields])
#     # Write data rows
#     for obj in queryset:
#         data_row = []
#         for field in fields:
#             value = getattr(obj, field.name)
#             if isinstance(value, datetime.datetime):
#                 value = value.strftime('%d/%m/%Y')
#             data_row.append(value)
#         writer.writerow(data_row)

#     return response

# export_to_csv.short_description = 'Выгрузить в CSV'  #short description
# ----------------------------------------------------------


    # import csv
    # from django.http import HttpResponse
    # from io import StringIO
    # f = StringIO()
    # writer = csv.writer(f)
    # writer.writerow(['Имя', 'Номер', 'Email', 'Дата Рождения',' Дата добавления'])

    # for s in queryset:
    #     writer.writerow([s.name, s.phone_number, s.email, s.date_of_birth,s.date_of_ordering])

    # f.seek(0)
    # response = HttpResponse(f, content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename=data.csv'
    # return response

# export_to_csv.short_description = "Выгрузить в CSV"

@admin.register(Emails_only)
class AdminEmail(admin.ModelAdmin):
    list_display = ("email","date_of_ordering")


# @admin.register(Person)
# class AdminPerson(admin.ModelAdmin):
#     list_display = ("name","phone_number","email","date_of_birth","date_of_ordering")
from import_export.admin import ImportExportModelAdmin
class personResource(resources.ModelResource):
    class Meta:
        model = Person

class PersonAdmin(ImportExportModelAdmin):
    resource_class = personResource
    fields = ("name","phone_number","email","date_of_birth","date_of_ordering")
    export_order =("name","phone_number","email","date_of_birth","date_of_ordering")
    
admin.site.register(Person, PersonAdmin)