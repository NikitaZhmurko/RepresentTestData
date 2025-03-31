# RepresentTestData 
Kleine Programmier-Aufgabe: Einlesen von Teststands-Dateien.
Hintergrund / Motivation: Von Prüfständen / Messaufbauten erzeugte Ergebnisse werden in unterschiedlichen Formaten und unterschiedlichen Strukturen gespeichert. Um diese Ergebnisse sinnvoll nutzen zu können müssen die Daten in eine sinnvolle Form gebracht werden. Nur so lassen sie sich optimal speichern, beispielsweise in einer Datenbank, und weiterverarbeiten.
Ein Beispiel hierfür ist die gegebene Datei eines Teststands.
Aufgabe Für diese Datei soll ein Python-Skript/Funktion geschrieben werden, welches die erzeugten Dateien einliest und strukturiert.
Die Python-Funktion soll
- Die .csv-Dateien einlesen
- Die enthaltenen Messdaten und Metadaten (die den Test beschreibenden allgemeine Informationen in den ersten Zeilen wie Name, Kommentare, …) in eine sinnvolle Struktur bringen (bspw. durch Gruppierung zusammengehörender Daten mit passendem Variablentyp)
- die strukturierten Daten in einem geeigneten Format zurückgeben (bspw. pandas DataFrame oä.)
Bonus / optional: Sinnvolle Darstellung der Daten in einer Web-App (gerne Plotly Dash, kein Hosting, lokal zu starten)
