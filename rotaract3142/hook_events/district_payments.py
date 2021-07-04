import frappe

def enable_reporting_access(payment, method):
    if payment.payment_category == "Admin Fees":
        frappe.db.set_value('Club', payment.club, 'disable_reporting_access', 0)