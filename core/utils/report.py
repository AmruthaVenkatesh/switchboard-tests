import os
class Report:

    def generateSelfContainedReport(self):
        command  = "--html=report.html --self-contained-html"

    def generateCssReport(self):
        command = "--html=report.html --css=highcontrast.css --css=accessible.css"

    def pytest_html_report_title(report):
        report.title = "My very own title!"


'