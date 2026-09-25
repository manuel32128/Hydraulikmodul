# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:36:52 2026

@author: msuette1
"""

#%% Imports
from Reglerauslegung_T_Summ import load_Data
from Reglerauslegung_T_Summ import compute_pi_tsum
from Reglerauslegung_T_Summ import plot_dual_axis

#%% Initialisierung
pfad = "C:/Sprungantwort_P01.xlsx"
spalten = ["P01_set(Stellgroeße)", 
           "P01_Flow(Regelgroeße)",
           "P-01_Flow"]
name_time_column = "Time"
header = 6

#%%% Sprungantwort 01
name_01 = "P01_01" 
start_01 = "09:19:22" 
end_01 = "09:22:00" 

#%%% Sprungantwort 02
name_02 = "P01_02" 
start_02 = "11:05:22" 
end_02 = "11:07:34" 

#%%% Sprungantwort 03
name_03 = "P01_03" 
start_03 = "09:35:09" 
end_03 = "09:37:15" 

#%% Call Function

#%%% Sprungantwort 01

Data_01 = load_Data(pfad, name_01, spalten, start_01, end_01, spalte_zeit=name_time_column)

y_data_01 = Data_01["P01_Flow(Regelgroeße)"].to_numpy()
u_data_01 = Data_01["P01_set(Stellgroeße)"].to_numpy()
t_data_01 = Data_01["Timestep"].to_numpy()

delta_y_01 = y_data_01[-1] - y_data_01[0]
delta_u_01 = u_data_01[-1] - u_data_01[0]

compute_pi_tsum(delta_u_01, delta_y_01, t_sigma=None, t_data=t_data_01, y_data=y_data_01)
plot_dual_axis(df=Data_01, 
               title="Sprungantwort P01", 
               xlabel="Zeit t in s", 
               ylabel1="Stellgröße $u$ (Pumpendrehzahl) in %", 
               ylabel2="Regelgröße $x$ (Volumenstrom $\dot V_\mathrm{P01}$) in m³/h",
               label1="Stellgröße $u$", 
               label2="Volumenstrom $\dot V_\mathrm{P01}$ geglätet", 
               label21="Volumenstrom $\dot V_\mathrm{P01}$ Rohdaten")
#%%% Sprungantwort 02

Data_02 = load_Data(pfad, name_02, spalten, start_02, end_02, spalte_zeit=name_time_column)

y_data_02 = Data_02["P01_Flow(Regelgroeße)"].to_numpy()
u_data_02 = Data_02["P01_set(Stellgroeße)"].to_numpy()
t_data_02 = Data_02["Timestep"].to_numpy()

delta_y_02 = y_data_02[-1] - y_data_02[0]
delta_u_02 = u_data_02[-1] - u_data_02[0]

compute_pi_tsum(delta_u_02, delta_y_02, t_sigma=None, t_data=t_data_02, y_data=y_data_02)
plot_dual_axis(df=Data_02, 
               title="Sprungantwort P01", 
               xlabel="Zeit t in s", 
               ylabel1="Stellgröße $u$ (Pumpendrehzahl) in %", 
               ylabel2="Regelgröße $x$ (Volumenstrom $\dot V_\mathrm{P01}$) in m³/h",
               label1="Stellgröße $u$", 
               label2="Volumenstrom $\dot V_\mathrm{P01}$ geglätet", 
               label21="Volumenstrom $\dot V_\mathrm{P01}$ Rohdaten")

#%%% Sprungantwort 03

Data_03 = load_Data(pfad, name_03, spalten, start_03, end_03, spalte_zeit=name_time_column)

y_data_03 = Data_03["P01_Flow(Regelgroeße)"].to_numpy()
u_data_03 = Data_03["P01_set(Stellgroeße)"].to_numpy()
t_data_03 = Data_03["Timestep"].to_numpy()

delta_y_03 = y_data_03[-1] - y_data_03[0]
delta_u_03 = u_data_03[-1] - u_data_03[0]

compute_pi_tsum(delta_u_03, delta_y_03, t_sigma=None, t_data=t_data_03, y_data=y_data_03)
plot_dual_axis(df=Data_03, 
               title="Sprungantwort P01", 
               xlabel="Zeit t in s", 
               ylabel1="Stellgröße $u$ (Pumpendrehzahl) in %", 
               ylabel2="Regelgröße $x$ (Volumenstrom $\dot V_\mathrm{P01}$) in m³/h",
               label1="Stellgröße $u$", 
               label2="Volumenstrom $\dot V_\mathrm{P01}$ geglätet", 
               label21="Volumenstrom $\dot V_\mathrm{P01}$ Rohdaten")