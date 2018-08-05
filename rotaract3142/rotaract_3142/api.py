import frappe

@frappe.whitelist(allow_guest=True)
def make_enquiry(fullname, email, message):
	print "DONE"