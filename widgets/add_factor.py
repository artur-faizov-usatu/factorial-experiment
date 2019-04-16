from widgets.add_factor_ui import Ui_AddFactorDialog
from qtpy.QtWidgets import QDialog
from qtpy.QtCore import Qt

import math

from algorithm.factor_experiment import Factor


class AddFactorDialog(QDialog):

    def __init__(self, parent):
        super().__init__(parent, flags=Qt.Dialog)
        self.ui = Ui_AddFactorDialog()
        self.ui.setupUi(self)
        self.connect_signals()
        self.factor = None
        self.DEFAULT_MAX_VALUE = 1000000
        self.DEFAULT_MIN_VALUE = -1000000

        self.ui.max_factor_value_sb.setMinimum(self.DEFAULT_MIN_VALUE)
        self.ui.max_factor_value_sb.setMaximum(self.DEFAULT_MAX_VALUE)
        self.ui.min_factor_value_sb.setMinimum(self.DEFAULT_MIN_VALUE)
        self.ui.min_factor_value_sb.setMaximum(self.DEFAULT_MAX_VALUE)

        self.factor_min_value = 0.0
        self.factor_max_value = 10.0
        self.zero_level_value = 0
        self.factor_var_interval = 1
        self.ui.min_factor_value_sb.setValue(self.factor_min_value)
        self.ui.max_factor_value_sb.setValue(self.factor_max_value)
        self.factor_name = "Factor"

        self.update_zero_level_value()

    def connect_signals(self):
        self.ui.min_factor_value_sb.valueChanged.connect(self.on_min_value_changed)
        self.ui.max_factor_value_sb.valueChanged.connect(self.on_max_value_changed)
        self.ui.factor_var_interval_sb.valueChanged.connect(self.on_var_interval_value_changed)
        self.ui.factor_name_le.textChanged.connect(self.on_factor_name_changed)

    def on_factor_name_changed(self, str_name):
        self.factor_name = str_name

    def on_min_value_changed(self, min_value):
        self.factor_min_value = min_value
        self.update_zero_level_value()

    def on_max_value_changed(self, max_value):
        self.factor_max_value = max_value
        self.update_zero_level_value()

    def on_var_interval_value_changed(self, var_interval):
        if (var_interval > self.factor_max_value - self.zero_level_value) \
                or (var_interval > self.zero_level_value - self.factor_min_value):
            self.factor_var_interval = 1
            self.ui.factor_var_interval_sb.setValue(1)
        else:
            self.factor_var_interval = var_interval

    def update_zero_level_value(self):
        self.zero_level_value = math.fabs(self.factor_max_value + self.factor_min_value) / 2
        value = '<html><head/><body><p><span style=" ' \
                'font-size:14pt; font-weight:600; color:#48b515;">{}</span></p></body></html>' \
            .format(self.zero_level_value)
        self.ui.zero_level_value_lbl.setText(value)

    def exec_(self):
        if super().exec_() == QDialog.Accepted:
            self.factor = Factor(self.factor_name,
                                 self.factor_min_value,
                                 self.factor_max_value,
                                 self.factor_var_interval,
                                 self.zero_level_value)
            return self.factor
        else:
            return 0
