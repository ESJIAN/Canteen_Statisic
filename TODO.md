# 2025.4.26

## main_window.py

- [X] 为 `pushButton`实现系统日期获取功能

在 [ui_utils.py](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 中实现一个获取系统当前日期的函数，并在 [main_window.py](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 中调用它。以下是实现步骤：

### 1. 在 [ui_utils.py](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 中添加日期获取函数

**from** **datetime** **import** **datetime**

**def** **get_current_date**(**)**:

**    **"""

**    获取系统当前日期，格式为 YYYY-MM-DD**

**    """**

**    **return** **datetime**.**now**(**)**.**strftime**(**"%Y-%m-**%d**"**)**

### 2. 在 [main_window.py](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 中调用该函数

修改 [main_window.py](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)，在按钮点击事件中调用 `get_current_date` 函数。

**from** PySide6.QtWidgets **import** **QApplication**, **QWidget**, QMessageBox

**from** src.gui.utils.ui_utils **import** get_current_date  **# 导入日期获取函数**

**class** **Ui_Form**(**object**)**:**

**    **# ...existing code...

**    **def** **setupUi**(**self**, **Form**)**:

**        **# ...existing code...

**        **# 为获取日期按钮绑定事件

**        **self**.pushButton.clicked.connect**(**self**.**show_current_date**)

**    **def** **show_current_date**(**self**)**:

**        **"""

**        显示当前系统日期**

**        """**

**        **current_date** **=** get_current_date**(**)**

**        QMessageBox.information**(**None**, **"当前日期"**, **f**"系统当前日期为：**{**current_date**}**"**)**

### 3. 功能说明

* [ui_utils.py](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 中的 `get_current_date` 函数使用 `datetime.now()` 获取当前日期，并格式化为 `YYYY-MM-DD` 格式。
* 在 [main_window.py](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 中，按钮 [self.pushButton](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 的点击事件绑定到 `show_current_date` 方法，调用 `get_current_date` 并通过 `QMessageBox` 显示日期。

完成后，运行程序，点击按钮即可在日期输入栏目中看到当前日期的获取

- [X] 实现暂存按钮逻辑

[Used 1 reference]()

要将动作与 **`暂存该条`** 按钮（[pushButton_7](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)）链接起来，可以在 [setupUi](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 方法中为按钮绑定 [temp_store_inputs](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 方法。

以下是修改后的代码：

**class** **Ui_Form**(**object**)**:**

**    **def** **setupUi**(**self**, **Form**)**:

**        **# ...existing code...

**        **# 绑定按钮点击事件

**        **self**.pushButton_7.clicked.connect**(**self**.**temp_store_inputs**)**  **# 暂存该条按钮绑定到 temp_store_inputs 方法

**    **# ...existing code...

**    **def** **temp_store_inputs**(**self**)**:

**        **"""

**        暂存所有输入框内的信息**

**        """**

**        **# 定义输入框的字典

**        **input_fields** **=** **{

**            **"date"**: **self**.date_2,**

**            **"foodType"**: **self**.foodType_2,**

**            **"name"**: **self**.name_2,**

**            **"info"**: **self**.info_2,**

**            **"amount"**: **self**.amount_2,**

**            **"quantity"**: **self**.LineEdit,**

**            **"unit_price"**: **self**.LineEdit_2,**

**            **"unit"**: **self**.LineEdit_3,**

**        **}

**        **# 调用 manual_temp_storage 函数获取输入框内容

**        **temp_data** **=** manual_temp_storage**(**input_fields**)

**        **# 打印暂存数据（可以替换为其他逻辑，如保存到文件或数据库）

**        **print**(**"暂存数据:"**, **temp_data**)**

---

刚刚漏掉了把动作与 `暂存该条`按钮链接起来，现在请你做一下

### 修改说明

1. **绑定按钮事件** ：

* 在 [setupUi](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 方法中，使用 [self.pushButton_7.clicked.connect(self.temp_store_inputs)](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 将按钮点击事件与 [temp_store_inputs](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 方法关联。

1. **功能测试** ：

* 运行程序，填写输入框内容后，点击 **`暂存该条`** 按钮（[pushButton_7](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)）。
* 控制台会打印输入框的内容。

---

### 示例输出

当输入框内容如下：

* 日期：`2025-04-26`
* 类别：`水果`
* 品名：`苹果`
* 备注：`新鲜`
* 金额：`100`
* 数量：`10`
* 单价：`10`
* 单位：`kg`

点击 **`暂存该条`** 按钮后，控制台输出：

**暂存数据: {'date': '2025-04-26', 'foodType': '水果', **'name': '苹果', 'info': '新鲜', 'amount': '100', **'quantity': '10', 'unit_price': '10', 'unit': **'kg'}

## ui_utils.py 文件

- [X] 实现TAG未填满时候的弹窗警告功能
- [X] 实现暂存单条目表格功能

  - [X] 解决包的导入问题

## 核心功能
