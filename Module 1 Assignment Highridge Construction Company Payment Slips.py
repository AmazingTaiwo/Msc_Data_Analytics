worker = []
staff = worker

# Introduction of loop to geerate 400 workers
for i in range(1, 401):
    staff_id = f"staff_{i}" # Generating staff id such as Staff_1, Staff_2 etc
    staff.append(staff_id)

# Print list of 400 Staff
print(staff[:401]) #Displayong list of 400 staff dynamicaly generated
print(f"Total number of staff: {len(staff)}") # Verifying the total count of staff generated

# Payslip Dummy data import
import random
from datetime import date

# Number of staff to generate
staff = 400

# Function to generate a staff payment slip
def generate_payment_slip(staff_id, name, salary, employee_level):
    try:
        # Get today's date for the payment slip
        payment_date = date.today()

        # Format for the payment slip
        payment_slip = f"""
        PAYMENT SLIP
        -------------------
        Worker ID: {staff_id}
        Name: {name}
        Salary: ${salary:,.2f}
        Employee Level: {employee_level}
        Payment Date: {payment_date}
        -------------------
        """
        return payment_slip
    except Exception as e:
        print(f"Error generating payment slip for {staff_id}: {e}")
        return None

# Generate staff list dynamically
staffs = []
for i in range(1,401):
    try:
        staff_id = f"staff_{i}"  # Unique staff ID
        name = f"Staff {i}"  # Staff naming convention
        gender = random.choice(["Male", "Female"])  # Random gender selection
        salary = random.randint(7500, 30000)  # Random salary between $6,000 and $50,000

        # Assign employee level based on conditions (salary Scale, Gender and employee group)
        if 10000 < salary < 20000:
            employee_level = "A1"
        elif 7500 < salary < 30000 and gender == "Female":
            employee_level = "A5-F"
        else:
            employee_level = "General"  # Default level for workers not matching the conditions

        # Add employee to staff list
        staff = {"staff_id": staff_id, "name": name, "salary": salary, "employee_level": employee_level, "gender": gender}
        staffs.append(staff)

    except Exception as e:
        print(f"Error generating staff {i}: {e}")

# Generate payment slips for all staff and store them
payment_slips = []
for staff in staffs:
    try:
        slip = generate_payment_slip(staff["staff_id"], staff["name"], staff["salary"], staff["employee_level"])
        if slip:  # Append only if the payment slip is generated successfully
            payment_slips.append(slip)
    except Exception as e:
        print(f"Error generating payment slip for {staff['staff_id']}: {e}")

# Print the 400 staff payment slips
for i in range(400):  # Print 400 staff payment slips for brevity
    try:
        print(payment_slips[i])
    except IndexError:
        print("Error: Payment slip index out of range.")
        
