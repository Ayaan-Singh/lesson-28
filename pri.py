class myclass:
    __p = 400
    def __pm(self):
        print("i am inside my class")
    def hello (self):
        print(f"hello my name is{myclass.__p}")

foo = myclass()
foo.hello()
foo.__pm