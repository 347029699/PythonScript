from win32com import client as wc
import os
from docx import Document
import re

label = ["转让方名称", "注册地（住所）", "法定代表人或负责人", "证件类别", "证件号", "注册资本(万元)",
         "注册资本币种",
         "所属行业", "企业类型", "经济类型", "经营规模", "国资监管类型", "国家出资企业或主管部门名称",
         "国家出资企业或主管部门统一社会信用代码或组织机构代码", "转让方内部决策文件类型", "批准单位名称",
         "批准文件类型", "批准文件名称", "批准日期", "标的名称", "挂牌起始价", "交易保证金", "设备品种", "设备名称",
         "设备规格", "数量", "标的所在位置", "现状", "标的踏勘联系人", "联系电话", "评估（估值）机构", "估值依据类别",
         "核准（备案）机构", "备案编号/核准编号", "核准(备案)日期", "评估基准日", "评估值(万元)", "单价评估值（万元）",
         "账面价值(万元)", "资产原值（万元）", "首次信息发布公告期",
         "首次信息发布期满后，如仅征集到一家及符合条件的意向受让方，则采取",
         "首次信息发布期满后，如征集到两家及以上符合条件的意向受让方，则采取", "信息发布期满后，如未征集到意向受让方",
         "价款支付方式", "与转让相关其他条件", "受让方资格条件", "是否允许联合受让", "是否交纳保证金", "交纳金额",
         "交纳截止时间", "竞价方式", "加价幅度", "自由竞价时间", "限时报价时间"]


def read(path):  # 读取word数据
    if os.path.exists(path):
        docx_path = doc_to_docx(path)  # 若是doc格式,转换成docx
        document = Document(docx_path)
        tables = document.tables
        data = dict()
        content = []
        try:
            for i in range(4):
                rows = tables[i].rows  # 第一个表格
                rows_length = len(tables[i].rows)  # 行数
                for r_num in range(rows_length):  # 行遍历
                    temp = ""
                    for r_cell in rows[r_num].cells:
                        if r_cell.text == temp:
                            continue
                        else:
                            content.append(r_cell.text)
                            temp = r_cell.text
            for m in label:
                d = content[content.index(m) + 1]
                if re.search(r"\u25a1", d) is not None:
                    data[m] = re.findall("\u2611(.*?)\\s", d)[0]
                else:
                    data[m] = d.strip()
        except Exception:
            return "file content error"
        else:
            return data
    else:
        return "file path error"


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
