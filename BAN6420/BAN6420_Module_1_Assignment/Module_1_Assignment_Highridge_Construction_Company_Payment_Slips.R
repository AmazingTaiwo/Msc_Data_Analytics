# Staff list and payslip generation for Highridge Construction Company
staff <- c()

# Introduction of loop to generate 400 staff IDs
for (i in 1:400) {
  staff_id <- paste("staff", i, sep = "_")  # Generating staff ID such as staff_1, staff_2, etc.
  staff <- c(staff, staff_id)  # Append staff ID to the vector
}

# Print list of 400 Staff
print(staff)  # Displaying list of 400 staff dynamically generated
cat("Total number of staff:", length(staff), "\n")  # Verifying the total count of staff generated

# Generate a staff pay slip
generate_pay_slip <- function(staff_id, name, salary, employee_level) {
  tryCatch({
    pay_date <- Sys.Date()  # Get today's date for the payment slip
    
    # Format for the pay slip
    pay_slip <- paste("
    PAYMENT SLIP
    -------------------
    Staff ID:", staff_id, "
    Name:", name, "
    Salary: $", formatC(salary, format = "f", digits = 2), "
    Employee Level:", employee_level, "
    Payment Date:", pay_date, "
    -------------------
    ")
    
    return(pay_slip)
  }, error = function(e) {
    cat("Error generating pay slip for", staff_id, "please reach out to IT Support:", e$message, "\n")
    return(NULL)
  })
}

# Generate staff list dynamically
staffs <- list()  # Initialize an empty list to store staff details

for (i in 1:400) {
  tryCatch({
    staff_id <- paste("staff", i, sep = "_")  # Unique staff ID
    name <- paste("Staff", i)  # Staff naming convention
    gender <- sample(c("Male", "Female"), 1)  # Gender selection
    salary <- sample(7500:30000, 1)  # Salary between $7,500 and $30,000
    
    # Assign employee level based on conditions (salary scale, gender, and employee group)
    if (salary > 10000 && salary < 20000) {
      employee_level <- "A1"
    } else if (salary > 7500 && salary < 30000 && gender == "Female") {
      employee_level <- "A5-F"
    } else {
      employee_level <- "Consultant"  # Default level for staff not matching the conditions
    }
    
    # Add employee to staff list
    staff <- list(staff_id = staff_id, name = name, salary = salary, employee_level = employee_level, gender = gender)
    staffs <- append(staffs, list(staff))
    
  }, error = function(e) {
    cat("Error generating staff", i, "please reach out to IT Support:", e$message, "\n")
  })
}

# Generate pay slips for all staff and store them
pay_slips <- list()  # Initialize an empty list to store the pay slips

for (staff in staffs) {
  tryCatch({
    slip <- generate_pay_slip(staff$staff_id, staff$name, staff$salary, staff$employee_level)
    if (!is.null(slip)) {  # Append only if the pay slip is generated successfully
      pay_slips <- append(pay_slips, list(slip))
    }
  }, error = function(e) {
    cat("Error generating pay slip for", staff$staff_id, "please reach out to IT Support:", e$message, "\n")
  })
}

# Print the first 400 pay slips for brevity
for (i in 1:400) {
  tryCatch({
    cat(pay_slips[[i]], "\n")
  }, error = function(e) {
    cat("Error: Pay slip index out of range. Please reach out to IT Support", e$message, "\n")
  })
}

