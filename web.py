import streamlit as st
import functions

def update_todos():
    if "new_todo" in st.session_state:
        new_todo = st.session_state["new_todo"] + "\n"
        todos = st.session_state["todos"]
        todos.append(new_todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""

def del_todo(index):
    if "todos" in st.session_state:
        st.session_state["todos"].pop(index)


if "todos" not in st.session_state:
    st.session_state["todos"] = functions.get_todos()

st.title("Testing web app..")
st.subheader("My To-Do app")

for idx,todo in enumerate(st.session_state["todos"]):
    if st.checkbox(label=todo, key=f"todo_{idx}"):
        del_todo(idx)
        st.rerun()
    #print(f"todo_{idx}")

st.text_input(label="Add a new task",key="new_todo",
              placeholder="Add a todo..",
              label_visibility="collapsed",
              on_change=update_todos )
