import frappe
from renovation.tests import FrappeTestFixture

"""
Frappe makes a couple of reports by default.
We can use them as fixtures

Frappe/Core Reports
-----------------------------------------------
- Transaction Log Report
    Administrator
    System Manager

- Document Share Report
    System Manager

- Permitted Documents For User
    System Manager

Frappe/Contacts Reports
-----------------------------------------------
- Address And Contacts
    Sales User
    Purchase User
    Maintenance User
    Account User

Frappe/Desk Reports
-----------------------------------------------
- ToDo
    System Manager

Frappe/Website Reports
-----------------------------------------------
- Website Analytics
    System Manager
    Website Manager
"""


class ReportFixtures(FrappeTestFixture):

    TRANSACTION_LOG_REPORT = "Transaction Log Report"
    DOCUMENT_SHARE_REPORT = "Document Share Report"
    PERMITTED_DOCUMENTS_FOR_USER = "Permitted Documents For User"
    ADDRESS_AND_CONTACTS = "Addresses And Contacts"
    TODO = "ToDo"
    WEBSITE_ANALYTICS = "Website Analytics"

    STANDARD_REPORTS = [
        TRANSACTION_LOG_REPORT,
        DOCUMENT_SHARE_REPORT,
        PERMITTED_DOCUMENTS_FOR_USER,
        ADDRESS_AND_CONTACTS,
        TODO,
        WEBSITE_ANALYTICS
    ]

    def __init__(self):
        super().__init__()
        self.DEFAULT_DOCTYPE = "Report"

    def make_fixtures(self):
        """
        We will add the STANDARD_REPORTS as fixtures
        """
        for report in self.STANDARD_REPORTS:
            self.add_document(frappe.get_doc("Report", report))

    def delete_fixtures(self):
        """
        We do not want to delete any Reports
        since all we have are standard reports
        """
        dt = "Report"
        self.fixtures[dt] = [
            x for x in self.fixtures[dt]
            if x.name not in self.STANDARD_REPORTS]

        # We still call the delete_fixtures in case
        # if the tests added some other random documents
        super().delete_fixtures()
