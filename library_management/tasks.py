import frappe

def new_user(doc, method):
    frappe.msgprint(f"New user has been created {doc.name}")
    frappe.log_error(title ="Library Hook", message=f"New user created: {doc.name}")