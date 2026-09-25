# -*- coding: utf-8 -*-
"""<<<<<
Created on Mon Aug  3 14:00:57 2026

@author: msuette1
"""
#%% Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
#%% Function load Data

def load_Data(datei_pfad: str,
              blatt_name: str,
              spalte_werte: str,
              start_zeit: str, 
              end_zeit: str,
              spalte_zeit: str = "Time",
              header_zeile: int = 6):



    """
    Liest ein Tabellenblatt aus Excel ein, filtert die Daten anhand eines Zeitfensters
    und gibt die Messwerte sowie die Zeitvektoren als ein  Dataframe zurück.
    
    Parameters:
    -----------
    datei_pfad  : Pfad zur Excel-Datei (z. B. 'C:/Messungen/Versuch_1.xlsx')
    blatt_name  : Name des Arbeitsblatts / Tabellenblatts (z. B. 'Mischventil')
    spalte_wert : Name der Spalte mit den Sensor-Messwerten (z. B. 'T_Mischwasser')
    start_zeit  : Anfangszeit im Format 'HH:MM:SS' (z. B. '10:00:00')
    end_zeit    : Endzeit im Format 'HH:MM:SS' (z. B. '10:10:00')
    spalte_zeit : Name der Zeitspalte (Standard: 'Time')
    
    Returns:
    --------
    t_sekunden  : NumPy-Array mit der Zeit in Sekunden ab Start des Zeitfensters (0, 1, 2, ...)
    y_werte     : NumPy-Array mit den gefilterten Messwerten
    """
    
#%%% Load Excel Sheet
    # Excel-Blatt einlesen
    df = pd.read_excel(datei_pfad, sheet_name=blatt_name, header=5)
    
    # Leerzeichen in Spaltennamen bereinigen
    df.columns = df.columns.astype(str).str.strip()
    
#%%% Check for columns
    # Prüfung, ob geforderte Spalten existieren
    if spalte_zeit not in df.columns:
        raise KeyError(f"Spalte '{spalte_zeit}' nicht in Blatt '{blatt_name}' gefunden.")
    for Spalte in spalte_werte:
        if Spalte not in df.columns:
            raise KeyError(f"Spalte 'Spalte' nicht in Blatt '{blatt_name}' gefunden.")
        
#%%% Time to sek
    # Uhrzeiten in Datetime-Objekte umwandeln (unterstützt Strings und Excel-Time-Format)
    raw_time = df[spalte_zeit].astype(str).str.strip()
    dt_series = pd.to_datetime(raw_time, format='%H:%M:%S', errors='coerce')
    if dt_series.isna().all():
        dt_series = pd.to_datetime(raw_time, errors='coerce')
        
    t_start = pd.to_datetime(start_zeit, format='%H:%M:%S').time()
    t_end = pd.to_datetime(end_zeit, format='%H:%M:%S').time()
    
    # Maske für das Zeitfenster erstellen, true/flase für Zeitbereich
    mask = (dt_series.dt.time >= t_start) & (dt_series.dt.time <= t_end)
    
    filtered_dt = dt_series.loc[mask]
    
#%%% Filter Data
    
    # Daten filtern und leere Zeilen entfernen
    for column in spalte_werte:
        df_filtered = df.loc[mask].dropna(subset=[column])
        if df_filtered.empty:
            raise ValueError(f"Keine Daten im Zeitfenster {start_zeit} bis {end_zeit} gefunden!")
    
#%%% Save Data
    # Relative Zeit in Sekunden ab Startpunkt berechnen (t_0 = 0s)
    t_sekunden = (filtered_dt - filtered_dt.iloc[0]).dt.total_seconds().to_numpy()
    
    Data_array = [t_sekunden]
    
    # Alle angegebenen Spalten (in spalte_werte) in einem Dataframe mit Timestep zusammen speichern
    for Name in spalte_werte:
        
        Data_array.append(df_filtered[Name].to_numpy())
    
    df_Data = pd.DataFrame(Data_array).T    # Zeilen array in spalten Dataframe speichern
    
    
    df_Data.columns = ["Timestep"] + spalte_werte
    # df_Data = df.set_index(filtered_dt)
    
    return df_Data


#%% Function for T_Sum

def compute_pi_tsum(delta_u, delta_y, t_sigma=None, t_data=None, y_data=None):
    """
    Berechnet die PI-Reglerparameter nach der T-Summen-Regel.
    
    Parameters:
    -----------
    delta_u : float
        Sprunghöhe der Stellgröße u (z.B. Ventilstellung in % oder 0..1)
    delta_y : float
        Veränderung der Temperatur y im Zielzustand (z.B. in °C)
    t_sigma : float, optional
        Manuell abgelesene Summenzeitkonstante T_Sigma in Sekunden
    t_data : array-like, optional
        Zeitvektor t der aufgenommenen Sprungantwort
    y_data : array-like, optional
        Messwertvektor y der aufgenommenen Sprungantwort
    """
    # 1. Streckenverstärkung K_S
    K_s = delta_y / delta_u
    
    # 2. Summenzeitkonstante T_Sigma bestimmen
    if t_sigma is None:
        if t_data is None or y_data is None:
            raise ValueError("Bitte entweder 't_sigma' angeben oder 't_data' und 'y_data' übergeben!")
        
        t = np.array(t_data)
        y = np.array(y_data)
        
        # Normierter Verlauf von 0 bis 1
        y_norm = (y - y[0]) / delta_y
        
        # Flächenintegration: Int_0^inf (1 - y_norm) dt
        t_sigma = np.trapezoid(1.0 - y_norm, t)
    
    # 3. Parametrierung nach T-Summen-Regel (Kuhn / Haalman)
    # Standard (Robust)
    kp_norm = 0.5 / K_s
    tn_norm = 0.5 * t_sigma
    ki_norm = kp_norm / tn_norm
    
    # Schnelle Einstellung
    kp_fast = 1.0 / K_s
    tn_fast = 0.7 * t_sigma
    ki_fast = kp_fast / tn_fast

    print("=" * 50)
    print(" ERGEBNISSE: T-SUMMEN-REGEL FÜR PI-REGLER")
    print("=" * 50)
    print(f"Streckenverstärkung  K_S     : {K_s:.4f}")
    print(f"Summenzeitkonstante  T_Sigma : {t_sigma:.2f} s")
    print("-" * 50)
    print("1. Robuste / Normale Einstellung (Empfohlen für Mischventile):")
    print(f"   -> Proportionalbeiwert  K_P : {kp_norm:.4f}")
    print(f"   -> Nachstellzeit        T_n : {tn_norm:.2f} s")
    print(f"   -> Integrationsbeiwert  K_I : {ki_norm:.4f} 1/s")
    print("-" * 50)
    print("2. Schnelle Einstellung (Aggressiver):")
    print(f"   -> Proportionalbeiwert  K_P : {kp_fast:.4f}")
    print(f"   -> Nachstellzeit        T_n : {tn_fast:.2f} s")
    print(f"   -> Integrationsbeiwert  K_I : {ki_fast:.4f} 1/s")
    print("=" * 50)

#%% Function plot Dataframe    
def plot_dual_axis(df, title, xlabel=None, ylabel1=None, ylabel2=None, label1=None, label2=None, label21=None):
    """
    Plottet die ersten drei Spalten eines DataFrames auf zwei Y-Achsen mit gemeinsamer X-Achse.
    
    Parameters:
    - df: pandas DataFrame (mindestens 3 Spalten)
    - title: str, Titel des Diagramms
    - xlabel: str, Beschriftung der X-Achse (optional, nutzt sonst Spaltennamen 1)
    - ylabel1: str, Beschriftung der 1. Y-Achse (optional, nutzt sonst Spaltennamen 2)
    - ylabel2: str, Beschriftung der 2. Y-Achse (optional, nutzt sonst Spaltennamen 3)
    """
    if df.shape[1] < 3:
        raise ValueError("Das DataFrame muss mindestens 3 Spalten enthalten.")

    # Spalten zuweisen
    x_col, y1_col, y2_col = df.columns[0], df.columns[1], df.columns[2]
    y21_col = df.columns[3] if len(df.columns) > 3 else None

    # Wunsch-Legenden-Namen oder Fallback auf Spaltennamen
    leg_label1 = label1 if label1 else str(y1_col)
    leg_label2 = label2 if label2 else str(y2_col)
    leg_label21 = label21 if label21 else (str(y21_col) if y21_col else None)

    # Standard-Beschriftungen festlegen, falls keine übergeben wurden
    xlabel = xlabel if xlabel else str(x_col)
    ylabel1 = ylabel1 if ylabel1 else str(y1_col)
    ylabel2 = ylabel2 if ylabel2 else str(y2_col)

    # Plot & erste Y-Achse erstellen
    fig, ax1 = plt.subplots(figsize=(10, 5))

    line1 = ax1.plot(df[x_col], df[y1_col], color='tab:blue', label=leg_label1, linewidth=2)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel1, color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Zweite Y-Achse erstellen (teilt sich die X-Achse mit ax1)
    ax2 = ax1.twinx()
    line2 = ax2.plot(df[x_col], df[y2_col], color='tab:orange', label=leg_label2, linewidth=2)
    ax2.set_ylabel(ylabel2, color='tab:orange')
    ax2.tick_params(axis='y', labelcolor='tab:orange')

    # Legenden beider Achsen zusammenführen
    lines = line1 + line2
    
    # Optionale 4. Spalte auf ax2 hinzufügen
    if y21_col:
        line3 = ax2.plot(df[x_col], df[y21_col], color='darkorange', label=leg_label21, linewidth=2, linestyle='--')
        lines += line3
    
    # Legenden beider Achsen zusammenführen
    labels = [line.get_label() for line in lines]
    ax1.legend(lines, labels)

    # Titel setzen & Layout anpassen
    plt.title(title, fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
#%% Ziegler & Nichols
from scipy.signal import savgol_filter

def calculate_pi_ziegler_nichols(t_array, y_array, delta_u, smooth=True, window_length=11, polyorder=2):
    """
    Berechnet PI-Reglerparameter nach Ziegler & Nichols (Wendetangenten-Verfahren).
    
    Parameters:
    -----------
    t_array : np.ndarray
        Array mit Zeitwerten in Sekunden (startend bei t=0).
    y_array : np.ndarray
        Array mit gemessenen Temperaturwerten.
    delta_u : float
        Stellgrößensprung am Ventil (z.B. 10.0 für 10 % Öffnung).
    smooth : bool, default=True
        Ob die Daten vor der Ableitung geglättet werden sollen (empfohlen bei Rauschen).
    window_length : int, default=11
        Fensterbreite für den Savitzky-Golay-Filter (muss ungerade sein).
    polyorder : int, default=2
        Polynomgrad für den Filter.

    """
    y0 = y_array[0]
    y_end = y_array[-1]
    delta_y = y_end - y0
    
    # 1. Streckenverstärkung Ks
    K_s = delta_y / delta_u
    
    # 2. Glättung für stabile Ableitung bei verrauschten Messdaten
    if smooth and len(y_array) >= window_length:
        y_proc = savgol_filter(y_array, window_length=window_length, polyorder=polyorder)
    else:
        y_proc = y_array.copy()
        
    # 3. Numerische Ableitung dy/dt (Steigung der Sprungantwort)
    dy_dt = np.gradient(y_proc, t_array)
    
    # Wendepunkt (Punkt der maximalen Steigung) ermitteln
    idx_wende = np.argmax(dy_dt)
    v_max = dy_dt[idx_wende]
    t_wende = t_array[idx_wende]
    y_wende = y_proc[idx_wende]
    
    # 4. Verzugszeit Tu (Schnittpunkt der Wendetangente mit Startwert y0)
    t_start_tan = t_wende - (y_wende - y0) / v_max
    T_u = max(t_start_tan - t_array[0], 1e-3) # Absicherung gegen negative Werte
    
    # 5. Ausgleichszeit Tg
    T_g = delta_y / v_max
    
    # 6. Ziegler & Nichols Formeln für PI-Regler
    kp_zn = 0.9 * (T_g / (K_s * T_u))
    tn_zn = 3.33 * T_u
    ki_zn = kp_zn / tn_zn
    
    print("=" * 50)
    print(" ERGEBNISSE: Ziegler & Nichols FÜR PI-REGLER")
    print("=" * 50)
    print(f"Streckenverstärkung K_s     : {K_s:.2f}")
    print(f"Maximale Steigung   v_max   : {v_max:.2f}")
    print(f"Ausgleichszeit      Tg      : {T_g:.2f}")
    print(f"Verzugszeit         Tu      : {T_u:.2f}")
    print("-" * 50)
    print(f"Wendepunkt          t       : {t_wende:.2f} s")
    print("-" * 50)
    print("Einstellwerte für den PI-Regler:")
    print(f"   -> Proportionalbeiwert  K_p : {kp_zn:.4f}")
    print(f"   -> Nachstellzeit        T_n : {tn_zn:.2f} s")
    print(f"   -> Integrationsbeiwert  K_I : {ki_zn:.4f} 1/s")
    print("=" * 50)
    