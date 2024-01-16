# 1.
class BaseUser:
    def __init__(self, first_name, second_name):
        self.first = first_name
        self.second = second_name
        print(f"{self.first} {self.second}")

    # 2.
    def my_infinite_arguments(self, *args):
        for arg in args:
            print(arg)

    # 3.
    def my_infinite_kwargs(self, **kwargs):
        for key in kwargs:
            if key == "first_name":
                print(f"Loop broken by key: {key}")
                break
            print(f"{key} = {kwargs[key]}")


if __name__ == "__main__":
    my_user = BaseUser("Ion", "marcel")
    my_user.my_infinite_arguments(432434, 43422, "mili", "blabla", True)
    my_user.my_infinite_kwargs(first_name="Ion", second_name="Marcel")
