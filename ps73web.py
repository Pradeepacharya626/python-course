import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("My to do list")
st.write("select the todo")

for todo in todos :
    st.checkbox(todo)

st.text_input(label="",placeholder="new todo")

print("Hii")             # it is printed in terminal

