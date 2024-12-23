# Initialize an empty vector to store the staff
worker <- c()
staff <- worker

# Introduction of loop to generate 400 staff
for (i in 1:400) {
  staff_id <- paste("staff", i, sep = "_")  # Generating staff ID such as staff_1, staff_2, etc.
  staff <- c(staff, staff_id)  # Append staff ID to the vector
}

# Print list of 400 Staff
print(staff)  # Displaying list of 400 staff dynamically generated

# Verifying the total number of staff generated
cat("Total number of staff:", length(staff), "\n")  # Print total count of staff generated

# Load necessary libraries
library(lubridate)

# Number of staff to be generate
staffs <- 400

# Function to generate 400 staff payment slip
generate_payment_slip <- function(staff_id, name, salary, employee_level) {
  tryCatch({
    # Get today's date for payment slip generation
    payment_date <- Sys.Date()
    
    # Format the payment slip
    payment_slip <- paste(
      "PAYMENT SLIP\n",
      "-------------------\n",
      paste("staff ID:", staff_id, "\n"),
      paste("Name:", name, "\n"),
      paste("Salary: $", format(salary, big.mark = ",", scientific = FALSE), "\n", sep = ""),
      paste("Employee Level:", employee_level, "\n"),
      paste("Payment Date:", payment_date, "\n"),
      "-------------------\n",
      sep = ""
    )
    return(payment_slip)
  }, error = function(e) {
    message(paste("Error generating payment slip for", staff_id, ":", e))
    return(NULL)
  })
}

# Initialize the staff list
staffs <- list()

# Generate 400 staff list dynamically
for (i in 1:400) {
  tryCatch({
    staff_id <- paste("staff", i, sep = "_")  # Unique staff ID
    name <- paste("Staff", i)  # Staff naming convention
    gender <- sample(c("Male", "Female"), 1)  # Gender selection
    salary <- sample(7500:30000, 1)  # salary range between $7,500 and $30,000
    
    # Assign Employee Level based on conditions statement
    if (salary > 10000 & salary < 20000) {
      employee_level <- "A1"
    } else if (salary > 7500 & salary < 30000 & gender == "Female") {
      employee_level <- "A5-F"
    } else {
      employee_level <- "General"  # employee level for staff not matching the conditions statement
    }
    
    # Add employee to staff list
    staff <- list(staff_id = staff_id, name = name, salary = salary, 
                  employee_level = employee_level, gender = gender)
    staffs[[i]] <- staff
  }, error = function(e) {
    message(paste("Error generating staff", i, ":", e))
  })
}

# Generate payment slips for all staff and store them
payment_slips <- list()

for (staff in staffs) {
  tryCatch({
    slip <- generate_payment_slip(staff$staff_id, staff$name, staff$salary, staff$employee_level)
    if (!is.null(slip)) {
      payment_slips <- append(payment_slips, list(slip))
    }
  }, error = function(e) {
    message(paste("Error generating payment slip for", staff$staff_id, ":", e))
  })
}

# Print 400 payment slips
for (i in 1:min(400, length(payment_slips))) {
  tryCatch({
    cat(payment_slips[[i]], "\n")
  }, error = function(e) {
    message("Error: Unable to print payment slip.")
  })
}

# Print total staff count
cat("Total number of staff: ", length(staffs), "\n")

