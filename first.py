# Counter
# def gen():
#     counter = 0
#     while counter <= 10:
#         print("yield")
#         print(counter)
#         yield counter
#         counter += 1
#
# for i in gen():
#     print("for loop")
#     print(i)


# Decorator
# import time
# import random
#
# def decorator(func):
#     def wrapper():
#         start = time.time()
#         result = func()
#         print("It took", time.time() - start, "seconds.")
#         return result
#     return wrapper
#
# @decorator
# def add():
#     time.sleep(random.randint(0, 3))
#     return 10 + 10
#
# @decorator
# def foo():
#     return 1
#
# print(add())


# class Human:
#
#     def foo(self):
#         return 1
#
#     def __call__(self, *args, **kwargs):
#         return "Hello from call"
#
# h1 = Human()
# print(h1.foo())
# print(h1())
#
# def foo():
#     return 1
#
# print(dir(foo))


# class Human:
#     c = 4
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
# h1 = Human("value_a", "value_b")
# print(h1.a)
# print(h1.__dict__["a"])
#
# print(h1.c)
# print(h1.__class__.__dict__["c"])
#
# h1.d = 4
# h1.__dict__["d"] = 5
# print(h1.d)
#
# print(h1.__dict__)    # Удобно использовать для просмотра того, что внутри класса.

class Human:
    def __init__(self, age, skill, productivity):
        self.age = age
        self.skill = skill
        self.productivity = productivity

    def __sub__(self, other):
        return self.age - other.age

    def __add__(self, other):
        return self.skill + ", " + other.skill

    def __mul__(self, other):
        return (self.productivity + other.productivity) / 2


young = Human(25, "Testing", 0.8)
old = Human(50, "Programming", 0.9)
year_difference = old - young
average_team_skills = old + young
average_productivity = old * young
print(f"Year difference: {year_difference};", f"Average team skills: {average_team_skills}.")
print(f"Average team productivity: {int(average_productivity * 100)}%")
print(f"Average team skills: {average_team_skills}.", f"Average team productivity: {int(average_productivity * 100)}%")
print(12345)

