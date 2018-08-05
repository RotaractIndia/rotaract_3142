import frappe

@frappe.whitelist(allow_guest=True)
def make_enquiry(fullname, email, message):
	todo = frappe.new_doc("ToDo")
	todo.update({
		"description": "Full Name: "+fullname + " | Email: "+ email + " | Message: "+ message
	})
	todo.save(ignore_permissions=True)
	frappe.db.commit()