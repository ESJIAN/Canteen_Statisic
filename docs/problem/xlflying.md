你的报错：

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
