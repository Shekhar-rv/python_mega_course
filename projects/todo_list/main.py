# Simple match case to match the user's input and act accordingly.

todos = []

while True:
    user_acton = (
        str(
            input(
                "What would you like to do?\nType 'add' or 'edit' or 'show' or type 'exit' or type 'complete': "
            )
        )
        .lower()
        .strip()
    )

    match user_acton:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "list":
            for index, todo in enumerate(todos, start=1):
                print(f"{index}. {todo}")
        case "edit":
            number = int(input("Enter the number of the todo you want to edit: "))
            todos[number - 1] = str(input("Enter the new todo: "))
        case "complete":
            number = int(input("Enter the number of the todo you want to complete: "))
            todos.pop(number - 1)
        case "exit" | "quit":
            break
        case _:
            print("Invalid action!")

print("Thanks for using the todo list!")
