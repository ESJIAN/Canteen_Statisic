# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'check_window_v1BvpeFr.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
import pandas as pd  # 用于读取 Excel 文件
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from src.gui.data_save_dialog import data_save_success

class ExcelCheckWindow(object): # Learning3:类定义时候是不能把 self 写进去
    """
    Excel 数据查看弹窗类
    """
    def set_up_Ui(self, Form):
        """
        表格窗口初始化
        :param Form: QWidget对象
        :return: None
        """
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 400)  # 调整窗口大小
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

        # 添加 Ctrl+S 快捷键保存逻辑
        self.save_shortcut = QShortcut(QKeySequence("Ctrl+S"), Form)
        self.save_shortcut.activated.connect(self.save_table_data)

    # 添加载入表格数据的逻辑
    def load_table_data(self, file_path):
        """
        从 Excel 文件中加载数据到 QTableWidget
        :param file_path: Excel 文件路径
        """
        try:
            # 如果表格存在打开表格
            if os.path.exists(file_path):
                # 使用 pandas 读取 Excel 文件
                data = pd.read_excel(file_path)

                # 设置表格行列数
                self.tableWidget.setRowCount(data.shape[0])  # 行数
                self.tableWidget.setColumnCount(data.shape[1])  # 列数
                self.tableWidget.setHorizontalHeaderLabels(data.columns)  # 设置表头

                # 填充表格数据
                for row in range(data.shape[0]):
                    for col in range(data.shape[1]):
                        item = QTableWidgetItem(str(data.iloc[row, col]))
                        self.tableWidget.setItem(row, col, item)

                print("Notice:表格数据加载成功！")
            # 如果表格不存在则打印错误信息
            else:
                print(f"Error:Excel文件不存在: {file_path}")
        except Exception as e:
            print(f"Error:加载表格数据时出错,报错信息为{e}")

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Excel 数据查看", None))

 # 添加保存表格数据的逻辑
    def save_table_data(self):
        """
        将 QTableWidget 中的数据保存到 Excel 文件
        :param: self
        :return: None
        """
        try:
            # 获取表格数据
            row_count = self.tableWidget.rowCount()
            col_count = self.tableWidget.columnCount()
            data = {}

            # 获取表头
            headers = [self.tableWidget.horizontalHeaderItem(col).text() for col in range(col_count)]

            # 获取每列数据
            for col in range(col_count):
                column_data = []
                for row in range(row_count):
                    item = self.tableWidget.item(row, col)
                    column_data.append(item.text() if item else "")
                data[headers[col]] = column_data

            # 转换为 DataFrame 并保存到 Excel
            df = pd.DataFrame(data)
            from src.gui.main_window import TEMP_SINGLE_STORAGE_EXCEL_PATH # Learning4:延迟导入
            save_path = TEMP_SINGLE_STORAGE_EXCEL_PATH  # 保存路径
            df.to_excel(save_path, index=False)
            print(f"Notice:表格数据已成功保存到 {save_path}")
            data_save_success(self)

        except Exception as e:
            print(f"Error:保存表格数据时出错: {e}")


    


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = ExcelCheckWindow()
    ui.set_up_Ui(Form)

    # 加载 Excel 文件数据
    excel_file_path = ".\\src\\data\\input\\manual\\temp_manual_input_data.xlsx"  # Learning1:相对目录的起算位置
    ui.load_table_data(excel_file_path)
    # 展示窗口
    Form.show()
    sys.exit(app.exec())

# Learning:
# 1. 文件路径的相对路径起算地址不是本文件,而是项目根目录
# 2. 实现加载表格到显示窗口的这个过程,一定是先把表格加载的动作解决再是弹出窗口
#    用
# 3. 类定义时候不能把 self 参数写进去
# 4. 子模块能够导入顶级模块的变量,但是顶级模块不能导入子模块的变量,但是需要延迟导入
#    否则会发生循环导入模块的错误

# TODO:
# - [x] 在以顶级脚本运行模式下实现打开测试表格 
# - [x] 实现打开表格时数据的保存功能
# - [x] 实现在主窗口中弹出表格展示窗口
# - [ ] 增加保存弹窗消息提醒功能