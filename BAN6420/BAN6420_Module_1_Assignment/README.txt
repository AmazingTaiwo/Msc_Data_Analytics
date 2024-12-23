
BAN6420: Programming in R & Python
Module 1 Assignment
Highridge Construction Company Payment Slips

Name: Babalola Taiwo
Learner IS: 162894

	This Python and R script was created to generates 400 staff list dynamically with their respective payslips generation for Highridge Construction Company.

	The script performs the following tasks:
		- Generates 400 staff IDs (suc as staff_1, staff_2, ..., staff_400).
		- Creates random data for the individual staff, includes their respective name, salary, gender, and employee level.
		- This program also assigns employee levels according to staff's salary and gender such as A1, A5-f and Consultant category.
		- It also generates a formatted pay slip for the individual staff .
		- Exceptions handling was also incoporated to ensure flexible execution and error logging.
		- The program prints payslips of 400 staffs.


	Key Features
		- Dynamic Staff list Generation: This script generates dynamically the ist of 400 staff IDs sequencially with other relevant data for the individual staff.
		- Randomized Data: The gender and salary per staff are assigned dynamically to simulate real-world data scenario.
		- Employee Level Assignment: Below employee levels was incorporated and assigned dynamically based on salary and gender for the provided consitional statement
       			- "A1": For salaries between $10,000 and $20,000.
       			- "A5-F": For female employees with salaries between $7,500 and $30,000.
       			- "Consultant": For all other employees.
 		- Pay Slip Generation: Payslip was generate of the indivifual member of the staff using below format such as:
           			- Staff ID
           			- Name
           			- Salary
           			- Employee Level
           			- Payment Date

		- Libraries: This script uses the following standard Python libraries:
                      		- Random (for generating random values)
                      		- Datetime (for fetching the current date)
	
	Notes:
		There are no external dependencies, and this script should run using Python or R installation.

	How to Run the Python Script
		- Download this repository zipped file to your local machine.
		- Extract the script into your prefered directory. 
		- Open a terminal or command prompt, navigate to the directory containing the just extracted script
		- Run the following command: python Module_1_Assignment_Highridge_Construction_Company_Payment_Slips.py
	
	How to Run the R Script
		- Download this repository zipped file to your local machine.
		- Extract the script into your prefered directory. 
		- Download and Install Rstudio and R-4.4.2-win.exe application on your PC
		- Launch the Rstudio application
		- Navigate to File > Open file > directory containing the previous extracted R script (Module_1_Assignment_Highridge_Construction_Company_Payment_Slips.R)
		- Run the script with Ctrl+Enter on your keyboard or click on the run option within the R application console.



	Python-Script Output:
		- The script will dynamically print the list of 400 staff and generate their repective pay slips. 
		- The Individual payslip will have the following details
			- Staff ID, 
                		- Name
                		- Salary
                		- Employee level
			- Payment date.
			- Error Handling was included to manage exceptions that may arise during the program genration. If any error occurs, an informative message will be displayed, afterwhich the program execution continues.

