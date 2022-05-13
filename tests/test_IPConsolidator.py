import csv, json, os, unittest
import IPConsolidator as app


class test_IPConsolidator(unittest.TestCase):
    data_folder=''

    def setUp(self):
        self.data_folder = './data' if test_IPConsolidator.data_folder == '' else test_IPConsolidator.data_folder
        self.target_file_name = 'combined.csv'  
        self.testapp = app.IPConsolidator()

    def testCount_list_files(self): #Test case for checking the count returned is same 
        self.assertEqual(len(self.testapp.list_files(self.data_folder)),6)

    def testEqual_list_files(self):#Test case for checking the list of files returned is correct
        self.assertSetEqual(set(self.testapp.list_files(self.data_folder)),{'file 1.csv','file 2 1.csv','file 3.csv','_combined.csv','Asia NA 11 22.csv','combined.csv'})

    def testinvalidfolder_invoke_job(self):#Test case to confirm process is not failing for an empty file
        with open(self.data_folder+"/new_empty_file.csv", 'w', newline='') as empty_data_file:
            write = csv.writer(empty_data_file)
            write.writerow('')
        self.assertEqual(self.testapp.invoke_job(),"Process completed successfully")


if __name__ == '__main__':
    unittest.main()