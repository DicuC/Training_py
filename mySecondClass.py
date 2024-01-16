from myFirstClass import BaseUser
# 4.
class UserActivity(BaseUser):
    def __init__(self, first_name, second_name):
        super().__init__(first_name, second_name)

    # 5.
    def my_sum(self, *args):
        return sum(args)

    # 7.
    def my_errors(self, employees):
        try:
            print(employees["mele"])
        except KeyError as e:
            print(f"Error: {e}")
        else:
            print("No exception occurred")
        finally:
            print("Finally block executed")

if __name__ == "__main__":
    activity = UserActivity("Jane", "Smith")
    print(activity.my_sum(1, 2, 3, 4))

    # Testarea gestiunii erorilor
    employees = {"mele": "developer", "someone": "manager"}
    activity.my_errors(employees)
    activity.my_errors({})

