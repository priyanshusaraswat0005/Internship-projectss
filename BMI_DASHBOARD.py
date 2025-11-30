import streamlit as st


st.title("BMI Calculator")

height = st.slider("Select your height (cm)", 100, 220, 170)

weight = st.slider("Select your weight (kg)", 40, 200, 70)

if st.button("Calculate BMI"):

    BMI = weight / (height / 100) ** 2
    st.write(f"Your BMI is {BMI:.2f}")

    if BMI < 18.5:
        st.write("You are underweight.")

    elif 18.5 <= BMI < 25:
        st.write("You have normal weight.")

    elif 25 <= BMI < 30:
        st.write("You are overweight.")
        
    else:
        st.write("You are obese.")
