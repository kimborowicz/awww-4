from django.contrib import admin

from .models import Question, Choice

admin.site.register(Choice)


class QuestionChoiceInline(admin.TabularInline):
    model = Choice
    fields = ['choice_text', 'votes']
    extra = 1
    classes = ['collapse']
    show_change_link = True


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionChoiceInline]
