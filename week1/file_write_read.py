with open("tasks.txt", "w") as f:
    f.write("Today's task: Complete Python exercises.\n")
with open("tasks.txt", "a") as f:
    f.write("Review data structures and OOP concepts.\n")
with open("tasks.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)