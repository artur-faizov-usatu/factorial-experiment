import sys
from qtpy.QtWidgets import QApplication
from widgets.exp_widget import ExpWidget


def main():
    qapp = QApplication(sys.argv)
    exp_widget = ExpWidget()
    exp_widget.show()
    sys.exit(qapp.exec_())


if __name__ == '__main__':
    main()
