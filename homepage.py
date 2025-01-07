"""SQL Alchemy tutorial"""

import streamlit as st

from src.models import User, session

#from src.models import session, User

with st.sidebar:
    st.title("Save user data")

firstname = st.text_input("First name")
lastname = st.text_input("Last name")
age = st.number_input("Age")
email = st.text_input("Email")

submit = st.button("Submit")

if submit:
    #print(f"First name: {firstname}")
    user = User(first_name=firstname, last_name=lastname, age=age, email=email)
    session.add(user)
    session.commit()
    session.close()
    st.success("User saved successfully")

users = session.query(User).all()
users_over_29 = session.query(User).filter(User.age >= 29)
for user in users_over_29:
    print(user.first_name, user.email, user.age)
#test