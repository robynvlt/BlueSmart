---
name: bluesmart
description: BlueSmart unterstützt Java-Aufgaben und Spiele in BlueJ anhand vorhandener Schulvorlagen. Verwende den Skill auch bei /BlueSmart oder $bluesmart. Geeignet für Graphics and Games und informatikschulbuch.de, Jahrgangsstufe 10.
---

# BlueSmart

## Aufruf

Wenn die Nutzereingabe mit `/BlueSmart` oder `/bluesmart` beginnt, wende diesen Skill auf die folgende Aufgabe an. `BlueSmart` ist der Anzeigename, `bluesmart` die technische Skill-Kennung. Der native Skill-Aufruf hängt vom Host ab; die Textauslöser ersetzen keine vom Host bereitgestellte Befehlsschnittstelle. Bei einem Aufruf ohne Aufgabe frage kurz nach dem BlueJ-Projekt oder dem gewünschten Spiel. Bei einer vorhandenen Aufgabe beginne mit der Arbeit und erledige die nötigen Ergänzungen und Prüfungen vollständig.

Arbeite auf Deutsch und orientiere dich zuerst am konkreten Projekt und an der Aufgabenstellung. Ziel ist fachlich richtiger Code, den die lernende Person selbst erklären und verändern kann. Behaupte keine garantierte Fehlerfreiheit oder Erkennbarkeit der Urheberschaft.

## Projekt verstehen

Lies `package.bluej`, die zu ändernden Klassen, ihre Oberklassen und aufgerufenen Methoden. Unterscheide Java- und Stride-Vorlagen. Bei `.stride` plus `.java` kläre anhand der Projektdateien und des Editors, welche Quelle bearbeitet wird; ändere nicht bloß eine möglicherweise erzeugte Java-Datei. Die beigefügte Wissensbasis erfasst Java, nicht die vollständige Stride-Semantik.

Lies [Unterrichtsstil](references/unterrichtsstil.md), wenn du eine Vorlage erstmals bearbeitest. Suche das Aufgabenprojekt in [Projektkatalog](references/projektkatalog.md). Nutze vorhandene Graphify-Daten als Suchhilfe; überprüfe Beziehungen am Quelltext, insbesondere bei mehrfach vorkommenden Klassennamen. Der portable Skill funktioniert auch ohne Graphify.

Für Graphics-and-Games-Aufrufe ist [die belegte API-Liste](references/gng-api.md) verfügbar. Prüfe vor dem Übernehmen, ob die lokale Bibliotheksvariante dieselben Signaturen hat. `Figur` verwendet beispielsweise `AktionAusführen`, während `Ereignisbehandlung` Takte an `TaktImpulsAusführen` weiterleitet.

Die Download-Vorlagen enthalten oft nur Lücken, Kommentare und Klassengerüste. Wenn die vollständige Buchaufgabe fehlt, benenne die fehlende Anforderung. Setze eindeutig vorgegebene Teile um; kennzeichne eine eigene Ergänzung als Annahme und nicht als offizielle Lösung. Ein kompilierendes Gerüst ist noch keine gelöste Aufgabe.

Bei einer neuen Spielgrundlage lies [Spielgrundlage und Tastatursteuerung](references/spielgrundlage.md). Gewünscht sind vollständige, einsetzbare Klassen einschließlich korrekt eingebundener Eingabe und einer klaren Startanleitung, keine fehlenden Hilfsklassen oder nur angekündigten notwendigen Ergänzungen.

## Mitgelieferte Wissensbasis

Das installierbare Paket enthält unter `assets/knowledge/` einen komprimierten Strukturgraphen, die Quellenzuordnung und die Downloadquellen der untersuchten Vorlagen. Für eine gezielte Abfrage ohne Graphify-Abhängigkeit nutze `python scripts/query_knowledge.py <Projektordnername> <Symbol> --depth 2`, beispielsweise `2_1_A01_Mondrian_Vorlage Figur`. Die Pfade der Skripte sind relativ zu diesem Skill.

Die Wissensdateien enthalten extrahierte Beziehungen und Herkunftsangaben, nicht den gesamten Chat oder sämtliche Originalquellen. Sie sind ein datierter Stand der untersuchten Materialien. Bei späteren Nutzerprojekten haben die tatsächlich vorliegenden Dateien Vorrang. Lade die große Wissensbasis nur für eine konkrete Recherche und übernimm unsichere Beziehungen nicht als belegte Laufzeitaufrufe.

## Passend implementieren

- Bewahre Klassen-, Attribut- und Methodennamen, Signaturen, Sichtbarkeiten und die Architektur der konkreten Vorlage. Deutsche Methoden mit großem Anfangsbuchstaben wie `PositionSetzen` sind hier normal. Erhalte Umlaute und prüfe die Zeichenkodierung.
- Verwende vorhandene `Figur`, `Kreis`, `Rechteck`, `Text`, `Turtle` und Ereignisbehandlung, wenn das Projekt sie nutzt. Ersetze sie nicht durch eine neue Grafikbibliothek. Manche Projekte wie Snake besitzen eigene Swing-Symbole: diese Schnittstellen gehen allgemeinen GNG-Mustern vor.
- Unterscheide `Ereignisbehandlung` und `EreignisBehandlung` sowie die exakten Schreibweisen von `TasteGedrückt` und `TaktImpulsAusführen`. Java unterscheidet Groß-/Kleinschreibung.
- Ergänze auf dem Niveau der Aufgabe: einzelne Referenzen, Schleifen, Felder, Listen, Vererbung und Interfaces sind je nach Projekt vorhanden. Weder pauschal moderne Java-Techniken einführen noch vorhandene `ArrayList`, `private`, `protected` oder `@Override` verbieten.
- Erhalte vorhandene Autorenangaben; schreibe neue Änderungen nicht den Schulbuchautoren zu. Verwende kurze, sachliche Kommentare. Keine absichtlichen Fehler oder erfundenen Arbeitsnachweise.
- Arbeite in einer Kopie, wenn Originalmaterial untersucht wird. Beschränke Änderungen an Bibliotheksklassen auf nachgewiesene Fehler oder ausdrückliche Anforderungen.

## Überprüfen und erklären

Übersetze jedes BlueJ-Projekt separat: gleichnamige Klassen aus verschiedenen Projektordnern dürfen nicht gemeinsam kompiliert werden. Nutze seine Zeichenkodierung und die JARs aus `+libs`. Ein fehlender SQLite-Treiber ist ein Abhängigkeitsproblem; prüfe die konkrete BlueJ-/Treiberkombination.

Bei verfügbarem Python und JDK kann `python scripts/check_project.py <Projektordner> --compile` die Metadaten lesen und die Java-Dateien mit den Projektbibliotheken in einem temporären Ordner übersetzen. Der Pfad zum Skript ist relativ zu diesem Skill. Das Skript führt das Programm nicht aus und prüft weder vollständige Aufgabenlösungen noch die Aktualität erzeugter Java-Dateien bei Stride.

Meldet eine erzeugte Stride-Java-Datei ein fehlendes `lang.stride`, fehlt dem externen Java-Aufruf möglicherweise die BlueJ-Laufzeit. Das ist allein kein Beleg für einen Fehler im Schülercode. `--build-root <beschreibbarer Ordner>` erlaubt einen eigenen temporären Buildbereich, wenn das System-Tempverzeichnis eingeschränkt ist.

Prüfe bei Ereignissen die Zustandsübergänge und bei Spielen Bewegung, Kollision, Punkte und Spielende. Lies [bearbeitete Beispiele](references/bearbeitete-beispiele.md) für belegte Fehlerbilder. Teste Grenzen und mindestens einen normalen Ablauf. Unterscheide Übersetzung, Logiktests mit Testdoubles und einen tatsächlich ausgeführten BlueJ-Grafiktest; behaupte nur durchgeführte Prüfungen.

Liefere die geänderten Dateien oder das Projekt, die wesentlichen Änderungen und eine kurze Erklärung mit einem nachvollziehbaren Beispiel. Nenne offene Annahmen und verbleibende Fehler. Falls BlueJ nicht gestartet wurde, gib konkrete Schritte zum Öffnen, Erzeugen des Startobjekts und Prüfen des Verhaltens an.
