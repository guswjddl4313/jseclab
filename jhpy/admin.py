from django.contrib import admin
from .models import Question, FilesAdmin, Answer, Notice

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(FilesAdmin)
admin.site.register(Notice)