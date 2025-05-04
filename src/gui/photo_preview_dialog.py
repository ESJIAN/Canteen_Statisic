from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, Qt)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget, QFileDialog, QDialog, QVBoxLayout)


def preview_image(self, image_path):
    """
    弹窗预览图片（支持多开预览窗口）
    :param image_path: 图片文件路径
    """
    self.dialog = QDialog()                        # 将窗口组件以 self 属性的形式增加，生命周期跟随主窗口
    self.dialog.setAttribute(Qt.WA_DeleteOnClose)  # 关闭时自动销毁，支持多开
    self.dialog.setWindowTitle("图片预览")
    layout = QVBoxLayout(self.dialog)
    label = QLabel(self.dialog)
    pixmap = QPixmap(image_path)
    label.setPixmap(pixmap.scaled(1000, 1000, Qt.KeepAspectRatio, Qt.SmoothTransformation))
    layout.addWidget(label)
    self.dialog.setLayout(layout)
    self.dialog.show()  # 使用show()而不是exec()，允许多开