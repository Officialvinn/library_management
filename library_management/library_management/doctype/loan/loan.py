# Copyright (c) 2026, Alvin and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class Loan(Document):
    def before_save(self):
        if not self.transaction_date:
            self.transaction_date = nowdate()

    def before_submit(self):
        loan_book = self.book
        book = frappe.get_doc("Book", loan_book)
        book.status = "Rented"
        book.save()

    def on_cancel(self):
        loan_book = self.book
        # When loan is cancelled → mark book as Available
        book = frappe.get_doc("Book", loan_book)
        book.status = "Available"
        book.save()