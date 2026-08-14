def main():
    print("PERSONAL INTRODUCTION PROGRAM")
    print("-" * 40)

    NAME = input("Enter your name: ")
    AGE = int(input("Enter your age: "))
    HOBBIES = input("Enter your hobbies: ")
    CITY = input("Enter your city: ")
    LANGUAGE = input("Enter your favorite programming language: ")
    STUDIES = input("Enter your field of study: ")
    EXTRA_CURRICULAR = input("Enter your extra-curricular activities: ")

    print("\nPERSONAL INTRODUCTION PROGRAM")
    print("-" * 40)
    print("My name is", NAME)
    print("I am", AGE, "years old")
    print("My hobbies are", HOBBIES)
    print("I live in", CITY)
    print("My favorite programming language is", LANGUAGE)
    print("I am pursuing a degree in", STUDIES)
    print("My extra-curricular activities include", EXTRA_CURRICULAR)
print("\nNice to meet you!")


if __name__ == "__main__":
    main()