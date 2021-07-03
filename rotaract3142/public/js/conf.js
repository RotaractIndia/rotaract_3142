
frappe.provide('rotaract3142');

// disable change log popups from frappe / erpnext
frappe.boot.change_log = []

// add toolbar icon
$(document).bind('toolbar_setup', () => {
	//////////////////////////////////////////////////
	// BUILDING THE HELP MENU

	const $article_links = $(".dropdown-help #help-links");
	const $help_menu = $('.dropdown-help ul .documentation-links');

	// link to FAQ's
	const $faq = $(`<li><a href="https://docs.google.com/document/d/1ybwmnK8poYZdvEHtw6nVhlaQG7ipLUfQ9ffbROG2HL4/edit" target="_blank">${__("FAQ's")}</a></li>`)
		.insertAfter($help_menu)

	const $keyboard_shortcuts = $(`<li><a href="#" onclick="return frappe.ui.toolbar.show_shortcuts(event)" >${__('Keyboard Shortcuts')}</a></li>`)
		.insertAfter($report_issue_menu_item);

	// Hack to remove all but the above elements
	$('.dropdown-help ul li')
		.not($faq)
		.not($keyboard_shortcuts)
		.remove();
});
