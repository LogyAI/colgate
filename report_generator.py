import pdfkit
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1920,1080))
display.start()

pdfkit.from_file("index.html", "report.pdf")