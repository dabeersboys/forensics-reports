#Requestor information
Request_Date = input("What was the date of the Examination Request? ")
Request_Agency = input("What is the requesting agency? ")
Request_Officer = input("What is the Title and Name of the requesting Officer? ")
Request_Case_Number = input("What is the associated case number? ")

#Evidence Intake Information
Evidence_Date = input("What date did you receive the evidence? ")
Evidence_Custodian = input("Who did you receive the evidence from? ")
Evidence_Item = input("What is the Item number and name? ")

#Evidence Extraction Information
extraction_date = input("What was the date of the Gray Key Acquisition? ")
device_manufacturer = input("What is the Make of the Device? ")
device_model = input("What is the modle of the device? ")
extraction_type = input("What type of acquisition did you get? ")
    
# Prompt the user to enter the filepath for the AXIOM Case Information text file    
Magnet_file = input("Enter the filepath for your AXIOM Case Information text file here: ")

# Initialize variable
Axiom_version = ""

# Read the AXIOM Case Information text file and extract the version information
with open(Magnet_file, "r") as file:
    for line in file:
        if line.startswith('Build'):
            axiom_version = line.strip().split(':')

Investigator = input("Who was the Portable Case Provided to? ")

Report_writer = input("Who is writing this report? ")

lines = [

]
paragraph_one = f"On {Request_Date}, I, Investigator {Report_writer}, with <UPDATE WITH YOUR AGENCY NAME>, received an examination request from {Request_Agency} {Request_Officer} related to {Request_Agency} case {Request_Case_Number}.  On {Evidence_Date} I received {Evidence_Item} from {Evidence_Custodian}.\n \n Examination of {Evidence_Item}\n"

paragraph_two = f"\n On {extraction_date}, I, {Report_writer}, plugged the {device_manufacturer} {device_model} into hardware software tool and completed a {extraction_type} acquisition of the device. A copy of the acquisition was placed on the <UPDATE WITH YOUR AGENCY NAME> Evidence Server.  A copy of the acquisition was also placed onto a forensic workstation to serve as a working copy. The acquisition was loaded into the forensics software, Magnet AXIOM {axiom_version}. A portable case that contained the contents of the device was created and provided to {Investigator}. No further examination was conducted by myself. It will be up to {Investigator} and the {Request_Agency} to search the contents within the scope of their search authority. \n"

paragraph_three = f"\n A copy of the portable case was placed onto a USB and logged into evidence at the <UPDATE YOUR AGENCY NAME>"


output_path = input("Enter report name here, include .txt at the end of the name: ")
with open(output_path, "w") as file:
    file.write(paragraph_one)
    file.write(paragraph_two)
    file.write(paragraph_three)
print("Report generated and saved as " + (output_path) + ".")
