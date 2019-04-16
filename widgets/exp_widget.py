from widgets.exp_widget_ui import Ui_Form
from widgets.add_factor import AddFactorDialog
from qtpy.QtWidgets import QWidget, QMessageBox, QPushButton
from qtpy.QtCore import Qt


class ExpWidget(QWidget):

    def __init__(self, parent):
        super().__init__(parent=parent, flags=Qt.Window)
        self.ui = None
        self.init_ui()
        self.factors = []

    def init_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.add_factor_btn.clicked.connect(self.on_add_factor_clicked)

    def on_add_factor_clicked(self):
        add_factor_dlg = AddFactorDialog(self)
        val = add_factor_dlg.exec_()
        print(val)

