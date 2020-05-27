from fpdf import FPDF
from datetime import datetime
pdfOutput = "static/"
def writeHeading(pdf, pdfHeading):
    pdf.set_font("Arial", size=28, style="B")
    pdf.cell(200, 10, txt=pdfHeading, ln=1, align="C")
    pdf.set_line_width(1)
    pdf.line(0, 25, 220, 25)
    pdf.ln(10)

def writeQuestionAndSolutions(pdf, question, solution):
    effective_page_width = pdf.w - 2*pdf.l_margin
    pdf.set_font("Arial", size=14, style="B")
    pdf.multi_cell(effective_page_width, 6, question)
    pdf.ln(5)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(effective_page_width, 5, solution)
    pdf.ln(10)


def writePdf(userid, questionAnsList):
    pdf = FPDF()
    pdf.add_page()
    timestamp = int(datetime.timestamp(datetime.now()))
    writeHeading(pdf, "Doubtnut Solutions")
    for i, eachObject in enumerate(questionAnsList):
        question = f"Question {i+1}: {eachObject['question']}"
        answer = f"Solution {i+1}: {eachObject['answer']}"
        writeQuestionAndSolutions(pdf, question, answer)
    pdf.output(f"{pdfOutput}{userid}-{timestamp}.pdf")




if __name__ == "__main__":
    txt = "Prove that the angle between the two tangents drawn from an external point to a circle is supplementary to the angle subtended by the line-segment joining the points of contact at the centre."
    loremipsum = """Lorem ipsum dolor sit amet, vel ne quando dissentias. ut. At mea wisi dolorum contentiones, in malis vitae viderer mel.

    Vis at dolores ocurreret splendide. Noster dolorum repudiare vis ei, te augue summo vis. An vim quas torquatos, electram posidonium eam ea, eros \
    blandit ea vel. Reque summo assueverit an sit. Sed nibh conceptam cu, pro ocurreret adversarium, ne enim docendi mandamus sea.
    """
    questionAnsObject = {"question":txt, "answer": loremipsum}
    questionAnsList = [questionAnsObject, questionAnsObject, questionAnsObject]
    writePdf("schandan696", questionAnsList)