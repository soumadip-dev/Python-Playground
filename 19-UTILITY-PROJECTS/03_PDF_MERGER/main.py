from PyPDF2 import PdfWriter


pdf_writer = PdfWriter()

pdf_file_list = []


number_of_pdfs = int(input("How many PDF files do you want to merge? "))


for file_index in range(number_of_pdfs):
    pdf_file_name = input(f"Enter the name of PDF file {file_index + 1}: ")
    pdf_file_list.append(pdf_file_name)


for pdf_file in pdf_file_list:
    pdf_writer.append(pdf_file)


output_file_name = "merged_output.pdf"
pdf_writer.write(output_file_name)

pdf_writer.close()


print("PDF files have been merged successfully.")
