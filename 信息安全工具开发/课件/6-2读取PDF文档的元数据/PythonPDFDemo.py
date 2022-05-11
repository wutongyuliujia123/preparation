# -*- coding:utf8 -*-
#from pyPdf import PdfFileReader,PdfFileWriter
#1.用pyPdf实现PDF文件复制，复制文件和原始文件存在差异，差异可用元数据表达
infn = 'in.pdf'
outfn = 'out.pdf'
##创建PDF文件读取器
# pdf_input = PdfFileReader(open(infn,'rb'))
##获取PDF文件页数
# page_count = pdf_input.getNumPages()
# print(page_count)
##获取某页数据
# print(pdf_input.getPage(1))
##创建写入器
# pdf_output = PdfFileWriter()
##遍历in.pdf读取每一页，并将该页放入写入器中
# for i in range(page_count):
#     page = pdf_input.getPage(i)
#     pdf_output.addPage(page)
##将写入器中的内容，写到out.pdf文件中
# pdf_output.write(open(outfn,'wb'))
#2.输出PDF文件相关的元数据
import PyPDF2
##创建读取器
reader = PyPDF2.PdfFileReader(open('out.pdf','rb'))
##获取PDF文件相关信息
info = reader.getDocumentInfo()
#print(dir(info))
##遍历info
for i in info:
    print("[+]" + i +":" + info[i])