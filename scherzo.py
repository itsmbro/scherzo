import streamlit as st
import random

# Lista di frasi scherzose
frasi_scherzose = [
    "Sei come un Wi-Fi lento, nessuno ha pazienza per te!",
    "Se fossi un'app, saresti quella che nessuno scarica.",
    "La tua intelligenza è come un browser con troppe schede aperte.",
    "Sei come un antivirus che non ha mai fatto un aggiornamento.",
    "Non sei il peggio, ma ci stai arrivando!",
    "Sei come una password dimenticata: difficile da ricordare e da trovare.",
    "Hai il carisma di un piatto di pasta senza sugo.",
    "Sei come un file corrotto: non funziona mai come dovrebbe."
]

# Titolo della pagina
st.title("Frasi Scherzose per Insegnarti a Non Prenderti Troppo sul Serio!")

# Bottone per generare una frase random
if st.button('Genera una frase random!'):
    frase = random.choice(frasi_scherzose)
    st.write(f"**{frase}**")

# Aggiungi un footer
st.markdown("---")
st.markdown("Made with ❤️ da [Il Tuo Nome]")
