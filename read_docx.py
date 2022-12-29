from win32com import client as wc
import os
from docx import Document


def read(path):  # 读取word数据
    if os.path.exists(path):
        docx_path = doc_to_docx(path)  # 若是doc格式,转换成docx
        document = Document(docx_path)
        for i in document.paragraphs:
            if i.text == '' or i.text == '\n':
                continue
            else:
                print(i.text)

        # tables = document.tables
        # rows = tables[0].rows  # 行数 obj
        # columns = tables[0].columns  # 列数 obj
        # rows_length = len(tables[0].rows)  # 行数
        # columns_length = len(tables[0].columns)  # 列数
        # for r_num in range(rows_length):  # 行遍历
        #     r_content = []
        #     for r_cell in rows[r_num].cells:
        #         r_content.append(r_cell.text)
        #     print(r_content)

        # tables = document.tables  # 获取文件中的表格集
        # table = tables[0]  # 获取文件中的第一个表格
        # data = dict()
    else:
        data = dict()
    return data


def doc_to_docx(path):
    filename, extension = os.path.splitext(path)
    if extension == ".doc" and filename.find("~$") < 0:
        word = wc.Dispatch("Word.Application")
        doc = word.Documents.Open(path)
        doc.SaveAs(os.path.splitext(path)[0] + ".docx", 12)
        doc.Close()
        word.Quit()
        return filename + ".docx"
    else:
        return path
