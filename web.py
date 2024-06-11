import streamlit as st
import functions

todos = functions.get_todo()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todo(todos)


st.title('Todo App')
st.subheader('This is my Todo App')
st.text('This app will help to boost your daily productivity')

for index, to_do in enumerate(todos):
    checkbox = st.checkbox(to_do, key=to_do)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[to_do]
        st.experimental_rerun()


st.text_input(label='', placeholder='Add a new todo..',
              on_change=add_todo, key='new_todo')
