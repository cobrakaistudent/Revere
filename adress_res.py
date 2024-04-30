#!/usr/bin/env python3

'''
Dev Notes:
- What happens when a site matches multiple files, which one should be used?
'''
import sys
import re
import os
import hermes

class Color:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'


def find_address_res_enodeb(site,log_file):
    '''
    Function to find the pattern 'get Address res ENodeB|LTE' in the log file
    site: site name
    log_file: path to the log file
    '''
    
    output = ""
    output += f"Processing log file: {log_file}\n"

    pattern = re.compile(r'get Address res ENodeB\|LTE\n.*?Total: (\d+) MOs', re.DOTALL)
    with open(log_file, 'r') as file:

        content = file.read()
        match   = pattern.search(content)
        # print(match.group())
        if match:
            total_mos = int(match.group(1))
            address_res = f"{site} get Address res ENodeB|LTE' Total MOs: {total_mos}\n"
            # print(address_res)
            if total_mos == 0:
                output += f"{False}, {address_res}\n"
            else:
                output += f"{True}, {address_res}\n"
            
        else:
            output += f"{False}, Pattern not found in log file\n"

    return output

def remove_missing_sites(site_names, missing_sites):
    '''
    Function to remove missing sites from the list of site names
    site_names: list of site names
    missing_sites: list of missing sites
    '''

    return [site_name for site_name in site_names if site_name not in missing_sites]

def find_missing_sites(site_names, file_dict):
    '''
    Function to find missing log files for sites
    site_names: list of site names
    file_dict: dictionary containing site names as keys and log file names as values
    '''

    missing_sites = []
    for site_name in site_names:
        if site_name not in file_dict:
            missing_sites.append(site_name)
    return missing_sites

def generate_dictionary(folder_path):
    '''
    Function to generate a dictionary of files in a folder
    folder_path: path to the folder containing the log files
    '''
    file_dict = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".log"):
            key = file_name.split('_')[0]
            file_dict[key] = os.path.join(folder_path, file_name)
    return file_dict

def main(site_names:list, folder_path='/home/shared/common/Overnight_Work/Rehomes/Postchecks'):
    """
    Main function to process log files for a list of sites in a folder
    site_names: list of site names
    folder_path: path to the folder containing the log files
    """

    output = ""
    output += f"===============================================\n"
    output += f"Initiating processing of log files in folder: \n{folder_path}\n"
    output += f"Site names: {site_names}\n"
    output += f"===============================================\n"
    output += f"1. Generating dictionary for files in folder\n"
    file_dict = generate_dictionary(folder_path)
    # output += "\nDictionary generated:\n"
    # for key, value in file_dict.items():
    #     output += f"{key}: {value}\n"

    output += "\n"
    output += f"2. Checking for missing log files for sites\n"  

    missing_sites = find_missing_sites(site_names, file_dict)
    if missing_sites:
        output += f"Missing log files for sites: {missing_sites}\n"
        site_names = remove_missing_sites(site_names, missing_sites)
        output += f"New site names: {site_names}\n"
        output += "\n"
    else:
        output += f"All log files found for sites\n"

    output += f"3. Processing log files for sites\n"
    for site in site_names:
        output += f"{site}\n"
        output += find_address_res_enodeb(site, file_dict[site])
        output += "\n"

    return output


if __name__ == "__main__":
    # Check if the script is run as the main module
    # Parse command-line arguments for site names and folder path
    site_names = sys.argv[1:-1]  # Skip the first argument (script name) and the last one (folder path)
    folder_path = sys.argv[-1]  # Last argument is the folder path
    # Call the main function with the parsed arguments
    body = main(site_names, folder_path)
    # Print the output to be captured by the Bash script
    print(body)

# if __name__ == "__main__":
#     # Example usage
#     # folder_path = r'C:\\Users\\AVildos1\\OneDrive - T-Mobile USA\\Documents\\Rehomes\\Postchecks'
#     folder_path = '/home/shared/common/Overnight_Work/Rehomes/Postchecks'
#     # site_names = ['M7WAS197A', 'M7WAS197A2', 'M7WAS197A3','WALLABE']
#     site_names = ['7WAS234A', 'L7WAS128A2', 'M7WAS197A3','WALLABE']
#     body = main(site_names, folder_path)
#     print(body)
#     sender = "address_res@smartnet.com"
#     recipient = "anuar.vildosola@smartlinkgroup.com"
#     subject = "Address Res ENodeB|LTE Check Failed"
#     smtp_server = "emailrelay:25"
#     hermes.send_email(sender, recipient, subject, body, smtp_server)
    

