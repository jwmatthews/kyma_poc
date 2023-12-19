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

    def get_coolstuff_custom_rules_yaml(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(dir_path, 'test_data/coolstuff_custom_rules.yaml')
  
    def get_helloworld_mdb_custom_rules_yaml(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(dir_path, 'test_data/helloworld-mdb_custom_rules.yaml')

    def get_kitchensink_yaml(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(dir_path, 'test_data/kitchensink.yaml')
     
    def get_ticket_monster_yaml(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(dir_path, 'test_data/ticket-monster.yaml') 

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

        app_name1 = "coolstuff"
        yaml = self.get_coolstuff_yaml()
        repo = self.get_coolstuff_repo()
        r = Report(yaml).get_report()
        a = Application(app_name1, r, None, "unused", "unused")
        hub._update_cached_violations(a)

        # Check that the length of keys matches the length of rulesets we had in test data
        self.assertEqual(len(hub.cached_violations.keys()),  len(r.keys()))
        for ruleset_name in r.keys():
            self.assertIn(ruleset_name, hub.cached_violations.keys()) 
            for violation_name in r[ruleset_name]["violations"].keys():
                # Looping over each violation_name in the Report  
                self.assertIn(violation_name, hub.cached_violations[ruleset_name])
                self.assertEqual(len(hub.cached_violations[ruleset_name][violation_name]), 1)  
                self.assertIn(app_name1, hub.cached_violations[ruleset_name][violation_name]) 

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
                self.assertIn(app_name1, hub.cached_violations[ruleset_name][violation_name])     
                self.assertIn(app_name2, hub.cached_violations[ruleset_name][violation_name])     

    def test_find_common_violation(self):
        app_name1 = "coolstuff"
        app_name2 = "kitchensink"
        app_name3 = "helloworld-mdb"
        app_name4 = "ticket_monster"

        hub = ApplicationHub()
        # Note we are using the same repo for all of these but a different analysis yaml
        hub.add_application(app_name1, self.get_coolstuff_custom_rules_yaml(), self.get_coolstuff_repo(), "main", "quarkus-migration")
        hub.add_application(app_name2, self.get_kitchensink_yaml(), self.get_coolstuff_repo(), "main", "quarkus-migration")
        hub.add_application(app_name3, self.get_helloworld_mdb_custom_rules_yaml(), self.get_coolstuff_repo(), "main", "quarkus-migration")
        hub.add_application(app_name4, self.get_ticket_monster_yaml(), self.get_coolstuff_repo(), "main", "quarkus-migration")

        ruleset_example_1 = "eap8/eap7"
        violation_example_1 = "javaee-to-jakarta-namespaces-00001"

        names = hub.find_common_violation(ruleset_example_1, violation_example_1)
        print(f"Names: {names}")    
        # Need to rework verification
        # Intentionally erroring out 
        self.assertTrue(False)

        # Check that we can find a common violation


       