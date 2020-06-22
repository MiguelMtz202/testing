from inputdatamanager import InputDataManager
#this is the main version 1.01

from docx.shared import Cm, Inches, Mm, Emu, Pt
from docxtpl import DocxTemplate, InlineImage

Data = InputDataManager

doc = DocxTemplate("neocemod-template.docx")
context = Data.newDictionary

doc.render(context)
newDocName = "gen_neocemod-report.docx"
doc.save(newDocName)