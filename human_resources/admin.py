from django.contrib import admin

from human_resources.citizen.model import CitizenModel
from human_resources.employee.model import EmployeeModel
from human_resources.inspector.model import InspectorModel
from human_resources.manager.model import ManagerModel
from human_resources.team.model import TeamModel
from human_resources.user.model import UserModel
from human_resources.worker.model import WorkerModel

admin.site.register(CitizenModel)
admin.site.register(EmployeeModel)
admin.site.register(InspectorModel)
admin.site.register(ManagerModel)
admin.site.register(TeamModel)
admin.site.register(UserModel)
admin.site.register(WorkerModel)
