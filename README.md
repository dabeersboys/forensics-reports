# forensics-reports
Several python scripts for "dump and go" type mobile forensic reports.
This is my frist set of python scripts, so don't be too hard on me. 

If you're anything like me you hate writing your forensic reports, you have a bunch of devices you rather be working on and the process of even just filling out your template for "Dump and Go" style reports, somethings are missed and errors occur. 

These scripts are easy to run scripts to help write your report for you to then copy and paste into what every report writing system you have in place. They are highly customizeable with your own templates with some tweaking and they may not be right for every situation.

Some have more automation than others.
ie-
  UFED2Axiom Reportwriter.py will prompt you for some questions, READ the Cellebrite .ufd file, pull information about your device, Then read the Magnet   
  Axiom Case Infomration.txt file pull some information, and populate it into your report. Others are strictly prompts for information to write your   
  report. 

*In each of these scripts you will see <UPDATE YOUR AGENCY NAME> Replace this with your agency or organization name and remove the brackets.

USAGE:
python <script_name.py>
ie- 
  python "GrayKey2Axiom Reportwriter.py"
  python "UFED2Axiom Reportwriter.py"
  python "UFED2UFDR Reportwriter.py"

  Have Fun!
