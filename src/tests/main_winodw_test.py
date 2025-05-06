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
import threading
import shutil

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, Qt)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget, QFileDialog, QDialog, QVBoxLayout)


# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__) # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错
# 获取项目根目录
project_root = os.path.abspath(os.path.join(current_file_path, '..', '..', '..')) # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错
# 将项目根目录添加到 sys.path
sys.path.insert(0, project_root) # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错

from src.gui.utils.detail_ui_button_utils import (
    commit_data_to_excel,
    get_current_date,
    manual_temp_storage,
    temp_list_rollback,
    show_setting_window,
    get_ini_setting,
    close_setting_window,
    convert_place_holder_to_text,
    cancel_input_focus,
    mode_not_right
)
# Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错
from src.gui.utils.detail_ui_button_utils import show_check_window
from configparser import ConfigParser
from src.core.excel_handler import clear_temp_xls_excel, clear_temp_xlxs_excel,store_single_entry_to_temple_excel # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错
from src.core.image_handler import image_to_excel
from src.gui.photo_preview_dialog import preview_image
import multiprocessing
import subprocess
from PySide6.QtWidgets import QMessageBox

TOTAL_FIELD_NUMBER = 10 # 录入信息总条目数

TEMP_SINGLE_STORAGE_EXCEL_PATH = os.path.join("src", "data", "input", "manual", "temp_manual_input_data.xls") # Learning9：路径读取常用相对路径读取方式，这与包的导入方式不同
TEMP_STORAGED_NUMBER_LISTS = 1 # 初始编辑条目索引号
TEMP_LIST_ROLLBACK_SIGNAL = True # Learning3：信号量，标记是否需要回滚

MAIN_WORK_EXCEL_PATH = ".\\src\\data\\storage\\cache\\主表\\" # 主工作表格路径
Sub_WORK_EXCEL_PATH = ".\\src\\data\\storage\\cache\\子表\\"  # 子工作表格路径

MAIN_WORK_EXCEL_PATH = os.path.join(project_root, MAIN_WORK_EXCEL_PATH) # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错
Sub_WORK_EXCEL_PATH = os.path.join(project_root, Sub_WORK_EXCEL_PATH) # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错
print(MAIN_WORK_EXCEL_PATH,Sub_WORK_EXCEL_PATH) # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错

#这个0/1用来表示是入库出库
MODE = 0

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

        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)  # 设置顶部间距为 0 像素(第二个0)

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

        self.setting = ClickableImage("")  # Use the ClickableImage class for clickable functionality
        self.setting.setObjectName("settingLabel")
        self.setting.setAlignment(Qt.AlignRight | Qt.AlignTop)  # type: ignore # Align to the top-right corner
        self.setting.setFixedSize(30, 30)  # Increase the size of the label
        self.setting.setText("⚙️")  # Use a gear emoji as a placeholder
        self.setting.setStyleSheet("font-size: 25px;")  # Make the gear emoji larger
        self.gridLayout_3.addWidget(self.setting, 0, 0, Qt.AlignRight | Qt.AlignTop)  # type: ignore # Add to the top-right corner of the main layout
        self.setting.mousePressEvent = lambda event: self.show_settings()  # Connect the click event to a function

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

        "提交数据按钮创建配置"
        
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")

        self.pushButton_6 = QPushButton(self.groupBox_3)
        self.buttonGroup.addButton(self.pushButton_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(220, 240, 75, 24))
        self.pushButton_6.clicked.connect(self.clear_temp_manual_list)
        
        self.pushButton_7 = QPushButton(self.groupBox_3)
        self.buttonGroup.addButton(self.pushButton_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(220, 100, 75, 24))
        self.pushButton_7.clicked.connect(self.temp_store_inputs)

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

        self.pushButton_2 = QPushButton(self.groupBox_3)               # Learing2：第一步创建按钮
        self.buttonGroup.addButton(self.pushButton_2)
        self.pushButton_2.setObjectName(u"pushButton_2")               # 设置按钮的ObjectName
        self.pushButton_2.setGeometry(QRect(220, 140, 75, 24))         # 设置按钮的几何位置 
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

        "输入界面右侧按钮创建"
        # 导入文件按钮 
        self.pushButton_3 = QPushButton(self.groupBox_4)                # 创建按钮，设置其父组件为grounpBox_4
        self.pushButton_3.setObjectName(u"pushButton_3")                # 设置该按钮的ObjectName
        self.pushButton_3.setGeometry(QRect(210, 30, 75, 24))           # 设置按钮位置
        self.pushButton_3.clicked.connect(self.photo_import)            # 绑定槽函数
        
        # 暂存该条按钮
        self.pushButton_4 = QPushButton(self.groupBox_4)                # 创建按钮，设置其父组件为grounpBox_4
        self.pushButton_4.setObjectName(u"pushButton_4")                # 设置该按钮的ObjectName
        self.pushButton_4.setGeometry(QRect(210, 70, 75, 24))           # 设置按钮位置
        self.pushButton_4.clicked.connect(self.temp_store_photo_inputs) # 绑定槽函数
        
        # 输入检查按钮
        self.pushButton_8 = QPushButton(self.groupBox_4)                # 创建按钮，设置其父组件为grounpBox_4
        self.pushButton_8.setObjectName(u"pushButton_8")                # 设置该按钮的ObjectName
        self.pushButton_8.setGeometry(QRect(210, 110, 75, 24))          # 设置按钮位置
        self.pushButton_8.clicked.connect(self.check_photo_input_data)  # 绑定槽函数

        # 提交数据按钮
        self.pushButton_9 = QPushButton(self.groupBox_4)                 # 创建按钮，设置其父组件为grounpBox_4
        self.pushButton_9.setObjectName(u"pushButton_9")                 # 设置该按钮的ObjectName
        self.pushButton_9.setGeometry(QRect(210, 150, 75, 24))           # 设置按钮位置
        self.pushButton_9.clicked.connect(self.commit_data)              # 绑定槽函数

        # 导入清空按钮
        self.pushButton_10 = QPushButton(self.groupBox_4)                # 创建按钮，设置其父组件为grounpBox_4
        self.pushButton_10.setObjectName(u"pushButton_10")               # 设置该按钮的ObjectName
        self.pushButton_10.setGeometry(QRect(210, 190, 75, 24))          # 设置按钮位置
        self.pushButton_10.clicked.connect(self.clear_temp_photo_import_list)  # 绑定槽函数


        self.tabWidget_2.addTab(self.tab_3, "")
        #点击切换入库/出库(测试中0504 16:40)(一行)
        self.tabWidget_2.tabBar().tabBarClicked.connect(self.on_tab_clicked)




        

        self.horizontalLayout_2.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab, "")

        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")

        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")


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
        Form.setWindowTitle(QCoreApplication.translate("Form", "食品管理系统", None))         # 设置窗口标题：食品管理系统
        self.groupBox_3.setTitle(QCoreApplication.translate("Form","手动导入", None))         # 设置组框标题：手动导入
        self.groupBox.setTitle(QCoreApplication.translate("Form", "录入信息", None))          # 设置组框标题：录入信息

        "输入框左侧Label名"
        self.line1Left.setText(QCoreApplication.translate("Form", u"\u65e5\u671f", None))    # 设置左侧Label：日期
        self.line1Right.setText("")  # 设置右侧输入框为空
        self.line2Left.setText(QCoreApplication.translate("Form", u"\u7c7b\u522b", None))    # 设置左侧Label：类别
        self.line3Left.setText(QCoreApplication.translate("Form", u"\u54c1\u540d", None))    # 设置左侧Label：品名
        self.line4Light.setText(QCoreApplication.translate("Form", u"\u5907\u6ce8", None))   # 设置左侧Label：备注
        self.line5Left.setText(QCoreApplication.translate("Form", u"\u91d1\u989d", None))    # 设置左侧Label：金额
        self.line6Left.setText(QCoreApplication.translate("Form", u"\u6570\u91cf", None))    # 设置左侧Label：数量
        self.line7Left.setText(QCoreApplication.translate("Form", u"\u5355\u4ef7", None))    # 设置左侧Label：单价
        self.line8Left.setText(QCoreApplication.translate("Form", u"\u5355\u4f4d", None))    # 设置左侧Label：单位
        self.line9Left.setText(QCoreApplication.translate("Form", u"\u516c\u53f8", None))    # 设置左侧Label：公司
        self.line10Left.setText(QCoreApplication.translate("Form", "单名", None))             # 设置左侧Label：单名

        "手动导入右侧按钮命名"
        self.pushButton.setText(QCoreApplication.translate("Form", "获取日期", None))         # 设置按钮文本：获取日期
        self.pushButton_7.setText(QCoreApplication.translate("Form", "暂存该条", None))       # 设置按钮文本：暂存该条
        self.pushButton_2.setText(QCoreApplication.translate("Form", "输入校验", None))       # 设置按钮文本：输入校验
        self.pushButton_5.setText(QCoreApplication.translate("Form", "提交数据", None))       # 设置按钮文本：提交数据
        self.pushButton_6.setText(QCoreApplication.translate("Form", "条目清空", None))       # 设置按钮文本：条目清空
        
        
        
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"信息栏", None))         # 设置组框标题：信息栏
        self.label.setText(QCoreApplication.translate("Form", u"正在编辑第", None))           # 设置标签文本：正在编辑第
        self.label_2.setText(QCoreApplication.translate("Form", u"项目", None))               # 设置标签文本：项目

        self.label_3.setText(QCoreApplication.translate("Form", "已暂存", None))

        self.spinBox.setValue(1)  # 重置SpinBox的值为1
        self.storageNum.setText(QCoreApplication.translate("Form",str(TEMP_STORAGED_NUMBER_LISTS-1), None))
        
        self.label_4.setText(QCoreApplication.translate("Form", u"\u9879", None))
        
        "照片导入右侧按钮命名"
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", "照片导入", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", "照片列表", None))
        
        self.pushButton_3.setText(QCoreApplication.translate("Form", "导入文件", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", "暂存该条", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", "输入检查", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", "提交数据", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", "条目清空", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Form", u"入库/切换", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"填写数据", None))

        #自动填充日期
        if get_ini_setting("Settings", "auto_fill_date") == "True":
            self.show_current_date()

        #绑定单价和数量文本框变化触发自动计算
        self.line7Right.textChanged.connect(self.auto_calc_amount)#单价数量绑定到一块儿
        self.line6Right.textChanged.connect(self.auto_calc_amount)#数量

        
        self.line1Right.setText("2025-5-5")       # 日期
        self.line2Right.setText("副食")           # 类别
        self.line3Right.setText("土豆")           # 品名
        self.line4Right.setText("备注")           # 备注
        self.line5Right.setText("420.0")         # 金额
        self.line6Right.setText("420")            # 数量
        self.line7Right.setText("1")              # 单价
        self.line8Right.setText("斤")             # 单位
        self.line9Right.setText("嘉亿格")       # 公司
        self.line10Right.setText("自购副食入库")  # 单名


    # retranslateUi
    """
    下面是一些按钮的槽函数，但是核心的功能实现在detail_ui_button_utils.py中
    """


    def on_tab_clicked(self, index):
        """
        当点击标签时，切换入库出库
        :param: self, index
        :return: None
        """
        global MODE
        text = ["入库/切换", "出库/切换"]
        t = text.index(self.tabWidget_2.tabText(index), 0)
        MODE = 1 - t
        print("当前模式", text[MODE], str(MODE))
        newText = text[1 - t]
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Form", newText, None))

    def auto_calc_amount(self):
        """
        当单价与数量都有的时候自动计算金额
        :param: self
        :return: None
        """
        #这里的代码不会太多，多了我就像你一样放到detail_ui_button_utils.py
        if get_ini_setting("Settings", "auto_calc_price") == "False":
            return
        try:
            if (self.line7Right.text() == "" or self.line6Right.text() == ""):
                self.line5Right.setText("")
            unitPrice = round(float(self.line7Right.text()), 2)
            amount = round(float(self.line6Right.text()), 2)
            totalPrice = str(round(unitPrice * amount, 2))
            self.line5Right.setText(totalPrice)
        except Exception as e:
            print(e)


    def show_current_date(self):
        """
        显示当前日期, 
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
        """
        input_fields = {
            "日期": f"2025-5-2",
            "品名": "大米",
            "类别": "主食",
            "单位": f"单位{SERIALS_NUMBER}",
            "单价": SERIALS_NUMBER+1,
            "数量": SERIALS_NUMBER+2,
            "金额": SERIALS_NUMBER+3,
            "备注": f"备注{SERIALS_NUMBER}",
            "公司": "聚鑫干调",
            "单名": "扶贫主食入库",
        }
        """
        input_fields = {
            "日期": self.line1Right.text(),
            "品名": self.line3Right.text(),
            "类别": self.line2Right.text(),
            "单位": self.line8Right.text(),
            "单价": self.line7Right.text(),
            "数量": self.line6Right.text(),
            "金额": self.line5Right.text(),
            "备注": self.line4Right.text(),
            "公司": self.line9Right.text(),
            "单名": self.line10Right.text(),
        }
        """
        input_fields = {
            "日期": "2025-5-3",..
            "品名": "大米",..
            "类别": "主食",..
            "单位": "kg",
            "单价": "7",
            "数量": "420",..
            "金额": "2940.0",..
            "备注": "备注",
            "公司": "汉付科技",..
            "单名": "扶贫主食出库",..
        }
        """
        print("输入的", input_fields)

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
        global MODE
        modeText = self.line10Right.text() if self.line10Right.text() != "" else self.line10Right.placeholderText()
        if "入库" in modeText and MODE == 1:
            print("自动切换为入库")
            MODE = 0
        elif "出库" in modeText and MODE == 0:
            print("自动切换为出库")
            MODE = 1
        
        main_workbook = MAIN_WORK_EXCEL_PATH + "2025.4.20.xls"
        sub_main_food_workbook = Sub_WORK_EXCEL_PATH + "2025年主副食-三矿版主食.xls"
        sub_auxiliary_food_workbook = Sub_WORK_EXCEL_PATH + "2025年 主副食-三矿版副食.xls"
        #commit_data_to_excel(self,main_workbook,sub_main_food_workbook,sub_auxiliary_food_workbook)
        threading.Thread(target=commit_data_to_excel, args=(self,main_workbook,sub_main_food_workbook,sub_auxiliary_food_workbook)).start() # Learning3：多线程提交数据，避免UI卡顿
        # Learning3：多线程提交数据，避免UI卡顿

    def clear_temp_manual_list(self):
        """
        清空手动输入条目
        :param: self
        :return: None

        """
        clear_temp_xls_excel()


    def information_edition_rollback(self): # Learning6：自定义方法一定要放一个self参数,不妨报错
        """
        信息栏，编辑条目回滚
        :param: self
        :return: None
        """
        # 调用 temp_list_rollback 函数实现条目回滚
        temp_list_rollback(self)

    def photo_import(self):
        """
        照片导入功能实现，支持批量导入和显示多张图片
        :param: self
        :return: None
        """
        # 1. 弹出文件选择器，支持多选图片
        
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg )")
        
        "检查选择的文件路径是否有效，加载文件到程序图片暂存文件夹，并且展示到界面上"
        if file_dialog.exec():
            # 获取选择的文件路径列表
            file_paths = file_dialog.selectedFiles()
            
            "将文件复制到 ./src/data/input/img 目录下"
            dest_dir = os.path.join(".", "src", "data", "input", "img")         # 目标目录
            os.makedirs(dest_dir, exist_ok=True)                                # 如果目标目录不存在，则创建它
            self.copied_paths = []                                              # 用于记录复制成功的文件路径列表，保存为属性
            for src_path in file_paths:                                         # 遍历每个文件路径
                dest_path = os.path.join(dest_dir, os.path.basename(src_path))  # 拼接目标路径已经文件名
                try: # 文件操作使用try和if进行容错考虑
                    shutil.copy2(src_path, dest_path)                           # 复制文件到目标路径
                    self.copied_paths.append(dest_path)                              # 记录复制成功的文件路径
                except Exception as e:
                    print(f"Error: 复制文件失败: {src_path} -> {dest_path}, 错误: {e}")
           
            "遍历复制后的文件路径,在父组件的容器布局中调用QLabel显示"
            if self.copied_paths:
                if not self.scrollAreaWidgetContents.layout():                  # 如果容器布局不存在，则创建它
                    self.scrollAreaWidgetContents.setLayout(QVBoxLayout())      # 为scrollAreaWidgetContents组件创建垂直布局
                layout = self.scrollAreaWidgetContents.layout()                 # 获取容器布局对象
                # 清空之前的内容，避免多次导入重复显示
                while layout.count():                                           # 清空布局
                    child = layout.takeAt(0)                                    # 从布局中移除子组件
                    if child.widget():                                          # 如果子组件是widget，则删除它
                        child.widget().deleteLater()                            # 删除子组件
                # 添加新图片文件名按钮，垂直紧凑排列
                for image_path in self.copied_paths:
                    btn = QPushButton(os.path.basename(image_path), self.scrollAreaWidgetContents)
                    btn.setFixedHeight(24)
                    # 增加轮廓阴影效果
                    btn.setStyleSheet("""
                        margin:0; 
                        padding:0; 
                        text-align:left; 
                        background:transparent; 
                        border: 1px solid #888; 
                        border-radius: 4px;
                        color:blue; 
                        text-decoration:underline;
                    """)
                    # 绑定点击事件，弹窗预览图片
                    btn.clicked.connect(lambda checked, path=image_path: preview_image(self,path))
                    layout.addWidget(btn)
                layout.addStretch(1)  # 保证紧凑排列
            
    
    def temp_store_photo_inputs(self):
        """
        将图片导入到临时存储区
        :param: self
        :return: None
        """
        if hasattr(self, "copied_paths") and self.copied_paths:
            pool = multiprocessing.Pool(processes=min(4, len(self.copied_paths)))
            # 调用pool的 apply_async 方法而不是 map 方法，防止主进程因为等待子线程的完成导致UI无响应
            for path in self.copied_paths:
                pool.apply_async(image_to_excel, args=(path,))
            pool.close()
            
    
        
    def check_photo_input_data(self): 
        """
        自动打开照片OCR转录后的数据所在文件夹，并弹窗提示用户手动打开表格检查数据
        :param: self
        :return: None
        """
        output_path = os.path.abspath("./src/data/input/manual/temp_img_input.xlsx")
        folder_path = os.path.dirname(output_path)
        # 弹窗提示，等待用户确认
        reply = QMessageBox.information(None, "提示", "即将打开 temp_img_input.xlsx 文件所在文件夹，请手动校核数据", QMessageBox.Ok | QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            # 打开文件夹
            if sys.platform.startswith('win'):
                os.startfile(folder_path)
            elif sys.platform.startswith('darwin'):
                subprocess.Popen(['open', folder_path])
            else:
                subprocess.Popen(['xdg-open', folder_path])

    def show_settings(self):
        """
        显示设置窗口
        :param: self
        :return: None
        """
        # 这里可以添加打开设置窗口的代码
        show_setting_window(self)

    def clear_temp_photo_import_list(self):
        """
        清空照片列表组件中的临时导入条目
        :param: self
        :return: None
        """
        # 一次性清空所有条目
        layout = self.scrollAreaWidgetContents.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
        


class KeyEventFilter(QObject):
    def eventFilter(self, watched, event):
        if event.type() == QEvent.KeyPress:
            key = event.key()
            modifiers = event.modifiers()
            if key == Qt.Key_Return:
                print("按下了 Enter")
            elif key == Qt.Key_Escape:
                cancel_input_focus(Form) # Learning3：取消输入框焦点
            elif key == Qt.Key_I and modifiers == Qt.ControlModifier:
                #print("按下了 Ctrl+Shift+I")
                convert_place_holder_to_text(Form)
            elif key == Qt.Key_S and modifiers == Qt.ControlModifier:
                if not hasattr(self, '_last_run') or (QTime.currentTime().msecsSinceStartOfDay() - self._last_run > 2000):
                    self._last_run = QTime.currentTime().msecsSinceStartOfDay()
                    ui.temp_store_inputs()  # 这儿只运行一次
            elif key == Qt.Key_D and modifiers == Qt.ControlModifier:
                ui.show_current_date()
        return super().eventFilter(watched, event)

class ClickableImage(QLabel):
    #chatgpt给的用于设置按钮的类
    def __init__(self, image_path):
        super().__init__()
        self.setPixmap(QPixmap(image_path).scaled(QSize(200, 200), Qt.KeepAspectRatio, Qt.SmoothTransformation)) # type: ignore
        self.setCursor(QCursor(Qt.PointingHandCursor)) # type: ignore
        self.setAlignment(Qt.AlignCenter) # type: ignore

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: # type: ignore
            print("图片被点击")



if __name__ == "__main__":

    # 创建一个QApplication对象
    app = QApplication(sys.argv) 
    # 创建一个QWidget对象
    Form = QWidget()
    # 创建Ui_Form对象
    ui = Ui_Form()
    key_filter = KeyEventFilter()
    app.installEventFilter(key_filter)  # 安装到整个应用程序，而不是 Form
    # 调用setupUi方法设置UI界面
    ui.setupUi(Form)
    # 设置窗口标题
    Form.show()
    # 设置关闭事件
    Form.closeEvent = lambda event: (clear_temp_xls_excel(),clear_temp_xlxs_excel(), print("Notice:清空暂存表格成功"), close_setting_window(ui), event.accept())
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
# [x] 2025.5.3 实现加载图片功能
#    [x] 2025.5.3. 实现点击滚动窗口中的文件条目实现以弹出的方式预览图片
# [x] 2025.5.4 实现导入图片区的暂存按钮功能
# [x] 2025.5.6 解决多线程识别图片时候主线程未响应的问题
# [ ] 2025.5.6 解决多线程识别图片功能对图片的覆写问题