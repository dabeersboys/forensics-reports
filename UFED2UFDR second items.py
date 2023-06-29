Evidence_Item = input("What is the evidence item number and descriptions? ")
# Prompt the user to enter the filepath for the UFD file
UFD_file = input("Enter the filepath for your UFD file here: ")

# Initialize variables
extraction_date = ""
extraction_tool = ""
extraction_type = ""
device_model = ""
device_manufacturer = ""

# Read the UFD file and extract information
with open(UFD_file, "r") as file:
    for line in file:
        try:
            key, value = line.strip().split('=')
            if key == 'Date':
                extraction_date = value
            elif key == 'AcquisitionTool':
                extraction_tool = value
            elif key == 'ExtractionType':
                extraction_type = value
            elif key == 'Model':
                device_model = value
            elif key == 'Vendor':
                device_manufacturer = value
        except ValueError:
            print(f"Ignoring this line")
    
PA_Version = input("What version of PA was used? ")

Investigator = input("Who was the UFDR Provided to? ")
Request_Agency = input("Who is the requesting Agency? ")

Report_writer = input("Who is writing this report? ")

lines = [

]
paragraph_one = f"\n Examination of {Evidence_Item}\n"

paragraph_two = f"\n On {extraction_date}, I, {Report_writer}, plugged the {device_manufacturer} {device_model} into {extraction_tool} and completed a {extraction_type} acquisition of the device. A copy of the acquisition was placed on the <UPDATE YOUR AGENCY NAME> Evidence Server.  A copy of the acquisition was also placed onto a forensic workstation to serve as a working copy. The acquisition was loaded into the forensics software, Cellebrite Physical Analyzer {PA_Version}. A UFED Reader report that contained the contents of the device was created and provided to {Investigator}. No further examination was conducted by myself. It will be up to {Investigator} and the {Request_Agency} to search the contents within the scope of their search authority. \n"

paragraph_three = f"\n A copy of the UFED Reader was placed onto a USB and logged into evidence at the <UPDATE YOUR AGENCY NAME>"


output_path = input("Enter report name here, include .txt at the end of the name: ")
with open(output_path, "w") as file:
    file.write(paragraph_one)
    file.write(paragraph_two)
    file.write(paragraph_three)
print("Report generated and saved as " + (output_path) + ".")
