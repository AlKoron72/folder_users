import streamlit as st
from utils.Folder import Folder
from utils.User import User
from utils.UI_handler import UIHandler

# Session State initialisieren
if "folders" not in st.session_state:
    st.session_state.folders = []  # Liste von Folder-Objekten
if "selected_folder" not in st.session_state:
    st.session_state.selected_folder = None  # Aktuell ausgewählter Ordner

# Funktionen
def create_folder():
    folder_name = UIHandler.show_input_dialog(
        title="Neuen Ordner erstellen",
        description="Gib den Namen des neuen Ordners ein (max. 32 Zeichen):",
        max_length=32,
    )
    if folder_name:
        if folder_name in [folder.name for folder in st.session_state.folders]:
            UIHandler.show_error("Ein Ordner mit diesem Namen existiert bereits.")
        else:
            st.session_state.folders.append(Folder(folder_name))
            UIHandler.show_success(f"Ordner '{folder_name}' wurde erstellt.")

def create_user():
    if st.session_state.selected_folder is None:
        UIHandler.show_error("Bitte wähle zuerst einen Ordner aus.")
        return

    user_name = UIHandler.show_input_dialog(
        title="Neuen Nutzer erstellen",
        description="Gib den Namen des neuen Nutzers ein (max. 32 Zeichen):",
        max_length=32,
    )
    if user_name:
        selected_folder = next(
            (folder for folder in st.session_state.folders if folder.name == st.session_state.selected_folder), None
        )
        if selected_folder:
            try:
                selected_folder.add_user(user_name)
                UIHandler.show_success(f"Nutzer '{user_name}' wurde hinzugefügt.")
            except ValueError as e:
                UIHandler.show_error(str(e))

def delete_folder(folder_name):
    if UIHandler.confirm_action(f"Ordner '{folder_name}' wirklich löschen?"):
        st.session_state.folders = [folder for folder in st.session_state.folders if folder.name != folder_name]
        if st.session_state.selected_folder == folder_name:
            st.session_state.selected_folder = None
        UIHandler.show_success(f"Ordner '{folder_name}' wurde gelöscht.")

def delete_user(folder_name, user_name):
    folder = next((folder for folder in st.session_state.folders if folder.name == folder_name), None)
    if folder:
        if UIHandler.confirm_action(f"Nutzer '{user_name}' wirklich löschen?"):
            folder.remove_user(user_name)
            UIHandler.show_success(f"Nutzer '{user_name}' wurde gelöscht.")

# Sidebar
st.sidebar.title("📂 Ordner und Nutzer")
for folder in st.session_state.folders:
    with st.sidebar.expander(f"📁 {folder.name}"):
        for user in folder.users:
            # Nutzer mit Icon und Löschen-Button anzeigen
            col1, col2 = st.sidebar.columns([4, 1])
            with col1:
                st.markdown(f"👤 {user.name}")
            with col2:
                if st.button("❌", key=f"delete_user_{folder.name}_{user.name}"):
                    delete_user(folder.name, user.name)

        # Ordner-Löschen-Button
        if st.button("Ordner löschen", key=f"delete_folder_{folder.name}"):
            delete_folder(folder.name)

# Ordner erstellen
if st.sidebar.button("📂 Neuen Ordner erstellen"):
    create_folder()

# Hauptbereich
st.title("Nutzer- und Ordnerverwaltung")
st.write("Wähle einen Ordner aus, um Nutzer hinzuzufügen oder zu verwalten.")

# Ordnerauswahl
folder_names = [folder.name for folder in st.session_state.folders]
selected_folder = st.selectbox("Ordner auswählen:", ["Kein Ordner"] + folder_names)
if selected_folder != "Kein Ordner":
    st.session_state.selected_folder = selected_folder

# Nutzer erstellen
if st.sidebar.button("👤 Neuen Nutzer erstellen"):
    create_user()