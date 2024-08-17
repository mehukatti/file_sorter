import json
import os
import time

def read_json(path):
    with open(path) as f:
        content = json.load(f)
    return content

def create_report(content):
    report_file = f"{os.getcwd()}\\report.txt"
    if os.path.exists(report_file):
        os.remove(report_file)
        time.sleep(2) # to avoid permissiondenied exception
    
    with open(report_file, "w") as f:
        f.write(content)

    # Lastly open the list for the user to see
    time.sleep(1.5) # to avoid permissiondenied exception
    os.system(report_file)
