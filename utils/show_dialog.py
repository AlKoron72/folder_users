import streamlit as st
from streamlit_modal import Modal

modal = Modal(key="example_modal", title="Beispiel Modal")

if st.button("Zeige Pop-up"):
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("### Eingabe erforderlich")
        user_input = st.text_input("Name", max_chars=32)
        if st.button("Bestätigen"):
            if len(user_input.strip()) == 0:
                st.error("Die Eingabe darf nicht leer sein.")
            else:
                st.success(f"Eingabe erfolgreich: {user_input}")
                modal.close()