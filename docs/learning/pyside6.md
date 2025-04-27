# error_windows.py

## 对GUI执行模式的深入理解

是的，在UI编程中，程序的执行模式并不是简单的顺序执行，而是一种 **事件驱动的执行模式** 。这种模式的核心是通过事件循环（Event Loop）来管理用户交互和程序逻辑。

### 事件驱动的执行模式

1. **事件循环** ：

* 当程序启动时，UI框架（如 PySide6 或 PyQt）会创建一个事件循环。
* 事件循环会持续运行，等待用户的输入（如鼠标点击、键盘输入）或系统事件（如窗口关闭、定时器触发）。

1. **信号与槽机制** ：

* 在 PySide6 中，信号与槽是事件驱动编程的核心。
* **信号** ：当某个事件发生时（如按钮被点击），会发出一个信号。
* **槽** ：信号可以连接到一个槽函数，槽函数是用来处理信号的回调函数。
* 例如：

  **self**.pushButton.clicked.connect**(**Form.close**)**

  当按钮被点击时，会触发 [clicked](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 信号，调用 [Form.close](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 方法关闭窗口。

1. **非顺序执行** ：

* 由于事件是异步触发的，程序的执行顺序取决于用户的操作和事件的发生顺序。
* 例如，窗口显示后，程序不会立即执行按钮的点击逻辑，而是等待用户点击按钮时才触发相关代码。

### UI编程的特点

* **异步性** ：程序的逻辑由事件触发，而不是按代码的顺序执行。
* **响应性** ：程序需要快速响应用户的操作，保持界面流畅。
* **并发性** ：某些操作（如网络请求或耗时任务）需要在后台运行，以免阻塞主线程。

### 总结

UI编程的执行模式更复杂，因为它需要处理用户交互、系统事件和后台任务。通过事件循环和信号槽机制，程序可以以一种灵活且高效的方式响应各种事件。

# ui_utils.py

## 窗口闪现问题

弹窗闪现的问题通常是因为 [QApplication.exec()](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 被调用后，程序的事件循环结束，导致窗口立即关闭。

简单的来讲出现这问题的原因无非是你想要创建一个新弹窗，但是Pyside6窗口的生命周期的维护是绑定函数的，你在子函数实现那么这个窗口的生命周期就由子函数维护，子函数一结束，这个窗口就消失了。

解决方案就是，子函数中传入self参数，把变量的执行改成属性的新增，这样即便子函数结束后，为目标对象新增的属性是不会随着子函数的结束而消失的，自然窗口闪现问题就得到了解决

---

### 问题原因

1. **重复创建 [QApplication](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 实例** ：

* 如果 [QApplication](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 已经存在，调用 [app.exec()](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 会导致事件循环结束后程序退出。
* 在 [show_error_window](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 函数中，每次调用都会尝试创建一个新的 [QApplication](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 或调用 [app.exec()](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)，这可能导致窗口闪现。

1. **事件循环的生命周期问题** ：

* 如果 [show_error_window](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 是在一个已经运行的 PyQt/PySide 应用中调用的，调用 [app.exec()](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 会干扰主事件循环。

---

### 解决方法

#### 方法 1：函数传参self参数，将子窗口的管理从局部函数的管控上升到self对象管控

```python
def show_error_window(self):
    """
    显示错误窗口
    :param: None
    :return: None
    """
    self.app = QApplication.instance()  # 检查是否已有 QApplication 实例
    if not self.app:
        self.app = QApplication([])  # 如果没有，则创建一个新的实例

    self.Form = QWidget()
    self.ui = Ui_Form()
    self.ui.setupUi(self.Form)
    self.Form.show()
    self.app.exec()  # Fixed1：若不加入self参数该独立事件的循环会导致窗口关闭后，程序无法继续执行，造成窗口闪现现象。


```

- # 方法解读
- ## 1. **生命周期绑定**

* 如果 [self](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 是主窗口的实例，那么 [show_error_window](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 中创建的 [QApplication](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 和窗口实例（[self.Form](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 和 [self.ui](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)）会成为主窗口对象的属性。
* 这样，弹窗的生命周期会与主窗口绑定，不会因为函数调用结束而被销毁。
* 弹窗不会因为函数调用结束而立即关闭（解决闪现问题）。
* 但如果主窗口销毁，弹窗也会随之销毁。

---

- ## 2. **避免局部变量销毁**

* 如果不传入 [self](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)，[self.Form](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 和 [self.ui](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 会是局部变量，函数执行完毕后会被销毁，导致弹窗无法正常显示。
* 传入 [self](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 后，这些变量会存储在调用对象中（因为这样的操作相当于新增属性），函数结束后仍然存在。
* 弹窗可以正常显示并保持打开状态，直到用户手动关闭。

---

- ## 3. **可能导致重复实例化**

* 如果多次调用 [show_error_window](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)，每次都会创建新的 [self.Form](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 和 [self.ui](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)，可能导致内存泄漏或重复实例化的问题。

**解决方法**：

* 在 [self](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 中检查是否已有弹窗实例，避免重复创建：

  **def** **show_error_window**(**self**)**:**

  **    **if** **hasattr**(**self**, **'Form'**)** **and** **self**.Form.isVisible**(**)**:**

  **        **return**  **# 如果弹窗已经存在且可见，则不重复创建

  **    **self**.app **=** QApplication.instance**(**)**

  **    **if** **not** **self**.app:**

  **        **self**.app **=** QApplication**(**[**]**)**

  **    **self**.Form **=** QWidget**(**)**

  **    **self**.ui **=** Ui_Form**(**)**

  **    **self**.ui.setupUi**(**self**.Form**)**

  **    **self**.Form.show**(**)**

---

- ## 4. **代码可读性和维护性**

* 使用 [self](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 使得弹窗的创建和管理更加清晰，因为它与主窗口共享状态。
* 但需要注意避免滥用 [self](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)，以免增加不必要的复杂性。

---

- ## 5. **总结**

传入 [self](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 后：

* 弹窗的生命周期与调用对象绑定，解决了闪现问题。
* 需要注意避免重复实例化弹窗，建议在 [self](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 中检查是否已有弹窗实例。
* 适合在主窗口或其他类中管理弹窗的场景。

---

#### 方法 2：使用 `QDialog` 代替 [QWidget](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)

`QDialog` 是专门用于弹窗的类，适合用作错误提示窗口。它可以通过 [exec()](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 方法阻塞当前逻辑，但不会干扰主事件循环。

修改 [show_error_window](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 函数如下：

**from** **PySide6**.**QtWidgets** **import** **QDialog**

**def** **show_error_window**(**)**:

**    **"""

**    显示错误窗口**

**    """**

**    **app** **=** QApplication.instance**(**)**  **# 检查是否已有 QApplication 实例**

**    **if** **not** **app**:**

**        **app** **=** QApplication**(**[**]**)**  **# 如果没有，则创建一个新的实例**

**    **Form** **=** **QDialog**(**)**  **# 使用 QDialog 代替 QWidget

**    **ui** **=** Ui_Form**(**)**

**    **ui**.setupUi**(**Form**)

**    **Form**.**setModal**(**True**)**  **# 设置为模态对话框**

**    **Form**.**exec**(**)**  **# 阻塞当前逻辑，直到窗口关闭

















## check_window.py




为该组件增加 `Ctrl+S` 快捷键保存表格数据到 Excel 文件的逻辑：


步骤：先编写槽函数，在编写信号事件，再把槽函数和信号事件连接起来


注意：如果该程序是作为主程序的一个弹窗实现的话


---

### 修改后的代码

**import** **pandas** **as** **pd**  **# 用于读取和保存 Excel 文件**

**from** **PySide6**.**QtCore** **import** **QCoreApplication**, **Qt**

**from** **PySide6**.**QtGui** **import** **QKeySequence**

**from** **PySide6**.**QtWidgets** **import** **(**QApplication**, **QHBoxLayout**, **QHeaderView**, **QSizePolicy**,**

**    **QTableWidget**, **QTableWidgetItem**, **QVBoxLayout**, **QWidget**, QShortcut**)

**class** **excel_check_window**(**object**)**:**

**    **def** **setupUi**(**self**, **Form**)**:

**        **if** **not** **Form**.objectName**(**)**:

**            **Form**.setObjectName**(**u**"Form"**)**

**        **Form**.resize**(**600**, **400**)**  **# 调整窗口大小

**        **self**.**horizontalLayout** **=** **QHBoxLayout**(**Form**)**

**        **self**.**horizontalLayout**.**setObjectName**(**u**"horizontalLayout"**)

**        **self**.**verticalLayout** **=** **QVBoxLayout**(**)

**        **self**.**verticalLayout**.**setObjectName**(**u**"verticalLayout"**)

**        **self**.**tableWidget** **=** **QTableWidget**(**Form**)**

**        **self**.**tableWidget**.**setObjectName**(**u**"tableWidget"**)

**        **self**.**verticalLayout**.**addWidget**(**self**.**tableWidget**)**

**        **self**.**horizontalLayout**.**addLayout**(**self**.**verticalLayout**)**

**        **self**.**retranslateUi**(**Form**)**

**        QMetaObject.connectSlotsByName**(**Form**)

**        **# 添加 Ctrl+S 快捷键保存逻辑

**        **self**.**save_shortcut** **=** QShortcut**(**QKeySequence**(**"Ctrl+S"**)**, **Form**)**

**        **self**.**save_shortcut**.activated.connect**(**self**.**save_table_data**)

**    **# 添加载入表格数据的逻辑

**    **def** **load_table_data**(**self**, **file_path**)**:

**        **"""

**        从 Excel 文件中加载数据到 QTableWidget**

**        :param file_path: Excel 文件路径**

**        """**

**        **try**:**

**            **# 使用 pandas 读取 Excel 文件

**            **data** **=** **pd**.**read_excel**(**file_path**)**

**            **# 设置表格行列数

**            **self**.**tableWidget**.**setRowCount**(**data**.**shape**[**0**]**)**  **# 行数

**            **self**.**tableWidget**.**setColumnCount**(**data**.**shape**[**1**]**)**  **# 列数

**            **self**.**tableWidget**.**setHorizontalHeaderLabels**(**data**.**columns**)**  **# 设置表头**

**            **# 填充表格数据

**            **for** **row** **in** **range**(**data**.**shape**[**0**]**)**:**

**                **for** **col** **in** **range**(**data**.**shape**[**1**]**)**:**

**                    **item** **=** **QTableWidgetItem**(**str**(**data**.**iloc**[**row**, **col**]**)**)**

**                    **self**.**tableWidget**.**setItem**(**row**, **col**, **item**)**

**            **print**(**"表格数据加载成功！"**)**

**        **except** **Exception** **as** **e**:**

**            **print**(**f**"加载表格数据时出错: **{**e**}**"**)

**    **# 添加保存表格数据的逻辑

**    **def** **save_table_data**(**self**)**:

**        **"""

**        将 QTableWidget 中的数据保存到 Excel 文件**

**        """**

**        **try**:**

**            **# 获取表格数据

**            **row_count** **=** **self**.**tableWidget**.**rowCount**(**)

**            **col_count** **=** **self**.**tableWidget**.**columnCount**(**)

**            **data** **=** **{**}**

**            **# 获取表头

**            **headers** **=** **[**self**.**tableWidget**.**horizontalHeaderItem**(**col**)**.**text**(**)** **for** **col** **in** **range**(**col_count**)**]

**            **# 获取每列数据

**            **for** **col** **in** **range**(**col_count**)**:

**                **column_data** **=** **[**]**

**                **for** **row** **in** **range**(**row_count**)**:

**                    **item** **=** **self**.**tableWidget**.**item**(**row**, **col**)**

**                    **column_data**.**append**(**item**.**text**(**)** **if** **item** **else** **""**)**

**                **data**[**headers**[**col**]**]** **=** **column_data

**            **# 转换为 DataFrame 并保存到 Excel

**            **df** **=** **pd**.**DataFrame**(**data**)**

**            **save_path** **=** **".**\\**src**\\**data**\\**output**\\**saved_table_data.xlsx"**  **# 保存路径

**            **df**.**to_excel**(**save_path**, **index**=**False**)**

**            **print**(**f**"表格数据已成功保存到 **{**save_path**}**"**)

**        **except** **Exception** **as** **e**:**

**            **print**(**f**"保存表格数据时出错: **{**e**}**"**)

**    **def** **retranslateUi**(**self**, **Form**)**:

**        **Form**.setWindowTitle**(**QCoreApplication**.**translate**(**"Form"**, **u**"Excel 数据查看"**, **None**)**)

**if** **__name__** **==** **"__main__"**:

**    **import** **sys

**    **app** **=** **QApplication**(**sys**.**argv**)**

**    **Form** **=** **QWidget**(**)

**    **ui** **=** **excel_check_window**(**)

**    **ui**.**setupUi**(**Form**)**

**    **# 示例：加载 Excel 文件数据

**    **excel_file_path** **=** **".**\\**src**\\**data**\\**input**\\**manual**\\**temp_manual_input_data.xlsx"**  **# Learning1:相对目录的起算位置

**    **ui**.**load_table_data**(**excel_file_path**)**

**    **Form**.**show**(**)

**    **sys**.**exit**(**app**.**exec**(**)**)**

**# Learning:**

**# 1. 文件路径的相对路径起算地址不是本文件,而是项目根目录**

**# **

**# **TODO**:**

**# - [ ] 在以顶级脚本运行模式下实现打开测试表格**

---

### 新增功能说明

1. **`Ctrl+S` 快捷键** ：

* 使用 `QShortcut` 创建快捷键 `Ctrl+S`，并绑定到 `save_table_data` 方法。
* 当用户按下 `Ctrl+S` 时，表格数据会被保存到指定的 Excel 文件中。

1. **保存表格数据的逻辑** ：

* 遍历 [QTableWidget](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 的所有单元格，提取数据并存储到一个字典中。
* 使用 Pandas 将字典转换为 `DataFrame`，然后保存为 Excel 文件。

1. **保存路径** ：

* 数据会保存到 `src\data\output\saved_table_data.xlsx` 文件中。
* 你可以根据需要修改保存路径。

---

### 示例运行

1. 运行程序后，加载 Excel 文件数据到表格。
2. 按下 `Ctrl+S`，表格中的数据会保存到 `saved_table_data.xlsx` 文件中。
3. 如果保存成功，控制台会打印：

   **表格数据已成功保存到 .\src\data\output\saved_table_data.xlsx**

---

### 注意事项

1. **依赖安装** ：

* 确保已安装 [pandas](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 和 `openpyxl`：

  **pip** **install** **pandas** **openpyxl**

1. **文件路径** ：

* 确保保存路径的目录存在。如果目录不存在，可以在保存前动态创建：

  **import** **os**

  **os**.**makedirs**(**os**.**path**.**dirname**(**save_path**)**, **exist_ok**=**True**)**

1. **表格数据完整性** ：

* 如果某些单元格为空，保存时会用空字符串代替。
