# 8.4 【基础】导入包的标准写法

> **总结**:Python导包主要有相对导入和绝对导入两种形式,**以有无点号区分**,导入目录语法的文件指针视角永远是在你本文文件所在的文件夹上而非文件上;`.`表示 `当前文件夹的..`,`..`表示 `上一级文件夹的..`,`...`表示 `上上一级别的文件夹的`,点号更多的时候以此类推,点号的含义是中文的 `的`

```ad-note
title:**快速回忆**
- 包是带有`__init__.py`的文件夹,单独的文件夹不能叫包
- 绝对导入语法中的`绝对`指的是基于项目文件夹的绝对而非计算机盘符的绝对.
- 绝对导入语法,比如`package.module.submodule`中的`package`是项目根目录下的第一个层级目录文件(非包)
- 绝对导入语法中,`package.module.submodule`中的`.`号翻译为`xx的`,
- 相对导入语法,比如`.package.module.submodule`的第一个`.`号翻译为`当前程序所在包目录的`,如果是`..`,翻译为`当前程序所在包目录的上一级包目录的`
- 相对导入法必须要求文件指针视角经过的所有文件夹都得带有一个`__init__.py`文件以说明这个文件夹是一个包,且相对导入父包时不允许以顶级脚本模式运行

```

## 8.4.1. 绝对导入

- ### 1. 语法

同时支持 `import` 以及 `from import` 两种导入语法

```python

import package.module.submodule  
from package.module.submodule import ClassOrFunc
```

如果单独上述代码无法运行,仍然报错无法见父包之类的问题的话在上述代码前加入以下代码()

```python
import sys
import os
# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)
# 获取项目根目录
project_root = os.path.abspath(os.path.join(current_file_path, '..', '..', '..'))
# 将项目根目录添加到 sys.path
sys.path.insert(0, project_root)
```

- ### 2. 特点

1. 直接写出顶层包名，路径清晰。
2. ==与当前模块位置无关==，只看项目的 `PYTHONPATH`（或当前工作目录＋`__init__.py`）。
3. 更易读、易维护，也是 PEP 8 ==推荐方式==。

- ### 3. 示例

项目结构：

```
myproj/
└─ src/ # PYTHONPATH 入口
   ├─ core/
   │   └─ excel_handler.py    # 定义 store_entry()
   └─ gui/
       └─ main_window.py
```

在 `main_window.py` 中：

```python
# 绝对导入
from core.excel_handler import store_entry
```

启动时（在包含 src 的根目录）：

```bash
python -m src.gui.main_window # 或者python  src.gui.main_window
```

- # 4. 机制

下面按照与相对导入相似的结构，详细剖析Python中**绝对导入（absolute import）**的内部机制。

---

- ## 4.1. 两个关键属性：`__name__` 和 `__package__`

1. **`__name__`**

   - 当模块通过 `import pkg.mod` 或 `python -m pkg.mod` 加载时，`__name__` 会被设为 `"pkg.mod"`。
   - 绝对导入不会改变 `__package__`，它始终指向模块所属的包（或空字符串表示顶层模块） ([5. The import system — Python 3.13.3 documentation](https://docs.python.org/3/reference/import.html?utm_source=chatgpt.com))。
2. **`__package__`**

   - 对于顶层模块（不在任何包内），`__package__ = ""`。
   - 对于包内模块，`__package__ = __name__.rpartition('.')[0]`，即包路径部分。
   - 绝对导入完全忽略 `__package__` 中的相对点语法，仅依据模块名进行查找。

---

- ## 4.2. PEP 328：默认绝对导入

PEP 328 提出从 Python 2.5 起，所有 `import name` 语句默认作为**绝对导入**，只在 `sys.path` 中搜索，不再隐式查找包内部同名模块。
要在 Python 2 中启用该行为，需要：

```python
from __future__ import absolute_import
```

绝对导入的好处是去除了命名歧义，确保 `import string` 一定加载标准库模块，而不会意外挂到当前包下的 `string.py` ([PEP 328 – Imports: Multi-Line and Absolute/Relative | peps.python.org](https://peps.python.org/pep-0328/?utm_source=chatgpt.com))。

---

- ## 4.3. 绝对导入的查找流程

> **总结**:相当于把项目自定义的包目录加入到 Python 解释器的 Lib 库中去了,还不用自己去给每一个文件夹配置 `__init__.py` 文件

当执行：

```python
import pkg.subpkg.mod    # 绝对导入
```

内部步骤（简化版）：

1. **形成模块全名**直接以 `"pkg.subpkg.mod"` 作为要加载的目标。
2. **遍历 `sys.meta_path` 查找 finder**Python 会依次询问各类 finder，看谁能处理 `"pkg.subpkg.mod"`。
3. **定位模块文件**

   - 对于文件系统包，finder 会在每个 `sys.path` 条目（包括当前工作目录、PYTHONPATH 等）下寻找 `pkg/subpkg/mod.py` 或对应的包目录 `pkg/subpkg/mod/__init__.py`。
   - 找到后，交给 loader 加载。
4. **执行并缓存**

   - loader 在一个新的模块对象中执行代码，设置模块的 `__file__`、`__name__="pkg.subpkg.mod"`、`__package__="pkg.subpkg"`。
   - 将模块放入 `sys.modules["pkg.subpkg.mod"]`，后续再 `import` 直接复用。

整个过程不涉及任何“向上定位父包”的操作，完全基于**模块全名**与 `sys.path` 列表 ([5. The import system — Python 3.13.3 documentation](https://docs.python.org/3/reference/import.html?utm_source=chatgpt.com))。

---

- ## 4.4. 举例说明

假设目录结构：

```
project/
└─ src/                   ← 已加入 PYTHONPATH
   ├─ core/
   │   └─ excel_handler.py
   └─ gui/
       └─ main_window.py
```

在 `main_window.py` 中写：

```python
# 绝对导入
from core.excel_handler import store_entry
```

- 启动时，`sys.path[0]` 包含 `…/project/src`。
- `import core.excel_handler`：finder 在 `…/project/src/core/excel_handler.py` 找到文件，按上述流程加载。
- 加载后，`store_entry` 可直接使用，无需包上下文。

---

## 8.4.2. 相对导入

- # 1. 语法

仅支持 `from import ` 语法

- 同目录：`from . import sibling_module`
- 子包：`from .subpkg import module`
- 父包：`from ..parentpkg import module`
- 多级父包：`from ...ancestorpkg import module`
- # 2. 原理
- 只能在包（带 `__init__.py`）内部的模块间使用。
- “`.`” 表示当前包，“`..`” 表示上一级包，依此类推。
- 解释器根据模块的 `__package__` 属性来解析相对路径。
- # 3. 示例

下面用一个示例包结构来说明这四种相对导入的写法。假设我们的项目结构是：

```
myproject/
└─ pkg/
   ├─ __init__.py
   ├─ mod1.py
   ├─ mod2.py
   ├─ subpkg/
   │  ├─ __init__.py
   │  └─ child_mod.py
   └─ subpkg2/
      ├─ __init__.py
      └─ subsubpkg/
         ├─ __init__.py
         └─ deeper_mod.py
```

---

- ## 3.1. 同目录导入

在 `pkg/mod1.py` 想导入同一目录下的 `mod2.py`：

```python
# 文件：pkg/mod1.py
from . import mod2

def foo():
    print("in mod1.foo()")
    mod2.bar()
```

```python
# 文件：pkg/mod2.py
def bar():
    print("in mod2.bar()")
```

运行（在 `myproject` 目录下）：

```bash
python -m pkg.mod1 # 或者 python pkg.mod1,前者以顶层脚本运行,后者以模块方式运行
```

---

- ## 3.2. 导入子包（子模块）

在 `pkg/mod1.py` 想导入子目录 `subpkg/child_mod.py`：

```python
# 文件：pkg/mod1.py
from .subpkg import child_mod

def foo():
    child_mod.child_func()
```

```python
# 文件：pkg/subpkg/child_mod.py
def child_func():
    print("in child_mod.child_func()")
```

运行（在 `myproject` 目录下）：

```python
 python -m pkg.mod1 # 或者 python  pkg.mod1
```

---

- ## 3.3. 导入父包模块

在 `pkg/subpkg/child_mod.py` 想导入父包 `pkg` 下的 `mod1.py`：

```python
# 文件：pkg/subpkg/child_mod.py
from .. import mod1

def child_func():
    print("in child_mod; now call mod1.foo()")
    mod1.foo()
```

运行：

```bash
python -m pkg.subpkg.child_mod # 不能以顶层脚本模式运行,原因如下所示
```

```ad-note
title:**为何导入父包模块不能以顶层脚本模式运行,但是导入子包却可以成功**
当你直接这样跑脚本：

	```bash
	python src/gui/main_window.py
	```

Python 会把脚本所在目录（`src/gui`）当作第一个搜索路径 `sys.path[0]`，而且并不会把它当作包里模块来加载（`__package__ = None`）。

---

## 为什么“导入子包”反而能成功？

假设你有：

	```
	src/
	 └─ gui/
	    ├─ main_window.py
	    └─ subpkg/
	       └─ child_mod.py
	```

在 `main_window.py` 里写：

	```python
	from .subpkg.child_mod import hello
	```

**发生的事情**：

1. Python 把 `src/gui` 作为 `sys.path[0]`，于是它在这个目录下找到了 `subpkg/child_mod.py`。
  
2. 因为找到了同目录下的 `subpkg`，实际上 Python 当作**顶层包**也能把它当“绝对模块”来加载。
  
3. 所以 `from .subpkg…` 虽然是相对写法，但在脚本模式下退化成“在当前目录下找 subpkg”——能够成功。
  

---

## 为什么“导入父包”就一定失败？

假设你想这样引入上一级的 `core`：

	```
	src/
	 ├─ core/
	 │   └─ excel_handler.py
	 └─ gui/
	     └─ main_window.py
	```

在 `main_window.py` 写：

	```python
	from ..core.excel_handler import store  # ← 上一级包
	```

**此时**：

1. 脚本模式下 `__package__ = None`，解释器不会尝试“去上一层目录”去找 `core`——它只在 `sys.path` 里搜索，而 `core` 在 `src` 下面，`src` 并不在 `sys.path[0]`（只有 `src/gui` 在）。
  
2. 既没有包上下文（`__package__`），也没有把 `src` 放到路径里，于是 `..core` 根本没地方可去，报 “no known parent package”。
  

---

## 小结对比

|导入目标|写法|脚本模式下搜索路径|结果|
|---|---|---|---|
|同级子包|`from .subpkg.child_mod import …`|`sys.path[0] = src/gui`|成功（在 `src/gui/subpkg` 找到）|
|父级兄弟包|`from ..core.excel_handler import …`|`sys.path[0] = src/gui`|失败（`src` 不在路径里，且无包上下文）|

---

## 正确做法

- 如果要用相对导入父包，必须：
  
    1. 在 `src/`、`src/gui/`、`src/core/` 都放 `__init__.py`，
  
    2. 用模块模式启动：
  
        ```bash
        python -m src.gui.main_window
        ```
  
  
    这样 `src` 会被认作包根，`__package__="src.gui"`，`..core` 才能解析。
  
- 或者改为绝对导入＋把 `src` 加到 `PYTHONPATH`，直接写：
  
    ```python
    from core.excel_handler import store
    ```
  
    并确保运行时 `src` 在 `sys.path` 中。

```

---

- ## 3.4. 多级父包导入

在更深层 `pkg/subpkg2/subsubpkg/deeper_mod.py` 想导入 `pkg/mod1.py`：

```python
# 文件：pkg/subpkg2/subsubpkg/deeper_mod.py
from ... import mod1

def deep():
    print("in deeper_mod.deep(); call mod1.foo()")
    mod1.foo()
```

运行：

```bash
python -m pkg.subpkg2.subsubpkg.deeper_mod  # 不能以顶层脚本模式运行 
```

---

**要点回顾：**

1. `.` 表示当前包；
2. `..` 表示上一级包；
3. `...` 表示上两级包；
4. 必须在每个目录下放置 `__init__.py`，并用 `python -m 包.模块` 启动，才能让 `__package__` 正确、相对导入才生效。

---

---

- # 4. 机制
- ## 4.1. 模块加载时的两个关键属性：`__name__` 和 `__package__`

1. **`__name__`**

   - 正常由 import 机制赋值，形式为 `"pkg.subpkg.modulename"`。
   - 如果直接用 `python somefile.py` 执行，`__name__` 会被硬设为 `"__main__"`，此时模块不被视为包内模块。
2. **`__package__`**

   - PEP 366 提出，用于明确模块的“包上下文”（package context）。
   - 当模块以 `-m pkg.mod` 方式执行时，`__package__` 会被设为 `"pkg"`（即 `__name__.rpartition('.')[0]`），这样相对导入才能知道自己的父包是谁；如果没有设，默认等于 `None`，相对导入会失败 ([PEP 366 – Main module explicit relative imports | peps.python.org](https://peps.python.org/pep-0366/?utm_source=chatgpt.com))。

---

- ## 4.2. 解析相对导入语法（PEP 328）

当遇到语句：

```python
from ..core.excel_handler import foo
```

解析流程大致如下（简化版） ([PEP 328 – Imports: Multi-Line and Absolute/Relative | peps.python.org](https://peps.python.org/pep-0328/?utm_source=chatgpt.com))：

1. **检查 `__package__`**

   - 如果 `__package__` 为 `None`，报错 “no known parent package”。
   - 否则，将 `__package__`（例如 `"src.gui"`）按 `.` 分割成包路径列表。
2. **计算目标包路径**

   - 语句中有两个点（`..`），表示向上两级：

     ```
     base = __package__.split('.')        # ["src","gui"]
     target_pkg = base[:-2]               # [] → 回到 “src” 之上
     ```
3. **构造绝对模块名**

   - 将 target_pkg 与导入路径拼接：

     ```
     target_full = target_pkg + ["core","excel_handler"]
                 = ["core","excel_handler"]
     module_name = ".".join(target_full)  # "core.excel_handler"
     ```
4. **委托给绝对导入逻辑**

   - 最终变为 `import core.excel_handler`，由 `sys.path`、`finder/loader` 去查找并加载模块。

---

- ## 4.3. 为什么直接 `python file.py` 会失败
- 以脚本方式执行时，模块 `main_window.py` 的 `__name__="__main__"`，`__package__=None`。
- 相对导入检查到 `__package__ is None`，无法定位父包，因而报错 ([How can I do relative imports in Python? - Stack Overflow](https://stackoverflow.com/questions/72852/how-can-i-do-relative-imports-in-python?utm_source=chatgpt.com))。

只有在**模块模式**（`python -m pkg.mod`）或被另一个包内模块 `import` 时，`__package__` 才会正确反映它在包层级中的位置，相对导入才会生效。

---

- ## 4.4. 导入查找的最终步骤

实际上，相对导入最终落脚在标准的**绝对导入机制**上（PEP 328 规定“绝对导入为默认，‘.’ 前缀表示包内相对导入”）：

1. Python 遍历 `sys.meta_path` 找到合适的 finder。
2. finder 在 `sys.path` 或包的 `__path__` 中定位文件，例如 `core/excel_handler.py`。
3. loader 创建模块对象、执行代码，并缓存到 `sys.modules["core.excel_handler"]`。

整个过程中，**相对导入只是计算出一个绝对模块名**，然后复用已有的绝对导入逻辑。

---

- ## 4.5. 关键结论
- 相对导入靠的是模块的 `__package__` 属性（PEP 366）来决定“当前包”是谁；
- 导入时先把“点”“..”转换成真正的包路径，再交给绝对导入流程；
- 只有在包上下文中（`__package__≠None`）才能用相对导入，脚本模式下永远失效。

---

- ## 4.6. 与绝对导入的对比

| 特性         | 绝对导入                                  | 相对导入                                              |
| ------------ | ----------------------------------------- | ----------------------------------------------------- |
| 语法         | `import pkg.mod``from pkg.sub import m` | `from . import sibling``from ..core import x`       |
| 依赖         | 仅依赖 `sys.path` 和模块全名            | 依赖模块的 `__package__` 属性                       |
| 启动方式限制 | 无——脚本模式或模块模式皆可              | 只能模块模式（`-m pkg.mod`）或被其它模块 `import` |
| 优缺点       | 清晰、不易错；重构时要改全路径            | 写起来短；包移动后路径可能更稳                        |

- **绝对导入**：直接使用完整包路径，解析过程只看模块名与 `sys.path`，与当前执行方式无关。
- **相对导入**：先由 `__package__` 计算出目标全名，再复用绝对导入机制；必须在包上下文中才能生效。

这样，你在项目中就可以根据场景自由选用：**大多数情况下优先绝对导入，包内部复杂依赖时可辅以相对导入**(辅以相对导入是以脚本模式运行,所以只能**支持相对导入子包**)。

## 8.4.3. 常见误区与建议

- # 1. 误区

| 误区                                        | 结果                                     | 修正                           |
| ------------------------------------------- | ---------------------------------------- | ------------------------------ |
| 直接运行脚本 `python gui/main_window.py`  | `ImportError: no known parent package` | 用 `-m` 或改为绝对导入       |
| 在非包目录没有 `__init__.py` 下用相对导入 | 报找不到包                               | 在每层目录加空 `__init__.py` |

**最佳实践**：

- 尽量使用**绝对导入**，路径清晰；
- 必要时在包内部用“`.`/`..`”进行**相对导入**；
- 始终通过 `python -m package.module` 启动包内模块。
- # 2. 建议

在 PEP8 中对模块的导入提出了要求，遵守 PEP8规范能让你的代码更具有可读性，我这边也列一下：

- import 语句应**尽量**当分行书写

```python
# bad examples
import os,sys

# good examples
import os
import sys
```

- import 语句应**尽量**当使用 absolute import

```python
# bad examples
from ..bar import  Bar

# good examples
from foo.bar import test
```

- import语句应**尽量**当放在文件头部，置于模块说明及docstring之后，全局变量之前
- 

```python
# time
# author
# 
#

import os
import sys


a = 0

```

- import语句应该按照**尽量**顺序排列，每组之间用一个空格分隔，按照内置模块，第三方模块，自己所写的模块调用顺序，同时每组内部按照字母表顺序排列

```python
# 内置模块
import os
import sys

# 第三方模块
import flask

# 本地模块
from foo import bar
```

# 子模块访问修改主模块变量的方法

下面给出六大类、七种常见的方法，在子模块中修改（或影响）主脚本（即 `__main__` 模块）变量的值，并配以示例与要点。

> **摘要**：
>
> 1. **可变对象**（mutable）直接传参并修改；
> 2. **返回值/回调**，由主脚本接收并赋值；
> 3. **导入 `__main__` 或 `sys.modules`**，直接写入主命名空间；
> 4. **内建命名空间**（`builtins`）中设值；
> 5. **类/实例属性**传递与修改；
> 6. **环境变量**或外部配置；
> 7. **执行上下文 `exec`**（较少用）。

下面逐一说明。

## 1. 可变对象传参（Mutable semantics）

### 1.1 原理

Python 中，列表 (`list`)、字典 (`dict`) 等可变对象作为参数传递时传递的是引用，子模块函数内部对其修改会反映到主脚本中。 ([Updating the variable values in a python script from other python script](https://discuss.python.org/t/updating-the-variable-values-in-a-python-script-from-other-python-script/41201?utm_source=chatgpt.com))

### 1.2 示例

```python
# main.py
import sub
data = {"count": 0}
sub.inc(data)
print(data["count"])  # 1

# sub.py
def inc(d):
    d["count"] += 1
```

## 2. 返回值／回调（Return or Callback）

### 2.1 返回值由主脚本接收

最简单、安全：子模块函数返回新的值，由主脚本显式赋回变量。 ([How to change the value of a module variable from within an object ...](https://stackoverflow.com/questions/34594936/how-to-change-the-value-of-a-module-variable-from-within-an-object-of-another-mo?utm_source=chatgpt.com))

```python
# main.py
import sub
x = 0
x = sub.inc(x)
# sub.py
def inc(x):
    return x + 1
```

### 2.2 传入回调函数

将主脚本的 setter 函数传给子模块，由子模块回调。

```python
# main.py
import sub
x = 0
def set_x(v): 
    global x; x = v
sub.register_callback(set_x)
sub.do_something()  # 内部会调用 set_x
```

## 3. 导入 `__main__` 或通过 `sys.modules` 直接写主命名空间

### 3.1 import __main__

子模块中直接 `import __main__`，然后赋值：

```python
# sub.py
import __main__
def set_main_var(v):
    __main__.x = v
```

此时主脚本 `x` 即被修改。 ([python - Modify a __main__.variable from inside a module given ...](https://stackoverflow.com/questions/60469967/modify-a-main-variable-from-inside-a-module-given-the-name-of-the-variable-a?utm_source=chatgpt.com))

### 3.2 利用 `sys.modules`

```python
# sub.py
import sys
def set_main_var(v):
    sys.modules['__main__'].x = v
```

等同于上述方法。 ([How to change the value of a module variable from within an object ...](https://stackoverflow.com/questions/34594936/how-to-change-the-value-of-a-module-variable-from-within-an-object-of-another-mo?utm_source=chatgpt.com))

## 4. 使用内建命名空间 `builtins`

### 4.1 原理

将变量放在 `builtins`，在任意模块中修改都会生效（风险：全局污染）。 ([Global variables shared across modules - Python discussion forum](https://discuss.python.org/t/global-variables-shared-across-modules/16833?utm_source=chatgpt.com))

```python
# main.py
import builtins
builtins.shared = 0

# sub.py
import builtins
def inc():
    builtins.shared += 1
```

## 5. 类／实例属性传递

### 5.1 通过对象封装状态

将主脚本变量封装在对象属性里，子模块持有该对象引用并修改属性。

```python
# main.py
import sub
class C: pass
ctx = C(); ctx.x = 0
sub.update(ctx)
print(ctx.x)

# sub.py
def update(obj):
    obj.x += 1
```

与可变对象传参原理相同，更面向对象。

## 6. 环境变量或外部配置

### 6.1 os.environ

将变量放入 `os.environ`，子模块修改后，主脚本可重新读取。适合跨进程。 ([python实现对导入包中的全局变量进行修改原创 - CSDN博客](https://blog.csdn.net/qq_45270849/article/details/135514634?utm_source=chatgpt.com))

```python
# sub.py
import os
def set_var(v):
    os.environ['X'] = str(v)
```

## 7. 动态执行上下文（exec）

### 7.1 exec 在主命名空间中

子模块通过传入主脚本的 `globals()`，在该命名空间 `exec` 代码：

```python
# main.py
import sub
ns = globals()
sub.run("x = 5", ns)

# sub.py
def run(code, ns):
    exec(code, ns)
```

可直接创建/修改主脚本变量，但不推荐（可读性差）。

---

### 小结

- **最常用**：方法1（可变对象）和方法2（返回值／回调），结构清晰、安全。
- **直接修改**：方法3（`__main__`／`sys.modules`）与方法4（`builtins`），但易导致全局污染与可维护性问题。
- **面向对象**：方法5 适合复杂状态管理；方法6 用于跨进程；方法7 较少见。

以上七种方式，覆盖了从最“Pythonic”到最“黑魔法”的做法，可根据场景权衡选择。

# sum函数的高级用法

你问的这句代码：

**existing_rows** **=** **sum**(**1** **for** **row_idx** **in** **range**(**sheet.nrows**) **if** **any**(**sheet.row_values**(**row_idx**)**)**)

**解读如下：**

* [sheet.nrows](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)：当前 Excel 表的总行数。
* [range(sheet.nrows)](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)：遍历所有行的索引。
* [sheet.row_values(row_idx)](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)：获取第 [row_idx](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 行的所有单元格的值，返回一个列表。
* [any(sheet.row_values(row_idx))](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)：判断这一行是否有至少一个单元格不是空（即这一行不是全空）。
* [sum(1 for ... if ...)](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)：对所有“不是全空”的行计数，每遇到一行非空就加1。

**最终作用：**

> 统计 Excel 表中“非全空”的行数（即已有有效数据的行数），通常用于确定追加写入时应该从哪一行开始写。

---

**举例：**

* 如果前3行有内容，第4、5行全是空的，则 [existing_rows](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 为3。
* 这样你可以从第4行开始追加新数据，避免覆盖原有内容。

---

**一句话总结：**
这句代码的作用是 **统计 Excel 表格中已有内容的行数** ，用于后续追加写入时定位起始行




# 学习3:列表推导式


这句代码：

**[**i** **for** **i**, **row** **in** **enumerate**(**sheet.rows**)** **if** row_index_name **in** **[**cell**.value **for** **cell** **in** **row**]**]

**作用：**

* 在 Excel 的 sheet 中，查找 **每一行是否包含指定的字符串 [row_index_name](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)** ，并返回所有满足条件的行索引（[i](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)）。

---

### 详细分解

1. [enumerate(sheet.rows)](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)
   遍历 sheet 的每一行，[i](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 是行号，[row](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 是该行的所有单元格对象。
2. `[cell.value for cell in row]`
   把当前行的所有单元格的值提取出来，形成一个列表。例如：`["主食（帮扶食品）", "米", 100, ...]`
3. `if row_index_name in [cell.value for cell in row]`
   判断 [row_index_name](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)（比如 `"主食（帮扶食品）"`）是否在当前行的所有单元格值中。
4. `[i for ... if ...]`
   如果在，收集该行的索引 [i](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) 到结果列表中。

---

### 举例

假设 sheet 的内容如下：

|   | A                | B  | C   |
| - | ---------------- | -- | --- |
| 0 | 主食（帮扶食品） | 米 | 100 |
| 1 | 副食（帮扶食品） | 面 | 200 |
| 2 | 主食（自购）     | 粟 | 150 |

如果 [row_index_name = &#34;主食（帮扶食品）&#34;](vscode-file://vscode-app/e:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)，
那么：

* 第0行的所有 cell.value 是 `["主食（帮扶食品）", "米", 100]`，包含目标字符串。
* 第1行不包含。
* 第2行不包含。

结果：`[0]`

---

**总结：**

* 这句代码的作用是： **查找 sheet 中所有包含指定内容的行索引** ，返回一个索引列表。
