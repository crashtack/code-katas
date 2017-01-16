class Person(object):

    def __init__(self, initial_age=0):
        """Initialize the persons age"""
        if initial_age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initial_age

    def yearPasses(self):
        """Increment age by 1 year"""
        self.age += 1

    def amIOld(self):
        """Return a message bassed on age"""
        if self.age < 13:
            print("You are young.")
            return "You are young."
        elif 13 <= self.age < 18:
            print("You are a teenager.")
            return "You are a teenager."
        else:
            print("You are old.")
            return "You are old."
