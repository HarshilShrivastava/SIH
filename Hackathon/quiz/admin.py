from django.contrib import admin
from quiz.models import (
    Domain,
    Question,
    Answer,
    GeneralMarks,
    DomainQuestion,
    DomainMarks,
    DomainAnswer

)
# Register your models here.

admin.site.register(Domain)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(GeneralMarks)
admin.site.register(DomainQuestion)
admin.site.register(DomainMarks)
admin.site.register(DomainAnswer)
