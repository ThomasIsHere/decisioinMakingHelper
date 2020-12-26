from django.contrib import admin

from .models import Question, Answer
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3


class QestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields':['creation_date','deadline_date']}),
        ('Question text', {'fields':['question_text']}),
    ]
    inlines = [AnswerInline]
    search_fields = ['question_text']


admin.site.register(Question, QestionAdmin)
#admin.site.register(Answer)
