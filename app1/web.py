import streamlit as st
import functions

todos = functions.todos_read()

st.title("Todo App")
st.subheader("This is todo app created by OxV3geta.")
st.write("This app increase your productivity.")

for todos in todos:
    st.checkbox(todos)

st.text_input(label="",placeholder="Add new todo...",value="")

print("yo")