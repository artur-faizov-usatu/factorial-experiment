from qtpy.QtCore import QAbstractTableModel, QModelIndex, Qt
from algorithm.factor_experiment import Factor

class FactorsTableModel(QAbstractTableModel):

    def __init__(self, factors=None, parent=None):
        super().__init__(parent=parent)
        self._factors = list()
        for f in factors:
            self.add_factor(f)


    def columnCount(self, *args, **kwargs):
        return 5

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return 1

    def headerData(self, section, orientation = Qt.Horizontal, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return "Фактор"
            elif section == 1:
                return "Код фактора"
            elif section == 2:
                return "Количество уровней"
            elif section == 3:
                return "Нулевой уровень"
            elif section == 4:
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

    factors = [
        Factor("factor1", 350, 50),
        Factor("factor2", 60, 10),
    ]
    app = QApplication([])
    model = FactorsTableModel(factors=factors)
    tv = QTableView()
    tv.setModel(model)
    tv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
    tv.show()
    sys.exit(app.exec_())


