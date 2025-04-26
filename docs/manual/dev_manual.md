> **引言**：为了更好的指导本次项目的开发，写了一个简短的开发手册以快速的上手本项目。本次的目录结构是我在Obsidian中用Copilot AI插件基于我做的代码整洁笔记知识进行生成的项目目录架构。

## 团队开发说明

1. 未经队长允许不可私自创建额外的功能文件夹
2. 变量命名、函数方法命名、批注、文件名的创建要求参见 `代码要求.md`

## 目录结构说明

### 根目录

- **`.gitignore`**: 指定需要 Git 忽略的文件和文件夹。
- **[LICENSE](vscode-file://vscode-app/d:/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)**: 项目的许可证文件，说明项目的使用权限。
- **`README.md`**: 项目的说明文档，通常包含项目简介、安装方法和使用说明。
- **`requirements.txt`**: 列出项目所需的 Python 依赖包。
- **`config/`**: 配置文件目录。
  - **`config.ini`**: 项目的配置文件，存储配置信息。
- **`TODO.md`**：记录开发过程中遇到的问题、错误和待办事项。

### 文档目录

- **`docs/`**: 项目文档目录。
  - **`dev_manual.md`**: 开发手册，面向开发者的技术文档。
  - **`user_manual.md`**: 用户手册，面向终端用户的使用说明。

### 日志目录

- **`logs/`**: 存储运行时生成的日志文件。
  - **`app.log`**: 应用程序的日志文件。

### 脚本目录

- **`scripts/`**: 存储项目相关的脚本。
  - **`install.sh`**: 安装脚本，用于安装项目依赖或初始化环境。
  - **`run.sh`**: 运行脚本，用于启动项目。

### 源代码目录

- **`src/`**: 项目的主要源代码目录。
  - **`main.py`**: 项目的主入口文件。
  - **`core/`**: 核心功能模块。
    - **`config_manager.py`**: 配置管理模块。
    - **`data_importer.py`**: 数据导入模块。
    - **`data_processor.py`**: 数据处理模块。
    - **`excel_handler.py`**: Excel 文件处理模块。
    - **`nlp_utils.py`**: 自然语言处理工具模块。
    - **`pdf_handler.py`**: PDF 文件处理模块。
    - **`report_generator.py`**: 报告生成模块。
    - **`rule_engine.py`**: 规则引擎模块。
    - **`text_handler.py`**: 文本处理模块。
    - **`user_manager.py`**: 用户管理模块。
    - **`models/`**: 数据模型目录。
      - **`food_item.py`**: 食品项数据模型。
  - **`gui/`**: 图形用户界面模块。
    - **`data_import_dialog.py`**: 数据导入对话框。
    - **`data_process_dialog.py`**: 数据处理对话框。
    - **`main_window.py`**: 主窗口逻辑。
    - **`report_generate_dialog.py`**: 报告生成对话框。
    - **`resources/`**: GUI 资源文件目录。
      - **`main_window.ui`**: 主窗口的 UI 文件。
    - **`utils/`**: GUI 工具模块。
      - **`ui_utils.py`**: GUI 工具函数，提供一些界面常用的工具函数，例如获取日期
  - **`tests/`**: 测试目录。
    - **`resources/`**
    - **`test_config_manager.py`**: 针对 `config_manager` 的测试。
    - **`test_excel_handler.py`**: 针对 `excel_handler` 的测试。
    - **`test_data_processor.py`**: 针对 `data_processor` 的测试。
    - **`test_data_importer.py`**: 针对 `data_importer` 的测试。
  - **`utils/`**: 通用工具模块。
    - **`logger.py`**: 日志工具模块。
    - **`exception.py`**: 异常处理模块。
    - 

# 程序运行说明

先执行 `main_window.py`，点击UI中的按钮会调用 `ui_utils.py`中的相关功能（目前只做到这里，很多功能模块文件都是空的，放在那占位用的）
