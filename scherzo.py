import streamlit as st
import pandas as pd
import os

# Funzione per calcolare il piano d'accumulo con interessi composti
def calcola_piano(capital_iniziale, durata_mesi, tasso_annuo, frequenza_interessi):
    try:
        saldo = capital_iniziale
        dati = []
        giorni_totali = durata_mesi * 30  # Approssimazione di 30 giorni per mese

        # Definizione della frequenza di capitalizzazione
        frequenze = {
            "Giornaliero": 365,
            "Mensile": 12,
            "Semestrale": 2,
            "Annuale": 1
        }

        n = frequenze[frequenza_interessi]  # Numero di capitalizzazioni all'anno
        tasso_periodico = tasso_annuo / n   # Tasso di interesse per periodo

        # Calcolo giorno per giorno
        for giorno in range(1, giorni_totali + 1):
            interesse = 0
            # Applichiamo l'interesse solo nei giorni di capitalizzazione
            if giorno % (365 // n) == 0:
                interesse = saldo * tasso_periodico
                saldo += interesse  # Aggiungi l'interesse al saldo

            # Aggiunta dei dati per ogni giorno
            dati.append({
                "Giorno": giorno,
                "Interesse maturato (€)": round(interesse, 2),
                "Saldo finale (€)": round(saldo, 2)
            })

        # Creazione del DataFrame
        df = pd.DataFrame(dati)

        # Salvataggio su file Excel
        file_path = os.path.join(os.getcwd(), 'piano_accumulo_capitale.xlsx')
        df.to_excel(file_path, index=False)

        return df, file_path

    except ValueError:
        return None, "Errore nei dati inseriti. Assicurati di inserire valori numerici validi."


# Interfaccia utente con Streamlit
st.title("Piano d'Accumulazione del Capitale")

# Input dell'utente
capital_iniziale = st.number_input("Capitale iniziale (€)", min_value=0.0, format="%.2f")
durata_mesi = st.number_input("Durata (mesi)", min_value=1, max_value=600, format="%d")
tasso_annuo = st.number_input("Tasso di interesse annuo (%)", min_value=0.0, format="%.2f")

# Scelta della frequenza degli interessi
frequenza_interessi = st.selectbox(
    "Frequenza di calcolo degli interessi",
    ["Giornaliero", "Mensile", "Semestrale", "Annuale"]
)

# Bottone per calcolare
if st.button("Calcola Piano"):
    if capital_iniziale > 0 and durata_mesi > 0 and tasso_annuo >= 0:
        df, result = calcola_piano(capital_iniziale, durata_mesi, tasso_annuo / 100, frequenza_interessi)
        if df is not None:
            st.dataframe(df)  # Visualizza il DataFrame con i risultati

            # Messaggio di successo
            st.success(f"File Excel creato con successo: {result}")
        else:
            st.error(result)
    else:
        st.error("Assicurati di inserire valori validi per tutti i campi.")
