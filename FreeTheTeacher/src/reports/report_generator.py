class ReportGenerator:
    def __init__(self):
        pass

    def generate_attendance_report(self, attendance_data):
        report = "Attendance Report\n"
        report += "=================\n"
        for student, status in attendance_data.items():
            report += f"{student}: {'Present' if status else 'Absent'}\n"
        return report

    def generate_grade_report(self, grade_data):
        report = "Grade Report\n"
        report += "=============\n"
        for student, grades in grade_data.items():
            average = sum(grades) / len(grades) if grades else 0
            report += f"{student}: Average Grade: {average:.2f}\n"
        return report

    def save_report(self, report, filename):
        with open(filename, 'w') as file:
            file.write(report)