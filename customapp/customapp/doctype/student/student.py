
import frappe
from frappe.model.document import Document
import datetime

@frappe.whitelist()
def create_user_if_not_exists(email):
    # Check if the user exists
    if not frappe.db.exists("User", email):
        # Check if the role "Student" exists
        if not frappe.db.exists("Role", "Student"):
            # If "Student" role does not exist, create it
            student_role = frappe.get_doc({
                "doctype": "Role",
                "role_name": "Student"
            })
            student_role.insert(ignore_permissions=True)
        
        # Fetch student details
        student = frappe.get_doc("Student", {"email": email})
        
        # Create a new user document
        new_user = frappe.get_doc({
            "doctype": "User",
            "email": email,
            "first_name": student.first_name,
            "last_name": student.last_name,
            # "send_welcome_email": 0  # Optional: To prevent sending a welcome email
        })
        new_user.append("roles", {
            "role": "Student",
            "role_profile_name": "Student"
        })
        new_user.insert(ignore_permissions=True)
        
        frappe.msgprint("User created successfully.")
    else:
        frappe.msgprint("User already exists.")

class Student(Document):
    
    def get_full_name(self):
        full_name_parts = [self.first_name, self.middle_name, self.last_name]
        full_name = " ".join(part for part in full_name_parts if part)
        return full_name
    
    def validate(self):
        if not hasattr(self, 'date_of_birth') or not self.date_of_birth:
            frappe.throw("Date of birth is required.")

        try:
            birth_date = datetime.datetime.strptime(self.date_of_birth, '%Y-%m-%d')
            if birth_date >= datetime.datetime.now():
                frappe.throw("Date of birth cannot be greater than the current date")
        except ValueError:
            frappe.throw("Invalid date format for date of birth. Please use YYYY-MM-DD format.")

    def before_save(self):
        self.full_name = self.get_full_name()
        
    def before_insert(self):
        # Set the joining date to the current date by default
        self.joining_date = datetime.datetime.now().date()