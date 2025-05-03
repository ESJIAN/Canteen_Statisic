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

from src.gui.utils.detail_ui_button_utils import commit_data_to_excel, get_current_date, manual_temp_storage, temp_list_rollback # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错
from src.gui.utils.detail_ui_button_utils import show_check_window
from src.core.excel_handler import clear_temp_excel, store_single_entry_to_temple_excel # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错

TOTAL_FIELD_NUMBER = 10 # 录入信息总条目数

TEMP_SINGLE_STORAGE_EXCEL_PATH = ".\\src\\data\\input\\manual\\temp_manual_input_data.xls" # Learning9：路径读取常用相对路径读取方式，这与包的导入方式不同
TEMP_STORAGED_NUMBER_LISTS = 1 # 初始编辑条目索引号
TEMP_LIST_ROLLBACK_SIGNAL = True # Learning3：信号量，标记是否需要回滚

MIAN_WORK_EXCEL_PATH = ".\\src\\data\\storage\\cache\\主表\\" # 主工作表格路径
Sub_WORK_EXCEL_PATH = ".\\src\\data\\storage\\cache\\子表\\"  # 子工作表格路径

SERIALS_NUMBER = 1
DEBUG_SIGN = True
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
        # 日期输入行
        self.line1Left = QLabel(self.groupBox)
        self.line1Left.setObjectName(u"date")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.line1Left)

        self.line1Right = QLineEdit(self.groupBox)
        self.line1Right.setObjectName(u"date_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.line1Right)
        # Learning4：标签-输入框组的结束

        # 类别输入行
        self.line2Left = QLabel(self.groupBox)
        self.line2Left.setObjectName(u"foodType")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.line2Left)

        self.line2Right = QLineEdit(self.groupBox)
        self.line2Right.setObjectName(u"foodType_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.line2Right)

        # 品名输入行
        self.line3Left = QLabel(self.groupBox)
        self.line3Left.setObjectName(u"name")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.line3Left)

        self.line3Right = QLineEdit(self.groupBox)
        self.line3Right.setObjectName(u"name_2")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.line3Right)

        # 单位输入行
        self.line8Left = QLabel(self.groupBox)
        self.line8Left.setObjectName(u"Label_3")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.line8Left)

        self.line8Right = QLineEdit(self.groupBox)
        self.line8Right.setObjectName(u"LineEdit_3")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.line8Right)
        
        # 单价输入行
        self.line7Left = QLabel(self.groupBox)
        self.line7Left.setObjectName(u"Label_2")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.line7Left)

        self.line7Right = QLineEdit(self.groupBox)
        self.line7Right.setObjectName(u"LineEdit_2")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.line7Right)


        # 数量输入行
        self.line6Left = QLabel(self.groupBox)
        self.line6Left.setObjectName(u"Label")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.line6Left)

        self.line6Right = QLineEdit(self.groupBox)
        self.line6Right.setObjectName(u"LineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.line6Right)

        # 金额输入行
        self.line5Left = QLabel(self.groupBox)
        self.line5Left.setObjectName(u"amount")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.line5Left)

        self.line5Right = QLineEdit(self.groupBox)
        self.line5Right.setObjectName(u"amount_2")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.line5Right)

        # 备注输入行
        self.line4Light = QLabel(self.groupBox)
        self.line4Light.setObjectName(u"info")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.line4Light)

        self.line4Right = QLineEdit(self.groupBox)
        self.line4Right.setObjectName(u"info_2")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.line4Right)

        # 公司输入行
        self.line9Left = QLabel(self.groupBox)
        self.line9Left.setObjectName(u"info_3")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.line9Left) # Learning5：使用QFormLayout.ItemRole.LabelRole 来设置标签

        self.line9Right = QLineEdit(self.groupBox)
        self.line9Right.setObjectName(u"info_4")    

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.line9Right) # Learning5：使用QFormLayout.ItemRole.FieldRole 来设置输入框

        # 主表入库类型单名输入行
        self.line10Left = QLabel(self.groupBox)
        self.line10Left.setObjectName(u"info_5")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.line10Left)
        
        self.line10Right = QLineEdit(self.groupBox)
        self.line10Right.setObjectName(u"info_6")
        
        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.line10Right)


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

        # 提交数据按钮创建配置

        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.buttonGroup.addButton(self.pushButton_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(220, 190, 75, 24))
        self.pushButton_5.clicked.connect(self.commit_data)


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
        self.spinBox.valueChanged.connect(self.information_edition_rollback) # Learning5：将SpinBox的值变化与信息栏回滚函数连接
                                                                             # Learning7：槽函数若有括号，则会立即执行，而不是在信号触发时执行
                                                                             # Learning8：valueChanged时候去获取起变化的值是变化之后的值           
        self.horizontalLayout.addWidget(self.spinBox)

        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.storageNum = QLabel(self.widget_5)
        self.storageNum.setObjectName(u"plainTextEdit")

        self.horizontalLayout.addWidget(self.storageNum)


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
        
        # 输入框左侧Label名
        self.line1Left.setText(QCoreApplication.translate("Form", u"\u65e5\u671f", None))
        self.line1Right.setText("")
        self.line2Left.setText(QCoreApplication.translate("Form", u"\u7c7b\u522b", None))
        self.line3Left.setText(QCoreApplication.translate("Form", u"\u54c1\u540d", None))
        self.line4Light.setText(QCoreApplication.translate("Form", u"\u5907\u6ce8", None))
        self.line5Left.setText(QCoreApplication.translate("Form", u"\u91d1\u989d", None))
        self.line6Left.setText(QCoreApplication.translate("Form", u"\u6570\u91cf", None)) # Learning2: unicode 编码,详情见 unicode.md 
        self.line7Left.setText(QCoreApplication.translate("Form", u"\u5355\u4ef7", None))
        self.line8Left.setText(QCoreApplication.translate("Form", u"\u5355\u4f4d", None))
        self.line9Left.setText(QCoreApplication.translate("Form", u"\u516c\u53f8", None)) 
        self.line10Left.setText(QCoreApplication.translate("Form", "单名", None))

        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u4fee\u8ba2\u63d0\u4ea4", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u6682\u5b58\u8be5\u6761", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4\u6570\u636e", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6\u65e5\u671f", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u68c0\u67e5", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"\u4fe1\u606f\u680f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6b63\u5728\u7f16\u8f91\u7b2c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9879", None))
        self.label_3.setText(QCoreApplication.translate("Form", "已暂存", None))

        self.spinBox.setValue(TEMP_STORAGED_NUMBER_LISTS)  # 重置SpinBox的值为0
        self.storageNum.setText(QCoreApplication.translate("Form",str(TEMP_STORAGED_NUMBER_LISTS-1), None))
        
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
            "日期": f"2025-5-2",
            "品名": f"品名{SERIALS_NUMBER}",
            "类别": "主食",
            "单位": f"单位{SERIALS_NUMBER}",
            "单价": SERIALS_NUMBER+1,
            "数量": SERIALS_NUMBER+2,
            "金额": SERIALS_NUMBER+3,
            "备注": f"备注{SERIALS_NUMBER}",
            "公司": "聚鑫干调",
            "单名": "扶贫主食入库",
        }

        # 调用 manual_temp_storage 函数获取输入框内容
        manual_temp_storage(self,input_fields) # 传入self参数


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
        mian_workbook = MIAN_WORK_EXCEL_PATH + "2025.4.20.xls"
        commit_data_to_excel(self,mian_workbook)


    def information_edition_rollback(self): # Learning6：自定义方法一定要放一个self参数,不妨报错
        """
        信息栏，编辑条目回滚
        :param: self
        :return: None
        """
        # 调用 temp_list_rollback 函数实现条目回滚
        temp_list_rollback(self)


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
    # 设置关闭事件
    Form.closeEvent = lambda event: (clear_temp_excel(), print("Notice:清空暂存表格成功"), event.accept())
    sys.exit(app.exec())

# Summerize:
# 1. 创建Widget时候的对于该widget的属性设置,包括名称,大小,布局，槽函数等放在一块
# 2. 代码中的GUI组件代码尽可能取分组，且要放置批注以便后续定位代码-GUI组件的匹配


# Learning:
# 1. 相对导入的情况一共分为四种,只有导入同级别目录和导入子包这两种情况以主脚本模式运行没有问题
#    但相对导入父包这情况就会遇上问题,所以为此我手动改成了绝对导入模式,此Bug知识点见doc/learning/python 8.4 节
# 2. 实现点击按钮响应事件的步骤主要有三个：1.创建按钮 2.写槽函数 3. 将按钮信号与槽函数绑定
#    这个逻辑是基于事件驱动的哲学
# 3. 对于函数内部来讲，如果产生形参名与实参名撞名的情况，则在函数内访问该变量，实际上实在访问
#    传入的形参名，如果形参未传入则返回的是布尔值 False
# 4. Qtcreator 生成的ui代码块默认张这样的格式：
# 5.
# 6. 
# 7. 
# 8.
# TODO：
# [x] 2025.4.30 实现暂存栏暂存条目数的动态更新
# [x] 2025.4.30 实现窗口关闭时自动清空临时存储表格的数据
# [x] 2025.4.30 实现spinBox控件值变化时，录入信息窗口更新相应项的条目信息
# [x] 2025.4.30 实现信息栏正在编辑第几项的跳转逻辑
