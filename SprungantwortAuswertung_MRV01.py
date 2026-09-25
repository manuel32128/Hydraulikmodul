# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 16:51:48 2026

@author: msuette1
"""

#%% Imports
from Reglerauslegung_T_Summ import load_Data
from Reglerauslegung_T_Summ import compute_pi_tsum
from Reglerauslegung_T_Summ import plot_dual_axis

#%% Initialisierung
pfad = "C:/Sprungantwort_MRV01.xlsx"
spalten = ["MRV01(Stellgroeße)", 
           "Pt-02(Regelgroeße)"]
name_time_column = "Time"
header = 6

#%%% Sprungantwort 01
# name_01 = "MRV01_01" 
# start_01 = "14:45:55" 
# end_01 = "14:47:43" 

#%%% Sprungantwort 02
# name_02 = "MRV01_01" 
# start_02 = "14:45:55" 
# end_02 = "14:48:30" 

#%%% Sprungantwort 03
# name_03 = "MRV01_02" 
# start_03 = "16:56:15" 
# end_03 = "16:58:32" 

#%%% Sprungantwort 04
# name_04 = "MRV01_02" 
# start_04 = "16:56:15" 
# end_04 = "17:05:34"

#%%% Sprungantwort 05
# name_05 = "MRV01_03" 
# start_05 = "10:45:16" 
# end_05 = "10:47:01"

#%%% Sprungantwort 06
# name_06 = "MRV01_04" 
# start_06 = "12:05:08" 
# end_06 = "12:23:00"

#%%% Sprungantwort 07
name_07 = "MRV01_05" 
start_07 = "13:42:10" 
end_07 = "13:43:30"

#%%% Sprungantwort 08
name_08 = "MRV01_06" 
start_08 = "14:00:12" 
end_08 = "14:01:15"

#%% Call Function

#%%% Sprungantwort 01

# Data_01 = load_Data(pfad, name_01, spalten, start_01, end_01, spalte_zeit=name_time_column)

# y_data_01 = Data_01["Pt-02(Regelgroeße)"].to_numpy()
# u_data_01 = Data_01["MRV01(Stellgroeße)"].to_numpy()
# t_data_01 = Data_01["Timestep"].to_numpy()

# delta_y_01 = y_data_01[-1] - y_data_01[0]
# delta_u_01 = u_data_01[-1] - u_data_01[0]

# compute_pi_tsum(delta_u_01, delta_y_01, t_sigma=None, t_data=t_data_01, y_data=y_data_01)
# plot_dual_axis(df=Data_01, title="Sprungantwort MRV01", xlabel="Zeitverlauf (Sekunden)", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 02

# Data_02 = load_Data(pfad, name_02, spalten, start_02, end_02, spalte_zeit=name_time_column)

# y_data_02 = Data_02["Pt-02(Regelgroeße)"].to_numpy()
# u_data_02 = Data_02["MRV01(Stellgroeße)"].to_numpy()
# t_data_02 = Data_02["Timestep"].to_numpy()

# delta_y_02 = y_data_02[-1] - y_data_02[0]
# delta_u_02 = u_data_02[-1] - u_data_02[0]

# compute_pi_tsum(delta_u_02, delta_y_02, t_sigma=None, t_data=t_data_02, y_data=y_data_02)
# plot_dual_axis(df=Data_02, title="Sprungantwort MRV01", xlabel="Zeitverlauf (Sekunden)", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 03

# Data_03 = load_Data(pfad, name_03, spalten, start_03, end_03, spalte_zeit=name_time_column)

# y_data_03 = Data_03["Pt-02(Regelgroeße)"].to_numpy()
# u_data_03 = Data_03["MRV01(Stellgroeße)"].to_numpy()
# t_data_03 = Data_03["Timestep"].to_numpy()

# delta_y_03 = y_data_03[-1] - y_data_03[0]
# delta_u_03 = u_data_03[-1] - u_data_03[0]

# compute_pi_tsum(delta_u_03, delta_y_03, t_sigma=None, t_data=t_data_03, y_data=y_data_03)
# plot_dual_axis(df=Data_03, title="Sprungantwort MRV01", xlabel="Zeitverlauf in s", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 04

# Data_04 = load_Data(pfad, name_04, spalten, start_04, end_04, spalte_zeit=name_time_column)

# y_data_04 = Data_04["Pt-02(Regelgroeße)"].to_numpy()
# u_data_04 = Data_04["MRV01(Stellgroeße)"].to_numpy()
# t_data_04 = Data_04["Timestep"].to_numpy()

# delta_y_04 = y_data_04[-1] - y_data_04[0]
# delta_u_04 = u_data_04[-1] - u_data_04[0]

# compute_pi_tsum(delta_u_04, delta_y_04, t_sigma=None, t_data=t_data_04, y_data=y_data_04)
# plot_dual_axis(df=Data_04, title="Sprungantwort MRV01", xlabel="Zeitverlauf in s", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 05

# Data_05 = load_Data(pfad, name_05, spalten, start_05, end_05, spalte_zeit=name_time_column)

# y_data_05 = Data_05["Pt-02(Regelgroeße)"].to_numpy()
# u_data_05 = Data_05["MRV01(Stellgroeße)"].to_numpy()
# t_data_05 = Data_05["Timestep"].to_numpy()

# delta_y_05 = y_data_05[-1] - y_data_05[0]
# delta_u_05 = u_data_05[-1] - u_data_05[0]

# compute_pi_tsum(delta_u_05, delta_y_05, t_sigma=None, t_data=t_data_05, y_data=y_data_05)
# plot_dual_axis(df=Data_05, title="Sprungantwort MRV01", xlabel="Zeitverlauf in s", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 06

# Data_06 = load_Data(pfad, name_06, spalten, start_06, end_06, spalte_zeit=name_time_column)

# y_data_06 = Data_06["Pt-02(Regelgroeße)"].to_numpy()
# u_data_06 = Data_06["MRV01(Stellgroeße)"].to_numpy()
# t_data_06 = Data_06["Timestep"].to_numpy()

# delta_y_06 = y_data_06[-1] - y_data_06[0]
# delta_u_06 = u_data_06[-1] - u_data_06[0]

# compute_pi_tsum(delta_u_06, delta_y_06, t_sigma=None, t_data=t_data_06, y_data=y_data_06)
# plot_dual_axis(df=Data_06, title="Sprungantwort MRV01", xlabel="Zeitverlauf in s", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 07

Data_07 = load_Data(pfad, name_07, spalten, start_07, end_07, spalte_zeit=name_time_column)

y_data_07 = Data_07["Pt-02(Regelgroeße)"].to_numpy()
u_data_07 = Data_07["MRV01(Stellgroeße)"].to_numpy()
t_data_07 = Data_07["Timestep"].to_numpy()

delta_y_07 = y_data_07[-1] - y_data_07[0]
delta_u_07 = u_data_07[-1] - u_data_07[0]

compute_pi_tsum(delta_u_07, delta_y_07, t_sigma=None, t_data=t_data_07, y_data=y_data_07)
plot_dual_axis(df=Data_07, 
               title=r"Sprungantwort MRV-01 mit $\mathbf{u = 31 \to 26\,\%}$", 
               xlabel="Zeit t in s", 
               ylabel1="Stellgröße $u$ in %", 
               ylabel2="Regelgröße $x$ in °C",
               label1="Ventilstellung", 
               label2=r"Temperatur $\vartheta_{\mathrm{Pt100-02}}$")
#%%% Sprungantwort 08

Data_08 = load_Data(pfad, name_08, spalten, start_08, end_08, spalte_zeit=name_time_column)

y_data_08 = Data_08["Pt-02(Regelgroeße)"].to_numpy()
u_data_08 = Data_08["MRV01(Stellgroeße)"].to_numpy()
t_data_08 = Data_08["Timestep"].to_numpy()

delta_y_08 = y_data_08[-1] - y_data_08[0]
delta_u_08 = u_data_08[-1] - u_data_08[0]

compute_pi_tsum(delta_u_08, delta_y_08, t_sigma=None, t_data=t_data_08, y_data=y_data_08)
plot_dual_axis(df=Data_08, 
               title=r"Sprungantwort MRV-01 mit $\mathbf{u = 29 \to 37\,\%}$", 
               xlabel="Zeit t in s", 
               ylabel1="Stellgröße $u$ in %", 
               ylabel2="Regelgröße $x$ in °C",
               label1="Ventilstellung", 
               label2=r"Temperatur $\vartheta_{\mathrm{Pt100-02}}$")