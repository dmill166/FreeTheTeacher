class GradebookManager:
    def __init__(self):
        self.grades = {}

    def add_grade(self, student_id, grade):
        if student_id not in self.grades:
            self.grades[student_id] = []
        self.grades[student_id].append(grade)

    def calculate_average(self, student_id):
        if student_id in self.grades and self.grades[student_id]:
            return sum(self.grades[student_id]) / len(self.grades[student_id])
        return 0

    def generate_grade_report(self):
        report = {}
        for student_id, grades in self.grades.items():
            report[student_id] = {
                'grades': grades,
                'average': self.calculate_average(student_id)
            }
        return report