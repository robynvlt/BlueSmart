# Bearbeitete Beispiele

Die Arbeitskopien liegen im lokalen Gesamtprojekt unter `worked-projects/`. Sie sind eigenständig erarbeitete Ergänzungen, keine offiziellen Musterlösungen. Vollständige Buchaufgaben waren nicht Bestandteil der untersuchten Kapitel-Webseite.

## Fahrradverleih — 2.2 A03 Fehleraufgabe

`Fahrrad.java`: Die schließende Klammer von `TypGeben` fehlt. `Kunde.java`: `NameGeben` muss einen `String` zurückgeben und den gespeicherten Namen statt einer festen Zeichenkette liefern. `Fahrradverleih.java`: Kunden müssen in `kunde1` und `kunde2` gespeichert werden; beim Druckaufruf fehlt ein Semikolon; `NameGebe` ist zu `NameGeben` zu berichtigen.

Die Arbeitskopie kompiliert. Logiktest mit Grafikdoubles: beide Kundennamen, Fahrradtyp und alle sechs Kombinationen der zwei Kunden und drei Räder. Ungültige Nummern und die Verwaltung bereits verliehener Räder sind keine zusätzlich implementierten Funktionen.

## Ampel — 2.3 A03

Die fünf markierten Ergänzungen betreffen dieselbe fehlende untere Lampe: Attribut, Konstruktion mit `y + 40` und Farbe `grün`, Ausschalten beim roten Startzustand, gemeinsames Positionieren und Einschalten in `GrünSetzen`.

Die Arbeitskopie kompiliert. Logiktest mit Lampendouble: roter Startzustand, grüner Zustand, Abstand und gemeinsames Verschieben sowie Ablehnung einer ungültigen Position. Ein vollständiger zeitgesteuerter Phasenzyklus wurde nicht aus einer unbekannten Buchanforderung hinzuerfunden.

## Snake — 2.3 A08

Vorher prüft `TaktImpulsAusführen` die alte Kopfposition, bewegt anschließend und vergibt einen Punkt. Beim Schritt über den Rand wird das Spiel dadurch erst im nächsten Takt beendet und vorher ein Punkt vergeben. Die Arbeitskopie bewegt zuerst, prüft die neue Position und vergibt nur bei einem zulässigen Zustand Punkte.

Die Arbeitskopie kompiliert. Zusätzlich verhindert sie direktes Umkehren und mehrere Richtungsänderungen innerhalb eines Taktes. Ein beendetes Spiel bewegt sich nicht weiter und lässt sich durch die Starttaste nicht versehentlich fortsetzen.

Tests führen die echte `Spiel`- und `Schlange`-Logik mit Doubles nur für Grafik und Zeitgeber aus: alle vier Bewegungsrichtungen, Folgen des Rumpfs, Gegenrichtung, schnelle Eingaben, alle vier Ränder, Punkte, Pause/Fortsetzen und Spielende. Das Original schlägt in diesen Regressionstests fehl, die Arbeitskopie besteht. Weitere Tests prüfen die Selbstkollision. Das echte Swing-Projekt wurde ausgeführt und sein Fenster mit Punktestand gerendert. Die BlueJ-Editorbedienung und physische Tastatureingaben wurden nicht automatisiert. Ein Neustartmechanismus und Änderungen an späteren Snake-Kapiteln sind keine zusätzlich eingeführten Funktionen.

## Steinzeit — 2.4 A00

Die Vorlage deklariert `sf6` doppelt und verwendet ein nicht deklariertes `sf7`. Außerdem fehlen die Konstruktion von `sf5`, die Anfangsposition von `sf2` und Bewegungsaufrufe für `sf2`, `sf7`, `sf8`. Die Arbeitskopie stellt acht einzeln verwaltete Gegner her und ergänzt diese Aufrufe, ohne auf eine spätere Listenlösung umzubauen.

Die Arbeitskopie kompiliert. Ein Logiktest prüft die Erzeugung, Startposition und Bewegung aller acht Gegner mit Doubles. Das echte Swing-Projekt wurde ausgeführt und gerendert; der BlueJ-Editor wurde nicht gestartet.

## Bewusst offene Aufgabe — 2.5 A06

`Dompteur.AufstellungEinnehmen` enthält `PositionSetzen(???, ???)`. Die verlangte geometrische Startaufstellung ist aus der Quelldatei nicht eindeutig ableitbar. Die Vorlage wurde deshalb nicht als vermeintliche offizielle Lösung vervollständigt. Benötigt wird die konkrete Buchaufgabe oder Skizze; erst danach lässt sich die passende Formel bestimmen.
