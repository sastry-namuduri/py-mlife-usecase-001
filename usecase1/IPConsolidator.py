import csv, json, os
import common_helper as helper
import file_operations

class IPConsolidator():
    
    """
    Class contains modules which accomplishes the process of 
        1) reading input folder (currently set in the configuration file 'static_variables.json)
        2) reading all the unique IPs from each file and tag them to the environment value dervied from the file name
        3) writing (2) to a file called combined.csv by overwriting 
    """

    def __init__(self):
        """
        Initializing with params
        """
        config = helper.read_config()
        self.dirName =  config['Data_Location']
        self.cmbndFileName = config['Combined_Filename']
 
    def process_files(self, all_files) -> list:
        """
        Arguments: 
                type : list
                    List of all files available in the input directory 
        Description: 
                Loop through each file and call 'read_env_file' function
        Return: 
                type : list
                    List of entries to add to the target file
        """        
        # Add headers to the target file
        entries_to_add = [('IP','Environment')] 
        # loop through each file in the input directory and invoke 'read_env_file' method
        for eachFile in all_files:
            entries_to_add += file_operations.read_env_file(self.dirName, eachFile)
        return entries_to_add
 

              
    def invoke_job(self) -> str:
        """
        Arguments: 
                None
        Description: 
                Main module to invoke the process which triggers other methods 
        Return: 
                type : str 
                    if the whole process is successful--> returns success message
                    if the whole process is failed    --> returns error message
        """          
        try:
            files_available = file_operations.list_files(self.dirName)
            if self.cmbndFileName in files_available:
                files_available.remove(self.cmbndFileName)
            entries_to_add = self.process_files(files_available)
            file_operations.write_to_target_file(self.dirName, self.cmbndFileName, entries_to_add)
            return "Process completed successfully"
        except Exception as e:
            print(e)
            return "Process completed with errors"