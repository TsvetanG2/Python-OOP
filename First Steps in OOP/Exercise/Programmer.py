class Programmer:

    def __init__(self, name, programmer_language, skills):
        self.name = name
        self.programmer_language = programmer_language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language == self.programmer_language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'

        return f'{self.name} does not know {language}'

    def change_language(self, new_language, skills_needed):
        if skills_needed <= self.skills and new_language != self.programmer_language:
            result = f'{self.name} switched from {self.programmer_language} to {new_language}'
            self.programmer_language = new_language
            return result

        elif skills_needed <= self.skills and new_language == self.programmer_language:
            return f'{self.name} already knows {new_language}'

        else:
            return f'{self.name} needs {self.skills} more skills'


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))