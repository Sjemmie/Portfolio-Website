import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        name_label = QLabel("Distance: ")
        self.name_label_edit = QLineEdit()

        time_label = QLabel("Time in Hours: ")
        self.time_edit = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["Metric (km)", "Imperial (miles)"])

        calculate_button = QPushButton("Calculate Speed")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_label_edit, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        time_hours = float(self.time_edit.text())
        distance = float(self.name_label_edit.text())
        average_speed = distance / time_hours

        if self.unit_combo.currentText() == "Metric (km)":
            average_speed = round(average_speed, 2)
            unit = "km/h"
        if self.unit_combo.currentText() == "Imperial (miles)":
            average_speed = round(average_speed * 0.621371, 2)
            unit = "mph"

        self.output_label.setText(f"Average speed is {average_speed} {unit}")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
