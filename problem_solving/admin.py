from django.contrib import admin

from problem_solving.problem.model import ProblemModel
from problem_solving.skill.model import SkillModel

admin.site.register(ProblemModel)
admin.site.register(SkillModel)

