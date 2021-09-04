from django.test import TestCase

from human_resources.inspector.model import InspectorModel
from human_resources.team.model import TeamModel
from human_resources.worker.model import WorkerModel
from problem_solving.problem.model import ProblemModel


class ProblemModelTests(TestCase):

    def test_assign_to_inspector_after_submit(self):
        """A new task is assigned correctly to an inspector"""
        problem = ProblemModel(status='NEW')
        inspector = InspectorModel(town_under_control='TEHRAN')
        problem.save()
        self.assertEqual(inspector, problem.assigned_to_inspector)

    def test_assign_assign_to_team(self):
        """Task is assigned to a team when approved"""
        inspector = InspectorModel(town_under_control='TEHRAN')
        worker = WorkerModel()
        team = TeamModel(leader=worker)
        problem = ProblemModel(status='APPROVED', assigned_to_inspector=inspector, number_of_needed_workers=1)
        problem.save()
        self.assertEqual(problem.assigned_to_team, team)
