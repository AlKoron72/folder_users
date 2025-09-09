import streamlit as st

# Dummy-Klasse für Folder
class Folder:
    def __init__(self, name):
        self.name = name
        self.users = []

# Session State initialisieren
if "folders" not in st.session_state:
    st.session_state.folders = []  # Liste von Folder-Objekten

# Funktionen
def create_folder():
    """
    Funktion zum Erstellen eines neuen Ordners.
    """
    folder_name = st.text_input("Gib den Namen des neuen Ordners ein:", key="folder_input")
    if st.button("Ordner erstellen", key="create_folder_button"):
        if folder_name.strip() == "":
            st.error("Der Ordnername darf nicht leer sein.")
        elif folder_name in [folder.name for folder in st.session_state.folders]:
            st.error("Ein Ordner mit diesem Namen existiert bereits.")
        else:
            # Ordner erstellen und zur Liste hinzufügen
            st.session_state.folders.append(Folder(folder_name))
            st.success(f"Ordner '{folder_name}' wurde erstellt.")

# Sidebar
st.sidebar.title("📂 Ordnerverwaltung")
if st.sidebar.button("📂 Neuen Ordner erstellen"):
    st.session_state.show_create_folder = True  # Zeige das Eingabefeld für Ordner

# Hauptbereich
st.title("Ordnerübersicht")

# Zeige das Eingabefeld für Ordner, falls aktiviert
if st.session_state.get("show_create_folder", False):
    create_folder()

# Zeige die Liste der Ordner
if len(st.session_state.folders) > 0:
    st.write("### Deine Ordner:")
    for folder in st.session_state.folders:
        st.write(f"📁 {folder.name}")
else:
    st.write("Noch keine Ordner erstellt.")