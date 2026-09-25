# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 08:42:20 2026

@author: msuette1
"""

#%% Imports
from Reglerauslegung_T_Summ import load_Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

#%% Initialisierung

#%%% Allgemein

cp_SE = 4180    # in J/kg*K
rho_SE = 990    # in kg/m³

cp_QU = 3560    # in J/kg*K
rho_QU = 1063   # in kg/m³

comp_ref_COP = []
COP_B0W35 = []
Pth_B0W35 = []
Pel_B0W35 = []
Pth_KW = []
T_Senke_In = []
T_Senke_Out = []
T_Quelle_In = []
T_Quelle_Out = []
Vdot_QU = []
Vdot_Senke = []
Eco_T_Senke_In = []
Eco_T_Senke_Out = []
Eco_T_Quelle_In = []
Eco_T_Quelle_Out = []



#%%% Datasheet

pfad_Datasheet_COP = "C:/Datasheet_WP_COP.xlsx"
df_COP = pd.read_excel(pfad_Datasheet_COP, usecols=[0, 1])
pfad_Datasheet_Pth = "C:/Datasheet_WP_Pth.xlsx"
df_Pth = pd.read_excel(pfad_Datasheet_Pth, usecols=[0, 1])
pfad_Datasheet_Pel = "C:/Datasheet_WP_Pel.xlsx"
df_Pel = pd.read_excel(pfad_Datasheet_Pel, usecols=[0, 1])



comp_ref_Datasheet_COP = df_COP['Comp.Ref']
COP_B0W35_Datasheet = df_COP['COP']
comp_ref_Datasheet_Pth = df_Pth['Comp.Ref']
Pth_B0W35_Datasheet = df_Pth['P_th']
comp_ref_Datasheet_Pel = df_Pel['Comp.Ref']
Pel_B0W35_Datasheet = df_Pel['P_el']

#%%% Messdaten
pfad = "C:/B0W35.xlsx"
spalten = ["56P1_WLeistungGes", 
           "DurchflussQuelleVAR",
           "DurchflussSenkeVAR",
           "EcoDTPrimCirc",
           "EcoMaxRefComp",
           "EcoPrimCircInTemp",
           "EcoPrimCircOutTemp",
           "EcoTotElCons",
           "EcoTotHeatPWR", 
           "HM_QU__HM_PT_T_IN",
           "HM_QU__HM_PT_T_OUT",
           "HM_SE__HM_PT_T_IN",
           "HM_SE__HM_PT_T_OUT",
           "P-01_PWRInput",
           "P-01_Speed",
           "P-02_PWRInput",
           "P-02_Speed",
           "EcoDTSecCirc",
           "EcoSecCircInTemp",
           "EcoSecCircOutTemp",
           "P-01_Flow_Scaled",
           "P-02_Flow_Scaled",         
           "Kaelteleistung_Quelle",     
           "Waermeleistung_Senke"]  

name_time_column = "Time"
header = 6
#%%%% Messpunkt 1 mit 20 % Verdichterdrehzahl
name_20 = "n1072_p20" 
start_20 = "11:24:00" 
end_20 = "11:54:00"

#%%%% Messpunkt 1.1 mit 25 % Verdichterdrehzahl
name_25 = "n1794_p25" 
start_25 = "16:30:00" 
end_25 = "17:00:00"

#%%%% Messpunkt 2 mit 30 % Verdichterdrehzahl
name_30 = "n2154_p30" 
start_30 = "14:19:00" 
end_30 = "14:49:00"

#%%%% Messpunkt 3 mit 40 % Verdichterdrehzahl
name_40 = "n2874_p40" 
start_40 = "15:20:00" 
end_40 = "15:50:00"

#%%%% Messpunkt 4 mit 50 % Verdichterdrehzahl
name_50 = "n3594_p50" 
start_50 = "16:30:00" 
end_50 = "17:00:00"

#%%%% Messpunkt 5 mit 60 % Verdichterdrehzahl
name_60 = "n4314_p60" 
start_60 = "11:20:00" 
end_60 = "11:50:00"

#%%%% Messpunkt 6 mit 70 % Verdichterdrehzahl
name_70 = "n5034_p70" 
start_70 = "13:00:00" 
end_70 = "13:30:00"

#%%%% Messpunkt 7 mit 80 % Verdichterdrehzahl
name_80 = "n5754_p80" 
start_80 = "14:00:00" 
end_80 = "14:30:00"

#%%%% Messpunkt 8 mit 90 % Verdichterdrehzahl
name_90 = "n6474_p90" 
start_90 = "14:55:00" 
end_90 = "15:25:00"

#%%%% Messpunkt 9 mit 100 % Verdichterdrehzahl
name_100 = "n7194_p100" 
start_100 = "15:55:00" 
end_100 = "16:25:00"

#%% Call Function

#%%% Load Messreihe 20 %

Data_20 = load_Data(pfad, name_20, spalten, start_20, end_20, spalte_zeit=name_time_column)

QU_T_IN_mean_20 = Data_20['HM_QU__HM_PT_T_IN'].mean()         # in °C
QU_T_OUT_mean_20 = Data_20['HM_QU__HM_PT_T_OUT'].mean()       # in °C
SE_T_IN_mean_20 = Data_20['HM_SE__HM_PT_T_IN'].mean()         # in °C
SE_T_OUT_mean_20 = Data_20['HM_SE__HM_PT_T_OUT'].mean()       # in °C
Eco_T_Senke_In.append(Data_20['EcoPrimCircInTemp'].mean())
Eco_T_Senke_Out.append(Data_20['EcoPrimCircOutTemp'].mean())
Eco_T_Quelle_In.append(Data_20['EcoSecCircInTemp'].mean())
Eco_T_Quelle_Out.append(Data_20['EcoSecCircOutTemp'].mean())
QU_Vdot_mean_20 = Data_20['DurchflussQuelleVAR'].mean()            # in m³/h
SE_Vdot_mean_20 = Data_20['DurchflussSenkeVAR'].mean()             # in m³/h
Pel_mean_20 = Data_20['56P1_WLeistungGes'].mean() /1000                  # kW

deltaT_SE_20 = SE_T_IN_mean_20 - SE_T_OUT_mean_20                  # Temp. Diff. in K
deltaT_QU_20 = QU_T_OUT_mean_20 - QU_T_IN_mean_20                  # Temp. Diff. in K
Qdot_SE_20 = SE_Vdot_mean_20/3600 * rho_SE * cp_SE * deltaT_SE_20 /1000         # thermische Leistung in kW
Qdot_QU_20 = QU_Vdot_mean_20/3600 * rho_QU * cp_QU * deltaT_QU_20 /1000         # thermische Leistung in kW
COP_20 = Qdot_SE_20/Pel_mean_20
Qdot_KW_20 = Qdot_SE_20-Qdot_QU_20
Pth_KW.append(Qdot_KW_20)
COP_B0W35.append(COP_20)
Pth_B0W35.append(Qdot_SE_20)
Pel_B0W35.append(Pel_mean_20)
comp_ref_COP.append(20)
T_Senke_In.append(SE_T_IN_mean_20)
T_Senke_Out.append(SE_T_OUT_mean_20)
T_Quelle_In.append(QU_T_IN_mean_20)
T_Quelle_Out.append(QU_T_OUT_mean_20)
Vdot_QU.append(QU_Vdot_mean_20)
Vdot_Senke.append(SE_Vdot_mean_20)

Data_20.plot(x='Timestep', y=['HM_QU__HM_PT_T_IN','HM_QU__HM_PT_T_OUT', 'HM_SE__HM_PT_T_IN','HM_SE__HM_PT_T_OUT'])
plt.xlabel('Zeit t in s')
plt.ylabel(r'Temperatur $\vartheta$ in °C')
plt.ylim(-5, 38)
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend(['Temp. Quelle Ein', 'Temp. Quelle Aus', 'Temp. Senke Ein', 'Temp. Senke Aus'])
plt.title('B0W35 Verdichterdrehzahl: 20% \n Temperaturverlauf', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

print("="*50)
print("B0W35, Verichterdrehzahl: 20%")
print("="*50)
print("Senke")
print("-"*20)
print("Soll VL = 35 °C")
print(f"Ist VL  = {SE_T_IN_mean_20:.2f} °C")
print("Soll RL = 30 °C")
print(f"Ist RL  = {SE_T_OUT_mean_20:.2f} °C")
print("-"*50)
print("Quelle")
print("-"*20)
print("Soll VL = -3 °C")
print(f"Ist VL  = {QU_T_IN_mean_20:.2f} °C")
print("Soll RL = 0 °C")
print(f"Ist RL  = {QU_T_OUT_mean_20:.2f} °C")

#%%% Load Messreihe 25 %

Data_25 = load_Data(pfad, name_25, spalten, start_25, end_25, spalte_zeit=name_time_column)

QU_T_IN_mean_25 = Data_25['HM_QU__HM_PT_T_IN'].mean()         # in °C
QU_T_OUT_mean_25 = Data_25['HM_QU__HM_PT_T_OUT'].mean()       # in °C
SE_T_IN_mean_25 = Data_25['HM_SE__HM_PT_T_IN'].mean()         # in °C
SE_T_OUT_mean_25 = Data_25['HM_SE__HM_PT_T_OUT'].mean()       # in °C
Eco_T_Senke_In.append(Data_25['EcoPrimCircInTemp'].mean())
Eco_T_Senke_Out.append(Data_25['EcoPrimCircOutTemp'].mean())
Eco_T_Quelle_In.append(Data_25['EcoSecCircInTemp'].mean())
Eco_T_Quelle_Out.append(Data_25['EcoSecCircOutTemp'].mean())
QU_Vdot_mean_25 = Data_25['DurchflussQuelleVAR'].mean()            # in m³/h
SE_Vdot_mean_25 = Data_25['DurchflussSenkeVAR'].mean()             # in m³/h
Pel_mean_25 = Data_25['56P1_WLeistungGes'].mean() /1000                 # kW

deltaT_SE_25 = SE_T_IN_mean_25 - SE_T_OUT_mean_25                  # Temp. Diff. in K
deltaT_QU_25 = QU_T_OUT_mean_25 - QU_T_IN_mean_25                  # Temp. Diff. in K
Qdot_SE_25 = (SE_Vdot_mean_25/3600 * rho_SE * cp_SE * deltaT_SE_25) /1000         # thermische Leistung in kW
Qdot_QU_25 = QU_Vdot_mean_25/3600 * rho_QU * cp_QU * deltaT_QU_25 /1000         # thermische Leistung in kW
COP_25 = Qdot_SE_25/Pel_mean_25
Qdot_KW_25 = Qdot_SE_25-Qdot_QU_25
Pth_KW.append(Qdot_KW_25)
COP_B0W35.append(COP_25)
Pth_B0W35.append(Qdot_SE_25)
Pel_B0W35.append(Pel_mean_25)
comp_ref_COP.append(25)
T_Senke_In.append(SE_T_IN_mean_25)
T_Senke_Out.append(SE_T_OUT_mean_25)
T_Quelle_In.append(QU_T_IN_mean_25)
T_Quelle_Out.append(QU_T_OUT_mean_25)
Vdot_QU.append(QU_Vdot_mean_25)
Vdot_Senke.append(SE_Vdot_mean_25)

Data_25.plot(x='Timestep', y=['HM_QU__HM_PT_T_IN','HM_QU__HM_PT_T_OUT', 'HM_SE__HM_PT_T_IN','HM_SE__HM_PT_T_OUT'])
plt.xlabel('Zeit t in s')
plt.ylabel(r'Temperatur $\vartheta$ in °C')
plt.ylim(-5, 38)
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend(['Temp. Quelle Ein', 'Temp. Quelle Aus', 'Temp. Senke Ein', 'Temp. Senke Aus'])
plt.title('B0W35 Verdichterdrehzahl: 25% \n Temperaturverlauf', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

print("="*50)
print("B0W35, Verichterdrehzahl: 25%")
print("="*50)
print("Senke")
print("-"*20)
print("Soll VL = 35 °C")
print(f"Ist VL  = {SE_T_IN_mean_25:.2f} °C")
print("Soll RL = 30 °C")
print(f"Ist RL  = {SE_T_OUT_mean_25:.2f} °C")
print("-"*50)
print("Quelle")
print("-"*20)
print("Soll VL = -3 °C")
print(f"Ist VL  = {QU_T_IN_mean_25:.2f} °C")
print("Soll RL = 0 °C")
print(f"Ist RL  = {QU_T_OUT_mean_25:.2f} °C")

#%%% Load Messreihe 30 %

Data_30 = load_Data(pfad, name_30, spalten, start_30, end_30, spalte_zeit=name_time_column)

QU_T_IN_mean_30 = Data_30['HM_QU__HM_PT_T_IN'].mean()         # in °C
QU_T_OUT_mean_30 = Data_30['HM_QU__HM_PT_T_OUT'].mean()       # in °C
SE_T_IN_mean_30 = Data_30['HM_SE__HM_PT_T_IN'].mean()         # in °C
SE_T_OUT_mean_30 = Data_30['HM_SE__HM_PT_T_OUT'].mean()       # in °C
Eco_T_Senke_In.append(Data_30['EcoPrimCircInTemp'].mean())
Eco_T_Senke_Out.append(Data_30['EcoPrimCircOutTemp'].mean())
Eco_T_Quelle_In.append(Data_30['EcoSecCircInTemp'].mean())
Eco_T_Quelle_Out.append(Data_30['EcoSecCircOutTemp'].mean())
QU_Vdot_mean_30 = Data_30['DurchflussQuelleVAR'].mean()            # in m³/h
SE_Vdot_mean_30 = Data_30['DurchflussSenkeVAR'].mean()             # in m³/h
Pel_mean_30 = Data_30['56P1_WLeistungGes'].mean() /1000                 # kW

deltaT_SE_30 = SE_T_IN_mean_30 - SE_T_OUT_mean_30                  # Temp. Diff. in K
deltaT_QU_30 = QU_T_OUT_mean_30 - QU_T_IN_mean_30                  # Temp. Diff. in K
Qdot_SE_30 = SE_Vdot_mean_30/3600 * rho_SE * cp_SE * deltaT_SE_30 /1000         # thermische Leistung in kW
Qdot_QU_30 = QU_Vdot_mean_30/3600 * rho_QU * cp_QU * deltaT_QU_30 /1000         # thermische Leistung in kW
COP_30 = Qdot_SE_30/Pel_mean_30
Qdot_KW_30 = Qdot_SE_30-Qdot_QU_30
Pth_KW.append(Qdot_KW_30)
COP_B0W35.append(COP_30)
Pth_B0W35.append(Qdot_SE_30)
Pel_B0W35.append(Pel_mean_30)
comp_ref_COP.append(30)
T_Senke_In.append(SE_T_IN_mean_30)
T_Senke_Out.append(SE_T_OUT_mean_30)
T_Quelle_In.append(QU_T_IN_mean_30)
T_Quelle_Out.append(QU_T_OUT_mean_30)
Vdot_QU.append(QU_Vdot_mean_30)
Vdot_Senke.append(SE_Vdot_mean_30)

Data_30.plot(x='Timestep', y=['HM_QU__HM_PT_T_IN','HM_QU__HM_PT_T_OUT', 'HM_SE__HM_PT_T_IN','HM_SE__HM_PT_T_OUT'])
plt.xlabel('Zeit t in s')
plt.ylabel(r'Temperatur $\vartheta$ in °C')
plt.ylim(-5, 38)
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend(['Temp. Quelle Ein', 'Temp. Quelle Aus', 'Temp. Senke Ein', 'Temp. Senke Aus'])
plt.title('B0W35 Verdichterdrehzahl: 30% \n Temperaturverlauf', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

print("="*50)
print("B0W35, Verichterdrehzahl: 30%")
print("="*50)
print("Senke")
print("-"*20)
print("Soll VL = 35 °C")
print(f"Ist VL  = {SE_T_IN_mean_30:.2f} °C")
print("Soll RL = 30 °C")
print(f"Ist RL  = {SE_T_OUT_mean_30:.2f} °C")
print("-"*50)
print("Quelle")
print("-"*20)
print("Soll VL = -3 °C")
print(f"Ist VL  = {QU_T_IN_mean_30:.2f} °C")
print("Soll RL = 0 °C")
print(f"Ist RL  = {QU_T_OUT_mean_30:.2f} °C")

#%%% Load Messreihe 40 %

Data_40 = load_Data(pfad, name_40, spalten, start_40, end_40, spalte_zeit=name_time_column)

QU_T_IN_mean_40 = Data_40['HM_QU__HM_PT_T_IN'].mean()         # in °C
QU_T_OUT_mean_40 = Data_40['HM_QU__HM_PT_T_OUT'].mean()       # in °C
SE_T_IN_mean_40 = Data_40['HM_SE__HM_PT_T_IN'].mean()         # in °C
SE_T_OUT_mean_40 = Data_40['HM_SE__HM_PT_T_OUT'].mean()       # in °C
Eco_T_Senke_In.append(Data_40['EcoPrimCircInTemp'].mean())
Eco_T_Senke_Out.append(Data_40['EcoPrimCircOutTemp'].mean())
Eco_T_Quelle_In.append(Data_40['EcoSecCircInTemp'].mean())
Eco_T_Quelle_Out.append(Data_40['EcoSecCircOutTemp'].mean())
QU_Vdot_mean_40 = Data_40['DurchflussQuelleVAR'].mean()            # in m³/h
SE_Vdot_mean_40 = Data_40['DurchflussSenkeVAR'].mean()             # in m³/h
Pel_mean_40 = Data_40['56P1_WLeistungGes'].mean() /1000                  # kW

deltaT_SE_40 = SE_T_IN_mean_40 - SE_T_OUT_mean_40                  # Temp. Diff. in K
deltaT_QU_40 = QU_T_OUT_mean_40 - QU_T_IN_mean_40                  # Temp. Diff. in K
Qdot_SE_40 = SE_Vdot_mean_40/3600 * rho_SE * cp_SE * deltaT_SE_40 /1000         # thermische Leistung in kW
Qdot_QU_40 = QU_Vdot_mean_40/3600 * rho_QU * cp_QU * deltaT_QU_40 /1000         # thermische Leistung in kW
COP_40 = Qdot_SE_40/Pel_mean_40
Qdot_KW_40 = Qdot_SE_40-Qdot_QU_40
Pth_KW.append(Qdot_KW_40)
COP_B0W35.append(COP_40)
Pth_B0W35.append(Qdot_SE_40)
Pel_B0W35.append(Pel_mean_40)
comp_ref_COP.append(40)
T_Senke_In.append(SE_T_IN_mean_40)
T_Senke_Out.append(SE_T_OUT_mean_40)
T_Quelle_In.append(QU_T_IN_mean_40)
T_Quelle_Out.append(QU_T_OUT_mean_40)
Vdot_QU.append(QU_Vdot_mean_40)
Vdot_Senke.append(SE_Vdot_mean_40)

Data_40.plot(x='Timestep', y=['HM_QU__HM_PT_T_IN','HM_QU__HM_PT_T_OUT', 'HM_SE__HM_PT_T_IN','HM_SE__HM_PT_T_OUT'])
plt.xlabel('Zeit t in s')
plt.ylabel(r'Temperatur $\vartheta$ in °C')
plt.ylim(-5, 38)
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend(['Temp. Quelle Ein', 'Temp. Quelle Aus', 'Temp. Senke Ein', 'Temp. Senke Aus'])
plt.title('B0W35 Verdichterdrehzahl: 40% \n Temperaturverlauf', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

print("="*50)
print("B0W35, Verichterdrehzahl: 40%")
print("="*50)
print("Senke")
print("-"*20)
print("Soll VL = 35 °C")
print(f"Ist VL  = {SE_T_IN_mean_40:.2f} °C")
print("Soll RL = 30 °C")
print(f"Ist RL  = {SE_T_OUT_mean_40:.2f} °C")
print("-"*50)
print("Quelle")
print("-"*20)
print("Soll VL = -3 °C")
print(f"Ist VL  = {QU_T_IN_mean_40:.2f} °C")
print("Soll RL = 0 °C")
print(f"Ist RL  = {QU_T_OUT_mean_40:.2f} °C")

#%%% Load Messreihe 50 %

Data_50 = load_Data(pfad, name_50, spalten, start_50, end_50, spalte_zeit=name_time_column)

QU_T_IN_mean_50 = Data_50['HM_QU__HM_PT_T_IN'].mean()         # in °C
QU_T_OUT_mean_50 = Data_50['HM_QU__HM_PT_T_OUT'].mean()       # in °C
SE_T_IN_mean_50 = Data_50['HM_SE__HM_PT_T_IN'].mean()         # in °C
SE_T_OUT_mean_50 = Data_50['HM_SE__HM_PT_T_OUT'].mean()       # in °C
Eco_T_Senke_In.append(Data_50['EcoPrimCircInTemp'].mean())
Eco_T_Senke_Out.append(Data_50['EcoPrimCircOutTemp'].mean())
Eco_T_Quelle_In.append(Data_50['EcoSecCircInTemp'].mean())
Eco_T_Quelle_Out.append(Data_50['EcoSecCircOutTemp'].mean())
QU_Vdot_mean_50 = Data_50['DurchflussQuelleVAR'].mean()            # in m³/h
SE_Vdot_mean_50 = Data_50['DurchflussSenkeVAR'].mean()             # in m³/h
Pel_mean_50 = Data_50['56P1_WLeistungGes'].mean() /1000                 # kW

deltaT_SE_50 = SE_T_IN_mean_50 - SE_T_OUT_mean_50                  # Temp. Diff. in K
deltaT_QU_50 = QU_T_OUT_mean_50 - QU_T_IN_mean_50                  # Temp. Diff. in K
Qdot_SE_50 = SE_Vdot_mean_50/3600 * rho_SE * cp_SE * deltaT_SE_50 /1000         # thermische Leistung in kW
Qdot_QU_50 = QU_Vdot_mean_50/3600 * rho_QU * cp_QU * deltaT_QU_50 /1000         # thermische Leistung in kW
COP_50 = Qdot_SE_50/Pel_mean_50
Qdot_KW_50 = Qdot_SE_50-Qdot_QU_50
Pth_KW.append(Qdot_KW_50)
COP_B0W35.append(COP_50)
Pth_B0W35.append(Qdot_SE_50)
Pel_B0W35.append(Pel_mean_50)
comp_ref_COP.append(50)
T_Senke_In.append(SE_T_IN_mean_50)
T_Senke_Out.append(SE_T_OUT_mean_50)
T_Quelle_In.append(QU_T_IN_mean_50)
T_Quelle_Out.append(QU_T_OUT_mean_50)
Vdot_QU.append(QU_Vdot_mean_50)
Vdot_Senke.append(SE_Vdot_mean_50)

Data_50.plot(x='Timestep', y=['HM_QU__HM_PT_T_IN','HM_QU__HM_PT_T_OUT', 'HM_SE__HM_PT_T_IN','HM_SE__HM_PT_T_OUT'])
plt.xlabel('Zeit t in s')
plt.ylabel(r'Temperatur $\vartheta$ in °C')
plt.ylim(-5, 38)
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend(['Temp. Quelle Ein', 'Temp. Quelle Aus', 'Temp. Senke Ein', 'Temp. Senke Aus'])
plt.title('B0W35 Verdichterdrehzahl: 50% \n Temperaturverlauf', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

print("="*50)
print("B0W35, Verichterdrehzahl: 50%")
print("="*50)
print("Senke")
print("-"*20)
print("Soll VL = 35 °C")
print(f"Ist VL  = {SE_T_IN_mean_50:.2f} °C")
print("Soll RL = 30 °C")
print(f"Ist RL  = {SE_T_OUT_mean_50:.2f} °C")
print("-"*50)
print("Quelle")
print("-"*20)
print("Soll VL = -3 °C")
print(f"Ist VL  = {QU_T_IN_mean_50:.2f} °C")
print("Soll RL = 0 °C")
print(f"Ist RL  = {QU_T_OUT_mean_50:.2f} °C")

#%%% Load Messreihe 60 %

Data_60 = load_Data(pfad, name_60, spalten, start_60, end_60, spalte_zeit=name_time_column)

QU_T_IN_mean_60 = Data_60['HM_QU__HM_PT_T_IN'].mean()         # in °C
QU_T_OUT_mean_60 = Data_60['HM_QU__HM_PT_T_OUT'].mean()       # in °C
SE_T_IN_mean_60 = Data_60['HM_SE__HM_PT_T_IN'].mean()         # in °C
SE_T_OUT_mean_60 = Data_60['HM_SE__HM_PT_T_OUT'].mean()       # in °C
Eco_T_Senke_In.append(Data_60['EcoPrimCircInTemp'].mean())
Eco_T_Senke_Out.append(Data_60['EcoPrimCircOutTemp'].mean())
Eco_T_Quelle_In.append(Data_60['EcoSecCircInTemp'].mean())
Eco_T_Quelle_Out.append(Data_60['EcoSecCircOutTemp'].mean())
QU_Vdot_mean_60 = Data_60['DurchflussQuelleVAR'].mean()            # in m³/h
SE_Vdot_mean_60 = Data_60['DurchflussSenkeVAR'].mean()             # in m³/h
Pel_mean_60 = Data_60['56P1_WLeistungGes'].mean() /1000                 # kW

deltaT_SE_60 = SE_T_IN_mean_60 - SE_T_OUT_mean_60                  # Temp. Diff. in K
deltaT_QU_60 = QU_T_OUT_mean_60 - QU_T_IN_mean_60                  # Temp. Diff. in K
Qdot_SE_60 = SE_Vdot_mean_60/3600 * rho_SE * cp_SE * deltaT_SE_60 /1000         # thermische Leistung in kW
Qdot_QU_60 = QU_Vdot_mean_60/3600 * rho_QU * cp_QU * deltaT_QU_60 /1000         # thermische Leistung in kW
COP_60 = Qdot_SE_60/Pel_mean_60
Qdot_KW_60 = Qdot_SE_60-Qdot_QU_60
Pth_KW.append(Qdot_KW_60)
COP_B0W35.append(COP_60)
Pth_B0W35.append(Qdot_SE_60)
Pel_B0W35.append(Pel_mean_60)
comp_ref_COP.append(60)
T_Senke_In.append(SE_T_IN_mean_60)
T_Senke_Out.append(SE_T_OUT_mean_60)
T_Quelle_In.append(QU_T_IN_mean_60)
T_Quelle_Out.append(QU_T_OUT_mean_60)
Vdot_QU.append(QU_Vdot_mean_60)
Vdot_Senke.append(SE_Vdot_mean_60)

Data_60.plot(x='Timestep', y=['HM_QU__HM_PT_T_IN','HM_QU__HM_PT_T_OUT', 'HM_SE__HM_PT_T_IN','HM_SE__HM_PT_T_OUT'])
plt.xlabel('Zeit t in s')
plt.ylabel(r'Temperatur $\vartheta$ in °C')
plt.ylim(-5, 38)
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend(['Temp. Quelle Ein', 'Temp. Quelle Aus', 'Temp. Senke Ein', 'Temp. Senke Aus'])
plt.title('B0W35 Verdichterdrehzahl: 60% \n Temperaturverlauf', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

print("="*50)
print("B0W35, Verichterdrehzahl: 60%")
print("="*50)
print("Senke")
print("-"*20)
print("Soll VL = 35 °C")
print(f"Ist VL  = {SE_T_IN_mean_60:.2f} °C")
print("Soll RL = 30 °C")
print(f"Ist RL  = {SE_T_OUT_mean_60:.2f} °C")
print("-"*50)
print("Quelle")
print("-"*20)
print("Soll VL = -3 °C")
print(f"Ist VL  = {QU_T_IN_mean_60:.2f} °C")
print("Soll RL = 0 °C")
print(f"Ist RL  = {QU_T_OUT_mean_60:.2f} °C")

#%%% Load Messreihe 70 %

Data_70 = load_Data(pfad, name_70, spalten, start_70, end_70, spalte_zeit=name_time_column)

QU_T_IN_mean_70 = Data_70['HM_QU__HM_PT_T_IN'].mean()         # in °C
QU_T_OUT_mean_70 = Data_70['HM_QU__HM_PT_T_OUT'].mean()       # in °C
SE_T_IN_mean_70 = Data_70['HM_SE__HM_PT_T_IN'].mean()         # in °C
SE_T_OUT_mean_70 = Data_70['HM_SE__HM_PT_T_OUT'].mean()       # in °C
Eco_T_Senke_In.append(Data_70['EcoPrimCircInTemp'].mean())
Eco_T_Senke_Out.append(Data_70['EcoPrimCircOutTemp'].mean())
Eco_T_Quelle_In.append(Data_70['EcoSecCircInTemp'].mean())
Eco_T_Quelle_Out.append(Data_70['EcoSecCircOutTemp'].mean())
QU_Vdot_mean_70 = Data_70['DurchflussQuelleVAR'].mean()            # in m³/h
SE_Vdot_mean_70 = Data_70['DurchflussSenkeVAR'].mean()             # in m³/h
Pel_mean_70 = Data_70['56P1_WLeistungGes'].mean() /1000                 # kW

deltaT_SE_70 = SE_T_IN_mean_70 - SE_T_OUT_mean_70                  # Temp. Diff. in K
deltaT_QU_70 = QU_T_OUT_mean_70 - QU_T_IN_mean_70                  # Temp. Diff. in K
Qdot_SE_70 = SE_Vdot_mean_70/3600 * rho_SE * cp_SE * deltaT_SE_70 /1000         # thermische Leistung in kW
Qdot_QU_70 = QU_Vdot_mean_70/3600 * rho_QU * cp_QU * deltaT_QU_70 /1000         # thermische Leistung in kW
COP_70 = Qdot_SE_70/Pel_mean_70
Qdot_KW_70 = Qdot_SE_70-Qdot_QU_70
Pth_KW.append(Qdot_KW_70)
COP_B0W35.append(COP_70)
Pth_B0W35.append(Qdot_SE_70)
Pel_B0W35.append(Pel_mean_70)
comp_ref_COP.append(70)
T_Senke_In.append(SE_T_IN_mean_70)
T_Senke_Out.append(SE_T_OUT_mean_70)
T_Quelle_In.append(QU_T_IN_mean_70)
T_Quelle_Out.append(QU_T_OUT_mean_70)
Vdot_QU.append(QU_Vdot_mean_70)
Vdot_Senke.append(SE_Vdot_mean_70)

Data_70.plot(x='Timestep', y=['HM_QU__HM_PT_T_IN','HM_QU__HM_PT_T_OUT', 'HM_SE__HM_PT_T_IN','HM_SE__HM_PT_T_OUT'])
plt.xlabel('Zeit t in s')
plt.ylabel(r'Temperatur $\vartheta$ in °C')
plt.ylim(-5, 38)
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend(['Temp. Quelle Ein', 'Temp. Quelle Aus', 'Temp. Senke Ein', 'Temp. Senke Aus'])
plt.title('B0W35 Verdichterdrehzahl: 70% \n Temperaturverlauf', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

print("="*50)
print("B0W35, Verichterdrehzahl: 70%")
print("="*50)
print("Senke")
print("-"*20)
print("Soll VL = 35 °C")
print(f"Ist VL  = {SE_T_IN_mean_70:.2f} °C")
print("Soll RL = 30 °C")
print(f"Ist RL  = {SE_T_OUT_mean_70:.2f} °C")
print("-"*50)
print("Quelle")
print("-"*20)
print("Soll VL = -3 °C")
print(f"Ist VL  = {QU_T_IN_mean_70:.2f} °C")
print("Soll RL = 0 °C")
print(f"Ist RL  = {QU_T_OUT_mean_70:.2f} °C")

#%%% Load Messreihe 80 %

Data_80 = load_Data(pfad, name_80, spalten, start_80, end_80, spalte_zeit=name_time_column)

QU_T_IN_mean_80 = Data_80['HM_QU__HM_PT_T_IN'].mean()         # in °C
QU_T_OUT_mean_80 = Data_80['HM_QU__HM_PT_T_OUT'].mean()       # in °C
SE_T_IN_mean_80 = Data_80['HM_SE__HM_PT_T_IN'].mean()         # in °C
SE_T_OUT_mean_80 = Data_80['HM_SE__HM_PT_T_OUT'].mean()       # in °C
Eco_T_Senke_In.append(Data_80['EcoPrimCircInTemp'].mean())
Eco_T_Senke_Out.append(Data_80['EcoPrimCircOutTemp'].mean())
Eco_T_Quelle_In.append(Data_80['EcoSecCircInTemp'].mean())
Eco_T_Quelle_Out.append(Data_80['EcoSecCircOutTemp'].mean())
QU_Vdot_mean_80 = Data_80['DurchflussQuelleVAR'].mean()            # in m³/h
SE_Vdot_mean_80 = Data_80['DurchflussSenkeVAR'].mean()             # in m³/h
Pel_mean_80 = Data_80['56P1_WLeistungGes'].mean() /1000                 # kW

deltaT_SE_80 = SE_T_IN_mean_80 - SE_T_OUT_mean_80                  # Temp. Diff. in K
deltaT_QU_80 = QU_T_OUT_mean_80 - QU_T_IN_mean_80                  # Temp. Diff. in K
Qdot_SE_80 = SE_Vdot_mean_80/3600 * rho_SE * cp_SE * deltaT_SE_80 /1000         # thermische Leistung in kW
Qdot_QU_80 = QU_Vdot_mean_80/3600 * rho_QU * cp_QU * deltaT_QU_80 /1000         # thermische Leistung in kW
COP_80 = Qdot_SE_80/Pel_mean_80
Qdot_KW_80 = Qdot_SE_80-Qdot_QU_80
Pth_KW.append(Qdot_KW_80)
COP_B0W35.append(COP_80)
Pth_B0W35.append(Qdot_SE_80)
Pel_B0W35.append(Pel_mean_80)
comp_ref_COP.append(80)
T_Senke_In.append(SE_T_IN_mean_80)
T_Senke_Out.append(SE_T_OUT_mean_80)
T_Quelle_In.append(QU_T_IN_mean_80)
T_Quelle_Out.append(QU_T_OUT_mean_80)
Vdot_QU.append(QU_Vdot_mean_80)
Vdot_Senke.append(SE_Vdot_mean_80)

Data_80.plot(x='Timestep', y=['HM_QU__HM_PT_T_IN','HM_QU__HM_PT_T_OUT', 'HM_SE__HM_PT_T_IN','HM_SE__HM_PT_T_OUT'])
plt.xlabel('Zeit t in s')
plt.ylabel(r'Temperatur $\vartheta$ in °C')
plt.ylim(-5, 38)
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend(['Temp. Quelle Ein', 'Temp. Quelle Aus', 'Temp. Senke Ein', 'Temp. Senke Aus'])
plt.title('B0W35 Verdichterdrehzahl: 80% \n Temperaturverlauf', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

print("="*50)
print("B0W35, Verichterdrehzahl: 80%")
print("="*50)
print("Senke")
print("-"*20)
print("Soll VL = 35 °C")
print(f"Ist VL  = {SE_T_IN_mean_80:.2f} °C")
print("Soll RL = 30 °C")
print(f"Ist RL  = {SE_T_OUT_mean_80:.2f} °C")
print("-"*50)
print("Quelle")
print("-"*20)
print("Soll VL = -3 °C")
print(f"Ist VL  = {QU_T_IN_mean_80:.2f} °C")
print("Soll RL = 0 °C")
print(f"Ist RL  = {QU_T_OUT_mean_80:.2f} °C")

#%%% Load Messreihe 90 %

Data_90 = load_Data(pfad, name_90, spalten, start_90, end_90, spalte_zeit=name_time_column)

QU_T_IN_mean_90 = Data_90['HM_QU__HM_PT_T_IN'].mean()         # in °C
QU_T_OUT_mean_90 = Data_90['HM_QU__HM_PT_T_OUT'].mean()       # in °C
SE_T_IN_mean_90 = Data_90['HM_SE__HM_PT_T_IN'].mean()         # in °C
SE_T_OUT_mean_90 = Data_90['HM_SE__HM_PT_T_OUT'].mean()       # in °C
Eco_T_Senke_In.append(Data_90['EcoPrimCircInTemp'].mean())
Eco_T_Senke_Out.append(Data_90['EcoPrimCircOutTemp'].mean())
Eco_T_Quelle_In.append(Data_90['EcoSecCircInTemp'].mean())
Eco_T_Quelle_Out.append(Data_90['EcoSecCircOutTemp'].mean())
QU_Vdot_mean_90 = Data_90['DurchflussQuelleVAR'].mean()            # in m³/h
SE_Vdot_mean_90 = Data_90['DurchflussSenkeVAR'].mean()             # in m³/h
Pel_mean_90 = Data_90['56P1_WLeistungGes'].mean() /1000                  # kW

deltaT_SE_90 = SE_T_IN_mean_90 - SE_T_OUT_mean_90                  # Temp. Diff. in K
deltaT_QU_90 = QU_T_OUT_mean_90 - QU_T_IN_mean_90                  # Temp. Diff. in K
Qdot_SE_90 = SE_Vdot_mean_90/3600 * rho_SE * cp_SE * deltaT_SE_90 /1000         # thermische Leistung in kW
Qdot_QU_90 = QU_Vdot_mean_90/3600 * rho_QU * cp_QU * deltaT_QU_90 /1000         # thermische Leistung in kW
COP_90 = Qdot_SE_90/Pel_mean_90
Qdot_KW_90 = Qdot_SE_90-Qdot_QU_90
Pth_KW.append(Qdot_KW_90)
COP_B0W35.append(COP_90)
Pth_B0W35.append(Qdot_SE_90)
Pel_B0W35.append(Pel_mean_90)
comp_ref_COP.append(90)
T_Senke_In.append(SE_T_IN_mean_90)
T_Senke_Out.append(SE_T_OUT_mean_90)
T_Quelle_In.append(QU_T_IN_mean_90)
T_Quelle_Out.append(QU_T_OUT_mean_90)
Vdot_QU.append(QU_Vdot_mean_90)
Vdot_Senke.append(SE_Vdot_mean_90)

Data_90.plot(x='Timestep', y=['HM_QU__HM_PT_T_IN','HM_QU__HM_PT_T_OUT', 'HM_SE__HM_PT_T_IN','HM_SE__HM_PT_T_OUT'])
plt.xlabel('Zeit t in s')
plt.ylabel(r'Temperatur $\vartheta$ in °C')
plt.ylim(-5, 38)
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend(['Temp. Quelle Ein', 'Temp. Quelle Aus', 'Temp. Senke Ein', 'Temp. Senke Aus'])
plt.title('B0W35 Verdichterdrehzahl: 90% \n Temperaturverlauf', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

print("="*50)
print("B0W35, Verichterdrehzahl: 90%")
print("="*50)
print("Senke")
print("-"*20)
print("Soll VL = 35 °C")
print(f"Ist VL  = {SE_T_IN_mean_90:.2f} °C")
print("Soll RL = 30 °C")
print(f"Ist RL  = {SE_T_OUT_mean_90:.2f} °C")
print("-"*50)
print("Quelle")
print("-"*20)
print("Soll VL = -3 °C")
print(f"Ist VL  = {QU_T_IN_mean_90:.2f} °C")
print("Soll RL = 0 °C")
print(f"Ist RL  = {QU_T_OUT_mean_90:.2f} °C")

#%%% Load Messreihe 100 %

Data_100 = load_Data(pfad, name_100, spalten, start_100, end_100, spalte_zeit=name_time_column)

QU_T_IN_mean_100 = Data_100['HM_QU__HM_PT_T_IN'].mean()         # in °C
QU_T_OUT_mean_100 = Data_100['HM_QU__HM_PT_T_OUT'].mean()       # in °C
SE_T_IN_mean_100 = Data_100['HM_SE__HM_PT_T_IN'].mean()         # in °C
SE_T_OUT_mean_100 = Data_100['HM_SE__HM_PT_T_OUT'].mean()       # in °C
Eco_T_Senke_In.append(Data_100['EcoPrimCircInTemp'].mean())
Eco_T_Senke_Out.append(Data_100['EcoPrimCircOutTemp'].mean())
Eco_T_Quelle_In.append(Data_100['EcoSecCircInTemp'].mean())
Eco_T_Quelle_Out.append(Data_100['EcoSecCircOutTemp'].mean())
QU_Vdot_mean_100 = Data_100['DurchflussQuelleVAR'].mean()            # in m³/h
SE_Vdot_mean_100 = Data_100['DurchflussSenkeVAR'].mean()             # in m³/h
Pel_mean_100 = Data_100['56P1_WLeistungGes'].mean() /1000                 # kW

deltaT_SE_100 = SE_T_IN_mean_100 - SE_T_OUT_mean_100                  # Temp. Diff. in K
deltaT_QU_100 = QU_T_OUT_mean_100 - QU_T_IN_mean_100                  # Temp. Diff. in K
Qdot_SE_100 = SE_Vdot_mean_100/3600 * rho_SE * cp_SE * deltaT_SE_100 /1000         # thermische Leistung in kW
Qdot_QU_100 = QU_Vdot_mean_100/3600 * rho_QU * cp_QU * deltaT_QU_100 /1000         # thermische Leistung in kW
COP_100 = Qdot_SE_100/Pel_mean_100
Qdot_KW_100 = Qdot_SE_100-Qdot_QU_100
Pth_KW.append(Qdot_KW_100)
COP_B0W35.append(COP_100)
Pth_B0W35.append(Qdot_SE_100)
Pel_B0W35.append(Pel_mean_100)
comp_ref_COP.append(100)
T_Senke_In.append(SE_T_IN_mean_100)
T_Senke_Out.append(SE_T_OUT_mean_100)
T_Quelle_In.append(QU_T_IN_mean_100)
T_Quelle_Out.append(QU_T_OUT_mean_100)
Vdot_QU.append(QU_Vdot_mean_100)
Vdot_Senke.append(SE_Vdot_mean_100)

Data_100.plot(x='Timestep', y=['HM_QU__HM_PT_T_IN','HM_QU__HM_PT_T_OUT', 'HM_SE__HM_PT_T_IN','HM_SE__HM_PT_T_OUT'])
plt.xlabel('Zeit t in s')
plt.ylabel(r'Temperatur $\vartheta$ in °C')
plt.ylim(-5, 38)
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend(['Temp. Quelle Ein', 'Temp. Quelle Aus', 'Temp. Senke Ein', 'Temp. Senke Aus'])
plt.title('B0W35 Verdichterdrehzahl: 100% \n Temperaturverlauf', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

print("="*50)
print("B0W35, Verichterdrehzahl: 100%")
print("="*50)
print("Senke")
print("-"*20)
print("Soll VL = 35 °C")
print(f"Ist VL  = {SE_T_IN_mean_100:.2f} °C")
print("Soll RL = 30 °C")
print(f"Ist RL  = {SE_T_OUT_mean_100:.2f} °C")
print("-"*50)
print("Quelle")
print("-"*20)
print("Soll VL = -3 °C")
print(f"Ist VL  = {QU_T_IN_mean_100:.2f} °C")
print("Soll RL = 0 °C")
print(f"Ist RL  = {QU_T_OUT_mean_100:.2f} °C")

#%% Results over Comp. Ref.

#%%% COP Kennlinie
plt.plot(comp_ref_COP, COP_B0W35, 
         color='green', 
         linestyle='--',
         marker='x',
         markersize=10,
         linewidth=1.5,
         label='B0W35 Messung')
plt.plot(comp_ref_Datasheet_COP, COP_B0W35_Datasheet,
         color='blue', 
         linestyle='-',
         linewidth=1.5,
         label='B0W35 Datenblatt')
plt.xlabel('Verdichtersrehzahl in %')
plt.ylabel('COP')
plt.ylim(2, 7)
plt.xlim(10, 100)
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend()
# plt.title('Betriebskurve COP', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

#%%% Thermische Leistung Kennlinie
plt.plot(comp_ref_COP, Pth_B0W35, 
         color='green', 
         linestyle='--',
         marker='x',
         markersize=10,
         linewidth=1.5,
         label='B0W35 Messung')
plt.plot(comp_ref_Datasheet_Pth, Pth_B0W35_Datasheet,
         color='blue', 
         linestyle='-',
         linewidth=1.5,
         label='B0W35 Datenblatt')
plt.xlabel('Verdichtersrehzahl in %')
plt.ylabel('Thermische Leistung in kW')
plt.ylim(0.0, 8.0)
plt.xlim(10, 100)
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend()
# plt.title('Betriebskurve Heizleistung', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

#%%% Elektrische Leistung Kennlinie
plt.plot(comp_ref_COP, Pel_B0W35, 
         color='green', 
         linestyle='--',
         marker='x',
         markersize=10,
         linewidth=1.5,
         label='B0W35 Messung')
# plt.plot(comp_ref_COP, Pth_KW, 
#          color='red', 
#          linestyle='--',
#          marker='o',
#          markersize=10,
#          linewidth=1.5,
#          label='P_th Kaltwassernetz')
plt.plot(comp_ref_Datasheet_Pel, Pel_B0W35_Datasheet,
         color='blue', 
         linestyle='-',
         linewidth=1.5,
         label='B0W35 Datenblatt')
plt.xlabel('Verdichtersrehzahl in %')
plt.ylabel('Elektrische Leistung in kW')
plt.ylim(0.0, 2.0)
plt.xlim(10, 100)
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend()
# plt.title('Betriebskurve elektrischer Verbrauch', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

#%%% Mittlerer Temperaturverlauf

plt.plot(comp_ref_COP, T_Senke_In, 
         color='darkred', 
         linestyle='--',
         marker='s',
         markersize=3,
         linewidth=1,
         label='Senke VL')
plt.plot(comp_ref_COP, Eco_T_Quelle_Out, 
         color='darkred', 
         linestyle='--',
         marker='x',
         markersize=5,
         linewidth=1,
         label='Eco Senke VL')
plt.plot(comp_ref_COP, T_Senke_Out, 
         color='red', 
         linestyle='--',
         marker='s',
         markersize=3,
         linewidth=1,
         label='Senke RL')
plt.plot(comp_ref_COP, Eco_T_Quelle_In, 
         color='red', 
         linestyle='--',
         marker='x',
         markersize=5,
         linewidth=1,
         label='Eco Senke RL')
plt.xlabel('Verdichtersrehzahl in %')
plt.ylabel('Temperatur in °C')
plt.ylim(29.5, 35.5)
plt.xlim(10, 100)
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend()
# plt.title('Gemittelter Temperaturverlauf über Verdichterdrehzahl', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

plt.plot(comp_ref_COP, T_Quelle_In, 
         color='darkblue', 
         linestyle='--',
         marker='s',
         markersize=3,
         linewidth=1,
         label='Quelle VL')
plt.plot(comp_ref_COP, Eco_T_Senke_Out, 
         color='darkblue', 
         linestyle='--',
         marker='x',
         markersize=5,
         linewidth=1,
         label='Eco Quelle VL')
plt.plot(comp_ref_COP, T_Quelle_Out, 
         color='blue', 
         linestyle='--',
         marker='s',
         markersize=3,
         linewidth=1,
         label='Quelle RL')
plt.plot(comp_ref_COP, Eco_T_Senke_In, 
         color='blue', 
         linestyle='--',
         marker='x',
         markersize=5,
         linewidth=1,
         label='Eco Quelle RL')
plt.xlabel('Verdichtersrehzahl in %')
plt.ylabel('Temperatur in °C')
plt.ylim(-4.5, 1.5)
plt.xlim(10, 100)
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend()
# plt.title('Gemittelter Temperaturverlauf über Verdichterdrehzahl', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

#%%% Mittlerer Volumenstromverlauf

plt.plot(comp_ref_COP, Vdot_Senke, 
         color='orange', 
         linestyle='--',
         marker='s',
         markersize=3,
         linewidth=1,
         label='Senke')
plt.plot(comp_ref_COP, Vdot_QU, 
         color='green', 
         linestyle='--',
         marker='s',
         markersize=3,
         linewidth=1,
         label='Quelle')
plt.xlabel('Verdichtersrehzahl in %')
plt.ylabel('Volumenstrom in m³/h')
plt.ylim(0, 1)
plt.xlim(10, 100)
plt.minorticks_on()
plt.grid(visible=True, which='major', color='#666666', linestyle='-', alpha=0.6)
plt.grid(visible=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.4)
plt.legend()
plt.title('Gemittelter Volumenstromverlauf', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show