from fpdf import FPDF
from sys import argv

#dict = {"NAME":argv[1],"Address":argv[2],"Mobile":argv[3],"Email":argv[4],"Date":argv[5],P_Address":argv[6],"P_NAME":argv[7],"P_PIN":argv[8]"Subject":argv[9],"Complaint":argv[10],"TIME":argv[11]}

class PDF(FPDF):
	def createLine(self):
		self.line(0,35,297,35)
	def header(self):
		self.set_font('Arial','B',24)
		self.multi_cell(0,8,"Proforma for Reporting the First Information (FIR) of a Cognizable Offence",0,'C',False)
		self.ln(20)
		self.line(0,35,297,35)
	def footer(self):
		self.set_y(-15)
		self.set_font('Arial','I',8)
		self.cell(0,10,'Page %s' % self.page_no(),0,0,'R')

	def StationDetails(self):
		self.set_font('Arial','B',12)
		self.cell(0,4,"Date : %s" % argv[5],0,0,'R')
		self.ln(5)
		self.multi_cell(0,4,'To,\n%s' % argv[7] +'\n%s\n' % argv[6] + '%s\n'%argv[8],0,'L',False)
		self.multi_cell(0,4,'\n\nSubject : %s' % argv[9])

	def FIR(self):
		self.set_font('Arial','',12)
		self.cell(0,4,'Dear Sir/Madam',0,0,'L')
		self.ln(30)
		self.multi_cell(0,6,'%s' % argv[10],0,'J',False)
		self.ln(30)
		self.multi_cell(0,4,'Yours Sincerely \n%s\n'%argv[1] + '\nMobile : %s\n'%argv[3] + '\nEmail: %s\n'%argv[4] +'\nAddress : %s\n'%argv[2],0,'L',False)

pdf=PDF()
pdf.add_page()
pdf.StationDetails()
pdf.FIR()
filepath="../firs/"
filename=filepath+argv[1]+'_'+argv[3]+'_'+argv[11]+'.pdf'
if(not pdf.output(filename)):
	print(filename)
else:
	print("File Could not be Created")