from django.contrib import admin

from blog.models import Article, Knowledge, Language, Project, Motivation, Competency, Job, Certificate, KeyWord

class KeyWordAdmin(admin.ModelAdmin):
    list_display = ('title', 'color')
    fields = ('title', 'color')
admin.site.register(KeyWord, KeyWordAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    fields = ('title', 'content', 'date', 'publish', 'keywords')
admin.site.register(Article, ArticleAdmin)

class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    fields = ('title', 'content', 'collapse')
admin.site.register(Knowledge, KnowledgeAdmin)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    fields = ('title', 'content')
admin.site.register(Language, LanguageAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    fields = ('title', 'content')
admin.site.register(Project, ProjectAdmin)

class MotivationAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    fields = ('title', 'content')
admin.site.register(Motivation, MotivationAdmin)

class CompetencyAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    fields = ('title', 'content')
admin.site.register(Competency, CompetencyAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    fields = ('title', 'content')
admin.site.register(Job, JobAdmin)

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    fields = ('title', 'content')
admin.site.register(Certificate, CertificateAdmin)
