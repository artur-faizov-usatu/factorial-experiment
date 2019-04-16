from widgets.exp_widget_ui import Ui_Form
from widgets.add_factor import AddFactorDialog
from widgets.models.factors_table_model import FactorsTableModel
from qtpy.QtWidgets import QWidget, QMessageBox, QPushButton, QHeaderView
from qtpy.QtCore import Qt
from algorithm.factor_experiment import Factor
import traceback

class ExpWidget(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent=parent, flags=Qt.Window)
        self.ui = None
        self.factors_model = None

        self.factors = []
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.factors_model = FactorsTableModel()
        self.ui.factors_tv.setModel(self.factors_model)
        self.ui.add_factor_btn.clicked.connect(self.on_add_factor_clicked)
        self.ui.factors_tv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.factors_tv.setStyleSheet("QHeaderView::section { background-color:#222233; "
                                         "color:#AAA8FF;selection-background-color: #0000FF; "
                                         "selection-color: #00FF00;}")




    def on_add_factor_clicked(self):

        dlg = AddFactorDialog(self)
        result = dlg.exec_()
        if result:
            self.factors_model.add_factor(result)

