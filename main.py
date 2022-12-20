from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time
import sys
import os
import loginui
import read_docx
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

page_list = {
    '【P3】预挂牌项目录入': 'http://www.nbcqjy.org/utr/utrg/pro/input.action?typeGz=P3',
    '【P3】预挂牌项目查询': 'http://www.nbcqjy.org/utr/utrg/pro/lists.action?typeGz=P3',
    '【G3】挂牌项目录入': 'http://www.nbcqjy.org/utr/utrg/pro/input.action?typeGz=G3',
    '【G3】挂牌项目查询': 'http://www.nbcqjy.org/utr/utrg/pro/lists.action?typeGz=G3',
    '【G0】非挂牌项目录入': 'http://www.nbcqjy.org/utr/utrg/pro/input.action?typeGz=G0',
    '【G0】非挂牌项目查询': 'http://www.nbcqjy.org/utr/utrg/pro/lists.action?typeGz=G0',
    '【T】非国有项目录入': 'http://www.nbcqjy.org/utr/utrg/pro/input.action?typeGz=T3',
    '【T】非国有项目查询': 'http://www.nbcqjy.org/utr/utrg/pro/lists.action?typeGz=T3',
    '企业增资预披露信息录入': 'http://www.nbcqjy.org/utr/utrz/pre/modify.action',
    '企业增资预披露查询': 'http://www.nbcqjy.org/utr/sendPage/utrz/prePro-list',
    '企业增资项目录入': 'http://www.nbcqjy.org/utr/utrz/gz/temp!list.action',
    '企业增资项目查询': 'http://www.nbcqjy.org/utr/sendPage/utrz/pro-list',
    '资产转让单资产项目录入': 'http://www.nbcqjy.org/utr/utr/pro/modify.action',
    '资产转让单资产项目查询': 'http://www.nbcqjy.org/utr/sendPage/utrm/pro/pro-list',
    '资产转让资产包录入': 'http://www.nbcqjy.org/utr/utr/pack/modify.action',
    '资产转让资产包查询': 'http://www.nbcqjy.org/utr/sendPage/utrm/pack/pack-list',
    '资产出租出租房及资产管理': 'http://www.nbcqjy.org/utr/sendPage/html?type=jsp&fileName=utrl/pack/seller-list',
    '资产出租租赁包管理（旧）': 'http://www.nbcqjy.org/utr/sendPage/html?type=jsp&fileName=utrl/pack/seller-list',
    '资产出租单租赁项目录入': 'http://www.nbcqjy.org/utr/utrlnew/pro/modify.action',
    '资产出租单租赁项目查询': 'http://www.nbcqjy.org/utr/sendPage/utrlnew/pro/pro-list',
    '资产出租租赁包录入': 'http://www.nbcqjy.org/utr/utrlnew/pack/modify.action',
    '资产出租租赁包查询': 'http://www.nbcqjy.org/utr/sendPage/utrlnew/pack/pack-list'
}

path = ""


def input_filepath(self):
    fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件", os.getcwd(),
                                                               "word文件(*.docx)、*.doc、*.docx")
    global path
    path = fileName
    ui.filePath.setText(fileName)


def clear_filepath(self):
    global path
    path = ""
    ui.filePath.setText("")


def start_func(self):
    username = ui.userName.text()
    passwd = ui.passwd.text()
    if len(username) == 0 or len(passwd) == 0:
        msg_box = QMessageBox(QMessageBox.Critical, '错误', '用户名或密码不能为空！')
        msg_box.exec_()
    elif len(path) == 0:
        msg_box = QMessageBox(QMessageBox.Critical, '错误', '请选择文件！')
        msg_box.exec_()
    else:
        main_func(username, passwd, path)


def main_func(username, passwd, filepath):
    data = read_docx.read(filepath)
    if not data:
        msg_box = QMessageBox(QMessageBox.Critical, '错误', '读取该文件数据为空或该路径不存在文件！')
        msg_box.exec_()
    else:
        print(data)
        driver = Service("E:/pythonProject/venv/Scripts/chromedriver.exe")
        browser = webdriver.Chrome(service=driver)
        browser.get('http://www.nbcqjy.org/utr/sendPage/flow/my-task-lists')
        browser.find_element(By.ID, "userEname").clear()
        browser.find_element(By.ID, "userEname").send_keys(username)
        browser.find_element(By.ID, "upass").clear()
        browser.find_element(By.ID, "upass").send_keys(passwd)
        browser.find_element(By.CLASS_NAME, "logging").click()
        time.sleep(1)
        error_message = browser.find_element(By.ID, "error-message").get_attribute("innerText")
        if len(error_message) > 0:
            browser.quit()
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '用户名或密码错误，无法登陆！')
            msg_box.exec_()
        else:
            browser.get(page_list['资产出租单租赁项目录入'])  # 选择栏目
            browser.find_element(By.NAME, "proName").clear()
            browser.find_element(By.NAME, "proName").send_keys("XXX房屋出租项目")  # 项目名称
            browser.find_element(By.NAME, "proPrice").clear()
            browser.find_element(By.NAME, "proPrice").send_keys("123")  # 出租底价
            browser.find_element(By.ID, "isGzw_T").click()  # 是否国资（是）
            # browser.find_element(By.ID, "isGzw_F").click()  # 是否国资（否）
            browser.find_element(By.XPATH, '//*[@id="addForm"]/table/tbody/tr[5]/td/span[1]/span/span').click()
            browser.find_element(By.XPATH, '/html/body/div[7]/div/div[12]').click()  # 标的所在地区-省 默认浙江省
            browser.find_element(By.XPATH, '//*[@id="addForm"]/table/tbody/tr[5]/td/span[2]/span/span').click()
            browser.find_element(By.XPATH, '/html/body/div[8]/div/div[3]').click()  # 标的所在地区-市  默认宁波市
            browser.find_element(By.XPATH, '//*[@id="addForm"]/table/tbody/tr[5]/td/span[3]/span/span').click()
            browser.find_element(By.XPATH, '/html/body/div[9]/div/div[11]').click()  # 标的所在地区-区  默认奉化区
            browser.find_element(By.XPATH, "//input[@value='A17001']").click()  # 资产来源 企业实物资产
            # browser.find_element(By.XPATH, "//input[@value='A17002']").click()  # 资产来源 行政事业单位实物资产
            # browser.find_element(By.XPATH, "//input[@value='A17003']").click()  # 资产来源 其他
            browser.find_element(By.XPATH, "//input[@value='1']").click()  # 租赁种类 公房出租
            # browser.find_element(By.XPATH, "//input[@value='2']").click()  # 租赁种类 其他
            browser.find_element(By.NAME, "pro4").clear()
            browser.find_element(By.NAME, "pro4").send_keys("浙江省宁波市奉化区123")  # 标的物所在地
            # browser.find_element(By.CLASS_NAME, "save_btn").click()
            time.sleep(5)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = loginui.Ui_Dialog()
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.selectFile.clicked.connect(input_filepath)  # 选择文件按钮绑定
    ui.clearFile.clicked.connect(clear_filepath)  # 清空文件按钮绑定
    ui.startButton.clicked.connect(start_func)  # 开始按钮绑定

    sys.exit(app.exec())
