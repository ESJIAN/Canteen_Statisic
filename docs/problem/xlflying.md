# 错误1

**sheet = main_workbook.sheets["扶贫主食入库"]**

**...**

**pywintypes.com_error: (-2147352567, 'Exception occ**urred.', ...)

**原因分析：**

* 你用 [main_workbook.sheets[&#34;扶贫主食入库&#34;]](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 访问 sheet，但 Excel 文件中**没有名为“扶贫主食入库”**的工作表（Sheet）。
* 或者该 sheet 名字有前后空格、隐藏字符、全角/半角等差异，导致找不到。

---

## 解决方法

### 1. 检查 Excel 文件中 sheet 的实际名称

用 Excel 打开 `2025.4.20.xls`，确认 sheet 名称 **完全一致** ，没有多余空格、符号或大小写差异。

### 2. 打印所有 sheet 名称进行比对

在出错前加一行打印所有 sheet 名称，帮助你定位问题：

**print**(**"所有sheet名："**, **[**s**.name **for** **s** **in** main_workbook.sheets**]**)**

### 3. 推荐防御式写法

**sheet_names** **=** **[**s**.name **for** **s** **in** main_workbook.sheets**]

**print**(**"所有sheet名："**, **sheet_names**)

**if** single_name **not** **in** **sheet_names**:

**    **print**(**f**"未找到入库类型名为 **{**single_name**}** 的sheet"**)

**    **return

**sheet** **=** main_workbook.sheets**[**single_name**]**

---

## 常见原因总结

* sheet 名称拼写不一致（如“扶贫主食入库 ”有空格）。
* sheet 名称有不可见字符或全角字符。
* 你传入的 [single_name](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 变量内容和实际 sheet 名称不一致。

---

**建议：**

1. 打印所有 sheet 名称，人工比对。
2. 必要时用 `.strip()` 去除 sheet 名前后空格。
3. 确认你的 Excel 文件确实有这个 sheet。

---

**示例修正：**

**sheet_names** **=** **[**s**.name **for** **s** **in** main_workbook.sheets**]

**print**(**"所有sheet名："**, **sheet_names**)

**target_name** **=** single_name.strip**(**)

**if** **target_name** **not** **in** **sheet_names**:

**    **print**(**f**"未找到入库类型名为 **{**target_name**}** 的sheet"**)

**    **return

**sheet** **=** main_workbook.sheets**[**target_name**]**

这样可以避免因为 sheet 名称不一致导致的 KeyError 或 com_error。

# 错误2：

**Error: 更新食堂物品收发存库存表时出错 Attempted to access 0-based **Range. xlwings/Excel Ranges are 1-based.

**原因：**

* 在 [xlwings](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 中，Excel 的行列索引是**从 1 开始**的（1-based），而不是 Python 常用的 0-based。
* 你在代码中有类似 [sheet.range((row_index, 1))](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 这样的写法，如果 [row_index](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 为 0，就会报这个错。

---

## 解决方法

**确保所有 [sheet.range((row_index, col_index))](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 的 [row_index](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 和 [col_index](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 都 ≥ 1。**

### 重点检查这段代码：

**for** **row_index** **in** **range**(**0**, sheet.used_range.rows.count**)**:

**    **if** sheet.range**(**(**row_index** , **1**)**)**.value **is** **None** **and** sheet.range**(**(**row_index** , **2**)**)**.value **is** **None** **and** **row_index** **!=** **0** **and** **row_index** **!=** **4**:**

**        **break

**# ...**

**sheet.range**(**(**row_index** , **1**)**)**.value **=** product_name**

* 这里 [row_index](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 从 0 开始，导致 [sheet.range((0, 1))](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 报错。

---

### 推荐修正

将所有相关 [row_index](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 的地方加 1，确保从 1 开始：

**for** **row_index** **in** **range**(**1**, sheet.used_range.rows.count **+** **1**)**:**

**    **if** sheet.range**(**(**row_index**, **1**)**)**.value **is** **None** **and** sheet.range**(**(**row_index**, **2**)**)**.value **is** **None** **and** **row_index** **!=** **1** **and** **row_index** **!=** **5**:**

**        **break

**# 更新该行A列的物品名称信息**

**sheet.range**(**(**row_index**, **1**)**)**.value **=** product_name**

* 如果你有特殊跳过首行/表头的需求，请相应调整判断条件。

---

**总结：**

* [xlwings](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 的 `.range((row, col))` 必须 [row &gt;= 1](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 且 [col &gt;= 1](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)。
* 检查所有相关代码，避免出现 0 作为行或列索引。

这样即可解决该报错。

# 错误3

是的，你遇到的这个错误：

**Error: 保存主表时出错 (-2147352567, 'Exception **occurred.', (0, 'Microsoft Excel', '文档未保存。', ...), **None)**

**很大概率和 Excel 进程未正常关闭有关。**

---

## 原因分析

* 如果你在调试或多次运行程序时， **Excel 进程未被关闭** ，文件句柄被占用，导致后续保存或写入时 Excel 拒绝保存（尤其是用 xlwings/xlwings.App 打开的文件）。
* 也可能是你打开了同一个文件的多个实例，或文件在 Windows 资源管理器中被占用。

---

## 解决方法

1. **确保每次操作后都关闭 Excel 应用和工作簿：**

   **main_workbook.save**(**)**

   **main_workbook.close**(**)**

   **app.quit**(**)**
2. **调试前手动结束所有 Excel 进程：**

   * 打开任务管理器，结束所有 `EXCEL.EXE` 进程。
   * 或在命令行运行：

     **taskkill /f /im excel.exe**
3. **避免多次打开同一个文件不关闭。**
4. **确保没有其他程序（如资源管理器、OneDrive等）占用该文件。**

---

## 代码建议

在 `with xw.App(visible=False) as app:` 结构下，`app` 会自动关闭，但如果你有异常提前退出，建议加上 `try...finally` 或确保 `main_workbook.close()` 被调用。

---

**总结：**

* 该错误常见于 Excel 文件被占用或进程未关闭。
* 关闭所有 Excel 进程，确保每次都正确关闭和保存工作簿，可以解决此问题。3. **避免多次打开同一个文件不关闭。**

4. **确保没有其他程序（如资源管理器、OneDrive等）占用该文件。**

---

## 代码建议

在 `with xw.App(visible=False) as app:` 结构下，`app` 会自动关闭，但如果你有异常提前退出，建议加上 `try...finally` 或确保 `main_workbook.close()` 被调用。

---

**总结：**

* 该错误常见于 Excel 文件被占用或进程未关闭。
* 关闭所有 Excel 进程，确保每次都正确关闭和保存工作簿，可以解决此问题。

# 错误4

你遇到的错误：

**Error: 保存主表时出错 (-2147417848, 'The object invoked **has disconnected from its clients.', None, None)

---

## 原因分析

这个错误通常是**Excel进程或对象提前被关闭或失效**导致的。常见原因包括：

1. **Excel进程被异常关闭** （如任务管理器强制关闭、代码中提前关闭了 app 或 workbook）。
2. **对象作用域问题** ，如 [main_workbook](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 或 [app](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 被销毁或超出 `with` 语句作用域后还在用。
3. **多线程/异步操作**导致 COM 对象失效。
4. **异常提前退出** ，导致 Excel 对象断开。

---

## 解决方法

### 1. **确保所有 Excel 操作都在 [with xw.App(...) as app:](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 作用域内完成**

不要在 `with` 语句块外部再访问 [main_workbook](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 或 [sheet](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)。

### 2. **不要提前关闭 workbook 或 app**

只在所有操作完成后再调用 [main_workbook.save()](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 和 [main_workbook.close()](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)，并确保这些操作都在 `with` 作用域内。

### 3. **异常处理时不要提前关闭 app**

如果你在 `try...except` 里提前关闭了 [main_workbook](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 或 [app](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)，后续再访问就会报这个错。

### 4. **不要让 Excel 进程被外部强制关闭**

调试时不要手动杀掉 Excel 进程。

---

## 推荐代码结构

**with** xw.App**(**visible**=**False**)** **as** **app**:

**    **try**:**

**        **main_workbook** **=** **app**.books.open**(**excel_file_path**)

**        **# ...所有Excel操作...

**        **main_workbook**.save**(**)**

**        **print**(**f**"Notice: 主工作表保存成功，文件路径: **{**excel_file_path**}**"**)

**        **main_workbook**.close**(**)**

**    **except** **Exception** **as** **e**:**

**        **print**(**f**"Error: **{**e**}**"**)

---

## 参考

你可以参考 [xlflying.md](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 中关于 Excel 进程和对象关闭的说明。

---

**总结：**

* 该错误本质是 Excel 对象失效或进程断开。
* 保证所有 Excel 操作都在 [with xw.App(...) as app:](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 作用域内完成，且不要提前关闭对象。
* 避免多线程/异步操作和外部强制关闭 Excel 进程。
