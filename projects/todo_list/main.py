# Simple match case to match the user's input and act accordingly.

todos = []

while True:
    user_acton = (
        str(
            input(
                "What would you like to do?\nType 'add' to add new items or 'show' to show the items.\nType 'exit' to exit!\nEnter your action: "
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
            for todo in todos:
                print(todo)
        case "exit" | "quit":
            break
        case _:
            print("Invalid action!")

print("Thanks for using the todo list!")
