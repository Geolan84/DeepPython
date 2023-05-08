import tracemalloc
import weakref
import timeit


class Person():
    """Class for default person."""
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


class Teacher(Person):
    """Teacher in the university."""
    def __init__(self, name: str, surname: str, academic_degree: str):
        self.academic_degree = academic_degree
        super().__init__(name, surname)


class Assistant(Person):
    """Assistant of teacher."""
    def __init__(self, name: str, surname: str, cource: int):
        self.cource = cource
        super().__init__(name, surname)


class SubjectSlots():
    """Impementation of Subject class with __slots__."""
    __slots__ = ("teacher", "assistant", "credits", "days")

    def __init__(self, teacher: Teacher, assistant:
                 Assistant, credits: int, days: int):
        self.teacher = teacher
        self.assistant = assistant
        self.credits = credits
        self.days = days


class SimpleSubject():
    """Implementation of Subject class without any unordinary adds."""
    def __init__(self, teacher: Teacher, assistant: Assistant,
                 credits: int, days: int):
        self.teacher = teacher
        self.assistant = assistant
        self.credits = credits
        self.days = days


class WeakrefSubject():
    """Implementation of Subject class with weakref."""
    def __init__(self, teacher: Teacher, assistant: Assistant,
                 credits: int, days: int):
        self.teacher = weakref.ref(teacher)
        self.assistant = weakref.ref(assistant)
        self.credits = credits
        self.days = days


N = 100000

# slots.
tracemalloc.start()
start_time = timeit.default_timer()
subjects = [SubjectSlots(Teacher("Ivan", 'Ivanov', 'docent'),
                         Assistant("Alex", "Gant", 3), 4, 1) for _ in range(N)]
for subject in subjects:
    subject.days += 1
print("CPU Time (Subjects with slots):",
      round(timeit.default_timer() - start_time, 4), "s")
print("Peak memory (Subject with slots):", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
del subjects
print()

# simple structure.
tracemalloc.start()
start_time = timeit.default_timer()
subjects = [SimpleSubject(Teacher("Ivan", 'Ivanov', 'docent'),
                          Assistant("Alex", "Gant", 3),
                          4, 1) for _ in range(N)]
for subject in subjects:
    subject.days += 1
print("CPU Time (Simple Subject):",
      round(timeit.default_timer() - start_time, 2), "s")
print("Peak memory (Simple Subject):", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
del subjects
print()

# weakref.
tracemalloc.start()
start_time = timeit.default_timer()
subjects = [WeakrefSubject(Teacher("Ivan", 'Ivanov', 'docent'),
                           Assistant("Alex", "Gant", 3),
                           4, 1) for _ in range(N)]
for subject in subjects:
    subject.days += 1
print("CPU Time (Weakref Subject):",
      round(timeit.default_timer() - start_time, 4), "s")
print("Peak memory (Weakref Subject):", tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
del subjects
