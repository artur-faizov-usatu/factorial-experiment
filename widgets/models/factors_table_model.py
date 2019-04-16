from qtpy.QtCore import QAbstractTableModel, QModelIndex, Qt
from algorithm.factor_experiment import Factor


class FactorsTableModel(QAbstractTableModel):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._factors = list()

    def columnCount(self, *args, **kwargs):
        return 6

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            column = index.column()
            row = index.row()
            factor = self._factors[row]
            if column == 0:
                return str(factor.name)
            elif column == 1:
                return "X{}".format(row + 1)
            elif column == 2:
                return factor.min
            elif column == 3:
                return factor.max
            elif column == 4:
                return factor.zero
            elif column == 5:
                return factor.interval

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return "Фактор"
            elif section == 1:
                return "Обозначение"
            elif section == 2:
                return "Минимум"
            elif section == 3:
                return "Максимум"
            elif section == 4:
                return "Нулевой уровень"
            elif section == 5:
                return "Интервал варьирования"

    def rowCount(self, *args, **kwargs):
        return len(self._factors)

    def add_factor(self, factor):
        rows = self.rowCount()
        position = rows - 1 if self.rowCount() > 0 else rows
        self.beginInsertRows(QModelIndex(), position, position)
        self._factors.append(factor)
        self.endInsertRows()


if __name__ == '__main__':
    import sys
    from qtpy.QtWidgets import QApplication, QTableView, QHeaderView

    factors = [Factor("die", 1,2,3432,4)]
    app = QApplication([])
    model = FactorsTableModel()
    tv = QTableView()
    tv.setModel(model)
    for f in factors:
        model.add_factor(f)
    tv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    tv.show()
    sys.exit(app.exec_())
