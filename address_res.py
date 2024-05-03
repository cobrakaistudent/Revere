#!/usr/bin/env python3

'''
@Author: anuar-sml
Dev Notes:
- What happens when a site matches multiple files, which one should be used? [PENDING]
- Show if the site has no contact in the log file. [PENDING]
- Show if the log file has the correct format i.e. SITENAME_TIMESTAMP.log [PENDING]
'''
import sys
import re
import os
import subprocess
import datetime
import platform
import getpass
# import hermes

# Get system information
system_info = f"System: {platform.system()}"
server_name = f"Server Name: {platform.node()}"
current_user = f"User: {getpass.getuser()}"
system_info_str = f"{system_info}\n{server_name}\n{current_user}"
hostname = platform.node()
username = getpass.getuser()

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


def ping_site(site, site_dict: dict):
    '''
    Function to ping a site from the site dump
    site: site name
    site_dict: dictionary containing the site dump
    '''

    output = ""
    if site in site_dict:
        output += f"Site: {site}\n"
        for ip in site_dict[site]:
            output += f"IP: {ip}\n"
            response = subprocess.run(['ping', '-c', '3', ip], stdout=subprocess.PIPE)
            if response.returncode == 0:
                output += f"{Color.GREEN}Ping successful{Color.RESET}\n"
            else:
                output += f"{Color.RED}Ping failed{Color.RESET}\n"
    else:
        output += f"No IP addresses found for site: {site}\n"

    return output

def generate_ip_dict(site_dump='/home/shared/common/sitefiles/ipdatabase'):
    '''
    Function to generate a dictionary with NodeId as key and IP address as value from a dump file.
    site_dump: path to the site dump file
    '''
    site_dict = {}
    try:
        with open(site_dump, 'r') as file:
            for line in file:
                line = re.split('\s+', line)
                if len(line) >= 2:
                    node_id = line[0]
                    ip_address = line[1].strip()
                    if node_id in site_dict:
                        site_dict[node_id].append(ip_address)
                    else:
                        site_dict[node_id] = [ip_address]
                else:
                    # Handle lines with fewer elements (if needed)
                    pass

        if not site_dict:
            print("Warning: Empty site dictionary generated from the file.")
        else:
            print("Site dictionary generated successfully:")
            

        return site_dict

    except FileNotFoundError:
        print(f"Error: File '{site_dump}' not found.")
        return None
    except Exception as e:
        print(f"Error: An exception occurred while reading the file: {e}")
        return None

def find_extgnb_partner_function(site:str, content:str):
    '''
    Function to find the pattern 'ExtGNBDUPartnerFunction=' in the log file
    site: site name
    content: content of the log file
    '''
    output = ""
    # output += f"Processing log file: {log_file}\n"

    pattern = re.compile(r'> get FUnction=1 nbid\$\n(.*?)Total: \d+ MOs', re.DOTALL)
    pattern2 = re.compile(r'> st term\n(.*?)Total: \d+ MOs', re.DOTALL)
    pattern3 = re.compile(r'> st termpointtognb=\d+\n(.*?)Total: \d+ MOs', re.DOTALL)  


    match = pattern.search(content)
    if match:
        mo_text = match.group(1)
        # partner_functions = re.findall(r'ExtGNBDUPartnerFunction=(\d+)', mo_text)
        partner_functions = re.findall(r'ExtGNBDUPartnerFunction=(\d{4,})', mo_text)


        if partner_functions:
            output += f"ExtGNBDUPartnerFunction values found: {', '.join(partner_functions)}\n"
            # You can process the partner functions further if needed


            match3 = pattern3.search(content)
            if match3:
                for i in partner_functions:
                    term_points_gnb = re.findall(r'(\(\w+\).+?ExternalGNodeBFunction={}.+?=.+?)'.format(i), match3.group(1))
                    for term_point2 in term_points_gnb:
                        output +=f"TermPointToGNB: {term_point2.strip()}\n"
            else:
                output += "No TermPointToGNB values found in the MOs\n"

            match2 = pattern2.search(content)
            # print(match2.group(1))
            if match2:
                for i in partner_functions:
                    # print(f"ExtGNBDUPartnerFunction: {i}")
                    # term_points = re.findall(r'ENodeBFunction=\d+,GUtraNetwork=\d+,ExternalGNodeBFunction={}'.format(i), match2.group(1))
                    term_points = re.findall(r'(\(\w+\).+?ExternalGNodeBFunction={}.+?=.+?)'.format(i), match2.group(1))
                    for term_point in term_points:
                        output +=f"TermPoint: {term_point.strip()}\n"
            else:
                output += "No TermPoint values found in the MOs\n"
        else:
            output += "No ExtGNBDUPartnerFunction values found in the MOs\n"
    else:
        output += "WARNING!!! get FUnction=1 nbid not found in log file\n"

    return output

def site_contact(site:str, content:str, dump_dict:dict):
    '''
    Function to detect the site contact in the log file.
    site: site name
    content: content of the log file
    dump_dict: dictionary containing the site dump
    '''
    
    output      = ""
    pattern     = re.compile(r'Checking ip contact.*?\s*Not OK', re.DOTALL)
    pattern2    = re.compile(r"Unable to connect to (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)")

    match       = pattern.search(content)
    match2      = pattern2.search(content)

    if match:
        output  += f"WARNING: {False}, {site} has no contact in the log file\n"
    # else:
    #     output += f"INFO: {True}, {site} has contact in the log file\n"

    if match2:
        output  += f"Unable to connect to {match2.group(1)}:{match2.group(2)}\n"
        
        

    # else:
    #     output += f"INFO: {True}, {site} has contact in the log file\n"

    return output

def find_address_res_enodeb(site:str,content:str):
    '''
    Function to detect the Address res precheck in the log file.
    site: site name
    content: content of the log file
    '''
    output = ""

    pattern = re.compile(r'get Address res ENodeB\|LTE\n.*?Total: (\d+) MOs', re.DOTALL)
    match   = pattern.search(content)

    if match:
        total_mos = int(match.group(1))
        address_res = f"{site} get Address res ENodeB|LTE' Total MOs: {total_mos}\n"
        
        if total_mos == 0:
            output += f"{False}, {address_res}\n"
        else:
            output += f"{True}, {address_res}\n"
        
    else:
        output += f"{False}, Address res pattern not found in log file\n"
        output +="\n"

    return output

def read_logfile(site:str,log_file, dump_dict:dict):
    '''
    Function to find the pattern 'get Address res ENodeB|LTE' in the log file
    site: site name
    log_file: path to the log file
    '''
    
    output = ""
    output += f"Processing log file: {log_file}\n"

    with open(log_file, 'r') as file:
        content = file.read()
        # output += f"###START###\n"
        output += site_contact(site,content,dump_dict)
        output += find_address_res_enodeb(site,content)
        output += find_extgnb_partner_function(site,content)
        # output += f"###END###\n"
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
    output += f"{datetime.datetime.now()}\n"
    output += f"{system_info}\n"
    output += f"{server_name}\n"
    output += f"{current_user}\n"
    output += f"Initiating Pre-Check processing of log files in folder: \n{folder_path}\n"
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
        output += "\n"
        output += f"--> Found site names: {site_names}<--\n"
        output += "\n"
    else:
        output += f"All log files found for sites\n"

    if site_names:
        dump_dict = generate_ip_dict()
        if not dump_dict:
            dump_dict={}
            output += "Error: Site dump not found\n"
        # print(datetime.datetime.now())
        # print(dump_dict)

    output += f"3. Processing log files for sites\n"

    for site in site_names:
        output += "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        output += f"{site}\n"
        output += read_logfile(site,file_dict[site],dump_dict)
        # output += "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
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


    

