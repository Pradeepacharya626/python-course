import streamlit as st
import functions

todos = functions.get_todos()

#layout must be "centered" or "wide"
st.set_page_config(layout="wide")

def add_todo() :
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("My to do list")

#we can use the html code for st.write
st.write("this app increase your <b> productivity </b>",
         unsafe_allow_html=True)

for index,todo in enumerate(todos) :
    checkbox = st.checkbox(todo,key=todo)
    if checkbox :
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="todo :",placeholder="new todo",
              on_change=add_todo,key="new_todo")

