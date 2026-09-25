# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:27:04 2026

@author: msuette1
"""

#%% Imports
from Reglerauslegung_T_Summ import load_Data
from Reglerauslegung_T_Summ import compute_pi_tsum
from Reglerauslegung_T_Summ import plot_dual_axis

#%% Initialisierung
pfad = "C:/Sprungantwort_MRV03.xlsx"
spalten = ["MRV03(Stellgroeße)", 
           "TC-08(Regelgroeße)"]
name_time_column = "Time"
header = 6

#%%% Sprungantwort 01
# name_01 = "MRV03_01" 
# start_01 = "11:32:27" 
# end_01 = "11:32:55" 

#%%% Sprungantwort 02
# # Wie 01 nur mit nachwirkung von MRV02 Regelung
# name_02 = "MRV03_01" 
# start_02 = "11:32:27" 
# end_02 = "11:34:21"

#%%% Sprungantwort 03
name_03 = "MRV03_02" 
start_03 = "12:15:57" 
end_03 = "12:17:26"

#%%% Sprungantwort 04
name_04 = "MRV03_03" 
start_04 = "15:54:28" 
end_04 = "15:55:16"

#%%% Sprungantwort 05
name_05 = "MRV03_04" 
start_05 = "15:56:09" 
end_05 = "15:57:09"

#%%% Sprungantwort 06
name_06 = "MRV03_05" 
start_06 = "12:27:03" 
end_06 = "12:28:40"

#%% Call Function

#%%% Sprungantwort 01

# Data_01 = load_Data(pfad, name_01, spalten, start_01, end_01, spalte_zeit=name_time_column)

# y_data_01 = Data_01["TC-08(Regelgroeße)"].to_numpy()
# u_data_01 = Data_01["MRV03(Stellgroeße)"].to_numpy()
# t_data_01 = Data_01["Timestep"].to_numpy()

# delta_y_01 = y_data_01[-1] - y_data_01[0]
# delta_u_01 = u_data_01[-1] - u_data_01[0]

# compute_pi_tsum(delta_u_01, delta_y_01, t_sigma=None, t_data=t_data_01, y_data=y_data_01)
# plot_dual_axis(df=Data_01, title="Sprungantwort MRV02", xlabel="Zeitverlauf (Sekunden)", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 02

# Data_02 = load_Data(pfad, name_02, spalten, start_02, end_02, spalte_zeit=name_time_column)

# y_data_02 = Data_02["TC-08(Regelgroeße)"].to_numpy()
# u_data_02 = Data_02["MRV03(Stellgroeße)"].to_numpy()
# t_data_02 = Data_02["Timestep"].to_numpy()

# delta_y_02 = y_data_02[-1] - y_data_02[0]
# delta_u_02 = u_data_02[-1] - u_data_02[0]

# compute_pi_tsum(delta_u_02, delta_y_02, t_sigma=None, t_data=t_data_02, y_data=y_data_02)
# plot_dual_axis(df=Data_02, title="Sprungantwort MRV02", xlabel="Zeitverlauf in s", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 03

Data_03 = load_Data(pfad, name_03, spalten, start_03, end_03, spalte_zeit=name_time_column)

y_data_03 = Data_03["TC-08(Regelgroeße)"].to_numpy()
u_data_03 = Data_03["MRV03(Stellgroeße)"].to_numpy()
t_data_03 = Data_03["Timestep"].to_numpy()

delta_y_03 = y_data_03[-1] - y_data_03[0]
delta_u_03 = u_data_03[-1] - u_data_03[0]

compute_pi_tsum(delta_u_03, delta_y_03, t_sigma=None, t_data=t_data_03, y_data=y_data_03)
plot_dual_axis(df=Data_03, title="Sprungantwort MRV03", xlabel="Zeitverlauf in s", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 04

Data_04 = load_Data(pfad, name_04, spalten, start_04, end_04, spalte_zeit=name_time_column)

y_data_04 = Data_04["TC-08(Regelgroeße)"].to_numpy()
u_data_04 = Data_04["MRV03(Stellgroeße)"].to_numpy()
t_data_04 = Data_04["Timestep"].to_numpy()

delta_y_04 = y_data_04[-1] - y_data_04[0]
delta_u_04 = u_data_04[-1] - u_data_04[0]

compute_pi_tsum(delta_u_04, delta_y_04, t_sigma=None, t_data=t_data_04, y_data=y_data_04)
plot_dual_axis(df=Data_04, title="Sprungantwort MRV03", xlabel="Zeitverlauf in s", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 05

Data_05 = load_Data(pfad, name_05, spalten, start_05, end_05, spalte_zeit=name_time_column)

y_data_05 = Data_05["TC-08(Regelgroeße)"].to_numpy()
u_data_05 = Data_05["MRV03(Stellgroeße)"].to_numpy()
t_data_05 = Data_05["Timestep"].to_numpy()

delta_y_05 = y_data_05[-1] - y_data_05[0]
delta_u_05 = u_data_05[-1] - u_data_05[0]

compute_pi_tsum(delta_u_05, delta_y_05, t_sigma=None, t_data=t_data_05, y_data=y_data_05)
plot_dual_axis(df=Data_05, title="Sprungantwort MRV03", xlabel="Zeitverlauf in s", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")

#%%% Sprungantwort 06

Data_06 = load_Data(pfad, name_06, spalten, start_06, end_06, spalte_zeit=name_time_column)

y_data_06 = Data_06["TC-08(Regelgroeße)"].to_numpy()
u_data_06 = Data_06["MRV03(Stellgroeße)"].to_numpy()
t_data_06 = Data_06["Timestep"].to_numpy()

delta_y_06 = y_data_06[-1] - y_data_06[0]
delta_u_06 = u_data_06[-1] - u_data_06[0]

compute_pi_tsum(delta_u_06, delta_y_06, t_sigma=None, t_data=t_data_06, y_data=y_data_06)
plot_dual_axis(df=Data_06, title="Sprungantwort MRV03", xlabel="Zeitverlauf in s", ylabel1="Ventilstellung in %", ylabel2="Temperatur in °C")
