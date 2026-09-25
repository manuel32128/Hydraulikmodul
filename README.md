# Hydraulikmodul – Python-Skripte

Begleitcode zur Master-Thesis „Inbetriebnahme, regelungstechnische Auslegung und
Validierung eines Hydraulikmoduls zur Vermessung von Wärmepumpen“
(M. Sütterlin, Hochschule Offenburg, 2026).

## Inhalt
- `Reglerauslegung_def.py`: Funktionen zur Auswertung von Sprungantworten und Berechnung der
  PI-Reglerparameter nach dem T-Summen-Verfahren nach Kuhn.
- `Auswertung_B0W35.py`: Mittelwertbildung der Messdaten sowie Berechnung von
  thermischer Leistung und COP je Messpunkt.
- `SprungantwortAuswertung_xxx.py`: Aufruf der Funktion aus `Reglerauslegung_def.py` und Auswertung
  der einzelnen Spungantworten für die spezifischen Regelstrecken.

## Messdaten
Der Ordner `messdaten` enthält die exportierten Messreihen der Validierungsmessung
im Betriebspunkt B0W35 (Verdichterdrehzahl 20–100 %) sowie die Sprungantwortversuche
zur Reglerparametrierung.

## Voraussetzungen
Python 3 mit den Paketen `numpy`, `pandas` und `matplotlib`.
