# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 1:04
# @Author  : ESJIAN
# @Email   : esjian@outlook.com
# @File    : ui_utils.py
# @Software: VsCode




from datetime import datetime

from PySide6.QtWidgets import QApplication, QWidget
import pandas as pd  
import os

from configparser import ConfigParser
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QLineEdit,QHBoxLayout,QGroupBox

from src.gui.error_window import TagNumShortage,IndexOutOfRange                 # Learning1：子模块的导入相对路径的起算点是主模块
from src.gui.check_window import ExcelCheckWindow               # Learning2:顶级脚本设定绝对倒入配置后不需要在子模块中重设
from src.gui.data_save_dialog import data_save_success
from src.core.excel_handler import store_single_entry_to_temple_excel  # Fixed1:将项目包以绝对形式导入,解决了相对导入不支持父包的报错
from src.core.excel_handler import commit_data_to_storage_excel

import __main__                                                 # Learning5:__main__模块的引用，访问主模块变量



def get_current_date():
    """
    获取系统当前日期，格式为 YYYY-MM-DD
    :param: None
    :return: 当前日期的字符串，格式为 YYYY-MM-DD
    """
    return datetime.now().strftime("%Y-%m-%d")


def manual_temp_storage(self,input_fields):
    """
    暂存当前条目所有输入框内的信息
    :param input_fields: 输入框的字典或列表，键为字段名，值为对应的 QLineEdit 对象
    :return: 包含所有输入框内容的字典
    """
    values_must_have = [
        self.line1Right,  # 日期
        self.line3Right,  # 品名
        self.line2Right,  # 类别
        self.line6Right,  # 数量
        self.line5Right,  # 金额
        self.line9Right,  # 公司
        self.line10Right  # 单名
    ]

    for i in values_must_have:
        if i.text() == "":
            i.setPlaceholderText("该项必填")
            #显示错误窗口
            show_error_window(self)
            return None


    __main__.TEMP_LIST_ROLLBACK_SIGNAL = False  # type: ignore # Learning3：信号量，标记是否需要回滚
    exsit_tag_number = 0                        # 统计有内容的输入框数量

    temp_storage = {}                           # 存储输入框内容的字典

    try:
        for field_name, input_field in input_fields.items():
            if __main__.DEBUG_SIGN == True:
                exsit_tag_number+=1
                temp_storage[field_name] = input_field

            elif input_field.text() :              # 检查输入框是否有内容
                exsit_tag_number+=1                # 统计有内容的输入框数量
                temp_storage[field_name] = input_field.text() # 将输入框内容存储到字典
        if __main__.DEBUG_SIGN == True:
            __main__.SERIALS_NUMBER += 1   # type: ignore

        if exsit_tag_number==__main__.TOTAL_FIELD_NUMBER:

            self.line1Right.setText("")         # Learning4：对QLineEdit组件使用setText()方法重置输入框内容
            self.line2Right.setText("")
            self.line3Right.setText("")
            self.line4Right.setText("")
            self.line5Right.setText("")
            self.line6Right.setText("")
            self.line7Right.setText("")
            self.line8Right.setText("")
            self.line9Right.setText("")
            self.line10Right.setText("")

            self.line1Right.setPlaceholderText(input_fields['日期'])
            self.line2Right.setPlaceholderText(input_fields['类别'])
            self.line3Right.setPlaceholderText(input_fields['品名'])
            self.line4Right.setPlaceholderText(input_fields['备注'])
            self.line5Right.setPlaceholderText(input_fields['金额'])
            self.line6Right.setPlaceholderText(input_fields['数量'])
            self.line7Right.setPlaceholderText(input_fields['单价'])
            self.line8Right.setPlaceholderText(input_fields['单位'])
            self.line9Right.setPlaceholderText(input_fields['公司'])
            self.line10Right.setPlaceholderText(input_fields['单名'])
            

            __main__.TEMP_STORAGED_NUMBER_LISTS +=1 # type: ignore # Learning5：形式参数传参进来的变量
            try:
                self.storageNum.setText(str(__main__.TEMP_STORAGED_NUMBER_LISTS-1))  # 更新存储数量的标签文本
            except Exception as e:
                print(f"Error: {e}")
                return None
            
            # 打印暂存数据（可以替换为其他逻辑，如保存到文件或数据库）
            print("暂存数据:", temp_storage)
            # 调用 store_single_entry_to_excel 函数存储数据到Excel文件,以xls方式存储

            store_single_entry_to_temple_excel(temp_storage, __main__.TEMP_SINGLE_STORAGE_EXCEL_PATH)
            data_save_success(self)             # 显示保存成功的消息提示弹窗
            self.spinBox.setValue(int(self.storageNum.text())) # 更新SpinBox的值为存储数量
            temp_list_rollback(self)
            return temp_storage
        else:
            print("Warning: Not all fields are filled.")
            show_error_window(self) # 显示错误窗口
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    

def show_error_window(self):
    """
    显示错误窗口
    :param: None
    :return: None
    """

    
    if hasattr(self, 'Form') and self.PopWindowApplicationForm.isVisible():
        return  # 如果弹窗已经存在且可见，则不重复创建

    # 检验self是否有名为app的属性
    self.PopWindowApplication = QApplication.instance()
    if not self.PopWindowApplication:
        # 若没有为self追加创建一个app属性,继承自QApplication
        self.PopWindowApplication = QApplication([])
        # 为self追加创建一个Form属性,继承自QWidget
        self.PopWindowApplicationForm = QWidget()
        # 为self追加一个ui属性,继承自TagNumShortage
        self.PopWindowApplicationUi = TagNumShortage()
        #
        self.PopWindowApplicationUi.setupUi(self.PopWindowApplicationForm)
        
        self.PopWindowApplicationForm.show()
    else:
        # 为self追加创建一个Form属性,继承自QWidget
        self.PopWindowApplicationForm = QWidget()
        # 为self追加一个ui属性,继承自TagNumShortage
        self.PopWindowApplicationUi = TagNumShortage()
        #
        self.PopWindowApplicationUi.setupUi(self.PopWindowApplicationForm)
        
        self.PopWindowApplicationForm.show()


def show_check_window(self,file_path):
    """
    显示检查窗口
    :param: self,file_path
    :return: None
    """
    # 为self追加创建一个app属性,继承自QApplication
    #self.PopWindowAplication = QApplication([])  # Learning3&Fixed2:一个程序只能有一个 QApplication 实例


    # 为self追加创建一个Form属性,继承自QWidget
    self.PopWindowApplicationForm = QWidget()
    # 为self追加一个ui属性,继承自excel_check_window
    self.PopWindowApplicationUi = ExcelCheckWindow()
    # 将 ui 属性与 form 属性 
    self.PopWindowApplicationUi.set_up_Ui(self.PopWindowApplicationForm)
    
    self.PopWindowApplicationUi.load_table_data(file_path)

    # 展示窗口
    self.PopWindowApplicationForm.show()
    

def commit_data_to_excel(self,model,workbook_path,sub_main_food_workbook,sub_auxiliary_food_workbook):
    """
    提交数据到主表、副表Excel文件
    :param: self
    :return: None
    """

    commit_data_to_storage_excel(self,model,workbook_path,sub_main_food_workbook,sub_auxiliary_food_workbook)


def temp_list_rollback(self):
    """
    实现点击信息栏中“正在编辑xx项目”上下箭头时,正在编辑条目回滚的视图回滚
    :param: self
    :return: None
    """

    print(f"Notice:当前编辑条目为第{self.spinBox.value()}项,条目切换信号为{__main__.TEMP_LIST_ROLLBACK_SIGNAL}")

    if self.spinBox.value()>0 and __main__.TEMP_LIST_ROLLBACK_SIGNAL == True: # Learning6：py的与符号是and关键字而不是&，&是位运算符
        try:
            temp_storage = pd.read_excel(__main__.TEMP_SINGLE_STORAGE_EXCEL_PATH)
            print(temp_storage)
            index = self.spinBox.value()
    
            # 如果目标条目索引号在已存储列表范围内，则切换到阅览已存储条目模式
            if 0 < index <= len(temp_storage):#这里左边改成开区间了, 不能为0, 下同
                # 获取当前条目的数据
                current_entry = temp_storage.iloc[index-1]
                # 更新输入框内容
                self.line1Right.setText(str(current_entry['日期']))
                self.line2Right.setText(str(current_entry['类别']))
                self.line3Right.setText(str(current_entry['品名']))
                self.line4Right.setText(str(current_entry['备注']))
                self.line5Right.setText(str(current_entry['金额']))
                self.line6Right.setText(str(current_entry['数量']))
                self.line7Right.setText(str(current_entry['单价']))
                self.line8Right.setText(str(current_entry['单位']))
                self.line9Right.setText(str(current_entry['公司']))
                self.line10Right.setText(str(current_entry['单名']))

            # 如果目标条目索引号超出已存储列表+1，则切换到输入条目模式
            elif 0 < index <= len(temp_storage)+1:
                self.line1Right.setText("")
                self.line2Right.setText("")
                self.line3Right.setText("")
                self.line4Right.setText("")
                self.line5Right.setText("")
                self.line6Right.setText("")
                self.line7Right.setText("")
                self.line8Right.setText("")
                self.line9Right.setText("")
                self.line10Right.setText("")

            # 如果目标编辑条目索引号超出已存储列表范围+1，则提示错误，并且返回最后改动的条目上
            else:
                print("Notice: 条目超出范围，请检查条目索引号")

                # 重置条目索引到报错前
                self.spinBox.setValue(int(self.storageNum.text())) # 更新SpinBox的值为存储数量

                # 弹窗报错
                # 为self追加创建一个Form属性,继承自QWidget
                self.PopWindowApplicationForm = QWidget()
                # 为self追加一个ui属性,继承自TagNumShortage
                self.PopWindowApplicationUi = IndexOutOfRange() # Learning7：不要误用成self.IndexOutOfRange(self)，因为IndexOutOfRange是一个类，而不是一个函数
                #
                self.PopWindowApplicationUi.setupUi(self.PopWindowApplicationForm)
                
                self.PopWindowApplicationForm.show()
                
                return None
                
        except Exception as e:
                    print(f"Error: {e}")
                    return None
    else:
        #将其设置为1
        if self.spinBox.value() <= 0:
            self.spinBox.setValue(1)
        __main__.TEMP_LIST_ROLLBACK_SIGNAL = True
        
def show_setting_window(self):
    """
    显示设置窗口
    :param: self
    :return: None
    """
    self.settings_window = QWidget()
    self.settings_window.setWindowTitle("设置")
    self.settings_window.resize(400, 300)

    # 将此布局与父widget关联
    main_layout = QHBoxLayout(self.settings_window)
    
    # 创建子Group Box 布局组件
    self.manual_group_box = QGroupBox(self.settings_window)
    self.manual_group_box.setTitle("手动导入设置")
    self.img_group_box = QGroupBox(self.settings_window)
    self.img_group_box.setTitle("照片导入设置")
    # 为 setting_window 对两个group box 设置布局
    main_layout.addWidget(self.manual_group_box)
    main_layout.addWidget(self.img_group_box)

    

    # 设定手动导入管理选项
    manual_layout = QVBoxLayout(self.manual_group_box)

    # Add toggle for "Auto-fill Date"
    self.auto_fill_date_toggle = QPushButton("自动填充日期")
    self.auto_fill_date_toggle.setCheckable(True)
    self.auto_fill_date_toggle.setChecked(get_ini_setting("Settings", "auto_fill_date", file_path='../../config/config.ini') == 'True')
    print(get_ini_setting("Settings", "auto_fill_date", file_path='../../config.ini') == 'True')
    self.auto_fill_date_toggle.clicked.connect(lambda: modify_ini_setting("Settings", "auto_fill_date", self.auto_fill_date_toggle.isChecked()))
    manual_layout.addWidget(self.auto_fill_date_toggle)

    # Add toggle for "Auto-calculate Total Price"
    self.auto_calc_price_toggle = QPushButton("自动根据单价数量计算总价")
    self.auto_calc_price_toggle.setCheckable(True)
    self.auto_calc_price_toggle.setChecked(get_ini_setting("Settings", "auto_calc_price", file_path='../../config/config.ini') == 'True')
    self.auto_calc_price_toggle.clicked.connect(lambda: modify_ini_setting("Settings", "auto_calc_price", self.auto_calc_price_toggle.isChecked()))
    manual_layout.addWidget(self.auto_calc_price_toggle)

    close_button = QPushButton("点击关闭")
    close_button.clicked.connect(self.settings_window.close)
    manual_layout.addWidget(close_button)

    # 设定照片导入管理选项
    img_layout = QVBoxLayout(self.img_group_box)

    # Add toggle for "Auto-fill Date"
    self.img_auto_fill_date_toggle = QPushButton("自动填充日期")
    self.img_auto_fill_date_toggle.setCheckable(True)
    self.img_auto_fill_date_toggle.setChecked(get_ini_setting("Settings", "img_auto_fill_date", file_path='../../config/config.ini') == 'True')
    #print(get_ini_setting("Settings", "img_auto_fill_date", file_path='../../config.ini') == 'True')
    self.img_auto_fill_date_toggle.clicked.connect(lambda: modify_ini_setting("Settings", "img_auto_fill_date", self.img_auto_fill_date_toggle.isChecked()))
    

    # Add toggle for "Auto-calculate Total Price"
    self.img_auto_calc_price_toggle = QPushButton("自动根据单价数量计算总价")
    self.img_auto_calc_price_toggle.setCheckable(True)
    self.img_auto_calc_price_toggle.setChecked(get_ini_setting("Settings", "img_auto_calc_price", file_path='../../config/config.ini') == 'True')
    self.img_auto_calc_price_toggle.clicked.connect(lambda: modify_ini_setting("Settings", "img_auto_calc_price", self.img_auto_calc_price_toggle.isChecked()))
    

    close_button = QPushButton("点击关闭")
    close_button.clicked.connect(self.settings_window.close)

    # 将子组件放入布局组件进行管理
    img_layout.addWidget(self.img_auto_fill_date_toggle)
    img_layout.addWidget(self.img_auto_calc_price_toggle)
    img_layout.addWidget(close_button)

    
    # 设定主窗口的布局
    self.settings_window.setLayout(main_layout)
    # 显示窗口
    self.settings_window.show()

def close_setting_window(self):
    """
    关闭设置窗口
    :param: self
    :return: None
    """
    if hasattr(self, 'settings_window'):
        self.settings_window.close()
        del self.settings_window

def modify_ini_setting(section, option, new_value, file_path='../../config/config.ini'):
    """
    修改INI配置文件中指定的设置项。如果文件、段或选项不存在则自动创建。

    参数:
        section (str): 配置段名
        option (str): 配置项名
        new_value (str): 新的值
        file_path (str): INI 文件路径

    返回:
        bool: 修改成功返回 True，失败返回 False
    """
    config = ConfigParser()
    # 如果文件存在就读取；否则创建空文件
    new_value = str(new_value)   
    if os.path.isfile(file_path):
        config.read(file_path, encoding='utf-8')
    else:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("")  # 创建空文件

    try:
        if section not in config:
            config.add_section(section)

        config[section][option] = new_value

        with open(file_path, 'w', encoding='utf-8') as f:
            config.write(f)
        print(f"'{section}' 中 '{option}' 的值已修改为: {new_value}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        print(f"Error: 无法修改 '{section}' 中 '{option}' 的值")
        return False

def get_ini_setting(section, option, file_path='../../config/config.ini'):
    """
    从INI配置文件中获取指定设置项的值。
    若文件、段或选项不存在，则自动创建并写入 "False"，然后返回 "False"。

    参数:
        section (str): 配置段名
        option (str): 配置项名
        file_path (str): INI 文件路径

    返回:
        str: 配置项的值；若不存在则返回 "False"
    """
    config = ConfigParser()

    # 文件不存在：创建空文件
    if not os.path.isfile(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True) if os.path.dirname(file_path) else None
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("")

    config.read(file_path, encoding='utf-8')

    updated = False

    if section not in config:
        config.add_section(section)
        updated = True

    if option not in config[section]:
        config[section][option] = "False"
        updated = True

    if updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            config.write(f)
        return "False"

    return config.get(section, option)

def convert_place_holder_to_text(self):
    """
    将当前输入框的占位符转换为文本
    :param: self
    :return: None
    """
    #检查当前聚焦的输入框
    current_widget = self.focusWidget()
    if isinstance(current_widget, QLineEdit):
        #获取当前输入框的占位符文本
        placeholder_text = current_widget.placeholderText()
        #将占位符文本设置为输入框的文本
        current_widget.setText(placeholder_text)
    
def cancel_input_focus(self):
    """
    取消当前输入框的焦点
    :param: self
    :return: None
    """
    #检查当前聚焦的输入框
    current_widget = self.focusWidget()
    if isinstance(current_widget, QLineEdit):
        #取消当前输入框的焦点
        current_widget.clearFocus()

def mode_not_right(self, MODE):
    text = self.line10Right.text()
    if "入库" in text or "出库" in text:
        # MODE == 0 表示当前系统是入库模式
        if "出库" in text and MODE == 0:
            return True  # 模式是入库，但写了出库
        elif "入库" in text and MODE == 1:
            return True  # 模式是出库，但写了入库
    return False



            



# Summary：
# 1. 抽象的看所有widget都是一个个的对象，都是有属性和方法的，属性就是它的状态，方法就是它能做的事情。


# Learning：
# 1. 弹窗事件循环的生命周期依赖于该调用函数的声明周期，如果该函数是一个独立的函数，那么它的生命周期就会在函数调用结束后结束，导致弹窗无法正常显示。
#    子弹窗要想和共享主窗口的声明周期，需要利用self的引用来实现。也就是在主窗口中创建子窗口的实例，并将其作为属性存储在主窗口中，这样子窗口就可以和主窗口共享生命周期了。
#    来源：Fixed1的修复
# 2. 顶级脚本设定绝对导入包配置代码后不需要在子模块中重设，因为主代码设置好的变量子代码可见
#    变量的传递分为单个文件内，和跨文件两种方式去传递
# 3. 在存在主窗口的时候，在创建子窗口时，不要创建新的QApplication实例，而是使用已经存在的实例。因为QApplication只能有一个实例，创建多个实例会导致错误。
#    来源：Fixed2的修复
# 4. 如果直接是self.date_2 = ""，self.date_2不再指向原来的 QLineEdit 对象，而是被重新赋值为一个字符串 ""
# 5. 
# 6. 
# 7. 明确一个类你是想调用还是想实例化，调用就是直接使用类名加括号，实例化就是以创建一个对象。

# TODO：
# - [x] 2025.4.46 实现报错弹窗功能 
#   - [x] 修复报错弹框的闪现问题
# - [x] 2025.4.27 实现调用check_window.py以展示表格操作弹窗
#   - [x] 修复 RuntimeError: Please destroy the QApplication singleton before creating a new QApplication instance.
#   - [x] 修复 Excel 展示弹窗，仅弹窗但是不显示内容的问题——原因见main_window.py的Learning3
# - [x] 2025.4.29 实现暂存重置输入框功能
# - [x] 2025.4.30 实当前编辑条目的更新、实现暂存条目数量的更新
#   - [x] 修复保存条目数量更新时，一直重复更新第一个的问题
# - [x] 2025.4.30 实现暂存条目回滚功能
#   - [x] 修复条目回滚箭头引起的条目索引变动与实际存储条目造成的索引变动皆触发索引窗口更新的问题
#     - [x] 修复Error: local variable 'exsit_tag_number' referenced before assignment
#     - [x] 修复点击箭头界面无索引更新现象的问题
#   - [x] 2025.5.1 修复滚动索引列表值不能跳到暂存列表数+1以至无法开始输入下一个条目的问题
#   - [x] 2025.5.1 修复Error: IndexOutOfRange() takes no arguments的问题
# - [ ] 2025.4.30 实现自动提交逻辑
#  - [x] 2025.5.1 实现公司表单金额自动增加
#  - [ ] 2025.5.2 实现入库类型的条目登记自动增加