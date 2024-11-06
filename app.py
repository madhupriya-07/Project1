import streamlit as st

st.title('Welcome programmers')
 
# header
st.header('Streamlit Hackshop')

# sub header
st.subheader('By IPS Tech Team')

# text
st.text('For 1st year AIDS -B')

# write
st.write('For 1st year AIDS -B')

# text_input function

name = st.text_input('Enter your name:')
age = st.number_input('Enter your age:',min_value=0)
cut_off = st.number_input('Enter your cut off:')
st.write(name)
st.write(age)
st.write(cut_off)
st.write('Your name is',name,'Your age is',age,'Your cut off is',cut_off)
# button
if st.button('Submit'):
    if name == "" and age == 0:
        st.write("pls, enter the name and age")
    elif name != "":
        st.write("Your name is(name) pls enter your age")
    else:
        st.write("Hello,(name)")
    # button
    phy_mark = st.number_input("Enter your phy_mark:")
    che_mark = st.number_input("Enter your che_mark:")
    maths_mark = st.number_input("Enter your maths_mark:")
    if phy_mark>90 and che_mark>90 and maths_mark>90:
        st.write("you are passed in first clss")
    elif phy_mark>=50 and che_mark>=50 and maths_mark>=50:
        st.write("you are passed in second class")
    else:
        st.write("you are failed in exam")