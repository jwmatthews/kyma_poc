import unittest
import os 
import pprint 

from git.exc import NoSuchPathError


from kyma_poc.report import Report
from kyma_poc.application_hub import ApplicationHub, Application 

class TestReports(unittest.TestCase):

    def get_coolstuff_yaml(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(dir_path, 'test_data/coolstuff.yaml')

    def get_coolstuff_repo(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # Assumes we've run the ../data/fetch.sh so repos are cloned
        return os.path.join(dir_path, '../data/coolstuff-quarkus') 

    def test_simple_create(self):
        hub = ApplicationHub()
        self.assertTrue(hub is not None)

    def test_add_application(self):
        hub = ApplicationHub()
        hub.add_application("coolstuff", self.get_coolstuff_yaml(), self.get_coolstuff_repo(), "main", "quarkus-migration")
        self.assertTrue(len(hub.get_application_names()) == 1)
        self.assertTrue("coolstuff" in hub.get_application_names())

        # Check that the parameters line up as we expected
        app = hub.get_application("coolstuff")
        self.assertTrue(app is not None)
        self.assertTrue(app.name == "coolstuff")
        self.assertTrue(app.report is not None)
        self.assertTrue(app.repo == self.get_coolstuff_repo())
        self.assertTrue(app.initial_branch == "main")
        self.assertTrue(app.solved_branch == "quarkus-migration")

        # Check that the report looks to be created correctly 
        report = app.report
        self.assertTrue(len(report.keys()) == 4)

    def test_add_application_with_bad_yaml_path(self):
        hub = ApplicationHub()
        with self.assertRaises(FileNotFoundError):
            hub.add_application("coolstuff", "bad_path", self.get_coolstuff_repo(), "main", "quarkus-migration")

    def test_add_application_with_bad_repo(self):
        hub = ApplicationHub()
        with self.assertRaises(NoSuchPathError):
            hub.add_application("coolstuff", self.get_coolstuff_yaml(), "bad_path", "main", "quarkus-migration")

    def test_add_application_with_bad_initial_branch(self):
        hub = ApplicationHub()
        with self.assertRaises(FileNotFoundError):
            hub.add_application("coolstuff", self.get_coolstuff_yaml(), self.get_coolstuff_repo(), "bad", "quarkus-migration")

    def test_add_application_with_bad_solved_branch(self):
        hub = ApplicationHub()
        with self.assertRaises(FileNotFoundError):
            hub.add_application("coolstuff", self.get_coolstuff_yaml(), self.get_coolstuff_repo(), "main", "bad")
    
    def test_add_application_with_no_solved_branch(self):
        # We expect it valid and fine to add an Application with no solved branch
        hub = ApplicationHub()
        hub.add_application("coolstuff", self.get_coolstuff_yaml(), self.get_coolstuff_repo(), "main", None)

    def test_add_application_with_no_initial_branch(self):
        # We expect it valid and fine to add an Application with no solved branch
        hub = ApplicationHub()
        with self.assertRaises(FileNotFoundError):
            hub.add_application("coolstuff", self.get_coolstuff_yaml(), self.get_coolstuff_repo(), None, "quarkus-migration")

    def test_update_cached_violations(self):
        hub = ApplicationHub()
        app_name = "coolstuff"
        yaml = self.get_coolstuff_yaml()
        repo = self.get_coolstuff_repo()

        r = Report(yaml).get_report()
        a = Application(app_name, r, None, "unused", "unused")
        hub._update_cached_violations(a)
        #pp = pprint.PrettyPrinter(indent=2)
        #pp.pprint(hub.cached_violations)
        # Check that the length of keys matches the length of rulesets we had in test data
        self.assertEqual(len(hub.cached_violations.keys()),  len(r.keys()))
        for ruleset_name in r.keys():
            self.assertIn(ruleset_name, hub.cached_violations.keys()) 
            for violation_name in r[ruleset_name]["violations"].keys():
                # Looping over each violation_name in the Report  
                self.assertIn(violation_name, hub.cached_violations[ruleset_name])
                self.assertEquals(len(hub.cached_violations[ruleset_name][violation_name]), 1)  
                self.assertIn(app_name, hub.cached_violations[ruleset_name][violation_name]) 

        ## Add a second app and verify
        app_name2 = "second_app_name"
        r2 = Report(yaml).get_report()
        a2 = Application(app_name2, r, None, "unused", "unused")
        hub._update_cached_violations(a2)
        # Ruleset names should be the same as before
        self.assertEqual(len(hub.cached_violations.keys()),  len(r.keys()))
        for ruleset_name in r.keys():
            self.assertIn(ruleset_name, hub.cached_violations.keys()) 
            for violation_name in r[ruleset_name]["violations"].keys():
                # Looping over each violation_name in the Report  
                self.assertIn(violation_name, hub.cached_violations[ruleset_name])
                self.assertEquals(len(hub.cached_violations[ruleset_name][violation_name]), 2)  
                self.assertIn(app_name, hub.cached_violations[ruleset_name][violation_name])     
                self.assertIn(app_name2, hub.cached_violations[ruleset_name][violation_name])     
       