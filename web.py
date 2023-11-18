import streamlit as st
import functions

todos = functions.read_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This app is to increase productivity")
content = """
Simply write a todo in the textbox, then press enter. Once you've completed a todo, press the checkbox next to it to 
remove the todo item from the list.
"""
st.write(content)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="m", label_visibility="hidden", placeholder="Write todos here...",
              on_change=add_todo, key="new_todo")
