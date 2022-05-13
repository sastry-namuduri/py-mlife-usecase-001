import os, csv
import common_helper as helper

def list_files(folder) -> list:
    """
    Arguments: 
            type : str
                Name of the Directory to list the files
    Description: 
            Returns the file names in the folder as list type
    Return: 
            type : list 
                List of file names
    """
    return os.listdir(folder)

def read_env_file(dirName, fileName) -> set:
    """
    Arguments: 
            type : str
                Environment file to read
    Description: 
            Read csv file and collect distinct IPs available in the file + derive environment value
    Return: 
            type : set
                set of tuples (IP, environment value)
    """        
    tobe_added_IPs = set()
    hdr = []
    # Check if the file is empty before processing
    if os.stat(dirName + "/" + fileName).st_size != 0:
        with open((dirName + "/" + fileName), newline='') as csv_data:
            reader = csv.reader(csv_data, delimiter=',',quotechar='"')     
            # skip header record
            hdr = next(reader)
            for row in reader:
                # for each row, store the tuple (ip, environment) in a set
                tobe_added_IPs.add( ((row[0].strip()), helper.get_env_from_filename(fileName)) )
        return tobe_added_IPs
    else: 
        return list()
    
def write_to_target_file(dirName, targetFilename, IPstoAdd) -> None:
    """
    Arguments: 
            type : set
                set of tuples (IP, environment value)
    Description: 
            write the entries to be added to the target file (combined.csv)
    Return: 
            None
    """          
    with open((dirName + "/" + targetFilename), 'w', newline='') as combined_csv:
        dataWriter = csv.writer(combined_csv)
        dataWriter.writerows(IPstoAdd)