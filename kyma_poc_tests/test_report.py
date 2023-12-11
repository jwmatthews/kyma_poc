import unittest
import os 
import pprint

from kyma_poc.report import Report 

class TestReports(unittest.TestCase):

    def get_coolstuff_yaml(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(dir_path, 'test_data/coolstuff.yaml')

    def test_create_with_bad_path(self):
        with self.assertRaises(FileNotFoundError):
            badRObj = Report("bad_path")
    
    def test_parse(self):
        report = Report(self.get_coolstuff_yaml()).get_report()
        self.assertTrue(report is not None)

    def test_impacted_files(self):
        pp = pprint.PrettyPrinter(indent=2)
        rObj = Report(self.get_coolstuff_yaml())
        self.assertTrue(rObj is not None)
        impacted_files = rObj.get_impacted_files()
        for f in impacted_files.keys():
            print(f"File: `{f}` has {len(impacted_files[f])} violations")
        #pp.pprint(impacted_files)
        #print(f"Found {len(impacted_files)} impacted files")
        #print(f"Found {impacted_files.keys()}")
        self.assertTrue(len(impacted_files) == 25)
        test_file_entry = 'src/main/java/com/redhat/coolstore/model/InventoryEntity.java'
        self.assertTrue(test_file_entry in impacted_files)
        test_entry = impacted_files[test_file_entry]
        self.assertTrue(len(test_entry) == 6)
        self.assertTrue('violation_name' in test_entry[0].keys())
        self.assertTrue('violation_description' in test_entry[0].keys())
        self.assertTrue('ruleset_name' in test_entry[0].keys())
        self.assertTrue('ruleset_description' in test_entry[0].keys())
        self.assertTrue('message' in test_entry[0].keys())

if __name__ == '__main__':
    unittest.main()
