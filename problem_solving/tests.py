from django.test import TestCase

from human_resources.citizen.model import CitizenModel
from human_resources.inspector.model import InspectorModel
from human_resources.team.model import TeamModel
from human_resources.worker.model import WorkerModel
from problem_solving.problem.model import ProblemModel


class ProblemModelTests(TestCase):

    def test_assign_to_inspector_after_submit(self):
        """A new task is assigned correctly to an inspector"""
        citizen = CitizenModel(city='TEHRAN', phone_number='0912334456')
        citizen.save()
        problem = ProblemModel(status='NEW', number_of_needed_workers=1, issuer=citizen)
        inspector = InspectorModel(salary=1000000, town_under_control='TEHRAN')
        inspector.save()
        problem.save()
        self.assertEqual(inspector, problem.assigned_to_inspector)

    def test_assign_assign_to_team(self):
        """Task is assigned to a team when approved"""
        citizen = CitizenModel(city='TEHRAN', phone_number='0912334456')
        citizen.save()
        inspector = InspectorModel(salary=1000000, town_under_control='TEHRAN')
        inspector.save()
        worker = WorkerModel(phone_number='091245535', salary=10000000)
        worker.save()
        team = TeamModel(leader=worker)
        team.save()
        problem = ProblemModel(status='APPROVED', assigned_to_inspector=inspector, number_of_needed_workers=1,
                               issuer=citizen)
        problem.save()
        self.assertEqual(problem.assigned_to_team, team)
