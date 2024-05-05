# Copyright (c) 2024, me and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

import frappe

def get_student_image(student):
    # Fetch the student document
    student_doc = frappe.get_doc("Student", student)

    # Check if the student document exists and has an image attached
    if student_doc and student_doc.get("img"):
        # Return the image URL
        return {"image": student_doc.get("img")}
    else:
        return {"image": None}
class Participants(Document):
	pass
