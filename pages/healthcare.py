import streamlit as st

# Dummy data for doctors
doctors_data = [
    {"name": "Dr. Ajay Kumar", "specialty": "Cardiologist", "phone": "+91 98765 43210", "image": "doctor1.jpg"},
    {"name": "Dr. Priya Sharma", "specialty": "Dermatologist", "phone": "+91 98765 43211", "image": "doctor2.jpg"},
    {"name": "Dr. Rahul Singh", "specialty": "Pediatrician", "phone": "+91 98765 43212", "image": "doctor3.jpg"},
]

def app():
    st.title("Jaipur City Guide - Healthcare 🏥")
    st.header("Find Doctors in Jaipur")

    # Select specialty
    specialties = set(doctor['specialty'] for doctor in doctors_data)
    selected_specialty = st.selectbox("Select Specialty", ["All"] + list(specialties))

    # Display doctors
    for doctor in doctors_data:
        if selected_specialty == "All" or selected_specialty == doctor['specialty']:
            st.write(f"## {doctor['name']}")
            st.image(doctor['image'], width=200)
            st.write(f"*Specialty:* {doctor['specialty']}")
            st.write(f"*Phone:* {doctor['phone']}")
            if st.button(f"Book Appointment with {doctor['name']}", key=doctor['name']):
                book_appointment(doctor['name'])

def book_appointment(doctor_name):
    st.write(f"## Book Appointment with {doctor_name}")
    with st.form(f"appointment_form_{doctor_name}"):
        name = st.text_input("Your Name")
        age = st.number_input("Age", min_value=0, max_value=150, step=1)
        number = st.text_input("Phone Number")
        health_issue = st.text_area("Describe Your Issue")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.success("Appointment Booked Successfully!")
            st.write(f"*Patient Name:* {name}")
            st.write(f"*Age:* {age}")
            st.write(f"*Phone:* {number}")
            st.write(f"*Health Issue:* {health_issue}")