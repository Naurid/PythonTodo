import streamlit as sl
import Functions as fx

todos = fx.GetList()
done_todos = fx.GetList("Files/DoneTasks.txt")

def add_todo():
    todo = sl.session_state["new_todo"] + "\n"
    todos.append(todo)
    fx.WriteList(todos)
    sl.session_state.new_todo = ""



sl.title("TODO")
sl.subheader("An App to streamline your tasks")

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        done_todos.append(todo)
        fx.WriteList(done_todos, "Files/DoneTasks.txt")
        todos.pop(index)
        fx.WriteList(todos)
        del sl.session_state[todo]
        sl.rerun()


sl.text_input(label="label",
              placeholder="Add a new task",
              label_visibility="collapsed",
              on_change=add_todo,
              key="new_todo")

with sl.expander("Tasks History"):
    for todo in done_todos:
        sl.text("- " +todo)
