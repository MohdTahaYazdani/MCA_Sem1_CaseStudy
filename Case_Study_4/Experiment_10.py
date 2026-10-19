# Experiment 10: University Admission Validation Dashboard


# Import Regular Expression to validate applicant's
import re

# Taking student data
name = str(input("Please enter your name: "))
email = input("Please enter your Email: ")
mobile = input("Please enter your Mobile number: ")
app = input("Please enter your application ID: ")

# Validating applicant's data
email_check = bool(re.match(r"^[\w.-]+@[\w.-]+\.\w+$",email))
mobile_check = bool(re.match(r"^[6-9]\d{9}$",mobile))
app_check = bool(re.match(r"^APP\d{4}$",app))

status = "ACCEPTED" if email_check and mobile_check and app_check else "RECHECK DETAILS"

# Display student dashboard
print("="*50)
print(f"{'UNIVERSITY ADMISSION DASHBOARD':^50}")
print("="*50)
print(f"{'Applicant:'} {name.capitalize()}")
print(f"{'Email:'} {'VALID' if email_check else 'INVALID'}")
print(f"{'Mobile:'} {'VALID' if mobile_check else 'INVALID'}")
print(f"{'Application ID:'} {'VALID' if app_check else 'INVALID'}")
print(f"{'Application:'} {status}")
print("="*50)