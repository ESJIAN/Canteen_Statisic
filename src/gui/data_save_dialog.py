from PySide6.QtWidgets import QMessageBox

def data_save_success(self):
    """
    显示保存条目成功的消息提示弹窗
    param: self
    return: None
    """

    self.msg_box = QMessageBox()
    self.msg_box.setIcon(QMessageBox.Icon.Information)  # 设置图标为信息类型
    self.msg_box.setWindowTitle("操作通知")  # 弹窗标题
    self.msg_box.setText("保存成功！")  # 弹窗内容
    self.msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)  # 添加“确定”按钮
    self.msg_box.exec()  # 显示弹窗






if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QWidget

    app = QApplication(sys.argv)
    window = QWidget()
    data_save_success(window)  # 显示保存成功的消息提示弹窗
    window.show()
    sys.exit(app.exec())