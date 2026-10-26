# Belegte Graphics-and-Games-Schnittstellen

Direkt aus den Java-Deklarationen des heruntergeladenen `GraphicsAndGames_BlueJ_Java`-Projekts ermittelt. Diese Liste gilt für diese Bibliotheksvariante; die Dateien des konkreten Aufgabenprojekts haben Vorrang. Die hier aufgeführten Methoden sind häufig paketöffentlich und benötigen Klassen im selben Standardpaket.

## Dreieck

```java
Dreieck ()
void PositionSetzen(int x, int y)
void Verschieben(int deltaX, int deltaY)
void Drehen(int grad)
void GrößeSetzen (int breite, int höhe)
void FarbeSetzen (String farbe)
void WinkelSetzen (int winkel)
void SichtbarkeitSetzen (boolean sichtbar)
void Entfernen ()
void NachVornBringen ()
void GanzNachVornBringen ()
void NachHintenBringen ()
void GanzNachHintenBringen ()
```

## Ereignisbehandlung

```java
Ereignisbehandlung ()
void TaktImpulsAusführen ()
void Starten ()
void Anhalten ()
void TaktdauerSetzen (int dauer)
void TasteGedrückt (char taste)
void SonderTasteGedrückt (int taste)
void MausGeklickt (int x, int y, int anzahl)
```

## Figur

```java
Figur ()
void AktionAusführen()
void TasteGedrückt (char taste)
void SonderTasteGedrückt (int taste)
void MausGeklickt (int x, int y, int anzahl)
void PositionSetzen(int x, int y)
void GrößeSetzen (int größe)
void WinkelSetzen (int winkel)
void SichtbarkeitSetzen (boolean sichtbar)
void Entfernen ()
void NachVornBringen ()
void GanzNachVornBringen ()
void NachHintenBringen ()
void GanzNachHintenBringen ()
void ZumStartpunktGehen()
void Gehen(double länge)
void Drehen(int grad)
int WinkelGeben()
int XPositionGeben()
int YPositionGeben()
boolean Berührt ()
boolean Berührt (String farbe)
boolean Berührt (Object objekt)
void FigurteilFestlegenRechteck (int x, int y, int breite, int höhe, String farbe)
void FigurteilFestlegenEllipse (int x, int y, int breite, int höhe, String farbe)
void FigurteilFestlegenDreieck (int x1, int y1, int x2, int y2, int x3, int y3, String farbe)
void EigeneFigurLöschen()
```

## Kreis

```java
Kreis ()
void PositionSetzen(int x, int y)
void Verschieben(int deltaX, int deltaY)
void Drehen(int grad)
void RadiusSetzen (int radius)
void FarbeSetzen (String farbe)
void WinkelSetzen (int winkel)
void SichtbarkeitSetzen (boolean sichtbar)
void Entfernen ()
void NachVornBringen ()
void GanzNachVornBringen ()
void NachHintenBringen ()
void GanzNachHintenBringen ()
```

## Rechteck

```java
Rechteck ()
void PositionSetzen(int x, int y)
void Verschieben(int deltaX, int deltaY)
void Drehen(int grad)
void GrößeSetzen (int breite, int höhe)
void FarbeSetzen (String farbe)
void WinkelSetzen (int winkel)
void SichtbarkeitSetzen (boolean sichtbar)
void Entfernen ()
void NachVornBringen ()
void GanzNachVornBringen ()
void NachHintenBringen ()
void GanzNachHintenBringen ()
```

## Text

```java
Text ()
void PositionSetzen(int x, int y)
void TextSetzen (String text)
void TextGrößeSetzen (int größe)
void TextVergrößern()
void TextVerkleinern()
void Verschieben(int deltaX, int deltaY)
void Drehen(int grad)
void FarbeSetzen (String farbe)
void WinkelSetzen (int winkel)
void SichtbarkeitSetzen (boolean sichtbar)
void Entfernen ()
void NachVornBringen ()
void GanzNachVornBringen ()
void NachHintenBringen ()
void GanzNachHintenBringen ()
```

## Turtle

```java
Turtle ()
void AktionAusführen()
void TasteGedrückt (char taste)
void SonderTasteGedrückt (int taste)
void MausGeklickt (int x, int y, int anzahl)
void PositionSetzen(int x, int y)
void GrößeSetzen (int größe)
void FarbeSetzen (String farbe)
void WinkelSetzen (int winkel)
void SichtbarkeitSetzen (boolean sichtbar)
void Entfernen ()
void NachVornBringen ()
void GanzNachVornBringen ()
void NachHintenBringen ()
void GanzNachHintenBringen ()
void ZumStartpunktGehen()
void Gehen(double länge)
void Drehen(int grad)
void Löschen()
void StiftHeben()
void StiftSenken()
int WinkelGeben()
int XPositionGeben()
int YPositionGeben()
void SichtbarkeitFürSymbolSetzen (boolean sichtbar)
boolean Berührt ()
boolean Berührt (String farbe)
boolean Berührt (Object objekt)
```

## Ereignisse korrekt zuordnen

`Figur` und `Turtle` leiten Takte an `AktionAusführen()` weiter. Die eigenständige `Ereignisbehandlung` verwendet dagegen `TaktImpulsAusführen()`. Beide Varianten leiten normale Tasten an `TasteGedrückt(char)`, Sondertasten an `SonderTasteGedrückt(int)` und Klicks an `MausGeklickt(int,int,int)` weiter. Andere Projekte, insbesondere Snake, können eigene Ereignisklassen besitzen. Die jeweilige Oberklasse lesen.

Die hier genannten Methoden wurden aus dem Quelltext ermittelt; ein erfolgreicher Aufruf hängt weiterhin von Sichtbarkeit, konkretem Projekt und Laufzeitumgebung ab.
