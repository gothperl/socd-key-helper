import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QRadioButton, QPushButton, QLabel, QHBoxLayout, QButtonGroup,
    QDialog, QFormLayout, QLineEdit
)

class CustomKeysDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Custom Key Bindings")
        self.setGeometry(150, 150, 250, 150)
        layout = QFormLayout()
        self.left = QLineEdit()
        self.right = QLineEdit()
        self.up = QLineEdit()
        self.down = QLineEdit()
        layout.addRow("Left:", self.left)
        layout.addRow("Right:", self.right)
        layout.addRow("Up:", self.up)
        layout.addRow("Down:", self.down)
        self.ok_btn = QPushButton("OK")
        self.ok_btn.clicked.connect(self.accept)
        layout.addWidget(self.ok_btn)
        self.setLayout(layout)

    def get_keys(self):
        return [
            self.left.text().strip(),
            self.right.text().strip(),
            self.up.text().strip(),
            self.down.text().strip()
        ]

class SOCDCleaner(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SOCD Key Helper")
        self.setGeometry(100, 100, 320, 180)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.info = QLabel(
            "SOCD Key Helper — a utility for handling simultaneous opposite direction key presses.\n"
            "Choose a control scheme (WASD, Arrows, or Custom) and use Snap Tap (Last Wins) mode.\n"
            "Custom key binding in the app will be available in the future."
        )
        layout.addWidget(self.info)

        self.group = QButtonGroup(self)
        self.rb_wasd = QRadioButton("WASD")
        self.rb_arrows = QRadioButton("Arrows")
        self.rb_custom = QRadioButton("Custom")
        self.rb_wasd.setChecked(True)
        self.group.addButton(self.rb_wasd)
        self.group.addButton(self.rb_arrows)
        self.group.addButton(self.rb_custom)

        layout.addWidget(self.rb_wasd)
        layout.addWidget(self.rb_arrows)
        layout.addWidget(self.rb_custom)

        btn_layout = QHBoxLayout()
        self.enable_btn = QPushButton("ENABLE")
        self.enable_label = QLabel("CLICK TO ENABLE / OFF DOUBLE CLICK")
        btn_layout.addWidget(self.enable_btn)
        btn_layout.addWidget(self.enable_label)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        # Connect radio buttons
        self.rb_wasd.toggled.connect(lambda: self.set_scheme("WASD"))
        self.rb_arrows.toggled.connect(lambda: self.set_scheme("Arrows"))
        self.rb_custom.toggled.connect(lambda checked: self.custom_scheme_selected(checked))

        # Connect enable button
        self.enable_btn.clicked.connect(self.toggle_enable)
        self.enable_btn.setCheckable(True)
        self.enable_btn.setChecked(False)
        self.enabled = False

    def set_scheme(self, scheme):
        pass  # Logic for changing scheme

    def custom_scheme_selected(self, checked):
        if checked:
            dlg = CustomKeysDialog(self)
            if dlg.exec_():
                keys = dlg.get_keys()
                # Здесь можно сохранить или использовать выбранные клавиши
                print("Custom keys:", keys)

    def toggle_enable(self):
        self.enabled = not self.enabled
        if self.enabled:
            self.enable_btn.setText("ENABLED")
            self.enable_label.setText("DOUBLE CLICK TO OFF")
        else:
            self.enable_btn.setText("ENABLE")
            self.enable_label.setText("CLICK TO ENABLE / OFF DOUBLE CLICK")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SOCDCleaner()
    window.show()
    sys.exit(app.exec_())