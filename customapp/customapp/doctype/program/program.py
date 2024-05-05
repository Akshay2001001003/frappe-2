# Copyright (c) 2024, me and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe

class Program(Document):
    pass

@frappe.whitelist()
def calculate_total_credits(program_name):
    total_credits = 0
    courses = frappe.get_all("Courses", filters={"parent": program_name}, fields=["credits"])
    for course in courses:
        total_credits += course.credits
    # program = frappe.get_doc("Program", program_name)
    # program.total_credits = total_credits
    # program.save()
    frappe.db.set_value("Program", program_name, "total_credits", total_credits)
    # return program.total_credits
    return total_credits