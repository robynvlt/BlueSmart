# Vorgabe für eine neue Spielgrundlage

Bei einer Anfrage wie „Baue die Grundlage für ein Spiel“ ist ein vollständiges, direkt einsetzbares BlueJ-Grundgerüst gewünscht. Liefere alle benötigten Klassen mit exakten Dateinamen, Einstiegskonstruktor, erforderlichen Bibliotheksdateien beziehungsweise eindeutigen Bezugsangaben und einer kurzen Startanleitung. Vorhandene Projektdateien haben Vorrang; wenn keine vorhanden sind, benenne die verwendete Java-/GNG-Variante ausdrücklich.

Eine gewöhnliche Grundlage umfasst Spielfenster, Spielzustand, eine bewegliche Spielfigur, zeitliche Aktualisierung sowie Start und Pause. Liefere konkrete Erweiterungspunkte für die eigentliche Spiellogik. Erfinde keine für das Spiel noch unbekannten Regeln. Platzhalter für freiwillige Erweiterungen sind von fehlendem Code zu unterscheiden, der bereits für den Start erforderlich wäre.

## Tastatursteuerung

Prüfe den tatsächlichen Ereignispfad der verwendeten Vorlage: Fensterfokus, Tastaturregistrierung, normale Tasten und Sondertasten. Ein definierter Callback allein beweist nicht, dass das Fenster ihn auslöst.

Unterscheide einzelne Tastendrücke von dauerhaftem Gedrückthalten. Für kontinuierliche Bewegung braucht es einen Tastenzustand, der beim Drücken gesetzt, beim Loslassen gelöscht und bei Fokusverlust zurückgesetzt wird. Mehrere gleichzeitig gedrückte Tasten und schnelle Eingaben dürfen keine hängende Bewegung verursachen. Verlasse dich dafür nicht auf das Wiederholungsintervall der Betriebssystemtastatur.

Die untersuchte Standard-GNG-Schnittstelle bietet keine allgemeinen Loslassen-Callbacks in ihren aufgelisteten Schülerklassen. Behaupte diese nicht und erfinde keine Methode wie `TasteLosgelassen`. Wenn kontinuierliches Gedrückthalten gefordert ist, untersuche die konkrete Bibliothek und liefere den nötigen kompatiblen Adapter oder die ausdrücklich erklärte Bibliotheksergänzung vollständig mit. Bei einem vorhandenen Projekt hat dessen Eingabesystem Vorrang.

## Prüfung und Lieferung

Übersetze das gesamte Grundgerüst, prüfe Start/Pause, Bewegung und Zustandsübergänge. Bei kontinuierlicher Eingabe prüfe auch Loslassen, Fokusverlust und mehrere Tasten. Unterscheide einen Aufruf des Callbacks im Logiktest von einem tatsächlichen Tastaturtest am Fenster. Gib ehrlich an, welche Prüfung durchgeführt wurde.

Erledige innerhalb der Anfrage auch die notwendigen Ergänzungen und Prüfungen. Beende die Arbeit nicht mit einer Liste optionaler nächster Schritte, wenn diese zum gewünschten funktionsfähigen Ergebnis gehören. Frage nur nach Anforderungen, ohne die eine wesentliche Entscheidung nicht möglich ist; erledige unabhängige Arbeiten weiter.
