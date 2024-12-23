# Staff list and payslip generation for Highridge Construction Company
staff = []

# Introduction of loop to geerate 400 staff
for i in range(1, 401):
    staff_id = f"staff_{i}" # Generating staff id such as Staff_1, Staff_2 etc
    staff.append(staff_id)

# Print list of 400 Staff
print(staff[:401]) #Displayong list of 400 staff dynamicaly generated
print("Total number of staff {0}".format(len(staff))) # Verifying the total count of staff generated

# Payslip Dummy data import
import random
from datetime import date

# Number of staff to generate
staff = 400

# Generate a staff pay slip
def generate_pay_slip(staff_id, name, salary, employee_level):
    try:
        # Get today's date for the payment slip
        pay_date = date.today()

        # Format for the pay slip
        pay_slip = f"""
        PAYMENT SLIP
        -------------------
        Staff ID: {staff_id}
        Name: {name}
        Salary: ${salary:,.2f}
        Employee Level: {employee_level}
        Payment Date: {pay_date}
        -------------------
        """
        return pay_slip
    except Exception as e:
        print(f"Error generating pay_slip for {staff_id} please reachout to IT Support: {e}")
        return None

# Generate staff list dynamically
staffs = []
for i in range(1,401):
    try:
        staff_id = f"staff_{i}"  # Unique staff ID
        name = f"Staff {i}"  # Staff naming convention
        gender = random.choice(["Male", "Female"])  # Gender selection
        salary = random.randint(7500, 30000)  # Salary Range $6,000 and $50,000

        # Assign employee level based on conditions (salary Scale, Gender and employee group)
        if 10000 < salary < 20000:
            employee_level = "A1"
        elif 7500 < salary < 30000 and gender == "Female":
            employee_level = "A5-F"
        else:
            employee_level = "Consultant"  # Default level for staff not matching the conditions

        # Add employee to staff list
        staff = {"staff_id": staff_id, "name": name, "salary": salary, "employee_level": employee_level, "gender": gender}
        staffs.append(staff)

    except Exception as e:
        print(f"Unable to Error generating staff {i} please reachout to IT Support: {e}")

# Generate pay slips for all staff and store them
pay_slips = []
for staff in staffs:
    try:
        slip = generate_pay_slip(staff["staff_id"], staff["name"], staff["salary"], staff["employee_level"])
        if slip:  # Append only if the pay slip is generated successfully
            pay_slips.append(slip)
    except Exception as e:
        print(f"Error generating pay slip for {staff['staff_id']} Please reachout to IT Support: {e}")

# Print the 400 staff pay slips
for i in range(400):  # Print 400 staff pay slips for brevity
    try:
        print(pay_slips[i])
    except IndexError:
        print("Error: Pay slip index out of range. Please reachout to IT Support")