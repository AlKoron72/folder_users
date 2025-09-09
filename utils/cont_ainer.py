import streamlit as st

# Zwei Spalten erstellen
col1, col2 = st.columns([3, 1])  # Linke Spalte ist breiter, rechte Spalte ist schmaler

# Hauptinhalt in der linken Spalte
with col1:
    st.title("Hauptinhalt")
    st.write("Hier ist der Hauptinhalt der App.")

# Rechte Spalte als "Sidebar"
with col2:
    st.title("Rechte Sidebar")
    st.write("Hier ist die simulierte rechte Sidebar.")
    st.button("Button in der rechten Sidebar")