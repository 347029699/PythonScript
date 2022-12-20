from win32com import client as wc
import os


def read(path):  # 读取word数据
    if os.path.exists(path):
        docx_path = doc_to_docx(path)  # 若是doc格式,转换成docx
        data = dict()
    else:
        data = dict()
    return data


def doc_to_docx(path):
    filename, extension = os.path.splitext(path)
    print(path)
    if extension == ".doc" and filename.find("~$") < 0:
        word = wc.Dispatch("Word.Application")
        doc = word.Documents.Open(path)
        doc.SaveAs(os.path.splitext(path)[0] + ".docx", 12)
        doc.Close()
        word.Quit()
        return filename + ".docx"
    else:
        return path
