import unittest
import os 
import pprint

from kyma_poc.report import Report 

class TestReports(unittest.TestCase):

    def get_coolstuff_yaml(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(dir_path, 'test_data/coolstuff.yaml')

    def test_parse(self):
        report = Report(self.get_coolstuff_yaml()).get_report()
        self.assertTrue(report is not None)

    def test_impacted_files(self):
        pp = pprint.PrettyPrinter(indent=2)
        rObj = Report(self.get_coolstuff_yaml())
        self.assertTrue(rObj is not None)
        impacted_files = rObj.get_impacted_files()
        #pp.pprint(impacted_files)
        #print(f"Found {len(impacted_files)} impacted files")
        #print(f"Found {impacted_files.keys()}")
        self.assertTrue(len(impacted_files) == 25)
        self.assertTrue('src/main/java/com/redhat/coolstore/model/InventoryEntity.java' in impacted_files)

if __name__ == '__main__':
    unittest.main()
