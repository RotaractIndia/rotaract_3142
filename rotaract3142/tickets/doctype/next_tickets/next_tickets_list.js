frappe.listview_settings['Next Tickets'] = {
    add_fields: ["paid"],

    get_indicator: function(doc) {
        if (doc.paid) {
            return [__("Paid"), "green", "paid,=,1"];
        } else {
            return [__("Failed"), "orange","paid,=,0"];
        }
    }
};