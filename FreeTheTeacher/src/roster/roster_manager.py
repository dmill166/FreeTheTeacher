class RosterManager:
    def __init__(self):
        self.roster = []

    def add_student(self, student_name):
        if student_name not in self.roster:
            self.roster.append(student_name)
            return f"{student_name} has been added to the roster."
        return f"{student_name} is already in the roster."

    def remove_student(self, student_name):
        if student_name in self.roster:
            self.roster.remove(student_name)
            return f"{student_name} has been removed from the roster."
        return f"{student_name} is not in the roster."

    def get_roster(self):
        return self.roster.copy()  # Return a copy to prevent modification of the original roster.