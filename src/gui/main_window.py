# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_v1MDUWYx.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
import os

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__) # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错
# 获取项目根目录
project_root = os.path.abspath(os.path.join(current_file_path, '..', '..', '..')) # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错
# 将项目根目录添加到 sys.path
sys.path.insert(0, project_root) # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错

from src.gui.utils.detail_ui_button_utils import get_current_date, manual_temp_storage # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错
from src.gui.utils.detail_ui_button_utils import show_check_window
from src.core.excel_handler import store_single_entry_to_excel # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错


TEMP_SINGLE_STORAGE_EXCEL_PATH = ".\\src\\data\\input\\manual\\temp_manual_input_data.xlsx"


class Ui_Form(object):
 


    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(779, 533)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_2 = QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 20, 309, 381))
        self.groupBox = QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 25, 208, 251))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        # Learning4：标签-输入框组的开始
        self.line1Left = QLabel(self.groupBox)
        self.line1Left.setObjectName(u"date")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.line1Left)

        self.line1Right = QLineEdit(self.groupBox)
        self.line1Right.setObjectName(u"date_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.line1Right)
        # Learning4：标签-输入框组的结束

        # 
        self.line2Left = QLabel(self.groupBox)
        self.line2Left.setObjectName(u"foodType")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.line2Left)

        self.line2Right = QLineEdit(self.groupBox)
        self.line2Right.setObjectName(u"foodType_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.line2Right)

        # 
        self.line3Left = QLabel(self.groupBox)
        self.line3Left.setObjectName(u"name")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.line3Left)

        self.line3Right = QLineEdit(self.groupBox)
        self.line3Right.setObjectName(u"name_2")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.line3Right)

        # 
        self.line4Right = QLabel(self.groupBox)
        self.line4Right.setObjectName(u"info")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.line4Right)

        self.line4Left = QLineEdit(self.groupBox)
        self.line4Left.setObjectName(u"info_2")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.line4Left)

        # 
        self.line5Left = QLabel(self.groupBox)
        self.line5Left.setObjectName(u"amount")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.line5Left)

        self.line5Right = QLineEdit(self.groupBox)
        self.line5Right.setObjectName(u"amount_2")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.line5Right)

        # 
        self.line6Left = QLabel(self.groupBox)
        self.line6Left.setObjectName(u"Label")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.line6Left)

        self.line6Right = QLineEdit(self.groupBox)
        self.line6Right.setObjectName(u"LineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.line6Right)

        # 
        self.line7Left = QLabel(self.groupBox)
        self.line7Left.setObjectName(u"Label_2")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.line7Left)

        self.line7Right = QLineEdit(self.groupBox)
        self.line7Right.setObjectName(u"LineEdit_2")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.line7Right)

        # 
        self.line8Left = QLabel(self.groupBox)
        self.line8Left.setObjectName(u"Label_3")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.line8Left)

        self.line9Right = QLineEdit(self.groupBox)
        self.line9Right.setObjectName(u"LineEdit_3")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.line9Right)

        # 
        self.line9Left = QLabel(self.groupBox)
        self.line9Left.setObjectName(u"info_3")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.line9Left) # Learning5：使用QFormLayout.ItemRole.LabelRole 来设置标签

        self.line9Right = QLineEdit(self.groupBox)
        self.line9Right.setObjectName(u"info_4")    

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.line9Right) # Learning5：使用QFormLayout.ItemRole.FieldRole 来设置输入框



        self.verticalLayout.addLayout(self.formLayout)

        self.pushButton_6 = QPushButton(self.groupBox_3)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.pushButton_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(220, 240, 75, 24))
        self.pushButton_7 = QPushButton(self.groupBox_3)
        self.buttonGroup.addButton(self.pushButton_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(220, 100, 75, 24))
        self.pushButton_7.clicked.connect(self.temp_store_inputs)
        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.buttonGroup.addButton(self.pushButton_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(220, 190, 75, 24))
        self.pushButton = QPushButton(self.groupBox_3)
        self.buttonGroup.addButton(self.pushButton)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 40, 75, 24))
        self.pushButton.clicked.connect(self.show_current_date)
        self.pushButton_2 = QPushButton(self.groupBox_3) # Learing2：第一步创建按钮
        self.buttonGroup.addButton(self.pushButton_2)
        self.pushButton_2.setObjectName(u"pushButton_2") # 设置按钮的ObjectName
        self.pushButton_2.setGeometry(QRect(220, 140, 75, 24)) # 设置按钮的几何位置 
        self.pushButton_2.clicked.connect(self.check_manual_input_data)# Learning3：第三步绑定按钮
        self.groupBox_5 = QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 290, 291, 81))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_5 = QWidget(self.groupBox_5)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout = QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.spinBox = QSpinBox(self.widget_5)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout.addWidget(self.spinBox)

        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.plainTextEdit = QPlainTextEdit(self.widget_5)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)


        self.horizontalLayout_3.addWidget(self.widget_5)

        self.groupBox_4 = QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(390, 20, 291, 381))
        self.groupBox_2 = QGroupBox(self.groupBox_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 20, 191, 261))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.groupBox_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 169, 224))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.pushButton_3 = QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(210, 30, 75, 24))
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")

        self.horizontalLayout_2.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget_3 = QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget_3.addTab(self.tab_6, "")

        self.gridLayout_2.addWidget(self.tabWidget_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        """
        Sets the text and titles of the UI elements to their respective translations.
        This method is automatically generated and is used to support internationalization.
        """
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u98df\u54c1\u7ba1\u7406\u7cfb\u7edf", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u624b\u52a8\u5bfc\u5165", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5f55\u5165\u4fe1\u606f", None))
        self.line1Left.setText(QCoreApplication.translate("Form", u"\u65e5\u671f", None))
        self.line1Right.setText("")
        self.line2Left.setText(QCoreApplication.translate("Form", u"\u7c7b\u522b", None))
        self.line3Left.setText(QCoreApplication.translate("Form", u"\u54c1\u540d", None))
        self.line4Right.setText(QCoreApplication.translate("Form", u"\u5907\u6ce8", None))
        self.line5Left.setText(QCoreApplication.translate("Form", u"\u91d1\u989d", None))
        self.line6Left.setText(QCoreApplication.translate("Form", u"\u6570\u91cf", None)) # Learning2: unicode 编码,详情见 unicode.md 
        self.line7Left.setText(QCoreApplication.translate("Form", u"\u5355\u4ef7", None))
        self.line8Left.setText(QCoreApplication.translate("Form", u"\u5355\u4f4d", None))
        self.line9Left.setText(QCoreApplication.translate("Form", u"\u516c\u53f8", None)) 
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u4fee\u8ba2\u63d0\u4ea4", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u6682\u5b58\u8be5\u6761", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4\u6570\u636e", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6\u65e5\u671f", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u68c0\u67e5", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"\u4fe1\u606f\u680f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6b63\u5728\u7f16\u8f91\u7b2c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9879", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6682\u5b58", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u9879", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"PDF\u5bfc\u5165", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u5bfc\u5165\u9884\u89c8", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u8f7d\u5165\u6587\u4ef6", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Tab 1", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Tab 1", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("Form", u"Tab 1", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("Form", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Tab 2", None))
    # retranslateUi
    
    
    """
    下面是一些按钮的槽函数，但是核心的功能实现在detail_ui_button_utils.py中
    """


    def show_current_date(self):
        """
        显示当前日期
        :param: self
        :return: None
        """
        # 获取当前日期
        current_date = get_current_date()
        # 设置QLineEdit的文本为当前日期
        self.line1Right.setText(current_date)
        # 设置QLineEdit为可写
        self.line1Right.setReadOnly(False)
    
    def temp_store_inputs(self):
        """
        暂存所有输入框内的信息
        :param: self
        :return: None
        """
        # 定义输入框的字典
        input_fields = {
            "日期": self.line1Right,
            "类别": self.line2Right,
            "品名": self.line3Right,
            "备注": self.line4Left,
            "金额": self.line5Right,
            "数量": self.line6Right,
            "单价": self.line7Right,
            "单位": self.line9Right,
            "公司":self.line9Left,
        }

        # 调用 manual_temp_storage 函数获取输入框内容
        manual_input_data = manual_temp_storage(self,input_fields) # 传入self参数

        # 打印暂存数据（可以替换为其他逻辑，如保存到文件或数据库）
        print("暂存数据:", manual_input_data)
        # 调用 store_single_entry_to_excel 函数存储数据到Excel文件
        store_single_entry_to_excel(manual_input_data, TEMP_SINGLE_STORAGE_EXCEL_PATH)
        

    def check_manual_input_data(self): # Learning3:传参参数名与某个全局变量同名，造成全局变量值无法被获取
        """
        弹窗且以EXCEL表格的形式检查手动输入的数据
        :param: self,excel_path
        :return: None
        """
        show_check_window(self,TEMP_SINGLE_STORAGE_EXCEL_PATH) 


    def commit_data(self):
        """
        提交数据
        :param: self
        :return: None
        """

        

        

        


        

if __name__ == "__main__":

    # 创建一个QApplication对象
    app = QApplication(sys.argv) 
    # 创建一个QWidget对象
    Form = QWidget()
    # 创建Ui_Form对象
    ui = Ui_Form()
    # 调用setupUi方法设置UI界面
    ui.setupUi(Form)
    # 设置窗口标题
    Form.show()
    sys.exit(app.exec())



# Learning:
# 1. 相对导入的情况一共分为四种,只有导入同级别目录和导入子包这两种情况以主脚本模式运行没有问题
#    但相对导入父包这情况就会遇上问题,所以为此我手动改成了绝对导入模式,此Bug知识点见doc/learning/python 8.4 节
# 2. 实现点击按钮响应事件的步骤主要有三个：1.创建按钮 2.写槽函数 3. 将按钮信号与槽函数绑定
#    这个逻辑是基于事件驱动的哲学
# 3. 对于函数内部来讲，如果产生形参名与实参名撞名的情况，则在函数内访问该变量，实际上实在访问
#    传入的形参名，如果形参未传入则返回的是布尔值 False

# TODO：
# [ ] 2025.4.30 实现暂存栏暂存条目数的动态更新
# [ ] 2025.4.30 实现信息栏正在编辑第几项的跳转逻辑