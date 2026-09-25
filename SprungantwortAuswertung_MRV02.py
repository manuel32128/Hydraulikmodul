# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:21:20 2026

@author: msuette1
"""

#%% Imports
from Reglerauslegung_T_Summ import load_Data
from Reglerauslegung_T_Summ import compute_pi_tsum
from Reglerauslegung_T_Summ import plot_dual_axis
from Reglerauslegung_T_Summ import calculate_pi_ziegler_nichols

#%% Initialisierung
pfad = "C:/Sprungantwort_MRV02.xlsx"
spalten = ["Ventilstellung_MRV02(Stellgröße)", 
           "Pt-04(Regelgroeße)",
           "TC-08"]
name_time_column = "Time"
header = 6

#%%% Sprungantwort 01
name_01 = "MRV02_03" 
start_01 = "11:00:04" 
end_01 = "11:10:12" 

#%%% Sprungantwort 02
name_02 = "MRV02_04" 
start_02 = "08:41:14" 
end_02 = "08:42:08"

#%%% Sprungantwort 03
name_03 = "MRV02_05" 
start_03 = "17:05:01" 
end_03 = "17:09:02"

#%%% Sprungantwort 04
name_04 = "MRV02_06" 
start_04 = "10:35:03" 
end_04 = "10:40:47"

#%%% Sprungantwort 05
name_05 = "MRV02_07" 
start_05 = "10:41:04" 
end_05 = "10:44:18"

#%% Call Function

#%%% Sprungantwort 01

Data_01 = load_Data(pfad, name_01, spalten, start_01, end_01, spalte_zeit=name_time_column)

y_data_01 = Data_01["Pt-04(Regelgroeße)"].to_numpy()
u_data_01 = Data_01["Ventilstellung_MRV02(Stellgröße)"].to_numpy()
t_data_01 = Data_01["Timestep"].to_numpy()

delta_y_01 = y_data_01[-1] - y_data_01[0]
delta_u_01 = u_data_01[-1] - u_data_01[0]

compute_pi_tsum(delta_u_01, delta_y_01, t_sigma=None, t_data=t_data_01, y_data=y_data_01)
calculate_pi_ziegler_nichols(t_data_01, y_data_01, delta_u_01)
plot_dual_axis(df=Data_01, title="Sprungantwort MRV02", xlabel="Zeitverlauf (Sekunden)", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 02

Data_02 = load_Data(pfad, name_02, spalten, start_02, end_02, spalte_zeit=name_time_column)

y_data_02 = Data_02["Pt-04(Regelgroeße)"].to_numpy()
u_data_02 = Data_02["Ventilstellung_MRV02(Stellgröße)"].to_numpy()
t_data_02 = Data_02["Timestep"].to_numpy()

delta_y_02 = y_data_02[-1] - y_data_02[0]
delta_u_02 = u_data_02[-1] - u_data_02[0]

compute_pi_tsum(delta_u_02, delta_y_02, t_sigma=None, t_data=t_data_02, y_data=y_data_02)
plot_dual_axis(df=Data_02, title="Sprungantwort MRV02", xlabel="Zeitverlauf in s", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 03

Data_03 = load_Data(pfad, name_03, spalten, start_03, end_03, spalte_zeit=name_time_column)

y_data_03 = Data_03["Pt-04(Regelgroeße)"].to_numpy()
u_data_03 = Data_03["Ventilstellung_MRV02(Stellgröße)"].to_numpy()
t_data_03 = Data_03["Timestep"].to_numpy()

delta_y_03 = y_data_03[-1] - y_data_03[0]
delta_u_03 = u_data_03[-1] - u_data_03[0]

compute_pi_tsum(delta_u_03, delta_y_03, t_sigma=None, t_data=t_data_03, y_data=y_data_03)
plot_dual_axis(df=Data_03, title="Sprungantwort MRV02", xlabel="Zeitverlauf in s", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 04

Data_04 = load_Data(pfad, name_04, spalten, start_04, end_04, spalte_zeit=name_time_column)

y_data_04 = Data_04["Pt-04(Regelgroeße)"].to_numpy()
u_data_04 = Data_04["Ventilstellung_MRV02(Stellgröße)"].to_numpy()
t_data_04 = Data_04["Timestep"].to_numpy()

delta_y_04 = y_data_04[-1] - y_data_04[0]
delta_u_04 = u_data_04[-1] - u_data_04[0]

compute_pi_tsum(delta_u_04, delta_y_04, t_sigma=None, t_data=t_data_04, y_data=y_data_04)
plot_dual_axis(df=Data_04, title="Sprungantwort MRV02", xlabel="Zeitverlauf in s", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 05

Data_05 = load_Data(pfad, name_05, spalten, start_05, end_05, spalte_zeit=name_time_column)

y_data_05 = Data_05["Pt-04(Regelgroeße)"].to_numpy()
u_data_05 = Data_05["Ventilstellung_MRV02(Stellgröße)"].to_numpy()
t_data_05 = Data_05["Timestep"].to_numpy()

delta_y_05 = y_data_05[-1] - y_data_05[0]
delta_u_05 = u_data_05[-1] - u_data_05[0]

compute_pi_tsum(delta_u_05, delta_y_05, t_sigma=None, t_data=t_data_05, y_data=y_data_05)
plot_dual_axis(df=Data_05, title="Sprungantwort MRV02", xlabel="Zeitverlauf in s", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")
