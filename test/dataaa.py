# import sys
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
# from PyQt4.QtWebKit import *
#
# app = QApplication(sys.argv)
#
# web = QWebView()
# web.load(QUrl("http://www.google.com"))
# # web.show()
#
# printer = QPrinter()
# printer.setPageSize(QPrinter.A4)
# printer.setOutputFormat(QPrinter.PdfFormat)
# printer.setOutputFileName("file.pdf")
#
#
# def convertIt():
#     web.print_(printer)
#     print "Pdf generated"
#     QApplication.exit()
#
#
# QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)
#
# sys.exit(app.exec_())
from lib2to3.pgen2 import driver

import weasyprint

pdf = weasyprint.HTML('http://www.google.com').write_pdf()

len(pdf)
file('google.pdf', 'w').write(pdf)


# screenshotBase64 = self.driver.get_screenshot_as_base64()

# driver.get_screenshot_as_file(‘/Screenshots/foo.png’)