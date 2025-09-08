import streamlit as st

class UIHandler:
    @staticmethod
    def show_input_dialog(title: str, description: str, max_length: int = 32) -> str:
        """
        Zeigt ein Eingabefeld in einem Pop-Up an und gibt die Eingabe zurück.
        """
        with st.form(key=f"form_{title}"):
            st.subheader(title)
            st.write(description)
            user_input = st.text_input("Eingabe:", max_chars=max_length)
            submitted = st.form_submit_button("Bestätigen")
            if submitted:
                if len(user_input.strip()) == 0:
                    st.error("Die Eingabe darf nicht leer sein.")
                else:
                    return user_input.strip()
        return None

    @staticmethod
    def show_error(message: str):
        """
        Zeigt eine Fehlermeldung an.
        """
        st.error(message)

    @staticmethod
    def show_success(message: str):
        """
        Zeigt eine Erfolgsmeldung an.
        """
        st.success(message)

    @staticmethod
    def confirm_action(message: str) -> bool:
        """
        Zeigt eine Bestätigungsaufforderung an und gibt True zurück, wenn bestätigt wurde.
        """
        return st.button(message)