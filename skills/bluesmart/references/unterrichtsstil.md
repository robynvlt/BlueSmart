# Belegter Unterrichtsstil

Grundlage: acht Java-BlueJ-Pakete und GraphicsAndGames von der [Kapitel-Webseite](https://informatikschulbuch.de/jahrgangsstufe-10/objektorientierte-modellierung-und-programmierungjgst10/), abgerufen am 26.10.2026. Zusätzlich wurden die neun Stride-Archive lokal gesichert. Dies ist eine Analyse von Unterrichtsmaterial, keine Methode zum Nachweis oder Verbergen von KI-Nutzung.

## Konkrete Muster

Die Pfade unten sind relativ zu `corpus/originals/`; nach den Archivnamen folgt in der Regel nochmals der gleichnamige Ordner.

| Beobachtung | Fundstelle | Konsequenz |
|---|---|---|
| Klassen und viele Methoden ohne explizites `public` | `2_2_Vorlagen_BlueJ_Java/.../2_2_A03Fehleraufgabe_Vorlage/Kunde.java` | Vorhandene Sichtbarkeit erhalten; nicht ungefragt alles öffentlich machen. |
| Deutsche Bezeichner, Methoden beginnen groß | `2_3_Vorlagen_BlueJ_Java/.../2_3_A03_Ampel_Vorlage/Ampel.java`: `GrünSetzen`, `PositionSetzen` | Exakt vorhandene Schreibweise verwenden. |
| Benannte Objektattribute und Objekterzeugung im Konstruktor | dieselbe `Ampel.java`: `lampeOben`, `lampeMitte` | Neue untere Lampe nach demselben Muster ergänzen. |
| Zeit- und Tastaturereignisse | `2_3_Vorlagen_BlueJ_Java/.../2_3_A08_Snake_Vorlage/Spiel.java` | Projektbezogene Callback-Signaturen überschreiben. |
| Eigene Darstellung getrennt von Spiellogik | Snake: `Schlange`, `KopfSymbol`, `RumpfSymbol`, `RandSymbol` | Keine allgemeine GNG-Schnittstelle für diese Symbole erfinden. |
| Explizite Deklaration und anschließende Zuweisung | Fahrradverleih: `Text kundenname; kundenname = new Text();` | Lokales Muster beibehalten, wenn die Aufgabe darauf aufbaut. |
| Listen und indexbasierte Schleifen | `2_5_Vorlagen_BlueJ_Java/.../2_5_A06_StartpositionenBerechnen_Vorlage/Dompteur.java` | `ArrayList<PosTurtle>` und `index = index + 1` sind Teil des Materials, kein Fremdstil. |
| Vererbung, `protected`, `private`, `super` | `2_7_Vorlagen_BlueJ_Java/.../2_7_A04_Medienverwaltung_Vorlage/{Medium,Song,Film}.java` | Fortgeschrittenere Merkmale passend zur konkreten Aufgabe einsetzen. |

## Keine universellen Schulregeln ableiten

Die Autoren verwenden unterschiedliche Stile. Manche Programme haben `main`, andere werden über Konstruktoren gestartet. Manche nutzen Swing direkt, andere GNG. Benennung und Sichtbarkeit sind projektbezogen, keine allgemeine Java-Norm. Vorhandene Lücken wie `//Ergänzen`, leere Methoden und `???` sind nicht automatisch unbeabsichtigte Defekte.

## Quellen und Wissensbasis

Im lokalen Gesamtpaket stehen `corpus/manifest.json` für Download-URLs und SHA-256-Werte, `corpus/source-map.json` für die Zuordnung der 867 Java-Dateien einschließlich eigenständiger Bibliothek zu 390 eindeutigen Inhalten und `graphify-out/graph.json` für den Strukturgraphen. Nur zwei eindeutige Java-Dateien benötigten Windows-1252 statt UTF-8. Analysekopien sind nach UTF-8 normalisiert; Originalarchive bleiben bytegetreu.

Graphify kann bei gemeinsamer Analyse gleichnamige Klassen projektübergreifend falsch zuordnen. Der lokale Graph wird deshalb pro BlueJ-Projekt aufgelöst und erst anschließend über identische Dateiinhalte zusammengeführt. Seine gerichteten Beziehungen bewahren mehrere Fundstellen und das jeweils belegende Projekt. Nicht aufgelöste Rohbefunde bleiben separat erhalten. Ein Graphpfad ist trotzdem ein Recherchehinweis, kein Beweis für einen funktionierenden Laufzeitaufruf. Genaue Grenzen stehen in `graphify-out/HEALTH.txt` und im Analysebericht. Stride-Quellen, Bilder, Buchtexte und sämtliche Laufzeitpfade sind nicht vollständig im Graphen erfasst.

Geprüftes Beispiel: In `2_1_A01_Mondrian_Vorlage/Figur.java:40–62` erzeugt der Konstruktor eine anonyme Implementierung von `Zeichenfenster.AktionsEmpfaenger` und registriert sie. Diese leitet Takte und Eingaben an `AktionAusführen`, `TasteGedrückt`, `SonderTasteGedrückt` und `MausGeklickt` weiter. Das Interface steht in `Zeichenfenster.java:22–28`. Bei dieser Variante genügt normalerweise das Überschreiben der vorhandenen Figurmethoden. Ein Graphziel ohne Quellpfad kann ein unaufgelöster Verweisknoten sein; es beweist keine Verbindung zu einem anderen Projekt.
